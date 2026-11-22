#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jalali Pneumatic Company (JPC) - Static SEO, GEO & Multi-Page Sync Build Script
Zero-dependency Python 3 script that:
1. Parses PRODUCTS_DATA from assets/js/products-data.js
2. Pre-renders crawlable HTML product cards between <!-- SSR_PRODUCTS_START --> and <!-- SSR_PRODUCTS_END -->
   in index.html, solenoid-valves.html, pneumatic-cylinders.html, and frl-accessories.html.
3. Injects rich ItemList + Product JSON-LD structured data (with sku, mpn, model, brand, manufacturer,
   additionalProperty technical specs, and zero incomplete Offer blocks)
   between <!-- SSR_JSONLD_PRODUCTS_START --> and <!-- SSR_JSONLD_PRODUCTS_END -->.
4. Synchronizes the Part 1/2/3 Industrial Design System Utility Bar, Sticky Header, Mobile Drawer,
   RFQ Basket Drawer, Footer, and cache-busted deferred asset links (?v=20261122) across ALL 9 HTML pages,
   and normalizes JSON-LD so Organization.founder ("امیر جلالی") appears once in JSON-LD and <=3 times visibly.
5. Regenerates llms.txt, llms-full.txt, sitemap.xml, and robots.txt cleanly.
"""

import html
import json
import re
from datetime import date
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PRODUCTS_JS_PATH = ROOT_DIR / "assets" / "js" / "products-data.js"
LLMS_TXT_PATH = ROOT_DIR / "llms.txt"
LLMS_FULL_PATH = ROOT_DIR / "llms-full.txt"
SITEMAP_PATH = ROOT_DIR / "sitemap.xml"
ROBOTS_PATH = ROOT_DIR / "robots.txt"

ASSET_VERSION = "20261122"

ALL_HTML_PAGES = [
    "index.html",
    "solenoid-valves.html",
    "pneumatic-cylinders.html",
    "frl-accessories.html",
    "festo-cross-reference.html",
    "pneumatic-cylinder-buying-guide.html",
    "solenoid-valve-guide.html",
    "pneumatics-lalehzar-tehran.html",
    "what-is-pneumatics-jpc.html",
]

PAGE_TARGETS = [
    ("index.html", "all", "https://jpciran.com/"),
    ("solenoid-valves.html", "valves", "https://jpciran.com/solenoid-valves.html"),
    ("pneumatic-cylinders.html", "cylinders", "https://jpciran.com/pneumatic-cylinders.html"),
    ("frl-accessories.html", "frl-accessories", "https://jpciran.com/frl-accessories.html"),
]


def parse_products_from_js(js_path: Path) -> list:
    """
    Pure Python 3 parser that extracts PRODUCTS_DATA array from assets/js/products-data.js
    without requiring Node.js or any external packages.
    """
    raw = js_path.read_text(encoding="utf-8")

    match = re.search(
        r"const\s+PRODUCTS_DATA\s*=\s*(\[.*?\])\s*;\s*(?:/\*|const\s+PRODUCT_FAMILIES|window\.PRODUCT_CATEGORIES)",
        raw,
        flags=re.DOTALL,
    )
    if not match:
        raise ValueError("Could not locate PRODUCTS_DATA array in products-data.js")

    js_array = match.group(1)

    cleaned_lines = []
    for line in js_array.splitlines():
        stripped = line.strip()
        if stripped.startswith("//"):
            continue
        cleaned_lines.append(line)
    js_clean = "\n".join(cleaned_lines)

    def replace_single_quoted(m: re.Match) -> str:
        inner = m.group(1)
        inner_escaped = inner.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{inner_escaped}"'

    js_clean = re.sub(r"'([^'\\]*(?:\\.[^'\\]*)*)'", replace_single_quoted, js_clean)
    js_clean = re.sub(r"(?m)^(\s*)([a-zA-Z_][a-zA-Z0-9_]*)\s*:", r'\1"\2":', js_clean)
    js_clean = re.sub(r",\s*([}\]])", r"\1", js_clean)

    return json.loads(js_clean)


def get_schematic_svg(schematic_type: str) -> str:
    if schematic_type in ("valve-5-2", "valve-5-2-double", "valve-5-3"):
        return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="20" y="14" width="40" height="36" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="60" y="14" width="40" height="36" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="6" y="22" width="14" height="20" rx="1" stroke="#F28C28" stroke-width="2"/>
            <line x1="9" y1="38" x2="17" y2="26" stroke="#F28C28" stroke-width="1.8"/>
            <path d="M100 26L106 20L110 32L114 20L118 26" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            <line x1="32" y1="50" x2="32" y2="14" stroke="currentColor" stroke-width="1.8"/>
            <polygon points="32,14 29,20 35,20" fill="currentColor"/>
            <line x1="48" y1="14" x2="48" y2="50" stroke="currentColor" stroke-width="1.8"/>
            <polygon points="48,50 45,44 51,44" fill="currentColor"/>
            <line x1="72" y1="50" x2="88" y2="14" stroke="#F28C28" stroke-width="1.8"/>
            <circle cx="32" cy="8" r="2.2" fill="currentColor"/>
            <circle cx="48" cy="8" r="2.2" fill="currentColor"/>
            <circle cx="40" cy="56" r="2.2" fill="#F28C28"/>
          </svg>"""
    if schematic_type == "valve-3-2":
        return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="24" y="14" width="36" height="36" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="60" y="14" width="36" height="36" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="10" y="22" width="14" height="20" rx="1" stroke="#F28C28" stroke-width="2"/>
            <line x1="12" y1="38" x2="21" y2="26" stroke="#F28C28" stroke-width="1.8"/>
            <line x1="42" y1="50" x2="42" y2="14" stroke="currentColor" stroke-width="1.8"/>
            <polygon points="42,14 39,20 45,20" fill="currentColor"/>
            <line x1="74" y1="38" x2="82" y2="38" stroke="#F28C28" stroke-width="2"/>
            <line x1="78" y1="38" x2="78" y2="50" stroke="#F28C28" stroke-width="2"/>
            <path d="M96 28L102 22L106 34L110 22L114 28" stroke="currentColor" stroke-width="1.8"/>
          </svg>"""
    if schematic_type in ("cylinder-double", "cylinder-tierod"):
        return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="14" y="14" width="72" height="36" rx="3" stroke="currentColor" stroke-width="2"/>
            <line x1="46" y1="14" x2="46" y2="50" stroke="#F28C28" stroke-width="3"/>
            <line x1="46" y1="32" x2="112" y2="32" stroke="currentColor" stroke-width="4"/>
            <rect x="108" y="25" width="6" height="14" rx="1" fill="#F28C28"/>
            <line x1="22" y1="14" x2="22" y2="6" stroke="currentColor" stroke-width="2"/>
            <line x1="78" y1="14" x2="78" y2="6" stroke="currentColor" stroke-width="2"/>
            <line x1="14" y1="20" x2="86" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
            <line x1="14" y1="44" x2="86" y2="44" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
          </svg>"""
    if schematic_type in ("cylinder-compact", "cylinder-mini"):
        return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="24" y="12" width="52" height="40" rx="3" stroke="currentColor" stroke-width="2"/>
            <line x1="50" y1="12" x2="50" y2="52" stroke="#F28C28" stroke-width="3"/>
            <line x1="50" y1="32" x2="104" y2="32" stroke="currentColor" stroke-width="4.5"/>
            <circle cx="34" cy="22" r="2.5" fill="currentColor"/>
            <circle cx="66" cy="22" r="2.5" fill="currentColor"/>
            <circle cx="34" cy="42" r="2.5" fill="currentColor"/>
            <circle cx="66" cy="42" r="2.5" fill="currentColor"/>
          </svg>"""
    if schematic_type == "cylinder-rodless":
        return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="10" y="24" width="100" height="22" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="44" y="12" width="32" height="12" rx="2" stroke="#F28C28" stroke-width="2"/>
            <line x1="60" y1="24" x2="60" y2="46" stroke="#F28C28" stroke-width="2.5"/>
            <line x1="18" y1="35" x2="102" y2="35" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
          </svg>"""
    return """<svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="18" y="12" width="26" height="40" rx="2" stroke="currentColor" stroke-width="2"/>
            <line x1="31" y1="12" x2="31" y2="52" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3 3"/>
            <circle cx="60" cy="32" r="14" stroke="#F28C28" stroke-width="2"/>
            <line x1="60" y1="32" x2="67" y2="24" stroke="#F28C28" stroke-width="2" stroke-linecap="round"/>
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
                <span class="mono" dir="ltr">{alt_code}</span> ←
              </button>
            </div>"""
    elif is_jpc and product.get("equivalentTo"):
        sample_equiv = " · ".join(product["equivalentTo"][:3])
        cross_ref_html = f"""
            <div class="equivalent-codes-strip">
              <span>کدهای هم‌ابعاد و معادل فنی:</span>
              <span class="mono" dir="ltr" style="font-weight:700; color:var(--steel-accent);">{html.escape(sample_equiv)}</span>
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
                    <span class="product-code-pill" dir="ltr">{pcode}</span>
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
                    <span class="spec-val mono" dir="ltr">{pport}</span>
                  </div>
                  <div class="spec-cell">
                    <span class="spec-key">فشار کاری (Pressure)</span>
                    <span class="spec-val mono" dir="ltr">{ppress}</span>
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
    Build schema.org ItemList with technical Product specification entities
    (sku, mpn, model, brand, manufacturer, additionalProperty) for B2B quotation
    catalogs without incomplete Offer blocks or invalid category strings.
    """
    list_items = []
    for idx, p in enumerate(products, start=1):
        props = [
            {"@type": "PropertyValue", "name": "Category (دسته‌بندی)", "value": p.get("categoryTitleFa", "")},
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

        product_schema = {
            "@type": "Product",
            "@id": f"{page_url}#product-{p['id']}",
            "sku": p["code"],
            "mpn": p["code"],
            "model": p["code"],
            "name": f"{p['nameFa']} ({p['nameEn']})",
            "alternateName": p["nameEn"],
            "description": f"{p['nameFa']} — کد فنی: {p['code']} | سایز پورت: {p['portSize']} | فشار کاری: {p['pressureRange']} | کاربرد: {p.get('applicationsFa', '')}",
            "image": "https://jpciran.com/assets/images/hero-pneumatics.jpg",
            "url": f"{page_url}#card-{p['id']}",
            "brand": {
                "@type": "Brand",
                "name": p["brand"],
            },
            "manufacturer": {
                "@type": "Organization",
                "name": p["brand"],
            },
            "additionalProperty": props,
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


def build_shared_header_and_drawers(filename: str) -> str:
    """
    Build the unified Section A (Utility Bar), Section B (Sticky Main Header),
    Mobile Navigation Drawer, and Multi-Item RFQ Slide-Over Drawer for any page.
    On index.html, anchor links point to #catalog, #sourcing, etc.
    On subpages, anchor links point to index.html#catalog, index.html#sourcing, etc.
    """
    is_home = filename == "index.html"
    prefix = "" if is_home else "index.html"

    nav_products_active = ' active' if filename in ("index.html", "solenoid-valves.html", "pneumatic-cylinders.html", "frl-accessories.html") else ''
    nav_xref_active = ' active' if filename == "festo-cross-reference.html" else ''
    nav_docs_active = ' active' if filename in ("what-is-pneumatics-jpc.html", "pneumatic-cylinder-buying-guide.html", "solenoid-valve-guide.html") else ''
    nav_about_active = ' active' if filename == "pneumatics-lalehzar-tehran.html" else ''

    return f"""  <!-- ===================================================================
       SECTION A — UTILITY BAR
       =================================================================== -->
  <div class="top-tech-bar">
    <div class="container top-tech-bar-inner">
      <div class="top-tech-items">
        <span class="top-tech-item">
          <span class="top-tech-dot"></span>
          <span>شرکت جلالی پنوماتیک (<strong class="mono" dir="ltr" style="color: #F28C28;">JPC</strong>) — تهران، لالهزار جنوبی، روبروی کوچه علیپور، پاساژ رزاقمنش، پلاک ۱</span>
        </span>
        <span class="top-tech-item">
          <span>تلفن‌های ثابت:</span>
          <a href="tel:+982133110796" class="mono" dir="ltr" style="color: #F5F7FA; font-weight: 700;">021-33110796</a>
          <span>|</span>
          <a href="tel:+982133932529" class="mono" dir="ltr" style="color: #F5F7FA; font-weight: 700;">021-33932529</a>
        </span>
        <span class="top-tech-item">
          <span>ساعات کاری:</span>
          <span>شنبه تا پنجشنبه ۰۹:۰۰ تا ۱۸:۰۰</span>
        </span>
      </div>
      <div class="top-tech-items">
        <span class="top-tech-item">
          <span>همراه و واتساپ:</span>
          <a href="tel:+989121305167" class="mono" dir="ltr" style="color: #20B47C; font-weight: 700;">09121305167</a>
        </span>
        <a href="https://wa.me/989121305167" target="_blank" rel="noopener noreferrer" class="top-tech-item" style="color: #20B47C; font-weight: 700;">
          <span>پشتیبانی و استعلام واتساپ</span>
        </a>
        <a href="https://ai.jpciran.com" target="_blank" rel="noopener noreferrer" class="top-tech-item" style="color: #F28C28; font-weight: 700;">
          <span>دستیار هوشمند تشخیص پلاک AI</span>
        </a>
      </div>
    </div>
  </div>

  <!-- ===================================================================
       SECTION B — STICKY MAIN HEADER
       =================================================================== -->
  <header class="site-header" id="top">
    <div class="container header-inner">
      <a href="index.html" class="brand-logo" aria-label="شرکت جلالی پنوماتیک (JPC) - صفحه اصلی">
        <div class="brand-mark">JPC</div>
        <div class="brand-text">
          <span class="brand-name-fa">شرکت جلالی پنوماتیک (JPC)</span>
          <span class="brand-name-sub">JALALI PNEUMATIC CO.</span>
          <span class="brand-owner-sub">با مدیریت امیر جلالی</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="ناوبری اصلی">
        <a href="{prefix}#catalog" class="nav-link{nav_products_active}">محصولات</a>
        <a href="{prefix}#sourcing" class="nav-link">
          <span>برندها</span>
          <span class="nav-link-badge" dir="ltr">JPC</span>
        </a>
        <a href="festo-cross-reference.html" class="nav-link{nav_xref_active}">معادلیابی قطعات</a>
        <a href="{prefix}#calculator" class="nav-link">ابزارهای مهندسی</a>
        <a href="what-is-pneumatics-jpc.html" class="nav-link{nav_docs_active}">مقالات تخصصی</a>
        <a href="pneumatics-lalehzar-tehran.html" class="nav-link{nav_about_active}">درباره ما</a>
        <a href="https://ai.jpciran.com" target="_blank" rel="noopener noreferrer" class="nav-link nav-link-ai">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9L12 3z"></path><path d="M5 3v4M3 5h4M19 17v4M17 19h4"></path></svg>
          <span>دستیار هوشمند تشخیص پلاک AI</span>
        </a>
      </nav>

      <div class="header-actions">
        <!-- Quick Technical Search Trigger -->
        <button
          type="button"
          class="header-search-trigger-btn js-focus-tech-search"
          id="header-search-trigger-btn"
          aria-label="جستجوی کد فنی"
          title="جستجوی کد فنی و مشخصات"
        >
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </button>

        <!-- Multi-Item RFQ Drawer Trigger Button -->
        <button
          type="button"
          class="header-rfq-btn js-open-rfq-drawer"
          id="header-rfq-btn"
          aria-label="مشاهده سبد استعلام چندقلمی"
        >
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
            <path d="M9 11l3 3L22 4"></path>
            <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path>
          </svg>
          <span class="header-rfq-label">سبد استعلام</span>
          <span class="rfq-count-pill js-rfq-count" id="header-rfq-count">0</span>
        </button>

        <button
          type="button"
          class="theme-toggle-btn"
          id="theme-toggle-btn"
          aria-label="تغییر تم روشن و تاریک"
          title="تغییر حالت نمایش (روشن / تاریک)"
        >
          <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
          </svg>
          <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="5"></circle>
            <line x1="12" y1="1" x2="12" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="23"></line>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
            <line x1="1" y1="12" x2="3" y2="12"></line>
            <line x1="21" y1="12" x2="23" y2="12"></line>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
          </svg>
        </button>

        <a href="https://wa.me/989121305167" target="_blank" rel="noopener noreferrer" class="btn btn-outline-tech btn-sm header-cta-desktop header-cta-secondary">
          <span>مشاوره فنی</span>
        </a>

        <a href="{prefix}#inquiry" class="btn btn-amber btn-sm header-cta-desktop">
          <span>استعلام قیمت</span>
        </a>

        <button
          type="button"
          class="mobile-menu-btn"
          id="mobile-menu-btn"
          aria-label="باز کردن منوی موبایل"
        >
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Navigation Drawer -->
  <div class="mobile-drawer-backdrop" id="mobile-drawer-backdrop"></div>
  <aside class="mobile-drawer" id="mobile-drawer" aria-label="منوی موبایل" aria-hidden="true">
    <div>
      <div class="mobile-drawer-header">
        <div class="brand-logo">
          <div class="brand-mark">JPC</div>
          <div class="brand-text">
            <span class="brand-name-fa">شرکت جلالی پنوماتیک (JPC)</span>
            <span class="brand-name-sub">JALALI PNEUMATIC CO.</span>
          </div>
        </div>
        <button type="button" class="mobile-drawer-close" id="mobile-drawer-close" aria-label="بستن منو">
          ✕
        </button>
      </div>

      <nav class="mobile-nav-list" aria-label="منوی ناوبری موبایل">
        <a href="https://ai.jpciran.com" target="_blank" rel="noopener noreferrer" class="mobile-nav-link mobile-nav-link-ai">
          <span style="display:inline-flex; align-items:center; gap:0.4rem;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9L12 3z"></path><path d="M5 3v4M3 5h4M19 17v4M17 19h4"></path></svg><span>دستیار هوشمند تشخیص پلاک AI</span></span>
          <span class="mono" dir="ltr">AI</span>
        </a>
        <a href="{prefix}#catalog" class="mobile-nav-link">
          <span>محصولات (کاتالوگ جامع)</span>
          <span class="mono" dir="ltr">ALL</span>
        </a>
        <a href="{prefix}#sourcing" class="mobile-nav-link">
          <span>برندها (JPC و برندهای اروپایی)</span>
          <span class="nav-link-badge" dir="ltr">JPC</span>
        </a>
        <a href="festo-cross-reference.html" class="mobile-nav-link">
          <span>معادلیابی قطعات</span>
          <span class="mono" dir="ltr">X-REF</span>
        </a>
        <a href="{prefix}#calculator" class="mobile-nav-link">
          <span>ابزارهای مهندسی (محاسبه‌گر نیروی جک)</span>
          <span class="mono" dir="ltr">N / kgf</span>
        </a>
        <a href="what-is-pneumatics-jpc.html" class="mobile-nav-link">
          <span>مقالات تخصصی پنوماتیک</span>
          <span class="mono" dir="ltr">DOCS</span>
        </a>
        <a href="pneumatics-lalehzar-tehran.html" class="mobile-nav-link">
          <span>درباره ما (فروشگاه لالهزار تهران)</span>
          <span class="mono" dir="ltr">ABOUT</span>
        </a>
        <a href="solenoid-valves.html" class="mobile-nav-link">
          <span>شیرهای برقی پنوماتیک</span>
          <span class="mono" dir="ltr">3/2 · 5/2</span>
        </a>
        <a href="pneumatic-cylinders.html" class="mobile-nav-link">
          <span>جک‌های پنوماتیک</span>
          <span class="mono" dir="ltr">ISO</span>
        </a>
        <a href="frl-accessories.html" class="mobile-nav-link">
          <span>واحد مراقبت هوا و اتصالات</span>
          <span class="mono" dir="ltr">FRL</span>
        </a>
        <a href="pneumatic-cylinder-buying-guide.html" class="mobile-nav-link">
          <span>راهنمای خرید جک پنوماتیک</span>
          <span class="mono" dir="ltr">GUIDE</span>
        </a>
        <a href="solenoid-valve-guide.html" class="mobile-nav-link">
          <span>راهنمای انتخاب شیر برقی</span>
          <span class="mono" dir="ltr">GUIDE</span>
        </a>
        <a href="{prefix}#inquiry" class="mobile-nav-link">
          <span>استعلام قیمت و مشاوره فنی</span>
          <span class="mono" dir="ltr">RFQ</span>
        </a>
      </nav>
    </div>

    <div class="mobile-drawer-footer">
      <button type="button" class="btn btn-rfq-add js-open-rfq-drawer" style="width: 100%; justify-content: center;">
        <span>مشاهده سبد استعلام چندقلمی</span>
        <span class="rfq-count-pill js-rfq-count">0</span>
      </button>
      <a
        href="https://wa.me/989121305167"
        target="_blank"
        rel="noopener noreferrer"
        class="btn btn-amber"
        style="width: 100%; justify-content: center;"
      >
        <span>مشاوره فنی و استعلام واتساپ</span>
      </a>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.4rem;">
        <a
          href="tel:+982133110796"
          class="btn btn-outline-tech btn-sm"
          style="width: 100%; justify-content: center;"
        >
          <span class="mono" dir="ltr">021-33110796</span>
        </a>
        <a
          href="tel:+982133932529"
          class="btn btn-outline-tech btn-sm"
          style="width: 100%; justify-content: center;"
        >
          <span class="mono" dir="ltr">021-33932529</span>
        </a>
      </div>
    </div>
  </aside>

  <!-- ===================================================================
       MULTI-ITEM RFQ SLIDE-OVER DRAWER (سبد استعلام قیمت چندقلمی)
       =================================================================== -->
  <div class="rfq-drawer-backdrop" id="rfq-drawer-backdrop"></div>
  <aside class="rfq-drawer" id="rfq-drawer" aria-label="سبد استعلام قیمت چندقلمی" aria-hidden="true">
    <div class="rfq-drawer-header">
      <div>
        <span class="mono" dir="ltr" style="font-size: 0.72rem; color: #F28C28;">MULTI-ITEM B2B RFQ LIST</span>
        <h3 style="font-size: 1.08rem; font-weight: 800; color: #FFFFFF;">
          لیست استعلام قیمت چندقلمی (BOM)
        </h3>
      </div>
      <div style="display:flex; align-items:center; gap:0.5rem;">
        <button
          type="button"
          class="btn btn-outline-light btn-xs"
          id="rfq-clear-btn"
          style="display:none;"
        >
          پاک کردن لیست
        </button>
        <button type="button" class="modal-close-btn" id="rfq-drawer-close" aria-label="بستن سبد استعلام">
          ✕
        </button>
      </div>
    </div>

    <div class="rfq-drawer-body" id="rfq-drawer-body"></div>

    <div class="rfq-drawer-footer">
      <button
        type="button"
        class="btn btn-amber"
        id="rfq-populate-form-btn"
        style="width: 100%; justify-content: center;"
      >
        <span>درج کل لیست در فرم استعلام رسمی B2B</span>
      </button>
      <div style="display:grid; grid-template-columns: 1.3fr 0.7fr; gap:0.5rem;">
        <a
          href="https://wa.me/989121305167"
          target="_blank"
          rel="noopener noreferrer"
          class="btn btn-steel btn-sm"
          id="rfq-send-whatsapp-btn"
          style="justify-content: center;"
        >
          ارسال لیست استعلام در واتساپ
        </a>
        <a
          href="https://t.me/JalaliPneumatic_Sales"
          target="_blank"
          rel="noopener noreferrer"
          class="btn btn-telegram btn-sm"
          id="rfq-send-telegram-btn"
          style="justify-content: center;"
        >
          ارسال در تلگرام
        </a>
      </div>
    </div>
  </aside>

  <main>"""


def build_shared_footer(filename: str) -> str:
    is_home = filename == "index.html"
    prefix = "" if is_home else "index.html"
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="brand-logo" style="margin-bottom: 1rem;">
            <div class="brand-mark">JPC</div>
            <div class="brand-text">
              <span class="brand-name-fa" style="color: #FFFFFF;">شرکت جلالی پنوماتیک (JPC)</span>
              <span class="brand-name-sub" style="color: #94A3B8;">JALALI PNEUMATIC COMPANY</span>
            </div>
          </div>
          <p style="font-size: 0.86rem; line-height: 1.8; color: #94A3B8;">
            <strong>شرکت جلالی پنوماتیک (JPC)</strong>؛ تأمین‌کننده و توزیع‌کننده تخصصی تجهیزات پنوماتیک صنعتی و اتوماسیون مبتنی بر هوای فشرده در لالهزار جنوبی تهران.
          </p>
          <div class="footer-eeat-box">
            <div><strong>آدرس فروشگاه:</strong> تهران، لالهزار جنوبی، روبروی کوچه علیپور، پاساژ رزاقمنش، پلاک ۱</div>
            <div><strong>تلفن‌های ثابت:</strong> <a href="tel:+982133110796" class="mono" dir="ltr" style="color:#22B8CF;">021-33110796</a> | <a href="tel:+982133932529" class="mono" dir="ltr" style="color:#22B8CF;">021-33932529</a></div>
            <div><strong>همراه و واتساپ:</strong> <a href="tel:+989121305167" class="mono" dir="ltr" style="color:#20B47C; font-weight:700;">09121305167</a> (<a href="https://wa.me/989121305167" target="_blank" rel="noopener noreferrer" class="mono" dir="ltr" style="color:#F28C28;">واتساپ مستقیم</a>)</div>
            <div><strong>ساعات کاری:</strong> شنبه تا پنجشنبه ۰۹:۰۰ تا ۱۸:۰۰ | <a href="https://www.google.com/maps/search/?api=1&query=%D8%AA%D9%87%D8%B1%D8%A7%D9%86+%D9%84%D8%A7%D9%84%D9%87+%D8%B2%D8%A7%D8%B1+%D8%AC%D9%86%D9%88%D8%A8%DB%8C+%D8%B1%D9%88%D8%A8%D8%B1%D9%88%DB%8C+%DA%A9%D9%88%DA%86%D9%87+%D8%B9%D9%84%DB%8C%D9%BE%D9%88%D8%B1+%D9%BE%D8%A7%D8%B3%D8%A7%DA%98+%D8%B1%D8%B2%D8%A7%D9%82+%D9%85%D9%86%D8%B4+%D9%BE%D9%84%D8%A7%DA%A9+%DB%B1" target="_blank" rel="noopener noreferrer" style="color:#F28C28; text-decoration:underline;">مسیریابی در گوگل مپ</a></div>
          </div>
        </div>

        <div>
          <h4 class="footer-col-title">دسته‌بندی محصولات</h4>
          <ul class="footer-links">
            <li><a href="solenoid-valves.html">شیرهای برقی پنوماتیک (3/2, 5/2, 5/3)</a></li>
            <li><a href="pneumatic-cylinders.html">جک و سیلندر پنوماتیک (پروفیلی، چهارمیل، کامپکت)</a></li>
            <li><a href="frl-accessories.html">واحد مراقبت هوا (FRL)، رگولاتور و مانومتر</a></li>
            <li><a href="frl-accessories.html">اتصالات، شیلنگ پنوماتیک و شیر فلوکنترل</a></li>
            <li><a href="{prefix}#categories">مرور هر ۹ گروه کالایی پنوماتیک</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-title">برندها و ابزارهای مهندسی</h4>
          <ul class="footer-links">
            <li><a href="{prefix}#jpc-brand">برند تجاری اختصاصی JPC</a></li>
            <li><a href="{prefix}#sourcing">تأمین و معادل‌یابی Festo، Norgren و Bosch Rexroth</a></li>
            <li><a href="{prefix}#calculator">محاسبه‌گر نیروی سیلندر پنوماتیک (N / kgf)</a></li>
            <li><a href="festo-cross-reference.html">ابزار معادل‌یابی کدهای فنی پنوماتیک</a></li>
            <li><a href="https://ai.jpciran.com" target="_blank" rel="noopener noreferrer" style="color:#F28C28; font-weight:700;">دستیار هوشمند تشخیص پلاک AI</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-title">مقالات تخصصی و نقشه‌های سایت</h4>
          <ul class="footer-links">
            <li><a href="festo-cross-reference.html">جدول معادل‌یابی فستو، نورگرن و رکسروت به JPC</a></li>
            <li><a href="pneumatic-cylinder-buying-guide.html">راهنمای خرید جک پنوماتیک</a></li>
            <li><a href="solenoid-valve-guide.html">راهنمای انتخاب شیر برقی ۵/۲ و ۵/۳</a></li>
            <li><a href="pneumatics-lalehzar-tehran.html">فروشگاه پنوماتیک لالهزار تهران</a></li>
            <li><a href="what-is-pneumatics-jpc.html">پنوماتیک چیست و معرفی برند JPC</a></li>
            <li><a href="assets/docs/jpc-general-catalog.pdf" download>دانلود کاتالوگ جامع JPC (PDF)</a></li>
            <li><a href="sitemap.xml" target="_blank">نقشه سایت (sitemap.xml)</a> | <a href="llms.txt" target="_blank">llms.txt</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          © تمامی حقوق برای <strong>شرکت جلالی پنوماتیک (JPC – Jalali Pneumatic Company) با مدیریت امیر جلالی</strong> محفوظ است.
        </div>
        <div class="mono" dir="ltr" style="color: #64748B;">
          JPC INDUSTRIAL PNEUMATICS · LALEHZAR SOUTH, TEHRAN, IRAN
        </div>
      </div>
    </div>
  </footer>"""


def sanitize_jsonld_amir_jalali(html_content: str) -> str:
    """
    Ensure every JSON-LD block in the HTML page mentions "امیر جلالی" at most once
    (specifically inside Organization.founder.name), and ensure WebSite entity is present.
    """
    def process_block(m: re.Match) -> str:
        full_tag = m.group(0)
        open_tag = m.group(1)
        body_str = m.group(2)
        close_tag = m.group(3)
        try:
            data = json.loads(body_str)
        except Exception:
            return full_tag

        def clean_obj(obj, in_founder=False):
            if isinstance(obj, dict):
                new_d = {}
                for k, v in obj.items():
                    if k == "founder":
                        new_d[k] = clean_obj(v, in_founder=True)
                    elif k == "author" and isinstance(v, dict) and "امیر جلالی" in str(v.get("name", "")):
                        new_d[k] = {
                            "@type": "Organization",
                            "@id": "https://jpciran.com/#organization",
                            "name": "شرکت جلالی پنوماتیک (JPC)",
                        }
                    else:
                        new_d[k] = clean_obj(v, in_founder=in_founder)
                return new_d
            if isinstance(obj, list):
                return [clean_obj(x, in_founder=in_founder) for x in obj]
            if isinstance(obj, str):
                if not in_founder and "امیر جلالی" in obj:
                    cleaned = (
                        obj.replace(" با مدیریت امیر جلالی", "")
                        .replace(" — با مدیریت امیر جلالی", "")
                        .replace(" (با مدیریت امیر جلالی)", "")
                        .replace("با مدیریت امیر جلالی", "")
                        .replace("امیر جلالی", "شرکت جلالی پنوماتیک")
                    )
                    return cleaned.strip()
                return obj
            return obj

        cleaned_data = clean_obj(data)

        # Ensure WebSite schema node exists in @graph if Organization is present
        if isinstance(cleaned_data, dict) and "@graph" in cleaned_data:
            graph = cleaned_data["@graph"]
            has_website = any(
                node.get("@type") == "WebSite" for node in graph if isinstance(node, dict)
            )
            if not has_website:
                graph.insert(
                    1,
                    {
                        "@type": "WebSite",
                        "@id": "https://jpciran.com/#website",
                        "url": "https://jpciran.com/",
                        "name": "شرکت جلالی پنوماتیک (JPC)",
                        "inLanguage": "fa-IR",
                        "publisher": {"@id": "https://jpciran.com/#organization"},
                    },
                )

        formatted = json.dumps(cleaned_data, ensure_ascii=False, indent=2)
        return f"{open_tag}\n{formatted}\n  {close_tag}"

    return re.sub(
        r"(<script\s+type=\"application/ld\+json\"[^>]*>)(.*?)(</script>)",
        process_block,
        html_content,
        flags=re.DOTALL,
    )


def sync_page_chrome_and_assets(html_path: Path) -> None:
    """
    Synchronize Section A Utility Bar, Section B Sticky Header, Mobile Drawer,
    RFQ Drawer, Section M Footer, JSON-LD founder deduplication, and cache-busted
    deferred JS/CSS assets (?v=20261122) across any HTML page.
    """
    filename = html_path.name
    content = html_path.read_text(encoding="utf-8")

    # 1. Replace top-tech-bar .. <main> with unified Section A + B + Drawers
    shared_top = build_shared_header_and_drawers(filename)
    content, n_top = re.subn(
        r"(?:<!--[^>]*SECTION A[^>]*-->\s*)?<div class=\"top-tech-bar\">.*?<main>",
        shared_top,
        content,
        count=1,
        flags=re.DOTALL,
    )
    if n_top == 0:
        raise RuntimeError(f"Could not sync top header block in {filename}")

    # 2. Replace <footer class="site-footer">..</footer> with unified Section M Footer
    shared_footer = build_shared_footer(filename)
    content, n_ftr = re.subn(
        r"<footer class=\"site-footer\">.*?</footer>",
        shared_footer,
        content,
        count=1,
        flags=re.DOTALL,
    )
    if n_ftr == 0:
        raise RuntimeError(f"Could not sync footer block in {filename}")

    # 3. Update CSS and JS cache-busting query string to ?v=20261122 and ensure defer on scripts
    content = re.sub(
        r'href="assets/css/styles\.css(?:\?v=[^"]+)?"',
        f'href="assets/css/styles.css?v={ASSET_VERSION}"',
        content,
    )
    for js_file in ("config.js", "products-data.js", "app.js"):
        content = re.sub(
            rf'<script\s+(?:defer\s+)?src="assets/js/{re.escape(js_file)}(?:\?v=[^"]+)?"\s*></script>',
            f'<script defer src="assets/js/{js_file}?v={ASSET_VERSION}"></script>',
            content,
        )

    # 4. Sanitize JSON-LD so امیر جلالی appears only once (inside Organization.founder)
    content = sanitize_jsonld_amir_jalali(content)

    html_path.write_text(content, encoding="utf-8")


def update_catalog_ssr_in_html(html_path: Path, category_filter: str, page_url: str, all_products: list) -> int:
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

    counter_html = f'نمایش <strong>{len(filtered)}</strong> مدل از <strong>{len(all_products)}</strong> تجهیز کاتالوگ'
    content = re.sub(
        r'(<div\s+class="catalog-result-counter"\s+id="catalog-result-counter">)(.*?)(</div>)',
        rf"\1{counter_html}\3",
        content,
        flags=re.DOTALL,
    )

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


def generate_llms_txt(out_path: Path) -> None:
    lines = [
        "# شرکت جلالی پنوماتیک | JPC – Jalali Pneumatic Company",
        "",
        "> خلاصه ساختاریافته ویژه موتورهای جستجوی هوش مصنوعی (GEO / AEO / LLMs) به دو زبان فارسی و انگلیسی",
        "> برای دریافت جدول کامل مشخصات فنی تمامی مدل‌ها، کدهای فنی و معادل‌های ابعادی به فایل [llms-full.txt](https://jpciran.com/llms-full.txt) مراجعه کنید.",
        "",
        "---",
        "",
        "## معرفی فارسی (Persian Summary)",
        "",
        "**نام مجموعه:** شرکت جلالی پنوماتیک (JPC)",
        "**مؤسس و مدیریت مجموعه:** با مدیریت امیر جلالی (Amir Jalali)",
        "**برند تجاری اختصاصی:** JPC (Jalali Pneumatic Company)",
        "**دامنه‌های رسمی:** `https://jpciran.com` و `https://jalalipneumatic.ir`",
        "**حوزه فعالیت:** تأمین تخصصی تجهیزات پنوماتیک صنعتی، شیرهای برقی، جک‌های پنوماتیک، واحدهای مراقبت هوا (FRL) و اتصالات در ایران.",
        "**آدرس فروشگاه مرکزی:** تهران، لالهزار جنوبی، روبروی کوچه علیپور، پاساژ رزاقمنش، پلاک ۱",
        "**تلفن‌های ثابت:** `021-33110796` | `021-33932529`",
        "**همراه و واتساپ:** `09121305167` (`https://wa.me/989121305167`)",
        "**ساعات کاری:** شنبه تا پنجشنبه ۰۹:۰۰ تا ۱۸:۰۰",
        "**دستیار هوشمند تشخیص پلاک (AI):** `https://ai.jpciran.com`",
        "",
        "### صفحات تخصصی و ابزارهای مهندسی",
        "- صفحه اصلی و جستجوی فنی کد قطعه: https://jpciran.com/",
        "- شیرهای برقی پنوماتیک (3/2, 5/2, 5/3): https://jpciran.com/solenoid-valves.html",
        "- جک و سیلندر پنوماتیک (ISO 15552 & 6432): https://jpciran.com/pneumatic-cylinders.html",
        "- واحد مراقبت هوا (FRL)، رگولاتور، فلوکنترل و اتصالات: https://jpciran.com/frl-accessories.html",
        "- جدول معادل‌یابی فستو، نورگرن و رکسروت به JPC: https://jpciran.com/festo-cross-reference.html",
        "- راهنمای خرید جک پنوماتیک: https://jpciran.com/pneumatic-cylinder-buying-guide.html",
        "- راهنمای انتخاب شیر برقی پنوماتیک: https://jpciran.com/solenoid-valve-guide.html",
        "- فروشگاه پنوماتیک لالهزار تهران: https://jpciran.com/pneumatics-lalehzar-tehran.html",
        "- پنوماتیک چیست و معرفی برند JPC: https://jpciran.com/what-is-pneumatics-jpc.html",
        "- دستیار هوشمند تشخیص پلاک AI: https://ai.jpciran.com",
        "",
    ]
    out_path.write_text("\n".join(lines), encoding="utf-8")


def generate_llms_full_txt(products: list, out_path: Path) -> None:
    lines = [
        "# شرکت جلالی پنوماتیک | JPC – Jalali Pneumatic Company (Full AI & Technical Catalog Reference)",
        "",
        "> **شرکت جلالی پنوماتیک (`JPC`)**؛ تأمین‌کننده و توزیع‌کننده تخصصی تجهیزات پنوماتیک صنعتی در ایران (تهران، لالهزار جنوبی، روبروی کوچه علیپور، پاساژ رزاقمنش، پلاک ۱).",
        "",
        "---",
        "",
        "## 1. Verified Corporate Profile (اطلاعات رسمی شرکت جلالی پنوماتیک)",
        "",
        "- **Company:** شرکت جلالی پنوماتیک (JPC)",
        "- **Management:** با مدیریت امیر جلالی (`Amir Jalali`)",
        "- **Address:** تهران، لالهزار جنوبی، روبروی کوچه علیپور، پاساژ رزاقمنش، پلاک ۱",
        "- **Landlines:** `021-33110796` | `021-33932529`",
        "- **WhatsApp / Mobile:** `09121305167` (`https://wa.me/989121305167`)",
        "- **Working Hours:** شنبه تا پنجشنبه ۰۹:۰۰ تا ۱۸:۰۰",
        "- **AI Nameplate Assistant:** `https://ai.jpciran.com` (دستیار هوشمند تشخیص پلاک AI)",
        "- **Canonical Website:** `https://jpciran.com/`",
        "",
        "---",
        "",
        "## 2. Complete Verified Product Catalog Table (جدول کامل محصولات و معادل‌های فنی)",
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
            "## 3. Detailed Technical Specifications by SKU",
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
                f"- **Compatible Equivalent Codes:** `{equivs}`",
                f"- **Keywords:** {keywords}",
                f"- **Applications:** {p.get('applicationsFa', '')}",
                "",
            ]
        )

    out_path.write_text("\n".join(lines), encoding="utf-8")


def generate_sitemap_xml(out_path: Path) -> None:
    today = date.today().isoformat()
    urls = [
        ("https://jpciran.com/", "weekly", "1.0"),
        ("https://jpciran.com/solenoid-valves.html", "weekly", "0.9"),
        ("https://jpciran.com/pneumatic-cylinders.html", "weekly", "0.9"),
        ("https://jpciran.com/frl-accessories.html", "weekly", "0.9"),
        ("https://jpciran.com/festo-cross-reference.html", "weekly", "0.9"),
        ("https://jpciran.com/pneumatic-cylinder-buying-guide.html", "monthly", "0.85"),
        ("https://jpciran.com/solenoid-valve-guide.html", "monthly", "0.85"),
        ("https://jpciran.com/pneumatics-lalehzar-tehran.html", "weekly", "0.9"),
        ("https://jpciran.com/what-is-pneumatics-jpc.html", "monthly", "0.85"),
    ]
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, changefreq, priority in urls:
        xml_lines.extend(
            [
                "  <url>",
                f"    <loc>{loc}</loc>",
                f"    <lastmod>{today}</lastmod>",
                f"    <changefreq>{changefreq}</changefreq>",
                f"    <priority>{priority}</priority>",
                "  </url>",
            ]
        )
    xml_lines.append("</urlset>")
    out_path.write_text("\n".join(xml_lines) + "\n", encoding="utf-8")


def generate_robots_txt(out_path: Path) -> None:
    content = """User-agent: *
Allow: /

# Search Engine Crawlers
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# AI & Generative Search Crawlers (GEO / AEO)
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: https://jpciran.com/sitemap.xml
# LLMs Summary: https://jpciran.com/llms.txt
# LLMs Full Catalog & Technical Index: https://jpciran.com/llms-full.txt
"""
    out_path.write_text(content, encoding="utf-8")


def main() -> None:
    products = parse_products_from_js(PRODUCTS_JS_PATH)
    print(f"[build-seo] Parsed {len(products)} products from {PRODUCTS_JS_PATH.name}")

    for filename, cat_filter, page_url in PAGE_TARGETS:
        html_path = ROOT_DIR / filename
        rendered_count = update_catalog_ssr_in_html(html_path, cat_filter, page_url, products)
        print(f"[build-seo] Injected {rendered_count} SSR product cards + ItemList JSON-LD into {filename}")

    for filename in ALL_HTML_PAGES:
        html_path = ROOT_DIR / filename
        sync_page_chrome_and_assets(html_path)
        print(f"[build-seo] Synced header/drawer/footer/JSON-LD & ?v={ASSET_VERSION} in {filename}")

    generate_llms_txt(LLMS_TXT_PATH)
    print(f"[build-seo] Generated {LLMS_TXT_PATH.name} ({LLMS_TXT_PATH.stat().st_size} bytes)")

    generate_llms_full_txt(products, LLMS_FULL_PATH)
    print(f"[build-seo] Generated {LLMS_FULL_PATH.name} ({LLMS_FULL_PATH.stat().st_size} bytes)")

    generate_sitemap_xml(SITEMAP_PATH)
    print(f"[build-seo] Generated {SITEMAP_PATH.name} ({SITEMAP_PATH.stat().st_size} bytes)")

    generate_robots_txt(ROBOTS_PATH)
    print(f"[build-seo] Generated {ROBOTS_PATH.name} ({ROBOTS_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
