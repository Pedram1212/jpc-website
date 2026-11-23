"""
Common Layout, Chrome, SVG Schematics, Supplier Block & JSON-LD Helpers
for JPC Iran Multi-Level Catalog Pages (`depth=0`, `depth=1`, `depth=2`).
"""

import html
import json

ASSET_VERSION = "20261122"
SITE_DOMAIN = "https://www.jpciran.com"


def esc(val) -> str:
    return html.escape(str(val if val is not None else ""))


def get_schematic_svg(schematic_type: str) -> str:
    if schematic_type == "valve-5-2":
        return """<svg viewBox="0 0 120 56" fill="none" stroke="currentColor" stroke-width="1.6" aria-label="شماتیک فنی شیر برقی ۵/۲ تک بوبین پنوماتیک">
            <rect x="26" y="10" width="34" height="34" rx="2"/>
            <rect x="60" y="10" width="34" height="34" rx="2"/>
            <rect x="8" y="18" width="18" height="18" rx="1.5"/>
            <line x1="12" y1="36" x2="22" y2="18"/>
            <polyline points="94,22 100,16 105,28 110,16 115,22"/>
            <line x1="36" y1="44" x2="36" y2="10"/>
            <polyline points="33,15 36,10 39,15"/>
            <line x1="50" y1="10" x2="50" y2="44"/>
            <polyline points="47,39 50,44 53,39"/>
            <line x1="70" y1="44" x2="84" y2="10"/>
            <polyline points="80,13 84,10 85,15"/>
            <text x="58" y="53" font-size="6.5" font-family="monospace" text-anchor="middle" fill="currentColor" stroke="none">5/2 SOLENOID ISO</text>
          </svg>"""
    if schematic_type == "valve-5-2-double":
        return """<svg viewBox="0 0 120 56" fill="none" stroke="currentColor" stroke-width="1.6" aria-label="شماتیک فنی شیر برقی ۵/۲ دو بوبین حافظه‌دار">
            <rect x="26" y="10" width="34" height="34" rx="2"/>
            <rect x="60" y="10" width="34" height="34" rx="2"/>
            <rect x="6" y="18" width="20" height="18" rx="1.5"/>
            <line x1="10" y1="36" x2="22" y2="18"/>
            <rect x="94" y="18" width="20" height="18" rx="1.5"/>
            <line x1="98" y1="36" x2="110" y2="18"/>
            <line x1="36" y1="44" x2="36" y2="10"/>
            <polyline points="33,15 36,10 39,15"/>
            <line x1="70" y1="44" x2="84" y2="10"/>
            <text x="60" y="53" font-size="6.5" font-family="monospace" text-anchor="middle" fill="currentColor" stroke="none">5/2 BISTABLE COIL</text>
          </svg>"""
    if schematic_type == "valve-5-3":
        return """<svg viewBox="0 0 120 56" fill="none" stroke="currentColor" stroke-width="1.6" aria-label="شماتیک فنی شیر برقی ۵/۳ سه حالته پنوماتیک">
            <rect x="18" y="10" width="28" height="34" rx="1.5"/>
            <rect x="46" y="10" width="28" height="34" rx="1.5"/>
            <rect x="74" y="10" width="28" height="34" rx="1.5"/>
            <rect x="3" y="19" width="15" height="16" rx="1"/>
            <rect x="102" y="19" width="15" height="16" rx="1"/>
            <line x1="53" y1="36" x2="53" y2="44"/><line x1="50" y1="36" x2="56" y2="36"/>
            <line x1="67" y1="36" x2="67" y2="44"/><line x1="64" y1="36" x2="70" y2="36"/>
            <line x1="53" y1="10" x2="53" y2="18"/><line x1="50" y1="18" x2="56" y2="18"/>
            <line x1="67" y1="10" x2="67" y2="18"/><line x1="64" y1="18" x2="70" y2="18"/>
            <text x="60" y="53" font-size="6.5" font-family="monospace" text-anchor="middle" fill="currentColor" stroke="none">5/3 CLOSED CENTER</text>
          </svg>"""
    if schematic_type == "valve-3-2":
        return """<svg viewBox="0 0 120 56" fill="none" stroke="currentColor" stroke-width="1.6" aria-label="شماتیک فنی شیر برقی ۳/۲ نرمال بسته">
            <rect x="28" y="10" width="32" height="34" rx="2"/>
            <rect x="60" y="10" width="32" height="34" rx="2"/>
            <rect x="10" y="18" width="18" height="18" rx="1.5"/>
            <line x1="44" y1="44" x2="44" y2="10"/>
            <polyline points="41,15 44,10 47,15"/>
            <line x1="76" y1="34" x2="76" y2="44"/>
            <line x1="72" y1="34" x2="80" y2="34"/>
            <text x="60" y="53" font-size="6.5" font-family="monospace" text-anchor="middle" fill="currentColor" stroke="none">3/2 NC DIRECT/PILOT</text>
          </svg>"""
    if schematic_type in ("cylinder-iso", "cylinder-tierod"):
        return """<svg viewBox="0 0 120 56" fill="none" stroke="currentColor" stroke-width="1.6" aria-label="شماتیک فنی جک پنوماتیک استاندارد ISO 15552">
            <rect x="14" y="12" width="72" height="30" rx="2"/>
            <line x1="46" y1="12" x2="46" y2="42" stroke-width="2.4"/>
            <line x1="46" y1="27" x2="112" y2="27" stroke-width="3.2"/>
            <rect x="106" y="22" width="6" height="10" rx="1"/>
            <circle cx="22" cy="12" r="2.2"/><circle cx="78" cy="12" r="2.2"/>
            <text x="54" y="53" font-size="6.5" font-family="monospace" text-anchor="middle" fill="currentColor" stroke="none">ISO 15552 DOUBLE-ACTING</text>
          </svg>"""
    if schematic_type in ("cylinder-compact", "cylinder-mini"):
        return """<svg viewBox="0 0 120 56" fill="none" stroke="currentColor" stroke-width="1.6" aria-label="شماتیک فنی جک کامپکت و مینی پنوماتیک">
            <rect x="26" y="10" width="48" height="34" rx="2"/>
            <line x1="50" y1="10" x2="50" y2="44" stroke-width="2.4"/>
            <line x1="50" y1="27" x2="102" y2="27" stroke-width="3.2"/>
            <circle cx="34" cy="17" r="2"/><circle cx="66" cy="17" r="2"/>
            <circle cx="34" cy="37" r="2"/><circle cx="66" cy="37" r="2"/>
            <text x="60" y="53" font-size="6.5" font-family="monospace" text-anchor="middle" fill="currentColor" stroke="none">COMPACT / MINI ACTUATOR</text>
          </svg>"""
    if schematic_type == "frl-unit":
        return """<svg viewBox="0 0 120 56" fill="none" stroke="currentColor" stroke-width="1.6" aria-label="شماتیک فنی واحد مراقبت هوای فشرده FRL">
            <polygon points="36,10 52,26 36,42 20,26"/>
            <line x1="36" y1="10" x2="36" y2="42" stroke-dasharray="2.5 2.5"/>
            <polygon points="84,10 100,26 84,42 68,26"/>
            <circle cx="84" cy="20" r="5"/>
            <line x1="82" y1="22" x2="87" y2="17"/>
            <line x1="52" y1="26" x2="68" y2="26"/>
            <text x="60" y="53" font-size="6.5" font-family="monospace" text-anchor="middle" fill="currentColor" stroke="none">FRL FILTER + REGULATOR</text>
          </svg>"""
    return """<svg viewBox="0 0 120 56" fill="none" stroke="currentColor" stroke-width="1.6" aria-label="شماتیک فنی اتصالات فشاری و شیر کنترل جریان پنوماتیک">
        <line x1="16" y1="26" x2="104" y2="26"/>
        <path d="M 42 18 Q 60 28 78 18"/>
        <path d="M 42 34 Q 60 24 78 34"/>
        <line x1="48" y1="38" x2="72" y2="14"/>
        <polyline points="67,14 72,14 72,19"/>
        <text x="60" y="53" font-size="6.5" font-family="monospace" text-anchor="middle" fill="currentColor" stroke="none">FITTINGS &amp; FLOW CONTROL</text>
      </svg>"""


