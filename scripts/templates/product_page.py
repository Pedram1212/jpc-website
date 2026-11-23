"""
Individual Product Page Template (`/product/<slug>/index.html`)
==============================================================
Renders all 12 required B2B engineering sections (A through L) for the 40
`published` Phase 2 Pilot SKUs in `data/catalog-500.json`.
"""

import urllib.parse
from .common import (
    SITE_DOMAIN,
    build_base_jsonld_graph,
    esc,
    get_schematic_svg,
    render_full_html_page,
)

CATEGORY_DIRECTORY_SLUG_MAP = {
    "pneumatic-cylinders": ("pneumatic-cylinders", "جک و سیلندر پنوماتیک"),
    "directional-control-valves": ("solenoid-valves", "شیرهای برقی و کنترل جهت"),
    "air-preparation-frl": ("air-preparation", "واحد مراقبت و آماده‌سازی هوا"),
    "pneumatic-fittings": ("pneumatic-fittings", "اتصالات و رابط‌های پنوماتیک"),
    "silencers-exhaust": ("silencers-exhaust", "صداخفه‌کن و اگزوز پنوماتیک"),
    "valve-manifold-accessories": ("solenoid-valves", "شیرآلات و قطعات جزیره شیر"),
    "pneumatic-kits": ("pneumatic-fittings", "کیت اتصالات و کنترل جریان"),
}

XREF_TIER_BADGES = {
    "verified_direct_replacement": ("جایگزین مستقیم تأییدشده", "#0D9488", "#CCFBF1"),
    "conditionally_compatible": ("جایگزین مشروط به بررسی پارامترها", "#B45309", "#FEF3C7"),
    "functionally_similar": ("مشابه عملکردی", "#1D4ED8", "#DBEAFE"),
    "unverified_candidate": ("نامزد بررسی مهندسی", "#475569", "#F1F5F9"),
}


def get_product_slug(product: dict) -> str:
    raw = str(product.get("seo", {}).get("urlSlug", "")).strip("/")
    if raw.startswith("product/"):
        return raw[len("product/"):].strip("/")
    return raw or product["id"]


def build_product_faqs(product: dict) -> list:
    import math

    ta = product.get("technicalAttributes", {})
    model = product["modelCode"]
    brand_disp = product.get("brandDisplay") or product["brand"]
    fam = product["family"]
    port = ta.get("portSize") or product.get("portSize") or "مطابق دیتاشیت"
    press = ta.get("pressureRange") or product.get("pressureRange") or "1 – 10 bar"
    bore = ta.get("boreMm")
    stroke = ta.get("strokeMm")
    rod = ta.get("rodDiameterMm")
    cush = ta.get("cushioning")
    vfunc = ta.get("valveFunction")
    volt = ta.get("coilVoltage")
    tube = ta.get("tubeOdMm")
    flow = ta.get("flowRateLMin")
    caveat = product.get("caveatsFa", "")

    faqs = []
    if bore and stroke:
        rod_d = rod or max(6, round(float(bore) * 0.32))
        area_ext = math.pi * (float(bore) / 2.0) ** 2
        area_ret = math.pi * ((float(bore) / 2.0) ** 2 - (float(rod_d) / 2.0) ** 2)
        f_ext_theo_n = round(area_ext * 0.6)
        f_ext_eff_n = round(f_ext_theo_n * 0.8)
        f_ret_theo_n = round(area_ret * 0.6)
        f_ret_eff_n = round(f_ret_theo_n * 0.8)
        f_ext_eff_kgf = round(f_ext_eff_n / 9.81, 1)
        f_ret_eff_kgf = round(f_ret_eff_n / 9.81, 1)

        faqs.append((
            f"مشخصات ابعادی و استاندارد نصب {product['titleFa']} (کد {model}) چیست؟",
            f"این سیلندر از سری {fam} برند {brand_disp} دارای قطر پیستون {bore} میلی‌متر، کورس حرکتی {stroke} میلی‌متر، قطر شفت استاندارد {rod_d} میلی‌متر، سایز پورت {port} و ضربه‌گیر {cush or 'استاندارد'} است و در محدوده فشار کاری {press} فعالیت می‌کند."
        ))
        faqs.append((
            f"نیروی تئوری و واقعی جک {model} در فشار استاندارد ۶ بار چقدر است؟",
            f"برای قطر پیستون {bore}mm و شفت {rod_d}mm در فشار کاری ۶ بار (0.6 MPa): نیروی تئوری کورس رفت حدود {f_ext_theo_n} نیوتن است که با اعمال ضریب راندمان ۸۰٪ (جهت جبران اصطکاک پکینگ و فشار برگشتی اگزوز)، نیروی عملیاتی مؤثر رفت حدود {f_ext_eff_n} نیوتن ({f_ext_eff_kgf} kgf) به دست می‌آید. در کورس برگشت نیز به دلیل اشغال سطح مقطع توسط شفت، نیروی تئوری {f_ret_theo_n} نیوتن و نیروی مؤثر واقعی حدود {f_ret_eff_n} نیوتن ({f_ret_eff_kgf} kgf) محاسبه می‌شود."
        ))
    elif vfunc:
        cv_approx = round(float(flow) / 980.0, 2) if flow else None
        flow_note = (
            f"با دبی اسمی حدود {flow} L/min (معادل تقریبی Cv ≈ {cv_approx}) "
            if flow
            else ""
        )
        faqs.append((
            f"آرایش شیر، سایز پورت و ولتاژ بوبین مدل {model} به چه صورت است؟",
            f"مدل {model} از خانواده {fam} برند {brand_disp} یک شیر کنترل جهت با آرایش {vfunc}، {flow_note}سایز پورت اتصال {port} و محدوده فشار کاری {press} است. وضعیت ولتاژ بوبین ({volt or '24V DC / 220V AC'}) پیش از صدور پیش‌فاکتور نهایی با نیاز تابلو برق شما تطبیق داده می‌شود."
        ))
        faqs.append((
            f"در انتخاب دبی (Qn / Cv) و ولتاژ بوبین برای شیر {model} به چه نکاتی دقت کنیم؟",
            f"سایز پورت ({port}) و دبی عبوری شیر باید متناسب با قطر جک و سرعت رفت‌وبرگشت مورد نیاز خط انتخاب شود تا افت فشار مسیر از ۰.۵ بار فراتر نرود. همچنین تطابق ولتاژ تغذیه PLC یا رله (24V DC در برابر 220V AC) و استاندارد سوکت DIN پیش از نصب الزامی است."
        ))
    elif tube:
        faqs.append((
            f"سایز شیلنگ و رزوه اتصال در قطعه {model} ({brand_disp}) چند است؟",
            f"این تجهیز از سری {fam} برند {brand_disp} برای قطر خارجی شیلنگ (Tube OD) برابر {tube} میلی‌متر و پورت/رزوه {port} در محدوده فشار {press} طراحی شده است. پیش از ثبت سفارش، تلرانس قطر خارجی شیلنگ (PU/PA) و تعداد در بسته بررسی می‌شود."
        ))
    else:
        faqs.append((
            f"کاربرد اصلی و مشخصات کلیدی {product['titleFa']} (کد {model}) چیست؟",
            f"مدل {model} متعلق به خانواده {fam} از برند {brand_disp} در گروه «{product['subCategory']}» با پورت/اتصال {port} و فشار کاری {press} است. {product.get('shortDescriptionFa', '')}"
        ))

    faqs.append((
        f"پیش از جایگزینی کد {model} با برند اختصاصی JPC یا برندهای دیگر چه مواردی باید کنترل شود؟",
        f"علاوه بر تطابق عملکردی در فشار کاری ({press})، واحد مهندسی JPC چهار پارامتر کلیدی را قبل از هرگونه جایگزینی بین‌برندی کنترل می‌کند: ۱) استاندارد ابعادی نصب و فاصله پیچ‌ها (مانند ISO 15552 یا الگوی منیفولد)، ۲) سایز و نوع رزوه پورت ({port} — موازی G در برابر مخروطی R/NPT)، ۳) ولتاژ و توان بوبین یا نوع شیار سنسور مگنتی، و ۴) {caveat or 'شرایط دمای محیط و نوع سیال'}."
    ))

    faqs.append((
        f"نحوه استعلام قیمت و زمان تحویل {model} از فروشگاه لاله‌زار تهران چگونه است؟",
        f"با توجه به نوسانات بازار صنعتی، قیمت و موجودی روز مدل {model} پس از ثبت در سبد استعلام (RFQ) یا ارسال به واتساپ فنی (09121305167) و تلفن‌های دفتر مرکزی لاله‌زار (021-33110796 و 021-33932529) اعلام و پیش‌فاکتور رسمی صادر می‌گردد."
    ))
    return faqs


