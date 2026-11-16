#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jalali Pneumatic Company (JPC) - Static SEO & GEO Build Script
Zero-dependency Python 3 script that:
1. Parses PRODUCTS_DATA from assets/js/products-data.js
2. Pre-renders crawlable HTML product cards between <!-- SSR_PRODUCTS_START --> and <!-- SSR_PRODUCTS_END -->
   in index.html, solenoid-valves.html, pneumatic-cylinders.html, and frl-accessories.html.
3. Injects rich ItemList + Product JSON-LD structured data (with sku, mpn, brand, category,
   additionalProperty technical specs, and B2B inquiry availability without fabricated prices)
   between <!-- SSR_JSONLD_PRODUCTS_START --> and <!-- SSR_JSONLD_PRODUCTS_END -->.
4. Generates llms-full.txt in the root directory with the complete bilingual company profile,
   dual-sourcing architecture, and full Markdown catalog table of all models and equivalents.
"""

import html
import json
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PRODUCTS_JS_PATH = ROOT_DIR / "assets" / "js" / "products-data.js"
LLMS_FULL_PATH = ROOT_DIR / "llms-full.txt"

PAGE_TARGETS = [
    ("index.html", "all", "https://jalalipneumatic.ir/"),
    ("solenoid-valves.html", "valves", "https://jalalipneumatic.ir/solenoid-valves.html"),
    ("pneumatic-cylinders.html", "cylinders", "https://jalalipneumatic.ir/pneumatic-cylinders.html"),
    ("frl-accessories.html", "frl-accessories", "https://jalalipneumatic.ir/frl-accessories.html"),
]


def parse_products_from_js(js_path: Path) -> list:
    """
    Pure Python 3 parser that extracts PRODUCTS_DATA array from assets/js/products-data.js
    without requiring Node.js or any external packages.
    """
    raw = js_path.read_text(encoding="utf-8")

    match = re.search(
        r"const\s+PRODUCTS_DATA\s*=\s*(\[.*\])\s*;\s*window\.PRODUCT_CATEGORIES",
        raw,
         flags=re.DOTALL,
    )
    if not match:
        raise ValueError("Could not locate PRODUCTS_DATA array in products-data.js")

    js_array = match.group(1)

    # Remove single-line // comments outside strings
    cleaned_lines = []
    for line in js_array.splitlines():
        stripped = line.strip()
        if stripped.startswith("//"):
            continue
        cleaned_lines.append(line)
    js_clean = "\n".join(cleaned_lines)

    # Convert single-quoted JS strings (e.g. 'G 1/4" (سایز ۱/۴ اینچ)') into valid JSON double-quoted strings
    def replace_single_quoted(m: re.Match) -> str:
        inner = m.group(1)
        inner_escaped = inner.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{inner_escaped}"'

    js_clean = re.sub(r"'([^'\\]*(?:\\.[^'\\]*)*)'", replace_single_quoted, js_clean)

    # Quote unquoted JS object keys: e.g. `    id: "jpc-4v210-08",` -> `    "id": "jpc-4v210-08",`
    js_clean = re.sub(r"(?m)^(\s*)([a-zA-Z_][a-zA-Z0-9_]*)\s*:", r'\1"\2":', js_clean)

    # Remove trailing commas before } or ]
    js_clean = re.sub(r",\s*([}\]])", r"\1", js_clean)

    return json.loads(js_clean)


def get_schematic_svg(schematic_type: str) -> str:
    if schematic_type in ("valve-5-2", "valve-5-2-double", "valve-5-3"):
        return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="20" y="14" width="40" height="36" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="60" y="14" width="40" height="36" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="6" y="22" width="14" height="20" rx="1" stroke="#F59E0B" stroke-width="2"/>
            <line x1="9" y1="38" x2="17" y2="26" stroke="#F59E0B" stroke-width="1.8"/>
            <path d="M100 26L106 20L110 32L114 20L118 26" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            <line x1="32" y1="50" x2="32" y2="14" stroke="currentColor" stroke-width="1.8"/>
            <polygon points="32,14 29,20 35,20" fill="currentColor"/>
            <line x1="48" y1="14" x2="48" y2="50" stroke="currentColor" stroke-width="1.8"/>
            <polygon points="48,50 45,44 51,44" fill="currentColor"/>
            <line x1="72" y1="50" x2="88" y2="14" stroke="#F59E0B" stroke-width="1.8"/>
            <circle cx="32" cy="8" r="2.2" fill="currentColor"/>
            <circle cx="48" cy="8" r="2.2" fill="currentColor"/>
            <circle cx="40" cy="56" r="2.2" fill="#F59E0B"/>
          </svg>"""
    if schematic_type == "valve-3-2":
        return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="24" y="14" width="36" height="36" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="60" y="14" width="36" height="36" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="10" y="22" width="14" height="20" rx="1" stroke="#F59E0B" stroke-width="2"/>
            <line x1="12" y1="38" x2="21" y2="26" stroke="#F59E0B" stroke-width="1.8"/>
            <line x1="42" y1="50" x2="42" y2="14" stroke="currentColor" stroke-width="1.8"/>
            <polygon points="42,14 39,20 45,20" fill="currentColor"/>
            <line x1="74" y1="38" x2="82" y2="38" stroke="#F59E0B" stroke-width="2"/>
            <line x1="78" y1="38" x2="78" y2="50" stroke="#F59E0B" stroke-width="2"/>
            <path d="M96 28L102 22L106 34L110 22L114 28" stroke="currentColor" stroke-width="1.8"/>
          </svg>"""
    if schematic_type in ("cylinder-double", "cylinder-tierod"):
        return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="14" y="14" width="72" height="36" rx="3" stroke="currentColor" stroke-width="2"/>
            <line x1="46" y1="14" x2="46" y2="50" stroke="#F59E0B" stroke-width="3"/>
            <line x1="46" y1="32" x2="112" y2="32" stroke="currentColor" stroke-width="4"/>
            <rect x="108" y="25" width="6" height="14" rx="1" fill="#F59E0B"/>
            <line x1="22" y1="14" x2="22" y2="6" stroke="currentColor" stroke-width="2"/>
            <line x1="78" y1="14" x2="78" y2="6" stroke="currentColor" stroke-width="2"/>
            <line x1="14" y1="20" x2="86" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
            <line x1="14" y1="44" x2="86" y2="44" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
          </svg>"""
    if schematic_type in ("cylinder-compact", "cylinder-mini"):
        return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="24" y="12" width="52" height="40" rx="3" stroke="currentColor" stroke-width="2"/>
            <line x1="50" y1="12" x2="50" y2="52" stroke="#F59E0B" stroke-width="3"/>
            <line x1="50" y1="32" x2="104" y2="32" stroke="currentColor" stroke-width="4.5"/>
            <circle cx="34" cy="22" r="2.5" fill="currentColor"/>
            <circle cx="66" cy="22" r="2.5" fill="currentColor"/>
            <circle cx="34" cy="42" r="2.5" fill="currentColor"/>
            <circle cx="66" cy="42" r="2.5" fill="currentColor"/>
          </svg>"""
    if schematic_type == "cylinder-rodless":
        return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="10" y="24" width="100" height="22" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="44" y="12" width="32" height="12" rx="2" stroke="#F59E0B" stroke-width="2"/>
            <line x1="60" y1="24" x2="60" y2="46" stroke="#F59E0B" stroke-width="2.5"/>
            <line x1="18" y1="35" x2="102" y2="35" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
          </svg>"""
    return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="18" y="12" width="26" height="40" rx="2" stroke="currentColor" stroke-width="2"/>
            <line x1="31" y1="12" x2="31" y2="52" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3 3"/>
            <circle cx="60" cy="32" r="14" stroke="#F59E0B" stroke-width="2"/>
            <line x1="60" y1="32" x2="67" y2="24" stroke="#F59E0B" stroke-width="2" stroke-linecap="round"/>
            <rect x="76" y="12" width="26" height="40" rx="2" stroke="currentColor" stroke-width="2"/>
            <line x1="8" y1="32" x2="18" y2="32" stroke="currentColor" stroke-width="2"/>
            <line x1="44" y1="32" x2="46" y2="32" stroke="currentColor" stroke-width="2"/>
            <line x1="74" y1="32" x2="76" y2="32" stroke="currentColor" stroke-width="2"/>
            <line x1="102" y1="32" x2="112" y2="32" stroke="currentColor" stroke-width="2"/>
          </svg>"""


def render_product_card_html(product: dict) -> str:
    is_jpc = product.get("brand") == "JPC"
    badge_class = "badge-jpc" if is_jpc else "badge-euro"
    status_class = (
        "status-available"
        if product.get("availabilityStatus") == "available"
        else "status-inquiry"
    )

    cat = product.get("category")
    if cat == "valves":
        third_label = "ولتاژ بوبین / آرایش"
        third_val = f"{product.get('voltage', '')} | {product.get('valveConfiguration', '')}"
    elif cat == "cylinders":
        third_label = "مشخصات کورس و سیلندر"
        third_val = product.get("boreStrokeSpec") or product.get("cylinderType", "")
    else:
        third_label = "مشخصات فنی / دبی"
        third_val = product.get("accessoryType") or product.get("flowRate", "")

    cross_ref_html = ""
    if not is_jpc and product.get("jpcAlternativeId"):
        alt_id = html.escape(product["jpcAlternativeId"])
        alt_code = html.escape(product.get("jpcAlternativeCode", "مشاهده JPC"))
        cross_ref_html = f"""
            <div class="jpc-equivalent-banner">
              <span class="jpc-equivalent-text">
                معادل ابعادی و فنی موجود در برند اختصاصی JPC
              </span>
              <button
                type="button"
                class="jpc-equivalent-switch-btn js-switch-to-jpc"
                data-target-id="{alt_id}"
                title="مشاهده معادل ابعادی و فنی در برند اختصاصی JPC"
              >
                {alt_code} ←
              </button>
            </div>"""
    elif is_jpc and product.get("equivalentTo"):
        sample_equiv = " · ".join(product["equivalentTo"][:3])
        cross_ref_html = f"""
            <div class="equivalent-codes-strip">
              <span>کدهای هم‌ابعاد و معادل فنی:</span>
              <span class="mono" style="font-weight:700; color:var(--steel-accent);">{html.escape(sample_equiv)}</span>
            </div>"""

    pid = html.escape(product["id"])
    pcode = html.escape(product["code"])
    pname_fa = html.escape(product["nameFa"])
    pbrand_fa = html.escape(product["brandFa"])
    pavail_fa = html.escape(product["availabilityFa"])
    pcat_fa = html.escape(product["categoryTitleFa"])
    pport = html.escape(product["portSize"])
    ppress = html.escape(product["pressureRange"])
    pthird_val = html.escape(third_val)
    pdatasheet = html.escape(product["datasheetUrl"])
    svg_markup = get_schematic_svg(product.get("schematicType", ""))

    return f"""          <article class="product-card {'is-jpc-brand' if is_jpc else ''}" id="card-{pid}" data-product-id="{pid}">
            <div>
              <div class="product-card-top">
                <span class="brand-badge {badge_class}">{pbrand_fa}</span>
                <span class="status-badge {status_class}">{pavail_fa}</span>
              </div>

              <div class="product-schematic-box">
                <div class="schematic-svg-wrap">
                  {svg_markup}
                </div>
                <div class="schematic-meta">
                  <div class="product-code-row">
                    <button
                      type="button"
                      class="copy-code-btn js-copy-btn"
                      data-copy="{pcode}"
                      title="کپی کد فنی"
                    >
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                      </svg>
                      <span>کپی</span>
                    </button>
                    <span class="product-code-pill">{pcode}</span>
                  </div>
                  <span class="product-cat-label">{pcat_fa}</span>
                </div>
              </div>

              <div class="product-card-body">
                <h3 class="product-title-fa">{pname_fa}</h3>
                {cross_ref_html}
                <div class="product-specs-table">
                  <div class="spec-cell">
                    <span class="spec-key">سایز پورت (Port)</span>
                    <span class="spec-val mono">{pport}</span>
                  </div>
                  <div class="spec-cell">
                    <span class="spec-key">فشار کاری (Pressure)</span>
                    <span class="spec-val mono">{ppress}</span>
                  </div>
                  <div class="spec-cell spec-cell-wide">
                    <span class="spec-key">{third_label}</span>
                    <span class="spec-val">{pthird_val}</span>
                  </div>
                </div>
              </div>
            </div>

            <div class="product-card-footer">
              <div class="product-card-actions">
                <button
                  type="button"
                  class="btn btn-amber btn-sm js-quote-trigger"
                  data-id="{pid}"
                >
                  درخواست استعلام قیمت
                </button>
                <button
                  type="button"
                  class="btn btn-rfq-add btn-sm js-add-rfq-btn"
                  data-id="{pid}"
                >
                  + افزودن به لیست استعلام
                </button>
              </div>
              <div class="product-sub-links">
                <button
                  type="button"
                  class="product-pdf-link js-spec-trigger"
                  data-id="{pid}"
                >
                  مشاهده مشخصات فنی و کدهای معادل ←
                </button>
                <a
                  href="{pdatasheet}"
                  download
                  class="product-pdf-link"
                >
                  دانلود PDF
                </a>
              </div>
            </div>
          </article>"""


def build_jsonld_itemlist(products: list, page_url: str, category_filter: str) -> str:
    """
    Build rich schema.org ItemList with Product entities including sku, mpn, brand,
    category, additionalProperty technical specs, and B2B inquiry availability.
    """
    list_items = []
    for idx, p in enumerate(products, start=1):
        props = [
            {"@type": "PropertyValue", "name": "Port Size (سایز پورت)", "value": p.get("portSize", "")},
            {"@type": "PropertyValue", "name": "Working Pressure (فشار کاری)", "value": p.get("pressureRange", "")},
            {"@type": "PropertyValue", "name": "Body Material (جنس بدنه)", "value": p.get("bodyMaterial", "")},
            {"@type": "PropertyValue", "name": "Flow / Performance (دبی / عملکرد)", "value": p.get("flowRate", "")},
        ]
        if p.get("voltage"):
            props.append({"@type": "PropertyValue", "name": "Voltage / Sensor (ولتاژ)", "value": p["voltage"]})
        if p.get("boreStrokeSpec"):
            props.append({"@type": "PropertyValue", "name": "Bore & Stroke (قطر و کورس)", "value": p["boreStrokeSpec"]})
        if p.get("equivalentTo"):
            props.append(
                {
                    "@type": "PropertyValue",
                    "name": "Compatible Cross-Reference Codes (کدهای هم‌ابعاد و معادل فنی)",
                    "value": ", ".join(p["equivalentTo"]),
                }
            )

        availability_url = (
            "https://schema.org/InStock"
            if p.get("availabilityStatus") == "available"
            else "https://schema.org/PreOrder"
        )

        product_schema = {
            "@type": "Product",
            "@id": f"{page_url}#product-{p['id']}",
            "sku": p["code"],
            "mpn": p["code"],
            "name": f"{p['nameFa']} ({p['nameEn']})",
            "AlternateName": p["nameEn"],
            "description": f"{p['nameFa']} — کد فنی: {p['code']} | سایز پورت: {p['portSize']} | فشار کاری: {p['pressureRange']} | کاربرد: {p.get('applicationsFa', '')}",
            "image": "https://jalalipneumatic.ir/assets/images/hero-pneumatics.jpg",
            "url": f"{page_url}#card-{p['id']}",
            "category": p["categoryTitleFa"],
            "brand": {
                "@type": "Brand",
                "name": p["brand"],
            },
            "additionalProperty": props,
            "offers": {
                "@type": "Offer",
                "url": f"{page_url}#inquiry",
                "availability": availability_url,
                "itemCondition": "https://schema.org/NewCondition",
                "seller": {
                    "@type": "Organization",
                    "name": "شرکت جلالی پنوماتیک (JPC – Jalali Pneumatic Company)",
                    "url": "https://jalalipneumatic.ir/",
                    "telephone": "+98-912-130-5167",
                    "founder": {
                        "@type": "Person",
                        "name": "امیر جلالی",
                        "alternateName": "Amir Jalali"
                    }
                },
            },
        }

        list_items.append(
            {
                "@type": "ListItem",
                "position": idx,
                "url": f"{page_url}#card-{p['id']}",
                "item": product_schema,
            }
        )

    schema_obj = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "@id": f"{page_url}#catalog-itemlist",
        "name": f"لیست تجهیزات پنوماتیک صنعتی شرکت جلالی پنوماتیک (JPC) - {category_filter}",
        "numberOfItems": len(list_items),
        "itemListElement": list_items,
    }

    json_str = json.dumps(schema_obj, ensure_ascii=False, indent=2)
    return f'<script type="application/ld+json" id="jpc-products-itemlist-schema">\n{json_str}\n  </script>'


def update_html_file(html_path: Path, category_filter: str, page_url: str, all_products: list) -> int:
    content = html_path.read_text(encoding="utf-8")

    if category_filter == "all":
        filtered = all_products
    else:
        filtered = [p for p in all_products if p.get("category") == category_filter]

    cards_html = "\n".join(render_product_card_html(p) for p in filtered)
    ssr_block = f"<!-- SSR_PRODUCTS_START -->\n{cards_html}\n          <!-- SSR_PRODUCTS_END -->"

    content, count_ssr = re.subn(
        r"<!--\s*SSR_PRODUCTS_START\s*-->.*?<!--\s*SSR_PRODUCTS_END\s*-->",
        ssr_block,
        content,
        flags=re.DOTALL,
    )
    if count_ssr == 0:
        raise RuntimeError(f"Missing SSR_PRODUCTS markers in {html_path.name}")

    # Update static result counter text for crawlers
    counter_html = f'نمایش <strong>{len(filtered)}</strong> مدل از <strong>{len(all_products)}</strong> تجهیز کاتالوگ'
    content = re.sub(
        r'(<div\s+class="catalog-result-counter"\s+id="catalog-result-counter">)(.*?)(</div>)',
        rf"\1{counter_html}\3",
        content,
        flags=re.DOTALL,
    )

    # Inject ItemList JSON-LD
    jsonld_block = (
        f"<!-- SSR_JSONLD_PRODUCTS_START -->\n  "
        f"{build_jsonld_itemlist(filtered, page_url, category_filter)}\n  "
        f"<!-- SSR_JSONLD_PRODUCTS_END -->"
    )
    content, count_jsonld = re.subn(
        r"<!--\s*SSR_JSONLD_PRODUCTS_START\s*-->.*?<!--\s*SSR_JSONLD_PRODUCTS_END\s*-->",
        jsonld_block,
        content,
        flags=re.DOTALL,
    )
    if count_jsonld == 0:
        raise RuntimeError(f"Missing SSR_JSONLD_PRODUCTS markers in {html_path.name}")

    html_path.write_text(content, encoding="utf-8")
    return len(filtered)


def generate_llms_full_txt(products: list, out_path: Path) -> None:
    """
    Generate llms-full.txt with complete bilingual entity profile, dual-sourcing architecture,
    E-E-A-T contact signals, and full Markdown catalog table + detailed product specifications.
    """
    lines = [
        "# شرکت جلالی پنوماتیک | JPC – Jalali Pneumatic Company (Full AI & Technical Catalog Reference)",
        "",
        "> **شرکت جلالی پنوماتیک (`JPC – Jalali Pneumatic Company`) با مدیریت امیر جلالی (`Amir Jalali`)**؛ واردکننده، تأمین‌کننده و توزیع‌کننده تخصصی تجهیزات پنوماتیک صنعتی و سیستم‌های اتوماسیون مبتنی بر هوای فشرده در ایران (تهران، محدوده بازار صنعتی / لالهزار).",
        "> **Jalali Pneumatic Company (`JPC`)**, founded and managed by **Amir Jalali (امیر جلالی)**, is an Iranian B2B industrial importer, supplier, and distributor of pneumatic components and compressed-air automation systems (`jpciran.com` / `jalalipneumatic.ir`), offering both international European brands (`Festo`, `Norgren`, `Bosch Rexroth`), reliable Asian industrial supply, and its proprietary commercial brand **`JPC`**.",
        "",
        "---",
        "",
        "## 1. Bilingual Corporate Identity & E-E-A-T Profile (هویت شرکت و مدیریت مجموعه)",
        "",
        "- **Persian Name (نام فارسی):** شرکت جلالی پنوماتیک (با مدیریت امیر جلالی)",
        "- **English Name (نام انگلیسی):** Jalali Pneumatic Company (`JPC`)",
        "- **Founder & Managing Director (مؤسس و مدیریت مجموعه):** امیر جلالی (`Amir Jalali`)",
        "- **Proprietary Commercial Brand (برند تجاری اختصاصی):** `JPC` (`JPC – Jalali Pneumatic Company`)",
        "- **Official Domains (دامنه‌های رسمی):** `https://jpciran.com` | `https://jalalipneumatic.ir`",
        "- **Business Activity (حوزه فعالیت):** واردات، تأمین و توزیع تجهیزات پنوماتیک صنعتی و اتوماسیون هوای فشرده (Industrial Pneumatics Importer, Supplier & B2B Distributor)",
        "- **Primary Market & Location (موقعیت مرکز فروش و تأمین):** تهران، محدوده بازار صنعتی / لالهزار (تأمین و ارسال سریع به سراسر کشور) | Tehran Industrial Market / Lalehzar District (Nationwide B2B Shipping across Iran)",
        "- **Direct Mobile & WhatsApp B2B Sales (شماره تماس مستقیم و واتساپ استعلام قیمت):** `+98-912-130-5167` / `00989121305167` / `0912 130 5167` (`https://wa.me/989121305167`)",
        "- **Sales Landline (تلفن ثابت واحد فروش):** `+98-21-33900000` (`021-33900000`)",
        "- **Telegram Sales Engineering (تلگرام مهندسی فروش):** `@JalaliPneumatic_Sales` (`https://t.me/JalaliPneumatic_Sales`)",
        "- **Email (پست الکترونیک بازرگانی):** `sales@jalalipneumatic.ir`",
        "- **Working Hours (ساعات کاری):** شنبه تا چهارشنبه ۸:۳۰ الی ۱۷:۳۰ | پنجشنبه ۸:۳۰ الی ۱۳:۳۰ (`Sat-Wed 08:30-17:30, Thu 08:30-13:30 IRST`)",
        "- **Canonical Website:** `https://jalalipneumatic.ir/` (`https://jpciran.com/`)",
        "",
        "---",
        "",
        "## 2. Dual-Sourcing & Multi-Brand Architecture (معماری تأمین دوگانه و چندبرنده)",
        "",
        "1. **Proprietary Commercial Brand (`JPC – Jalali Pneumatic Company`):**",
        "   - Imported pneumatic product line marketed under the company's proprietary commercial brand `JPC`.",
        "   - Engineered for dimensional and technical compatibility (`تطابق ابعادی و فنی`) with international standards (`ISO 15552` profile cylinders, `ISO 6432` mini cylinders, `3/2`, `5/2`, and `5/3` directional solenoid valves, and modular `FRL` air preparation units).",
        "2. **European Industrial Brands Supply (`تأمین برندهای معتبر اروپایی`):**",
        "   - Sourcing and supplying pneumatic components from European markets including **Festo (فستو)**, **Norgren (نورگرن)**, and **Bosch & Bosch Rexroth (بوش و بوش رکسروت)** for high-sensitivity production lines and machinery MRO.",
        "3. **Asian / Chinese Industrial Tier (`تأمین از سازندگان معتبر آسیایی/چینی`):**",
        "   - Cost-effective pneumatic components, push-in fittings, polyurethane (`PU`) tubing, and flow control valves for OEM machine builders and high-volume workshops.",
        "",
        "---",
        "",
        "## 3. Complete Product Catalog Table (جدول کامل محصولات و معادل‌های فنی)",
        "",
        "| ردیف | کد فنی مدل (SKU / Code) | نام فارسی تجهیز | English Product Name | برند (Brand) | سایز پورت (Port) | فشار کاری (Pressure) | کدهای هم‌ابعاد و معادل فنی (Compatible Equivalents) |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]

    for idx, p in enumerate(products, start=1):
        equivs = ", ".join(p.get("equivalentTo", []))
        lines.append(
            f"| {idx} | `{p['code']}` | {p['nameFa']} | {p['nameEn']} | **{p['brand']}** | `{p['portSize']}` | `{p['pressureRange']}` | `{equivs}` |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## 4. Detailed Technical Specifications by Product (مشخصات فنی تفصیلی تک‌تک مدل‌ها)",
            "",
        ]
    )

    for p in products:
        equivs = ", ".join(p.get("equivalentTo", []))
        keywords = "، ".join(p.get("keywords", []))
        lines.extend(
            [
                f"### {p['code']} — {p['nameFa']}",
                f"- **English Title:** {p['nameEn']}",
                f"- **Brand:** {p['brandFa']} (`{p['brand']}`)",
                f"- **Category:** {p['categoryTitleFa']} (`{p['category']}`)",
                f"- **Port Size:** `{p['portSize']}`",
                f"- **Working Pressure:** `{p['pressureRange']}`",
                f"- **Voltage / Actuation:** `{p.get('voltage', 'N/A')}`",
                f"- **Body Material:** {p.get('bodyMaterial', '')}",
                f"- **Flow Rate / Cushioning:** {p.get('flowRate', '')}",
                f"- **Operating Temperature:** `{p.get('operatingTemp', '')}`",
                f"- **Standard / Protection Class:** `{p.get('protectionClass', '')}`",
                f"- **Compatible Equivalent Codes (Cross-Reference):** `{equivs}`",
                f"- **Iranian Market Keywords:** {keywords}",
                f"- **Industrial Applications:** {p.get('applicationsFa', '')}",
                f"- **Technical Datasheet PDF:** `https://jalalipneumatic.ir/{p['datasheetUrl']}`",
                "",
            ]
        )

    lines.extend(
        [
            "---",
            "",
            "## 5. Key Pages & Technical Tools (صفحات تخصصی و ابزارهای مهندسی سایت)",
            "",
            "- **Main Catalog & Cylinder Force Calculator:** `https://jalalipneumatic.ir/`",
            "- **Pneumatic Solenoid Valves (شیرهای برقی پنوماتیک 3/2, 5/2, 5/3):** `https://jalalipneumatic.ir/solenoid-valves.html`",
            "- **Pneumatic Cylinders (جک‌های پنوماتیک پروفیلی، چهارمیل، کامپکت، قلمی و رادلس):** `https://jalalipneumatic.ir/pneumatic-cylinders.html`",
            "- **FRL Air Preparation & Accessories (واحد مراقبت هوا، فلوکنترل، فیتینگ و شیلنگ PU):** `https://jalalipneumatic.ir/frl-accessories.html`",
            "- **Concise LLM Overview:** `https://jalalipneumatic.ir/llms.txt`",
            "- **XML Sitemap:** `https://jalalipneumatic.ir/sitemap.xml`",
            "",
        ]
    )

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    products = parse_products_from_js(PRODUCTS_JS_PATH)
    print(f"[build-seo] Parsed {len(products)} products from {PRODUCTS_JS_PATH.name}")

    for filename, cat_filter, page_url in PAGE_TARGETS:
        html_path = ROOT_DIR / filename
        rendered_count = update_html_file(html_path, cat_filter, page_url, products)
        print(f"[build-seo] Injected {rendered_count} SSR product cards + ItemList JSON-LD into {filename}")

    generate_llms_full_txt(products, LLMS_FULL_PATH)
    print(f"[build-seo] Generated {LLMS_FULL_PATH.name} ({LLMS_FULL_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