def build_chrome_header(base_prefix: str = "", active_section: str = "products") -> str:
    """
    Build Section A Utility Bar, Section B Sticky Header, Mobile Drawer & RFQ Drawer
    using depth-aware relative links (`base_prefix` = `""`, `"../"`, or `"../../"`).
    Contains 1 visible mention of «امیر جلالی» (in the Utility Bar).
    """
    root_home = f"{base_prefix}index.html" if base_prefix else "index.html"
    products_dir = f"{base_prefix}products/index.html"
    cat_cyl = f"{base_prefix}products/pneumatic-cylinders/index.html"
    cat_val = f"{base_prefix}products/solenoid-valves/index.html"
    cat_frl = f"{base_prefix}products/air-preparation/index.html"
    cat_fit = f"{base_prefix}products/pneumatic-fittings/index.html"

    return f"""  <!-- SECTION A — TOP INDUSTRIAL UTILITY BAR -->
  <div class="top-tech-bar" role="region" aria-label="اطلاعات تماس، ساعات کاری و دسترسی سریع">
    <div class="container top-tech-bar-inner">
      <div class="tech-bar-right">
        <span class="tech-status-dot" aria-hidden="true"></span>
        <span><strong>شرکت جلالی پنوماتیک (JPC)</strong> <span class="util-hide-sm">· با مدیریت امیر جلالی</span></span>
        <span class="tech-bar-divider util-hide-md" aria-hidden="true"></span>
        <span class="util-hide-md">تهران، لاله‌زار جنوبی، روبروی کوچه علیپور، پاساژ رزاق‌منش، پلاک ۱</span>
        <span class="tech-bar-divider util-hide-lg" aria-hidden="true"></span>
        <span class="util-hide-lg">شنبه تا پنج‌شنبه ۰۹:۰۰ تا ۱۸:۰۰</span>
      </div>
      <div class="tech-bar-left">
        <a href="tel:02133110796" class="util-contact-link" aria-label="تماس با خط ثابت اول ۰۲۱-۳۳۱۱۰۷۹۶">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span class="mono" dir="ltr">021-33110796</span>
        </a>
        <span class="tech-bar-divider util-hide-sm" aria-hidden="true"></span>
        <a href="tel:02133932529" class="util-contact-link util-hide-sm" aria-label="تماس با خط ثابت دوم ۰۲۱-۳۳۹۳۲۵۲۹">
          <span class="mono" dir="ltr">021-33932529</span>
        </a>
        <span class="tech-bar-divider" aria-hidden="true"></span>
        <a href="https://wa.me/989121305167" target="_blank" rel="noopener noreferrer" class="util-contact-link util-whatsapp-link" aria-label="استعلام در واتساپ ۰۹۱۲۱۳۰۵۱۶۷">
          <span>واتساپ:</span>
          <span class="mono" dir="ltr">09121305167</span>
        </a>
        <span class="tech-bar-divider util-hide-md" aria-hidden="true"></span>
        <a href="https://ai.jpciran.com" target="_blank" rel="noopener noreferrer" class="util-ai-pill" aria-label="ورود به دستیار هوشمند تشخیص پلاک JPC AI">
          <span aria-hidden="true">✦</span>
          <span>دستیار هوشمند پلاک‌خوان (AI)</span>
        </a>
      </div>
    </div>
  </div>

  <!-- SECTION B — STICKY MAIN HEADER -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="{root_home}" class="brand-logo" aria-label="شرکت جلالی پنوماتیک JPC - صفحه اصلی">
        <div class="brand-emblem">
          <span class="brand-jpc">JPC</span>
          <span class="brand-sub">INDUSTRIAL</span>
        </div>
        <div class="brand-text">
          <span class="brand-title">شرکت جلالی پنوماتیک</span>
          <span class="brand-subtitle">مرجع تخصصی تأمین، معادل‌یابی و اتوماسیون پنوماتیک صنعتی</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="منوی اصلی ناوبری مهندسی">
        <a href="{products_dir}" class="nav-link {'active' if active_section == 'products' else ''}">محصولات</a>
        <a href="{cat_val}" class="nav-link {'active' if active_section == 'valves' else ''}">شیرهای برقی</a>
        <a href="{cat_cyl}" class="nav-link {'active' if active_section == 'cylinders' else ''}">جک و سیلندر</a>
        <a href="{cat_frl}" class="nav-link {'active' if active_section == 'frl' else ''}">واحد مراقبت</a>
        <a href="{cat_fit}" class="nav-link {'active' if active_section == 'fittings' else ''}">اتصالات و شیلنگ</a>
        <a href="{base_prefix}brands/jpc/index.html" class="nav-link nav-link-jpc {'active' if active_section == 'brands' else ''}">برندها</a>
        <a href="{base_prefix}festo-cross-reference.html" class="nav-link">معادل‌یابی فنی</a>
        <a href="{root_home}#calculator" class="nav-link">ابزارهای مهندسی</a>
        <a href="{base_prefix}pneumatics-lalehzar-tehran.html" class="nav-link">تماس و آدرس</a>
      </nav>

      <div class="header-actions">
        <a
          href="{products_dir}"
          class="header-search-trigger"
          title="جستجو در ۵۰۰ کد فنی کاتالوگ"
          aria-label="جستجوی کد فنی در کاتالوگ ۵۰۰ قطعه‌ای"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <span class="header-search-trigger-label">جستجوی کد فنی</span>
        </a>

        <button
          type="button"
          class="rfq-header-btn js-open-rfq-drawer"
          title="مشاهده لیست استعلام قیمت (RFQ)"
          aria-label="سبد استعلام قیمت چندقلمی"
        >
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true">
            <path d="M9 5H7a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-2"></path>
            <rect x="9" y="3" width="6" height="4" rx="1"></rect>
            <line x1="9" y1="12" x2="15" y2="12"></line>
            <line x1="9" y1="16" x2="13" y2="16"></line>
          </svg>
          <span class="rfq-btn-label">سبد استعلام</span>
          <span class="rfq-count-badge js-rfq-count-badge">0</span>
        </button>

        <a
          href="https://ai.jpciran.com"
          target="_blank"
          rel="noopener noreferrer"
          class="btn btn-ai-scan btn-sm header-ai-cta"
          title="دستیار هوشمند تشخیص پلاک و معادل‌یابی پنوماتیک با هوش مصنوعی"
        >
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true">
            <path d="M12 2L14.5 9.5L22 12L14.5 14.5L12 22L9.5 14.5L2 12L9.5 9.5L12 2Z"/>
          </svg>
          <span>دستیار هوشمند (AI)</span>
        </a>

        <a
          href="{root_home}#rfq"
          class="btn btn-amber btn-sm header-rfq-cta"
        >
          <span>ثبت درخواست استعلام</span>
        </a>

        <button
          type="button"
          class="mobile-menu-btn"
          id="mobile-menu-btn"
          aria-label="باز کردن منوی موبایل"
          aria-expanded="false"
          aria-controls="mobile-drawer"
        >
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true">
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
  <aside class="mobile-drawer" id="mobile-drawer" aria-hidden="true" aria-label="منوی ناوبری موبایل">
    <div class="mobile-drawer-header">
      <div class="brand-text">
        <span class="brand-title">شرکت جلالی پنوماتیک (JPC)</span>
        <span class="brand-subtitle">تأمین و مهندسی تجهیزات پنوماتیک</span>
      </div>
      <button type="button" class="modal-close-btn" id="mobile-drawer-close" aria-label="بستن منو">✕</button>
    </div>

    <div class="mobile-drawer-quick-actions">
      <a href="{products_dir}" class="btn btn-outline-tech btn-sm mobile-nav-link" style="width:100%; justify-content:center;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <span>جستجو در ۵۰۰ کد فنی کاتالوگ</span>
      </a>
    </div>

    <nav class="mobile-nav-list" aria-label="دسترسی سریع موبایل">
      <a href="{products_dir}" class="mobile-nav-link">کاتالوگ جامع محصولات (/products/)</a>
      <a href="{cat_val}" class="mobile-nav-link">شیرهای برقی و کنترل جهت پنوماتیک</a>
      <a href="{cat_cyl}" class="mobile-nav-link">جک و سیلندر پنوماتیک (ISO 15552 / کامپکت)</a>
      <a href="{cat_frl}" class="mobile-nav-link">واحد مراقبت و آماده‌سازی هوا (FRL)</a>
      <a href="{cat_fit}" class="mobile-nav-link">اتصالات فشاری و رابط‌های پنوماتیک</a>
      <a href="{base_prefix}products/pneumatic-tubing/index.html" class="mobile-nav-link">شیلنگ و لوله‌های پنوماتیک</a>
      <a href="{base_prefix}products/flow-control-valves/index.html" class="mobile-nav-link">شیرهای کنترل جریان و سرعت</a>
      <a href="{base_prefix}products/pressure-regulators/index.html" class="mobile-nav-link">رگلاتورهای فشار و فیلتر رگلاتور</a>
      <a href="{base_prefix}products/silencers-exhaust/index.html" class="mobile-nav-link">صداخفه‌کن و اگزوز پنوماتیک</a>
      <a href="{base_prefix}brands/jpc/index.html" class="mobile-nav-link" style="color: var(--amber-cta); font-weight: 800;">برند اختصاصی JPC</a>
      <a href="{base_prefix}brands/festo/index.html" class="mobile-nav-link">کاتالوگ و معادل‌یابی فستو (Festo)</a>
      <a href="{base_prefix}brands/norgren/index.html" class="mobile-nav-link">کاتالوگ و معادل‌یابی نورگرن (Norgren)</a>
      <a href="{base_prefix}brands/bosch-rexroth/index.html" class="mobile-nav-link">نمایه کدهای تاریخی Bosch Rexroth / AVENTICS</a>
      <a href="https://ai.jpciran.com" target="_blank" rel="noopener noreferrer" class="mobile-nav-link" style="color: #087F8C; font-weight: 800;">✦ دستیار هوشمند تشخیص پلاک (AI)</a>
      <a href="{base_prefix}festo-cross-reference.html" class="mobile-nav-link">جدول معادل‌یابی فستو، نورگرن و رکسروت</a>
      <a href="{root_home}#calculator" class="mobile-nav-link">محاسبه‌گر مهندسی نیروی جک پنوماتیک</a>
      <a href="{base_prefix}pneumatics-lalehzar-tehran.html" class="mobile-nav-link">آدرس فروشگاه لاله‌زار، نقشه و تماس</a>
    </nav>

    <div class="mobile-drawer-contact-box">
      <div class="mobile-contact-title">دفتر مرکزی فروش و مهندسی (لاله‌زار جنوبی)</div>
      <p class="mobile-contact-address">تهران، لاله‌زار جنوبی، روبروی کوچه علیپور، پاساژ رزاق‌منش، پلاک ۱</p>
      <div class="mobile-contact-phones">
        <a href="tel:02133110796" class="mono" dir="ltr">021-33110796</a>
        <a href="tel:02133932529" class="mono" dir="ltr">021-33932529</a>
      </div>
      <div class="mobile-contact-hours">ساعات کاری: شنبه تا پنج‌شنبه ۰۹:۰۰ تا ۱۸:۰۰</div>
    </div>

    <div style="margin-top: auto; display: flex; flex-direction: column; gap: 0.65rem; padding-top: 0.75rem;">
      <a href="https://ai.jpciran.com" target="_blank" rel="noopener noreferrer" class="btn btn-ai-scan" style="width: 100%; justify-content: center;">
        ✦ دستیار هوشمند تشخیص پلاک (AI)
      </a>
      <a href="https://wa.me/989121305167" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="width: 100%;">
        استعلام مستقیم واتساپ (09121305167)
      </a>
      <a href="tel:02133110796" class="btn btn-outline-tech" style="width: 100%;">
        تماس با دفتر لاله‌زار: 021-33110796
      </a>
    </div>
  </aside>

  <!-- Multi-Item RFQ (Request For Quotation) Basket Drawer -->
  <div class="rfq-drawer-backdrop" id="rfq-drawer-backdrop"></div>
  <aside class="rfq-drawer" id="rfq-drawer" aria-hidden="true" aria-label="لیست استعلام قیمت چندقلمی">
    <div class="rfq-drawer-header">
      <div>
        <div class="rfq-drawer-title">
          <span>لیست استعلام قیمت مهندسی (RFQ)</span>
          <span class="rfq-count-badge visible js-rfq-count-badge">0</span>
        </div>
        <p style="font-size: 0.76rem; color: var(--text-muted); margin-top: 0.2rem;">
          اقلام انتخابی خود را یکجا برای دریافت پیش‌فاکتور رسمی ارسال نمایید
        </p>
      </div>
      <button type="button" class="modal-close-btn" id="rfq-drawer-close" aria-label="بستن سبد استعلام">✕</button>
    </div>

    <div class="rfq-drawer-body">
      <div id="rfq-items-container"></div>

      <div style="margin-top: 1.1rem; display: grid; grid-template-columns: 1fr 1fr; gap: 0.6rem;">
        <div>
          <label for="rfq-customer-company" style="display: block; font-size: 0.76rem; font-weight: 700; color: var(--text-secondary); margin-bottom: 0.3rem;">
            نام شرکت / واحد صنعتی (اختیاری):
          </label>
          <input
            type="text"
            id="rfq-customer-company"
            class="form-input"
            placeholder="مثلاً: کارخانه فولاد / ماشین‌سازی..."
            style="padding: 0.5rem 0.65rem; font-size: 0.8rem;"
          />
        </div>
        <div>
          <label for="rfq-customer-phone" style="display: block; font-size: 0.76rem; font-weight: 700; color: var(--text-secondary); margin-bottom: 0.3rem;">
            شماره تماس پاسخگویی (اختیاری):
          </label>
          <input
            type="tel"
            id="rfq-customer-phone"
            class="form-input mono"
            dir="ltr"
            placeholder="0912..."
            style="padding: 0.5rem 0.65rem; font-size: 0.8rem;"
          />
        </div>
      </div>

      <div style="margin-top: 0.75rem;">
        <label for="rfq-customer-note" style="display: block; font-size: 0.78rem; font-weight: 700; color: var(--text-secondary); margin-bottom: 0.35rem;">
          توضیحات تکمیلی استعلام (شرایط کاری، فشار، ولتاژ یا درخواست معادل JPC):
        </label>
        <textarea
          id="rfq-customer-note"
          class="form-textarea"
          rows="2"
          placeholder="مثلاً: لطفاً علاوه بر کدهای اصلی، قیمت معادل ابعادی برند JPC را نیز در پیش‌فاکتور اعلام فرمایید..."
          style="min-height: 60px; font-size: 0.82rem;"
        ></textarea>
      </div>
    </div>

    <div class="rfq-drawer-footer">
      <a
        href="https://wa.me/989121305167"
        id="rfq-whatsapp-send-btn"
        target="_blank"
        rel="noopener noreferrer"
        class="btn btn-whatsapp"
        style="width: 100%;"
      >
        ارسال کل لیست استعلام در واتساپ (09121305167)
      </a>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
        <button type="button" class="btn btn-outline-tech btn-sm" id="rfq-copy-list-btn">
          کپی متن لیست استعلام
        </button>
        <a
          href="mailto:info@jpciran.com"
          id="rfq-email-send-btn"
          class="btn btn-outline-tech btn-sm"
          style="text-align: center; justify-content: center;"
        >
          ارسال لیست با ایمیل
        </a>
      </div>
      <div style="display: grid; grid-template-columns: 1fr auto; gap: 0.5rem;">
        <button type="button" class="btn btn-amber btn-sm" id="rfq-populate-form-btn">
          انتقال به فرم استعلام صفحه
        </button>
        <button type="button" class="btn btn-outline-tech btn-sm" id="rfq-clear-btn" style="color: #dc2626;">
          پاکسازی لیست
        </button>
      </div>
    </div>
  </aside>"""