def render_product_page(product: dict, all_products: list, families_by_id: dict) -> str:
    """
    Generate the complete HTML string for `/product/<slug>/index.html` (`depth=2`, `base_prefix="../../"`).
    """
    base_prefix = "../../"
    slug = get_product_slug(product)
    canonical_url = f"{SITE_DOMAIN}/product/{slug}/"

    cat_dir_slug, cat_short_fa = CATEGORY_DIRECTORY_SLUG_MAP.get(
        product["categoryId"], ("pneumatic-fittings", product["categoryTitleFa"])
    )
    family_id = product["familyId"]
    family_obj = families_by_id.get(family_id, {})
    family_title_fa = family_obj.get("titleFa", f"سری {product['family']}")

    ta = product.get("technicalAttributes", {})
    model_code = product["modelCode"]
    sku = product["sku"]
    article_no = product.get("articleNumber")
    brand_disp = product.get("brandDisplay") or product["brand"]
    brand_slug = product["manufacturerId"]

    # Section A: Breadcrumbs
    breadcrumbs = [
        ("صفحه اصلی", f"{SITE_DOMAIN}/"),
        ("محصولات", f"{SITE_DOMAIN}/products/"),
        (cat_short_fa, f"{SITE_DOMAIN}/products/{cat_dir_slug}/"),
        (f"سری {product['family']}", f"{SITE_DOMAIN}/series/{family_id}/"),
        (model_code, canonical_url),
    ]

    # Same-family variants (show published variants first with direct links, plus sample draft variants)
    same_family_all = [
        p for p in all_products
        if p["familyId"] == family_id and p["sku"] != sku
    ]
    same_family_pub = [p for p in same_family_all if p["publicationStatus"] == "published"]
    same_family_draft = [p for p in same_family_all if p["publicationStatus"] != "published"][:6]

    # Map published products by id/sku for cross-reference linking
    pub_by_id = {p["id"]: p for p in all_products if p["publicationStatus"] == "published"}
    pub_by_sku = {p["sku"]: p for p in all_products if p["publicationStatus"] == "published"}

    # Build FAQs
    faqs = build_product_faqs(product)

    # JSON-LD Product + FAQPage nodes (NO incomplete Offer block per GSC rules!)
    additional_props = [
        {"@type": "PropertyValue", "name": s["label"], "value": str(s["value"])}
        for s in product.get("specs", [])
    ]
    product_ld = {
        "@type": "Product",
        "@id": f"{canonical_url}#product",
        "name": product["titleFa"],
        "alternateName": [product["titleEn"], model_code, sku],
        "sku": sku,
        "mpn": model_code,
        "model": model_code,
        "description": product["descriptionFa"],
        "brand": {
            "@type": "Brand",
            "name": brand_disp,
        },
        "manufacturer": {
            "@type": "Organization",
            "name": product["manufacturerAttribution"],
        },
        "url": canonical_url,
        "additionalProperty": additional_props,
    }
    if article_no:
        product_ld["identifier"] = article_no

    faq_ld = {
        "@type": "FAQPage",
        "@id": f"{canonical_url}#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }

    jsonld_str = build_base_jsonld_graph(
        canonical_url=canonical_url,
        breadcrumbs=breadcrumbs,
        extra_nodes=[product_ld, faq_ld],
    )

    # Section C Gallery HTML
    media = product.get("media", {})
    svg_markup = get_schematic_svg(product.get("schematicType", "cylinder-iso"))
    if media.get("hasProductPhoto") and media.get("imageUrl"):
        gallery_visual_html = f"""
          <img
            src="{base_prefix}{esc(media['imageUrl'])}"
            alt="{esc(product['titleFa'])} - کد فنی {esc(model_code)}"
            style="max-width: 100%; max-height: 240px; object-fit: contain; border-radius: 8px;"
            loading="eager"
          />
        """
        gallery_badge_text = "تصویر محصول تأییدشده در مخزن JPC"
    else:
        gallery_visual_html = f"""
          <div style="width: 100%; max-width: 280px; color: #087F8C; padding: 1rem;">
            {svg_markup}
          </div>
        """
        gallery_badge_text = "شماتیک مهندسی استاندارد ISO 1219 (تصویر کاتالوگی در حال تطبیق)"

    # Section D Primary Technical Highlights
    highlights = []
    if ta.get("boreMm") is not None:
        highlights.append(("قطر پیستون (Bore)", f"{ta['boreMm']} mm", True))
    if ta.get("strokeMm") is not None:
        highlights.append(("کورس حرکتی (Stroke)", f"{ta['strokeMm']} mm", True))
    if ta.get("rodDiameterMm") is not None:
        highlights.append(("قطر شفت (Rod Ø)", f"{ta['rodDiameterMm']} mm", True))
    if ta.get("valveFunction"):
        highlights.append(("آرایش و عملکرد شیر", ta["valveFunction"], True))
    if ta.get("coilVoltage"):
        highlights.append(("ولتاژ تحریک بوبین", ta["coilVoltage"], False))
    if ta.get("tubeOdMm"):
        highlights.append(("قطر شیلنگ (Tube OD)", f"{ta['tubeOdMm']} mm", True))
    highlights.append(("سایز پورت / رزوه", ta.get("portSize") or product.get("portSize"), True))
    highlights.append(("محدوده فشار کاری", ta.get("pressureRange") or product.get("pressureRange"), True))
    if ta.get("cushioning"):
        highlights.append(("نوع ضربه‌گیر", ta["cushioning"], False))
    if ta.get("flowRateLMin") is not None:
        highlights.append(("دبی اسمی (Flow Rate)", f"{ta['flowRateLMin']} L/min", True))
    highlights.append(("استاندارد مرجع", " / ".join(ta.get("standards") or ["ISO"]), True))
    highlights = highlights[:6]

    highlights_html = "\n".join(
        f"""
        <div style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 0.75rem 0.9rem;">
          <div style="font-size: 0.74rem; color: #64748B; margin-bottom: 0.25rem;">{esc(lbl)}</div>
          <div class="{'mono' if is_ltr else ''}" {'dir="ltr"' if is_ltr else ''} style="font-size: 0.92rem; font-weight: 800; color: #10243A; font-variant-numeric: tabular-nums;">{esc(val)}</div>
        </div>"""
        for lbl, val, is_ltr in highlights
    )

    # Section E WhatsApp direct inquiry link
    wa_text = (
        f"سلام وقت بخیر، از وب‌سایت شرکت جلالی پنوماتیک (JPC) جهت استعلام قیمت و موجودی تجهیز زیر پیام می‌دهم:\n"
        f"• عنوان: {product['titleFa']}\n"
        f"• کد مدل سازنده: {model_code}\n"
        f"• کد SKU سایت: {sku}\n"
        f"• برند: {brand_disp}"
    )
    wa_url = f"https://wa.me/989121305167?text={urllib.parse.quote(wa_text)}"

    # Section F Detailed Technical Table rows
    table_rows = [
        ("کد دقیق مدل سازنده (Manufacturer Model)", model_code, True),
        ("کد شناسایی کاتالوگ (JPC Site SKU)", sku, True),
        ("شماره سفارش سازنده (Article / Part No.)", article_no if article_no else "ثبت‌نشده در جدول مرجع (استعلام بر اساس کد مدل)", bool(article_no)),
        ("برند تجاری", brand_disp, False),
        ("انتساب حقوقی سازنده", product["manufacturerAttribution"], True),
        ("خانواده / سری محصول", product["family"], True),
        ("گروه کالایی اصلی", product["categoryTitleFa"], False),
        ("زیرگروه تخصصی", product["subCategory"], False),
    ]
    if ta.get("boreMm") is not None:
        table_rows.append(("قطر پیستون (Bore Diameter)", f"{ta['boreMm']} mm", True))
    if ta.get("strokeMm") is not None:
        table_rows.append(("کورس حرکتی (Stroke Length)", f"{ta['strokeMm']} mm", True))
    if ta.get("rodDiameterMm") is not None:
        table_rows.append(("قطر شفت پیستون (Piston Rod Diameter)", f"{ta['rodDiameterMm']} mm", True))
    if ta.get("portSize"):
        table_rows.append(("سایز پورت / رزوه اتصال (Port Thread)", ta["portSize"], True))
    if ta.get("tubeOdMm"):
        table_rows.append(("قطر خارجی شیلنگ سازگار (Tube OD)", f"{ta['tubeOdMm']} mm", True))
    if ta.get("valveFunction"):
        table_rows.append(("آرایش و تابع شیر (Valve Function)", ta["valveFunction"], False))
    if ta.get("coilVoltage"):
        table_rows.append(("ولتاژ بوبین / تحریک الکتریکی", ta["coilVoltage"], False))
    if ta.get("cushioning"):
        table_rows.append(("سیستم ضربه‌گیر انتهایی (Cushioning)", ta["cushioning"], False))
    if ta.get("actuationType"):
        table_rows.append(("نوع تحریک و عملکرد (Actuation)", ta["actuationType"], False))
    if ta.get("flowRateLMin") is not None:
        table_rows.append(("دبی اسمی عبوری (Nominal Flow Rate)", f"{ta['flowRateLMin']} L/min", True))
    table_rows.append(("محدوده فشار کاری (Operating Pressure)", ta.get("pressureRange") or product.get("pressureRange"), True))
    table_rows.append(("استانداردهای فنی مرجع", " · ".join(ta.get("standards") or ["ISO"]), True))
    if ta.get("packQuantity") is not None:
        table_rows.append(("تعداد در بسته استاندارد (Pack Quantity)", f"{ta['packQuantity']} عدد", False))
    table_rows.append(("وضعیت قیمت و موجودی", "استعلام قیمت روز (B2B Quotation)", False))
    table_rows.append(("وضعیت اعتبارسنجی فنی", product.get("verificationStatusFa", ""), False))

    table_rows_html = "\n".join(
        f"""              <tr>
                <th scope="row" style="width: 38%; background: #F8FAFC; font-weight: 700; color: #1E293B;">{esc(k)}</th>
                <td class="{'mono' if is_ltr else ''}" {'dir="ltr"' if is_ltr else ''} style="font-variant-numeric: tabular-nums; font-weight: {'700' if is_ltr else '500'};">{esc(v)}</td>
              </tr>"""
        for k, v, is_ltr in table_rows
    )

    # Section G Caveats & Legacy callouts
    pack_caveat_html = ""
    if ta.get("packQuantityCaveatFa"):
        pack_caveat_html = f"""
        <div style="margin-top: 0.9rem; padding: 0.9rem 1.1rem; background: #FFFBEB; border-right: 4px solid #F28C28; border-radius: 8px; font-size: 0.86rem; color: #92400E;">
          <strong>نکته مهم بسته‌بندی / کیت (Packaging &amp; Bundle Caveat):</strong> {esc(ta['packQuantityCaveatFa'])}
        </div>"""

    legacy_callout_html = ""
    if product.get("isLegacyBrand"):
        legacy_callout_html = f"""
        <div style="margin-top: 0.9rem; padding: 0.9rem 1.1rem; background: #FEF2F2; border-right: 4px solid #DC2626; border-radius: 8px; font-size: 0.86rem; color: #991B1B;">
          <strong>توجه مهندسی (کد مرجع تاریخی Bosch Rexroth / AVENTICS):</strong>
          این ردیف از کاتالوگ تاریخی سیستم‌های پنوماتیک Rexroth / AVENTICS سری <span dir="ltr" class="mono">{esc(product['family'])}</span> استخراج شده است و به‌منظور شناسایی قطعات ماشین‌آلات موجود، بررسی امکان تأمین یا پیشنهاد جایگزین مهندسی ارائه می‌شود. پیش از هرگونه سفارش، مشخصات مکانیکی/الکتریکی و وضعیت تولید فعلی باید توسط واحد فنی JPC بررسی گردد.
        </div>"""

    # Section I Cross-Reference & Same-Family Variants HTML
    xref_cards_html = ""
    for xr in product.get("crossReferences", []):
        tier_key = xr.get("tier", "unverified_candidate")
        tier_label, tier_color, tier_bg = XREF_TIER_BADGES.get(
            tier_key, ("نامزد بررسی مهندسی", "#475569", "#F1F5F9")
        )
        target_prod = pub_by_id.get(xr.get("targetId")) or pub_by_sku.get(xr.get("targetSku"))
        target_link_html = ""
        if target_prod:
            t_slug = get_product_slug(target_prod)
            target_link_html = f"""
              <a href="{base_prefix}product/{esc(t_slug)}/index.html" class="btn btn-outline-tech btn-xs" style="margin-top: 0.55rem;">
                مشاهده صفحه فنی {esc(target_prod['modelCode'])} ←
              </a>"""
        xref_cards_html += f"""
          <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 0.45rem;">
              <span class="mono" dir="ltr" style="font-weight: 800; color: #10243A; font-size: 0.92rem;">{esc(xr['targetModel'])}</span>
              <span style="font-size: 0.72rem; font-weight: 800; color: {tier_color}; background: {tier_bg}; padding: 0.2rem 0.55rem; border-radius: 999px;">
                {esc(tier_label)}
              </span>
            </div>
            <div style="font-size: 0.78rem; color: #64748B; margin-bottom: 0.35rem;">برند هدف: <strong>{esc(xr['targetBrand'])}</strong></div>
            <p style="font-size: 0.82rem; color: #334155; line-height: 1.75; margin: 0;">{esc(xr['engineeringNoteFa'])}</p>
            {target_link_html}
          </div>"""

    variants_html = ""
    if same_family_pub or same_family_draft:
        v_rows = []
        for vp in same_family_pub[:8]:
            v_slug = get_product_slug(vp)
            v_ta = vp.get("technicalAttributes", {})
            spec_summary = (
                f"Ø{v_ta['boreMm']}×{v_ta['strokeMm']}mm ({v_ta.get('cushioning') or 'ISO'})"
                if (v_ta.get("boreMm") and v_ta.get("strokeMm"))
                else (v_ta.get("valveFunction") or v_ta.get("portSize") or vp["subCategory"])
            )
            v_rows.append(f"""
              <a href="{base_prefix}product/{esc(v_slug)}/index.html" style="display: flex; justify-content: space-between; align-items: center; padding: 0.65rem 0.85rem; background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 8px; text-decoration: none; color: #10243A;">
                <div>
                  <span class="mono" dir="ltr" style="font-weight: 800; color: #087F8C;">{esc(vp['modelCode'])}</span>
                  <span style="font-size: 0.8rem; color: #475569; margin-right: 0.5rem;">{esc(vp['titleFa'])}</span>
                </div>
                <span class="mono" dir="ltr" style="font-size: 0.78rem; color: #64748B;">{esc(spec_summary)} ←</span>
              </a>""")
        for dp in same_family_draft[:4]:
            v_rows.append(f"""
              <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.6rem 0.85rem; background: #FFFFFF; border: 1px dashed #CBD5E1; border-radius: 8px;">
                <div>
                  <span class="mono" dir="ltr" style="font-weight: 700; color: #1E293B;">{esc(dp['modelCode'])}</span>
                  <span style="font-size: 0.78rem; color: #64748B; margin-right: 0.5rem;">{esc(dp['shortDescriptionFa'])}</span>
                </div>
                <button type="button" class="btn btn-rfq-add btn-xs js-add-rfq-btn" data-id="{esc(dp['id'])}">+ افزودن به استعلام</button>
              </div>""")
        variants_html = "\n".join(v_rows)
    else:
        variants_html = f"""
          <p style="font-size: 0.85rem; color: #64748B;">
            سایر سایزها و واریانت‌های سری <span dir="ltr" class="mono">{esc(product['family'])}</span> را در <a href="{base_prefix}series/{esc(family_id)}/index.html" style="color: #087F8C; font-weight: 700;">صفحه خانواده سری {esc(product['family'])}</a> مشاهده فرمایید.
          </p>"""

    # Section J FAQs HTML
    faqs_html = "\n".join(
        f"""
        <details class="faq-item" {'open' if idx == 0 else ''} style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem 1.15rem; margin-bottom: 0.75rem;">
          <summary style="font-weight: 800; color: #10243A; cursor: pointer; font-size: 0.94rem;">{esc(q)}</summary>
          <p style="margin-top: 0.65rem; font-size: 0.87rem; color: #475569; line-height: 1.85;">{esc(a)}</p>
        </details>"""
        for idx, (q, a) in enumerate(faqs)
    )

    main_html = f"""
    <!-- SECTION A — BREADCRUMB NAVIGATION -->
    <nav aria-label="مسیر راهنما (Breadcrumb)" style="background: #F1F5F9; border-bottom: 1px solid #E1E7EE; padding: 0.75rem 0; font-size: 0.82rem;">
      <div class="container" style="display: flex; flex-wrap: wrap; align-items: center; gap: 0.45rem; color: #475569;">
        <a href="{base_prefix}index.html" style="color: #087F8C; font-weight: 700;">صفحه اصلی</a>
        <span aria-hidden="true">←</span>
        <a href="{base_prefix}products/index.html" style="color: #087F8C; font-weight: 700;">محصولات</a>
        <span aria-hidden="true">←</span>
        <a href="{base_prefix}products/{esc(cat_dir_slug)}/index.html" style="color: #087F8C; font-weight: 700;">{esc(cat_short_fa)}</a>
        <span aria-hidden="true">←</span>
        <a href="{base_prefix}series/{esc(family_id)}/index.html" style="color: #087F8C; font-weight: 700;">سری <span dir="ltr" class="mono">{esc(product['family'])}</span></a>
        <span aria-hidden="true">←</span>
        <strong class="mono" dir="ltr" style="color: #10243A;">{esc(model_code)}</strong>
      </div>
    </nav>

    <!-- SECTIONS B, C, D, E — PRODUCT IDENTITY, GALLERY, HIGHLIGHTS & RFQ WORKSTATION -->
    <section class="section" style="padding: 2.25rem 0;">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: 1.75rem; align-items: start;">

          <!-- LEFT/RIGHT COL 1: SECTION C (GALLERY) & SECTION D (PRIMARY HIGHLIGHTS) -->
          <div style="display: flex; flex-direction: column; gap: 1.25rem;">
            <!-- SECTION C — PRODUCT GALLERY & ISO SCHEMATIC -->
            <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: 1.35rem; text-align: center;">
              <div style="display: flex; justify-content: space-between; align-items: center; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 0.85rem;">
                <span class="brand-badge {'badge-jpc' if product['brand'] == 'JPC' else 'badge-euro'}">{esc(product['brandFa'])}</span>
                <span style="font-size: 0.74rem; color: #64748B; background: #F1F5F9; padding: 0.22rem 0.6rem; border-radius: 999px;">
                  {esc(gallery_badge_text)}
                </span>
              </div>

              <div style="min-height: 210px; display: flex; align-items: center; justify-content: center; background: #F8FAFC; border: 1px dashed #CBD5E1; border-radius: 10px; padding: 1rem;">
                {gallery_visual_html}
              </div>

              <div style="margin-top: 0.9rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
                <span style="font-size: 0.78rem; color: #64748B;">
                  شماتیک استاندارد: <strong class="mono" dir="ltr">{esc(product.get('schematicType', 'ISO-1219'))}</strong>
                </span>
                <button
                  type="button"
                  class="btn btn-outline-tech btn-xs js-spec-trigger"
                  data-id="{esc(product['id'])}"
                >
                  🔍 بزرگ‌نمایی شماتیک و جدول سریع
                </button>
              </div>
            </div>

            <!-- SECTION D — PRIMARY TECHNICAL HIGHLIGHTS -->
            <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: 1.35rem;">
              <h2 style="font-size: 1rem; font-weight: 800; color: #10243A; margin-bottom: 0.9rem;">
                مشخصات کلیدی خرید در یک نگاه (Key Technical Highlights)
              </h2>
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(145px, 1fr)); gap: 0.65rem;">
                {highlights_html}
              </div>
            </div>
          </div>

          <!-- COL 2: SECTION B (IDENTITY) & SECTION E (RFQ WORKSTATION) -->
          <div style="display: flex; flex-direction: column; gap: 1.25rem;">
            <!-- SECTION B — PRODUCT IDENTITY -->
            <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: 1.5rem;">
              <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center; margin-bottom: 0.65rem;">
                <a href="{base_prefix}brands/{esc(brand_slug)}/index.html" style="font-size: 0.76rem; font-weight: 800; color: #087F8C; background: #E6F4F6; padding: 0.25rem 0.65rem; border-radius: 6px; text-decoration: none;">
                  برند: {esc(brand_disp)}
                </a>
                <a href="{base_prefix}series/{esc(family_id)}/index.html" style="font-size: 0.76rem; font-weight: 800; color: #10243A; background: #F1F5F9; padding: 0.25rem 0.65rem; border-radius: 6px; text-decoration: none;">
                  خانواده: <span dir="ltr" class="mono">{esc(product['family'])}</span>
                </a>
                <a href="{base_prefix}products/{esc(cat_dir_slug)}/index.html" style="font-size: 0.76rem; font-weight: 700; color: #475569; background: #F8FAFC; border: 1px solid #E1E7EE; padding: 0.22rem 0.6rem; border-radius: 6px; text-decoration: none;">
                  {esc(product['subCategory'])}
                </a>
              </div>

              <h1 style="font-size: clamp(1.25rem, 3vw, 1.65rem); font-weight: 900; color: #10243A; line-height: 1.45; margin-bottom: 0.4rem;">
                {esc(product['titleFa'])}
              </h1>
              <div class="mono" dir="ltr" style="font-size: 0.88rem; color: #64748B; margin-bottom: 1rem;">
                {esc(product['titleEn'])}
              </div>

              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(175px, 1fr)); gap: 0.65rem; background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 0.9rem;">
                <div>
                  <span style="font-size: 0.74rem; color: #64748B; display: block;">کد دقیق مدل سازنده:</span>
                  <div style="display: flex; align-items: center; gap: 0.4rem; margin-top: 0.2rem;">
                    <strong class="mono" dir="ltr" style="font-size: 0.98rem; color: #10243A;">{esc(model_code)}</strong>
                    <button type="button" class="copy-code-btn js-static-copy-btn" data-copy="{esc(model_code)}" title="کپی کد مدل">کپی</button>
                  </div>
                </div>
                <div>
                  <span style="font-size: 0.74rem; color: #64748B; display: block;">کد SKU کاتالوگ JPC:</span>
                  <strong class="mono" dir="ltr" style="font-size: 0.9rem; color: #087F8C; margin-top: 0.2rem; display: block;">{esc(sku)}</strong>
                </div>
                <div>
                  <span style="font-size: 0.74rem; color: #64748B; display: block;">شماره سفارش سازنده (Article No.):</span>
                  <strong class="mono" dir="ltr" style="font-size: 0.88rem; color: #334155; margin-top: 0.2rem; display: block;">{esc(article_no if article_no else 'استعلام بر اساس کد مدل')}</strong>
                </div>
                <div>
                  <span style="font-size: 0.74rem; color: #64748B; display: block;">انتساب سازنده:</span>
                  <strong style="font-size: 0.82rem; color: #334155; margin-top: 0.2rem; display: block;">{esc(product['manufacturerAttribution'])}</strong>
                </div>
              </div>
            </div>

            <!-- SECTION E — REQUEST FOR QUOTATION (RFQ) B2B BOX -->
            <div style="background: #10243A; color: #F8FAFC; border-radius: 14px; padding: 1.5rem; box-shadow: 0 10px 25px rgba(16,36,58,0.12);">
              <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem;">
                <div>
                  <span style="font-size: 0.75rem; color: #38BDF8; font-weight: 800; display: block;">میز استعلام قیمت و تأمین صنعتی (B2B RFQ)</span>
                  <h2 style="font-size: 1.1rem; font-weight: 800; color: #FFFFFF; margin-top: 0.15rem;">
                    استعلام قیمت و موجودی روز <span dir="ltr" class="mono" style="color: #F28C28;">{esc(model_code)}</span>
                  </h2>
                </div>
                <span style="background: rgba(242,140,40,0.18); color: #F28C28; border: 1px solid rgba(242,140,40,0.4); font-size: 0.76rem; font-weight: 800; padding: 0.28rem 0.7rem; border-radius: 999px;">
                  {esc(product['commercial']['quotationState'])}
                </span>
              </div>

              <p style="font-size: 0.83rem; color: #CBD5E1; line-height: 1.75; margin-bottom: 1rem;">
                قیمت و موجودی این کد فنی بدون عددسازی صوری، بر اساس تعداد درخواستی و شرایط تحویل روز از دفتر مرکزی لاله‌زار تهران اعلام می‌شود.
              </p>

              <div style="display: grid; grid-template-columns: 110px 1fr; gap: 0.65rem; margin-bottom: 0.9rem;">
                <div>
                  <label for="pdp-rfq-qty" style="display: block; font-size: 0.76rem; color: #CBD5E1; margin-bottom: 0.3rem;">تعداد درخواستی:</label>
                  <input
                    type="number"
                    id="pdp-rfq-qty"
                    min="1"
                    value="1"
                    class="form-input mono"
                    dir="ltr"
                    style="background: #19344F; color: #FFFFFF; border-color: rgba(255,255,255,0.2); text-align: center; font-weight: 800;"
                  />
                </div>
                <div>
                  <label for="pdp-rfq-note" style="display: block; font-size: 0.76rem; color: #CBD5E1; margin-bottom: 0.3rem;">یادداشت فنی (ولتاژ، کورس، درخواست معادل JPC):</label>
                  <input
                    type="text"
                    id="pdp-rfq-note"
                    class="form-input"
                    placeholder="مثلاً: لطفاً قیمت کد اصلی و معادل JPC اعلام شود"
                    style="background: #19344F; color: #FFFFFF; border-color: rgba(255,255,255,0.2);"
                  />
                </div>
              </div>

              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 0.65rem;">
                <button
                  type="button"
                  id="pdp-add-rfq-btn"
                  data-product-id="{esc(product['id'])}"
                  class="btn btn-amber"
                  style="width: 100%; justify-content: center; font-weight: 800;"
                >
                  + افزودن به سبد استعلام (RFQ)
                </button>
                <a
                  href="{esc(wa_url)}"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="btn btn-whatsapp"
                  style="width: 100%; justify-content: center;"
                >
                  استعلام مستقیم واتساپ (09121305167)
                </a>
              </div>

              <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.9rem; padding-top: 0.75rem; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.78rem; color: #94A3B8;">
                <span>پاسخگویی مهندسی فروش: <strong>شنبه تا پنج‌شنبه ۰۹:۰۰ تا ۱۸:۰۰</strong></span>
                <button
                  type="button"
                  class="btn btn-outline-tech btn-xs js-static-copy-btn"
                  data-copy="{esc(canonical_url)}"
                  style="color: #E2E8F0; border-color: rgba(255,255,255,0.25);"
                >
                  🔗 کپی لینک صفحه محصول
                </button>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- SECTION F — DETAILED TECHNICAL TABLE -->
    <section class="section" id="technical-specifications" style="padding: 1.5rem 0;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.25rem, 3vw, 1.85rem);">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.1rem;">
            <div>
              <span class="section-eyebrow">جدول مشخصات مهندسی و پارامترهای کاتالوگ</span>
              <h2 style="font-size: 1.2rem; font-weight: 800; color: #10243A; margin-top: 0.2rem;">
                مشخصات فنی کامل <span dir="ltr" class="mono">{esc(model_code)}</span>
              </h2>
            </div>
            <span class="mono" dir="ltr" style="font-size: 0.78rem; color: #64748B;">SKU: {esc(sku)}</span>
          </div>

          <div class="table-responsive">
            <table class="tech-comparison-table" aria-label="جدول مشخصات فنی {esc(product['titleFa'])}">
              <tbody>
{table_rows_html}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION G — TECHNICAL EXPLANATION & CAVEATS -->
    <section class="section" id="technical-explanation" style="padding: 1.5rem 0;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.25rem, 3vw, 1.85rem);">
          <span class="section-eyebrow">بررسی فنی، کاربرد صنعتی و ملاحظات انتخاب</span>
          <h2 style="font-size: 1.2rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 0.9rem;">
            تحلیل مهندسی و راهنمای به‌کارگیری {esc(product['titleFa'])}
          </h2>
          <p style="font-size: 0.92rem; color: #1E293B; line-height: 1.95; margin-bottom: 0.85rem;">
            {esc(product['descriptionFa'])}
          </p>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1.1rem;">
            <div style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem;">
              <h3 style="font-size: 0.92rem; font-weight: 800; color: #10243A; margin-bottom: 0.45rem;">۱. عملکرد و کاربرد در خطوط تولید</h3>
              <p style="font-size: 0.84rem; color: #475569; line-height: 1.8; margin: 0;">
                این مدل از خانواده <span dir="ltr" class="mono">{esc(product['family'])}</span> برند {esc(brand_disp)} در سیستم‌های اتوماسیون صنعتی، ماشین‌آلات بسته‌بندی، خطوط مونتاژ و مدارهای هوای فشرده کارخانجات با فشار کاری <span dir="ltr" class="mono">{esc(ta.get('pressureRange') or product.get('pressureRange'))}</span> مورد استفاده قرار می‌گیرد.
              </p>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem;">
              <h3 style="font-size: 0.92rem; font-weight: 800; color: #10243A; margin-bottom: 0.45rem;">۲. نکات کنترل و تطبیق پیش از نصب</h3>
              <p style="font-size: 0.84rem; color: #475569; line-height: 1.8; margin: 0;">
                {esc(product['caveatsFa'])}
              </p>
            </div>
          </div>
          {pack_caveat_html}
          {legacy_callout_html}
        </div>
      </div>
    </section>

    <!-- SECTION H — TECHNICAL DOCUMENTS & SOURCE CATALOGS -->
    <section class="section" id="technical-documents" style="padding: 1.5rem 0;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.25rem, 3vw, 1.85rem);">
          <span class="section-eyebrow">مستندات فنی و مراجع کاتالوگ سازنده</span>
          <h2 style="font-size: 1.15rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 0.85rem;">
            دیتاشیت و مدارک مرجع <span dir="ltr" class="mono">{esc(model_code)}</span>
          </h2>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem;">
            <div style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1.1rem; display: flex; flex-direction: column; justify-content: space-between; gap: 0.75rem;">
              <div>
                <div style="font-size: 0.78rem; font-weight: 800; color: #087F8C;">مرجع مستندات سازنده ({esc(brand_disp)})</div>
                <div style="font-size: 0.86rem; color: #334155; margin-top: 0.3rem;">
                  فایل PDF یا صفحه مرجع استخراج مشخصات فنی سری <span dir="ltr" class="mono">{esc(product['family'])}</span>
                </div>
              </div>
              <a href="{esc(product['sourceUrl'])}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-tech btn-sm">
                مشاهده مستند مرجع سازنده ↗
              </a>
            </div>

            <div style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1.1rem; display: flex; flex-direction: column; justify-content: space-between; gap: 0.75rem;">
              <div>
                <div style="font-size: 0.78rem; font-weight: 800; color: #10243A;">کاتالوگ فنی گروه {esc(cat_short_fa)} JPC</div>
                <div style="font-size: 0.86rem; color: #334155; margin-top: 0.3rem;">
                  جدول ابعاد نصب، راهنمای انتخاب و کدهای معادل شرکت جلالی پنوماتیک
                </div>
              </div>
              <a href="{base_prefix}{esc(product['datasheetUrl'])}" download class="btn btn-outline-tech btn-sm">
                دانلود PDF راهنمای گروه کالایی
              </a>
            </div>

            <div style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1.1rem; display: flex; flex-direction: column; justify-content: space-between; gap: 0.75rem;">
              <div>
                <div style="font-size: 0.78rem; font-weight: 800; color: #F28C28;">درخواست نقشه ابعادی دقیق (CAD / 2D Drawing)</div>
                <div style="font-size: 0.86rem; color: #334155; margin-top: 0.3rem;">
                  ارسال برگه مشخصات ابعادی و تاییدیه تطابق از طریق واتساپ مهندسی فروش
                </div>
              </div>
              <a href="{esc(wa_url)}" target="_blank" rel="noopener noreferrer" class="btn btn-amber btn-sm">
                درخواست دیتاشیت در واتساپ
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION I — COMPATIBLE, CROSS-REFERENCE & SAME-FAMILY PRODUCTS -->
    <section class="section" id="compatible-products" style="padding: 1.5rem 0;">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: 1.5rem;">
          <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: 1.4rem;">
            <span class="section-eyebrow">سطح‌بندی تطابق مهندسی (Cross-Reference Tiers)</span>
            <h2 style="font-size: 1.1rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 0.9rem;">
              محصولات هم‌خانواده و کدهای معادل / جایگزین
            </h2>
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
              {xref_cards_html}
            </div>
          </div>

          <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: 1.4rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.9rem;">
              <div>
                <span class="section-eyebrow">سایر کدهای فنی سری <span dir="ltr" class="mono">{esc(product['family'])}</span></span>
                <h2 style="font-size: 1.1rem; font-weight: 800; color: #10243A; margin-top: 0.2rem;">
                  واریانت‌ها و سایزهای مرتبط در این خانواده
                </h2>
              </div>
              <a href="{base_prefix}series/{esc(family_id)}/index.html" class="btn btn-outline-tech btn-xs">
                مشاهده کل سری ({esc(family_obj.get('skuCount', len(same_family_all) + 1))} کد) ←
              </a>
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.55rem;">
              {variants_html}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION J — PRODUCT-SPECIFIC TECHNICAL FAQ -->
    <section class="section" id="product-faq" style="padding: 1.5rem 0;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.25rem, 3vw, 1.85rem);">
          <span class="section-eyebrow">پرسش‌های متداول مهندسی و خرید</span>
          <h2 style="font-size: 1.2rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 1rem;">
            سؤالات پرتکرار درباره <span dir="ltr" class="mono">{esc(model_code)}</span>
          </h2>
          {faqs_html}
        </div>
      </div>
    </section>

    <!-- SECTION K — RELATED TECHNICAL ARTICLES & ENGINEERING CALCULATORS -->
    <section class="section" id="related-guides-tools" style="padding: 1.5rem 0 2.5rem;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.25rem, 3vw, 1.85rem);">
          <span class="section-eyebrow">ابزارهای محاسباتی و دانشنامه مهندسی JPC</span>
          <h2 style="font-size: 1.15rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 1rem;">
            راهنماهای مهندسی مرتبط با {esc(cat_short_fa)}
          </h2>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 0.85rem;">
            <a href="{base_prefix}index.html#calculator" style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem; text-decoration: none; color: #10243A;">
              <div style="font-weight: 800; font-size: 0.9rem; color: #087F8C; margin-bottom: 0.3rem;">⚙️ محاسبه‌گر نیروی جک پنوماتیک</div>
              <p style="font-size: 0.8rem; color: #475569; margin: 0; line-height: 1.7;">محاسبه نیروی تئوری و واقعی (۸۰٪) رفت و برگشت سیلندر بر حسب نیوتن و کیلوگرم‌نیرو</p>
            </a>
            <a href="{base_prefix}compare/index.html" style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem; text-decoration: none; color: #10243A;">
              <div style="font-weight: 800; font-size: 0.9rem; color: #087F8C; margin-bottom: 0.3rem;">⚖️ مرکز معادل‌یابی و مقایسه فنی</div>
              <p style="font-size: 0.8rem; color: #475569; margin: 0; line-height: 1.7;">مقایسه خط‌به‌خط Festo DSBC، MFH، VUVG، MS و Rexroth HF03-LG با JPC</p>
            </a>
            <a href="{base_prefix}pneumatic-cylinder-buying-guide.html" style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem; text-decoration: none; color: #10243A;">
              <div style="font-weight: 800; font-size: 0.9rem; color: #087F8C; margin-bottom: 0.3rem;">📘 راهنمای انتخاب جک پنوماتیک ISO 15552</div>
              <p style="font-size: 0.8rem; color: #475569; margin: 0; line-height: 1.7;">بررسی قطر پیستون، کورس، ضربه‌گیر PPV/PPS و مقاومت کمانش شفت</p>
            </a>
            <a href="{base_prefix}solenoid-valve-guide.html" style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem; text-decoration: none; color: #10243A;">
              <div style="font-weight: 800; font-size: 0.9rem; color: #087F8C; margin-bottom: 0.3rem;">⚡ راهنمای تخصصی شیر برقی ۵/۲ و ۵/۳</div>
              <p style="font-size: 0.8rem; color: #475569; margin: 0; line-height: 1.7;">تفاوت تک‌بوبین و دوبوبین، مرکز بسته/باز و انتخاب ولتاژ بوبین</p>
            </a>
            <a href="{base_prefix}guides/frl-air-preparation-guide/index.html" style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem; text-decoration: none; color: #10243A;">
              <div style="font-weight: 800; font-size: 0.9rem; color: #087F8C; margin-bottom: 0.3rem;">🌬️ مرکز انتخاب واحد مراقبت هوا (FRL)</div>
              <p style="font-size: 0.8rem; color: #475569; margin: 0; line-height: 1.7;">استاندارد خلوص ISO 8573-1، فیلتر ۵/۴۰ میکرون، رگلاتور و تخلیه اتوماتیک</p>
            </a>
            <a href="{base_prefix}guides/pneumatic-troubleshooting-guide/index.html" style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem; text-decoration: none; color: #10243A;">
              <div style="font-weight: 800; font-size: 0.9rem; color: #087F8C; margin-bottom: 0.3rem;">🛠️ مرکز عیبیابی مدارهای پنوماتیک</div>
              <p style="font-size: 0.8rem; color: #475569; margin: 0; line-height: 1.7;">رفع نشتی اگزوز، سوختن بوبین، تشخیص رزوه G/R و پلاک‌خوان هوشمند</p>
            </a>
          </div>
        </div>
      </div>
    </section>
"""

    # Inline script wiring the PDP Quantity + Technical Note + Add-to-RFQ button directly into localStorage RFQ basket
    pdp_inline_script = f"""  <script>
    document.addEventListener("DOMContentLoaded", function () {{
      var addBtn = document.getElementById("pdp-add-rfq-btn");
      if (!addBtn) return;
      addBtn.addEventListener("click", function () {{
        var pid = addBtn.getAttribute("data-product-id");
        var qtyEl = document.getElementById("pdp-rfq-qty");
        var noteEl = document.getElementById("pdp-rfq-note");
        var qty = Math.max(1, parseInt(qtyEl ? qtyEl.value : "1", 10) || 1);
        var note = noteEl ? String(noteEl.value || "").trim() : "";
        var products = window.PRODUCTS_DATA || [];
        var prod = null;
        for (var i = 0; i < products.length; i++) {{
          if (products[i].id === pid || products[i].sku === "{esc(sku)}") {{
            prod = products[i];
            break;
          }}
        }}
        if (!prod) return;
        try {{
          var raw = localStorage.getItem("jpc_rfq_items");
          var list = raw ? JSON.parse(raw) : [];
          if (!Array.isArray(list)) list = [];
          var existing = null;
          for (var j = 0; j < list.length; j++) {{
            if (list[j].id === prod.id) {{
              existing = list[j];
              break;
            }}
          }}
          if (existing) {{
            existing.qty = (existing.qty || 1) + qty;
            if (note) existing.note = note;
          }} else {{
            list.push({{
              id: prod.id,
              code: prod.code,
              nameFa: prod.nameFa,
              brand: prod.brand,
              brandFa: prod.brandFa,
              portSize: prod.portSize,
              qty: qty,
              note: note
            }});
          }}
          localStorage.setItem("jpc_rfq_items", JSON.stringify(list));
          if (note) {{
            localStorage.setItem("jpc_rfq_note", note);
          }}
          var openDrawerBtn = document.querySelector(".js-open-rfq-drawer");
          if (openDrawerBtn) {{
            window.location.reload();
          }}
        }} catch (e) {{}}
      }});
    }});
  </script>"""

    return render_full_html_page(
        title=product["seo"]["seoTitle"] or f"{product['titleFa']} | {model_code} | شرکت جلالی پنوماتیک JPC",
        meta_description=product["seo"]["metaDescription"] or product["shortDescriptionFa"],
        canonical_url=canonical_url,
        base_prefix=base_prefix,
        active_section=product["category"],
        jsonld_str=jsonld_str,
        main_html=main_html,
        page_category_attr=product["category"],
        extra_inline_script=pdp_inline_script,
    )