def build_supplier_support_block(base_prefix: str = "") -> str:
    """
    Section L — Supplier & Support Block (contains the 2nd visible mention of «امیر جلالی»).
    """
    return f"""  <!-- SECTION L — SUPPLIER & ENGINEERING SUPPORT BLOCK -->
  <section class="section" id="supplier-support-block" style="background: #EEF2F7; border-top: 1px solid #E1E7EE; padding: 2.75rem 0;">
    <div class="container">
      <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.25rem, 3vw, 2rem); display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; align-items: center;">
        <div>
          <span class="section-eyebrow">مرجع رسمی تأمین و مهندسی پنوماتیک در لاله‌زار تهران</span>
          <h2 style="font-size: 1.25rem; font-weight: 800; color: #10243A; margin: 0.35rem 0 0.65rem;">
            شرکت جلالی پنوماتیک (JPC) — با مدیریت امیر جلالی
          </h2>
          <p style="font-size: 0.88rem; color: #475569; line-height: 1.85; margin-bottom: 0.9rem;">
            واحد مهندسی و فروش شرکت جلالی پنوماتیک آماده بررسی لیست خرید (BOM)، تطبیق کدهای فنی <strong>Festo</strong>، <strong>Norgren</strong> و کدهای تاریخی <strong>Bosch Rexroth / AVENTICS</strong> و ارائه پیش‌فاکتور رسمی برند اختصاصی <strong>JPC</strong> با ارسال سریع از بازار صنعتی لاله‌زار تهران به سراسر کشور است.
          </p>
          <div style="display: flex; flex-wrap: wrap; gap: 0.6rem;">
            <a href="https://wa.me/989121305167" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-sm">
              استعلام قیمت در واتساپ: <span class="mono" dir="ltr">09121305167</span>
            </a>
            <a href="https://ai.jpciran.com" target="_blank" rel="noopener noreferrer" class="btn btn-ai-scan btn-sm">
              ✦ دستیار هوشمند تشخیص پلاک (AI)
            </a>
            <a href="{base_prefix}pneumatics-lalehzar-tehran.html" class="btn btn-outline-tech btn-sm">
              مشاهده نقشه و راهنمای مراجعه حضوری
            </a>
          </div>
        </div>
        <div style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1.15rem; font-size: 0.84rem; color: #172334; display: flex; flex-direction: column; gap: 0.55rem;">
          <div><strong>نشانی فروشگاه و دفتر مرکزی:</strong> تهران، لاله‌زار جنوبی، روبروی کوچه علیپور، پاساژ رزاق‌منش، پلاک ۱</div>
          <div>
            <strong>تلفن‌های ثابت فروش:</strong>
            <a href="tel:02133110796" class="mono" dir="ltr" style="color: #087F8C; font-weight: 800;">021-33110796</a>
            <span> و </span>
            <a href="tel:02133932529" class="mono" dir="ltr" style="color: #087F8C; font-weight: 800;">021-33932529</a>
          </div>
          <div>
            <strong>خط مستقیم واتساپ فنی:</strong>
            <a href="https://wa.me/989121305167" target="_blank" rel="noopener noreferrer" class="mono" dir="ltr" style="color: #087F8C; font-weight: 800;">09121305167</a>
          </div>
          <div><strong>ساعات کاری:</strong> شنبه تا پنج‌شنبه ۰۹:۰۰ تا ۱۸:۰۰</div>
        </div>
      </div>
    </div>
  </section>"""


def build_modals_and_footer(base_prefix: str = "") -> str:
    """
    Build Quick Quote Modal, Technical Detail / Zoom Inspection Modal, and Section M Footer.
    Contains the 3rd (and final) visible mention of «امیر جلالی» (in the Footer copyright line).
    """
    root_home = f"{base_prefix}index.html" if base_prefix else "index.html"
    return f"""  <!-- QUICK QUOTE MODAL -->
  <div class="modal-backdrop" id="quick-quote-modal" role="dialog" aria-modal="true" aria-labelledby="quick-quote-modal-title">
    <div class="modal-card">
      <div class="modal-header">
        <div>
          <h3 class="modal-title" id="quick-quote-modal-title">درخواست استعلام قیمت و موجودی</h3>
          <div style="margin-top: 0.35rem;">
            <span class="product-code-pill" id="modal-product-code" dir="ltr">JPC-CODE</span>
          </div>
        </div>
        <button type="button" class="modal-close-btn" data-close-modal aria-label="بستن پنجره">✕</button>
      </div>
      <div class="modal-body">
        <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 1rem;">
          تجهیز انتخابی: <strong id="modal-product-title" style="color: var(--text-primary);">تجهیز پنوماتیک</strong>
        </p>
        <form id="modal-quote-form">
          <div class="form-grid">
            <div class="form-group">
              <label class="form-label" for="modal-name">نام یا نام شرکت *</label>
              <input type="text" id="modal-name" class="form-input" required placeholder="نام شرکت یا مسئول خرید" />
            </div>
            <div class="form-group">
              <label class="form-label" for="modal-phone">شماره موبایل / تلفن *</label>
              <input type="tel" id="modal-phone" class="form-input mono" dir="ltr" required placeholder="0912..." />
            </div>
            <div class="form-group">
              <label class="form-label" for="modal-qty">تعداد مورد نیاز</label>
              <input type="text" id="modal-qty" class="form-input" value="1 عدد" />
            </div>
            <div class="form-group">
              <label class="form-label" for="modal-note">توضیحات فنی (ولتاژ، کورس، درخواست معادل JPC)</label>
              <input type="text" id="modal-note" class="form-input" placeholder="مثلاً: بوبین 24V DC یا معادل JPC" />
            </div>
          </div>
          <div style="display: flex; flex-direction: column; gap: 0.65rem; margin-top: 1.25rem;">
            <button type="submit" class="btn btn-amber" style="width: 100%;">
              ثبت و ارسال به واتساپ واحد فروش
            </button>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
              <a href="https://wa.me/989121305167" id="modal-direct-wa-btn" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-sm">
                استعلام فوری واتساپ
              </a>
              <a href="https://t.me/+989121305167" id="modal-direct-tg-btn" target="_blank" rel="noopener noreferrer" class="btn btn-telegram btn-sm">
                ارسال در تلگرام
              </a>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>

  <!-- TECHNICAL DETAIL & SCHEMATIC ZOOM MODAL -->
  <div class="modal-backdrop" id="tech-detail-modal" role="dialog" aria-modal="true" aria-labelledby="tech-modal-title">
    <div class="modal-card" style="max-width: 680px;">
      <div class="modal-header">
        <div>
          <span class="product-code-pill" id="tech-modal-code" dir="ltr">CODE</span>
          <h3 class="modal-title" id="tech-modal-title" style="margin-top: 0.4rem;">مشخصات فنی تجهیز</h3>
        </div>
        <button type="button" class="modal-close-btn" data-close-modal aria-label="بستن پنجره">✕</button>
      </div>
      <div class="modal-body" id="tech-modal-body"></div>
    </div>
  </div>

  <!-- SECTION M — FOOTER -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand-col">
          <div class="brand-logo" style="margin-bottom: 0.5rem;">
            <div class="brand-emblem">
              <span class="brand-jpc">JPC</span>
              <span class="brand-sub">INDUSTRIAL</span>
            </div>
            <div class="brand-text">
              <span class="brand-title" style="color: #F8FAFC;">شرکت جلالی پنوماتیک</span>
              <span class="brand-subtitle" style="color: #94A3B8;">مرجع تخصصی تأمین و مهندسی تجهیزات پنوماتیک صنعتی</span>
            </div>
          </div>
          <p class="footer-desc">
            تأمین‌کننده تخصصی شیرآلات برقی، جک‌های پنوماتیک استاندارد ISO 15552، واحدهای مراقبت هوا (FRL) و اتصالات صنعتی با برند اختصاصی <strong>JPC</strong> و تأمین برندهای معتبر جهانی (Festo، Norgren و Bosch Rexroth) برای صنایع، کارخانجات و خطوط تولید سراسر کشور.
          </p>
          <div style="margin-top: 1rem; font-size: 0.82rem; color: #CBD5E1; line-height: 1.85; background: rgba(255,255,255,0.03); padding: 0.85rem 1rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
            <div><strong style="color: #F28C28;">آدرس دفتر مرکزی و فروشگاه:</strong> تهران، لاله‌زار جنوبی، روبروی کوچه علیپور، پاساژ رزاق‌منش، پلاک ۱</div>
            <div style="margin-top: 0.25rem;">
              <strong style="color: #F8FAFC;">تلفن‌های ثابت:</strong>
              <a href="tel:02133110796" class="mono" dir="ltr" style="color: #38BDF8; font-weight: 700;">021-33110796</a>
              <span> و </span>
              <a href="tel:02133932529" class="mono" dir="ltr" style="color: #38BDF8; font-weight: 700;">021-33932529</a>
              <span style="margin: 0 0.4rem;">|</span>
              <strong style="color: #F8FAFC;">واتساپ:</strong>
              <a href="https://wa.me/989121305167" class="mono" dir="ltr" style="color: #4ADE80; font-weight: 700;">09121305167</a>
            </div>
            <div style="margin-top: 0.25rem;">
              <strong style="color: #F8FAFC;">ساعات کاری:</strong> شنبه تا پنج‌شنبه ۰۹:۰۰ تا ۱۸:۰۰
            </div>
          </div>
        </div>

        <div>
          <h4 class="footer-col-title">دسته‌بندی محصولات</h4>
          <ul class="footer-links">
            <li><a href="{base_prefix}products/index.html">کاتالوگ جامع محصولات (۵۰۰ کد فنی)</a></li>
            <li><a href="{base_prefix}products/pneumatic-cylinders/index.html">جک و سیلندر پنوماتیک ISO 15552</a></li>
            <li><a href="{base_prefix}products/solenoid-valves/index.html">شیرهای برقی و کنترل جهت پنوماتیک</a></li>
            <li><a href="{base_prefix}products/air-preparation/index.html">واحد مراقبت و آماده‌سازی هوا (FRL)</a></li>
            <li><a href="{base_prefix}products/pneumatic-fittings/index.html">اتصالات و رابط‌های پنوماتیک</a></li>
            <li><a href="{base_prefix}products/pneumatic-tubing/index.html">شیلنگ و لوله‌های پنوماتیک</a></li>
            <li><a href="{base_prefix}products/flow-control-valves/index.html">شیرهای کنترل جریان و سرعت</a></li>
            <li><a href="{base_prefix}products/pressure-regulators/index.html">رگلاتورهای فشار و فیلتر رگلاتور</a></li>
            <li><a href="{base_prefix}products/silencers-exhaust/index.html">صداخفه‌کن و اگزوز پنوماتیک</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-title">برندها و ابزارهای مهندسی</h4>
          <ul class="footer-links">
            <li><a href="{base_prefix}brands/jpc/index.html">برند تجاری اختصاصی JPC</a></li>
            <li><a href="{base_prefix}brands/festo/index.html">تأمین و معادل‌یابی فستو (Festo)</a></li>
            <li><a href="{base_prefix}brands/norgren/index.html">تأمین و معادل‌یابی نورگرن (Norgren)</a></li>
            <li><a href="{base_prefix}brands/bosch-rexroth/index.html">نمایه تاریخی Bosch Rexroth / AVENTICS</a></li>
            <li><a href="{root_home}#calculator">محاسبه‌گر نیروی سیلندر پنوماتیک (N / kgf)</a></li>
            <li><a href="{base_prefix}festo-cross-reference.html">ابزار معادل‌یابی کدهای فنی پنوماتیک</a></li>
            <li><a href="https://ai.jpciran.com" target="_blank" rel="noopener noreferrer" style="color:#F28C28; font-weight:700;">دستیار هوشمند تشخیص پلاک AI</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-title">مقالات تخصصی و نقشه‌های سایت</h4>
          <ul class="footer-links">
            <li><a href="{base_prefix}festo-cross-reference.html">جدول معادل‌یابی فستو، نورگرن و رکسروت به JPC</a></li>
            <li><a href="{base_prefix}pneumatic-cylinder-buying-guide.html">راهنمای خرید جک پنوماتیک</a></li>
            <li><a href="{base_prefix}solenoid-valve-guide.html">راهنمای انتخاب شیر برقی ۵/۲ و ۵/۳</a></li>
            <li><a href="{base_prefix}pneumatics-lalehzar-tehran.html">فروشگاه پنوماتیک لاله‌زار تهران</a></li>
            <li><a href="{base_prefix}what-is-pneumatics-jpc.html">پنوماتیک چیست و معرفی برند JPC</a></li>
            <li><a href="{base_prefix}assets/docs/jpc-general-catalog.pdf" download>دانلود کاتالوگ جامع JPC (PDF)</a></li>
            <li><a href="{base_prefix}sitemap.xml" target="_blank">نقشه سایت (sitemap.xml)</a> | <a href="{base_prefix}llms.txt" target="_blank">llms.txt</a></li>
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


def build_base_jsonld_graph(canonical_url: str, breadcrumbs: list, extra_nodes: list = None) -> str:
    """
    Build valid JSON-LD @graph with Organization (containing the single founder=امیر جلالی node),
    WebSite, BreadcrumbList, and any page-specific nodes (Product, ItemList, FAQPage, CollectionPage).
    """
    org_node = {
        "@type": ["Organization", "LocalBusiness"],
        "@id": "https://jpciran.com/#organization",
        "name": "شرکت جلالی پنوماتیک (JPC)",
        "alternateName": ["Jalali Pneumatic Company", "JPC", "جلالی پنوماتیک", "jpciran.com"],
        "url": "https://www.jpciran.com/",
        "telephone": ["+98-21-33110796", "+98-21-33932529", "+98-912-130-5167"],
        "founder": {
            "@type": "Person",
            "name": "امیر جلالی",
            "jobTitle": "مدیریت شرکت جلالی پنوماتیک (JPC)",
        },
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "لاله‌زار جنوبی، روبروی کوچه علیپور، پاساژ رزاق‌منش، پلاک ۱",
            "addressLocality": "تهران",
            "addressRegion": "تهران",
            "addressCountry": "IR",
        },
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"],
                "opens": "09:00",
                "closes": "18:00",
            }
        ],
    }

    website_node = {
        "@type": "WebSite",
        "@id": "https://jpciran.com/#website",
        "url": "https://www.jpciran.com/",
        "name": "شرکت جلالی پنوماتیک (JPC)",
        "inLanguage": "fa-IR",
        "publisher": {"@id": "https://jpciran.com/#organization"},
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://www.jpciran.com/?q={search_term_string}",
            "query-input": "required name=search_term_string",
        },
    }

    breadcrumb_node = {
        "@type": "BreadcrumbList",
        "@id": f"{canonical_url}#breadcrumb",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": idx + 1,
                "name": name,
                "item": url,
            }
            for idx, (name, url) in enumerate(breadcrumbs)
        ],
    }

    graph = [org_node, website_node, breadcrumb_node]
    if extra_nodes:
        graph.extend(extra_nodes)

    payload = {
        "@context": "https://schema.org",
        "@graph": graph,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def render_full_html_page(
    title: str,
    meta_description: str,
    canonical_url: str,
    base_prefix: str,
    active_section: str,
    jsonld_str: str,
    main_html: str,
    page_category_attr: str = "all",
    extra_inline_script: str = "",
) -> str:
    """
    Assemble complete semantic RTL Persian HTML document with depth-aware relative links.
    """
    header_html = build_chrome_header(base_prefix=base_prefix, active_section=active_section)
    supplier_html = build_supplier_support_block(base_prefix=base_prefix)
    footer_and_modals = build_modals_and_footer(base_prefix=base_prefix)

    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(meta_description)}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
  <link rel="canonical" href="{esc(canonical_url)}" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="fa_IR" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(meta_description)}" />
  <meta property="og:url" content="{esc(canonical_url)}" />
  <meta property="og:site_name" content="شرکت جلالی پنوماتیک (JPC)" />
  <link rel="stylesheet" href="{base_prefix}assets/css/styles.css?v={ASSET_VERSION}" />
  <script type="application/ld+json">
{jsonld_str}
  </script>
</head>
<body data-page-category="{esc(page_category_attr)}">
{header_html}

  <main id="main-content">
{main_html}
{supplier_html}
  </main>

{footer_and_modals}

  <script src="{base_prefix}assets/js/config.js?v={ASSET_VERSION}" defer></script>
  <script src="{base_prefix}assets/js/products-data.js?v={ASSET_VERSION}" defer></script>
  <script src="{base_prefix}assets/js/app.js?v={ASSET_VERSION}" defer></script>
{extra_inline_script}
</body>
</html>
"""
