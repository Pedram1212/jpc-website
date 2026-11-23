"""
Multi-Level Catalog Templates:
- Main Catalog Hub: `/products/index.html` (`depth=1`, `base_prefix="../"`)
- 8 Category Pages: `/products/<category-slug>/index.html` (`depth=2`, `base_prefix="../../"`)
- 4 Brand Pages: `/brands/<brand-slug>/index.html` (`depth=2`, `base_prefix="../../"`)
- 30 Product Family / Series Pages: `/series/<family-slug>/index.html` (`depth=2`, `base_prefix="../../"`)
"""

from .common import (
    SITE_DOMAIN,
    build_base_jsonld_graph,
    esc,
    get_schematic_svg,
    render_full_html_page,
)
from .product_page import get_product_slug

# ---------------------------------------------------------------------------
# 8 Required Category Pages Specification (`/products/<slug>/`)
# ---------------------------------------------------------------------------
CATEGORY_PAGES_SPEC = [
    {
        "slug": "pneumatic-cylinders",
        "uiCategory": "cylinders",
        "h1Fa": "جک و سیلندر پنوماتیک صنعتی (استاندارد ISO 15552، چهارمیل، کامپکت و قلمی)",
        "titleSeo": "جک و سیلندر پنوماتیک صنعتی (ISO 15552، کامپکت و قلمی) | استعلام قیمت JPC و فستو",
        "metaDesc": "کاتالوگ فنی و استعلام قیمت جک و سیلندر پنوماتیک استاندارد ISO 15552، سری DNC، SC، ADVU و MAL برند JPC و ۳۰0 مدل جک فستو سری DSBC و DSBC-D3 در لاله‌زار تهران.",
        "introFa": "عملگرها و سیلندرهای پنوماتیک قلب حرکتی خطوط تولید، ماشین‌آلات بسته‌بندی و سیستم‌های اتوماسیون صنعتی هستند. در این بخش، مشخصات فنی ۳۰۴ کد جک پنوماتیک شامل خانواده استاندارد ISO 15552 (سری‌های JPC DNC و Festo DSBC / DSBC-D3)، جک‌های چهارمیل مهارشده (JPC SC)، جک‌های کامپکت کورس کوتاه (JPC ADVU) و جک‌های قلمی استوانه‌ای (JPC MAL) با امکان فیلتر بر اساس قطر پیستون (۲۵ تا ۱۲۵ میلی‌متر)، کورس حرکتی و نوع ضربه‌گیر (PPV / PPS) گردآوری شده است.",
        "matchCategoryIds": ["pneumatic-cylinders"],
        "matchFamilies": ["jpc-dnc", "jpc-sc", "jpc-advu", "jpc-mal", "festo-dsbc", "festo-dsbc-d3"],
        "subcategoriesFa": ["جک استاندارد ISO 15552", "جک استاندارد سه‌شیار D3", "جک میله‌کش چهارمیل (SC)", "جک کامپکت (ADVU)", "جک قلمی (MAL)"],
        "faqs": [
            ("تفاوت جک استاندارد ISO 15552 سری DNC/DSBC با جک چهارمیل SC چیست؟", "جک‌های ISO 15552 (مانند JPC DNC و Festo DSBC) دارای ابعاد نصب و فاصله سوراخ‌های کاملاً یکسان طبق استاندارد بین‌المللی ISO 15552 هستند و جایگزینی برندها با یکدیگر بدون تغییر شاسی امکان‌پذیر است؛ در حالی که جک‌های سری SC دارای استاندارد ابعادی آسیایی بوده و قبل از جایگزینی باید فاصله پیچ‌های سر و ته بررسی شود."),
            ("تفاوت ضربه‌گیر PPV و PPS در سیلندرهای پنوماتیک فستو DSBC چیست؟", "در مدل‌های PPVA، ضربه‌گیر انتهای کورس توسط پیچ سوزنی روی کله‌گی قابل تنظیم دستی است؛ اما در مدل‌های PPSA، ضربه‌گیر پنوماتیک به‌صورت خودتنظیم (Self-adjusting) متناسب با سرعت و بار پیستون عمل می‌کند."),
        ],
    },
    {
        "slug": "solenoid-valves",
        "uiCategory": "valves",
        "h1Fa": "شیرهای برقی و کنترل جهت پنوماتیک (۵/۲، ۵/۳ و ۳/۲ تک‌بوبین و دوبوبین)",
        "titleSeo": "شیر برقی پنوماتیک ۵/۲، ۵/۳ و ۳/۲ (JPC، نورگرن V60/V61 و رکسروت) | جلالی پنوماتیک",
        "metaDesc": "مشخصات فنی، معادل‌یابی و استعلام قیمت شیر برقی پنوماتیک 5/2، 5/3 و 3/2 برند JPC (سری 4V210، 4V220، 4V330C)، شیرهای Norgren سری V60/V61/V63 و سیستم جزیره‌ای Rexroth HF03-LG.",
        "introFa": "شیرهای برقی و کنترل جهت پنوماتیک وظیفه هدایت هوای فشرده به پورت‌های رفت و برگشت سیلندرها و عملگرها را بر عهده دارند. این گروه شامل ۴۸ کد شیر کنترل جهت از جمله شیرهای ۵/۲ تک‌بوبین و دوبوبین و ۵/۳ مرکز بسته برند اختصاصی JPC (سری‌های 4V210، 4V220، 4V330C و 3V210)، شیرهای اسپول و پایلوتی Norgren سری‌های V60، V61 و V63 و کدهای مرجع سیستم جزیره‌ای Bosch Rexroth / AVENTICS سری HF03-LG است.",
        "matchCategoryIds": ["directional-control-valves", "valve-manifold-accessories"],
        "matchFamilies": ["jpc-4v210", "jpc-4v220", "jpc-4v330c", "jpc-3v210", "norgren-v60", "norgren-v61", "norgren-v63", "rexroth-hf03-lg"],
        "subcategoriesFa": ["شیر برقی ۵/۲ تک‌بروبین و دوبوبین", "شیر برقی ۵/۳ مرکز بسته و APB", "شیر برقی ۳/۲ نرمال بسته", "شیر کنترل جهت و قطعات سیستم جزیره‌ای HF03-LG"],
        "faqs": [
            ("تفاوت شیر برقی ۵/۲ تک‌بوبین (4V210) با دوبوبین (4V220) چیست؟", "شیر ۵/۲ تک‌بوبین دارای برگشت فنری است و با قطع برق بوبین به حالت اولیه بازمی‌گردد؛ اما شیر ۵/۲ دوبوبین حافظه‌دار (Bistable) است و حتی پس از قطع پالس برق، آخرین وضعیت خود را حفظ می‌کند."),
            ("در استعلام شیرهای Norgren سری V60 و V61 چه پارامتری باید حتماً مشخص شود؟", "علاوه بر سایز پورت (G1/8 در V60 و G1/4 در V61) و آرایش شیر (3/2، 5/2 یا 5/3 APB)، ولتاژ دقیق بوبین (24V DC یا 220V AC) و نوع سوکت باید پیش از نهایی‌سازی سفارش تأیید گردد."),
        ],
    },
    {
        "slug": "air-preparation",
        "uiCategory": "frl-accessories",
        "h1Fa": "واحد مراقبت و آماده‌سازی هوای فشرده (FRL: فیلتر، رگلاتور و روغن‌زن)",
        "titleSeo": "واحد مراقبت پنوماتیک FRL (سری AC4010 برند JPC و Excelon نورگرن BL72/BL73/BL74)",
        "metaDesc": "مرجع تخصصی واحد مراقبت هوای فشرده سه تکه و دو تکه FRL برند JPC مدل AC4010-04-D و سری Excelon نورگرن (BL72، BL73، BL74) در سایزهای G1/4 تا G1/2 با تخلیه اتوماتیک.",
        "introFa": "کیفیت هوای فشرده مهم‌ترین عامل در افزایش طول عمر پکینگ‌های سیلندر و اسپول شیرهای برقی است. واحدهای مراقبت هوا (FRL) شامل فیلتر رطوبت‌گیر، رگلاتور تنظیم فشار و روغن‌زن میکروفوگ در برند اختصاصی JPC (سری AC2010 تا AC4010 با کاسه محافظ فلزی و تخلیه اتوماتیک) و واحدهای ترکیبی Norgren سری Excelon (BL72، BL73 و BL74) در این صفحه دسته‌بندی شده‌اند.",
        "matchCategoryIds": ["air-preparation-frl"],
        "matchFamilies": ["jpc-ac4010", "norgren-bl72", "norgren-bl73", "norgren-bl74"],
        "subcategoriesFa": ["واحد مراقبت ترکیبی FRL با تخلیه اتوماتیک", "ست فیلتر رگولاتور روغن‌زن Norgren Excelon سایز G1/4 تا G1/2"],
        "faqs": [
            ("تفاوت تخلیه اتوماتیک و نیمه‌اتوماتیک در کاسه فیلتر واحد مراقبت چیست؟", "در تخلیه اتوماتیک (پسوند D در JPC AC4010-04-D یا کدهای GA در Norgren BL72)، به محض رسیدن سطح آب تقطیرشده به حد مشخص، شناور داخلی مسیر تخلیه را باز می‌کند؛ در حالی که در مدل دستی/نیمه‌اتوماتیک تخلیه با فشار دادن شیر زیر کاسه یا قطع فشار خط انجام می‌شود."),
            ("دقت فیلتراسیون استاندارد واحد مراقبت پنوماتیک چند میکرون است؟", "برای مصارف عمومی کارگاهی و جک‌ها و شیرهای استاندارد، المان فیلتر ۲۵ یا ۴۰ میکرون و برای ابزار دقیق و شیرهای حساس المان ۵ میکرون استفاده می‌شود."),
        ],
    },
    {
        "slug": "pneumatic-fittings",
        "uiCategory": "frl-accessories",
        "h1Fa": "اتصالات فشاری و رابط‌های پنوماتیک (سری QS فستو، JPC و اتصالات رزوه‌ای)",
        "titleSeo": "اتصالات پنوماتیک فشاری و رزوه‌ای (۱۰۰ کد سری QS فستو و کیت اتصالات JPC)",
        "metaDesc": "کاتالوگ کامل ۱۰۳ کد اتصالات فشاری و رابط شیلنگ پنوماتیک شامل سری‌های QS، QSS، QSSF، QSC، QSH، QSL-H و QSLV فستو (Festo) و اتصالات برنجی برند JPC.",
        "introFa": "اتصالات سریع فشاری (Push-in Fittings) امکان لوله‌کشی ایمن و بدون نشتی شیلنگ‌های پلی‌اورتان (PU) و پلی‌آمید (PA) را در تابلوهای پنوماتیک فراهم می‌کنند. این بخش شامل بیش از ۱۰۰ کد فنی از خانواده Festo QS (مستقیم، کاهنده، پنلی، زانویی، سه‌راهی و درپوش فشاری در سایزهای ۴ تا ۱۶ میلی‌متر و رزوه‌های G1/8 تا G1/2) به همراه مجموعه اتصالات صنعتی JPC است.",
        "matchCategoryIds": ["pneumatic-fittings", "pneumatic-kits"],
        "matchFamilies": ["jpc-hvff", "festo-qs", "festo-qs-reducing", "festo-qss", "festo-qss-f", "festo-qssf", "festo-qsc", "festo-qs-h", "festo-qsh", "festo-qsl-h", "festo-qslv"],
        "subcategoriesFa": ["رابط مستقیم دوطرفه (QS)", "رابط کاهنده (QS-reducing)", "رابط پنلی و رزوه‌دار (QSS / QSSF)", "زانویی و سه‌راهی فشاری (QSL-H / QSLV)", "درپوش فشاری شیلنگ (QSC)"],
        "faqs": [
            ("نحوه تشخیص سایز شیلنگ مناسب برای اتصالات فشاری سری QS فستو چگونه است؟", "عدد درج‌شده در کد اتصالات فشاری (مانند QS-8 یا QSLV-G1/4-8) همواره نشان‌دهنده قطر خارجی شیلنگ (Outside Diameter - OD) بر حسب میلی‌متر است، نه قطر داخلی شیلنگ."),
            ("نکته مهم درباره تعداد در بسته (Pack Quantity) در سفارش اتصالات فستو چیست؟", "اتصالات سری QS فستو در بسته‌بندی‌های ۱۰، ۲۰، ۵۰ یا ۱۰۰ عددی عرضه می‌شوند؛ پیش از نهایی‌سازی پیش‌فاکتور، واحد شمارش (عدد یا بسته) توسط کارشناسان فروش JPC شفاف‌سازی می‌شود."),
        ],
    },
    {
        "slug": "pneumatic-tubing",
        "uiCategory": "frl-accessories",
        "h1Fa": "شیلنگ‌های پنوماتیک پلی‌اورتان (PU)، پلی‌آمید و رابط‌های بین‌راهی شیلنگ",
        "titleSeo": "شیلنگ پنوماتیک PU و رابط‌های اتصال شیلنگ (سایز ۴ تا ۱۶ میلی‌متر) | JPC Iran",
        "metaDesc": "تأمین و استعلام قیمت شیلنگ پنوماتیک پلی‌اورتان (PU) در سایزهای ۴، ۶، ۸، ۱۰، ۱۲ و ۱۶ میلی‌متر و رابط‌های مستقیم و کاهنده شیلنگ فستو (QS / QSS) و JPC.",
        "introFa": "انتخاب شیلنگ پنوماتیک با قطر خارجی دقیق و تلرانس استاندارد، شرط اصلی آب‌بندی کامل در کولت اتصالات فشاری است. در این بخش، مجموعه شیلنگ‌های پلی‌اورتان (PU) منعطف برند JPC به همراه رابط‌های مستقیم شیلنگ به شیلنگ (QS)، رابط‌های کاهنده سایز شیلنگ (QS-reducing)، رابط‌های پنلی عبوری شیلنگ (QSS) و درپوش‌های مسدودکننده مسیر شیلنگ (QSC) برای سایزهای ۴ تا ۱۶ میلی‌متر ارائه شده است.",
        "matchCategoryIds": ["pneumatic-kits"],
        "matchFamilies": ["jpc-hvff", "festo-qs", "festo-qs-reducing", "festo-qss", "festo-qsc"],
        "subcategoriesFa": ["شیلنگ پلی‌اورتان PU سایز ۴ تا ۱۶ میلی‌متر", "رابط مستقیم دوطرفه شیلنگ (QS)", "رابط کاهنده سایز شیلنگ (QS-reducing)", "درپوش انتهای شیلنگ (QSC)"],
        "faqs": [
            ("چه سایز شیلنگی برای جک‌ها و شیرهای برقی صنعتی مناسب‌تر است؟", "برای جک‌های قطر ۲۵ و ۳۲ میلی‌متر معمولاً شیلنگ ۶ یا ۸ میلی‌متر، برای جک‌های قطر ۴۰ تا ۶۳ میلی‌متر شیلنگ ۸ یا ۱۰ میلی‌متر، و برای جک‌های قطر ۸۰ تا ۱۲۵ میلی‌متر یا خطوط اصلی تغذیه شیلنگ ۱۰، ۱۲ یا ۱۶ میلی‌متر توصیه می‌شود."),
            ("حداکثر فشار کاری مجاز شیلنگ‌های پلی‌اورتان (PU) چقدر است؟", "در دمای محیط ۲۰ درجه سانتی‌گراد، فشار کاری استاندارد شیلنگ‌های PU صنعتی بین ۸ تا ۱۰ بار است و با افزایش دما، فشار مجاز کاری کاهش می‌یابد."),
        ],
    },
    {
        "slug": "flow-control-valves",
        "uiCategory": "frl-accessories",
        "h1Fa": "شیرهای کنترل جریان، فلوکنترل سرسیلندری و بین‌راهی پنوماتیک",
        "titleSeo": "شیر کنترل جریان و فلوکنترل پنوماتیک (سرسیلندری SL و بین‌راهی HVFF/ASC) | JPC",
        "metaDesc": "راهنمای انتخاب و استعلام قیمت شیر کنترل سرعت و جریان پنوماتیک (فلوکنترل سرسیلندری، بین‌راهی سری ASC و HVFF برند JPC و اتصالات کنترل مسیر فستو) در لاله‌زار تهران.",
        "introFa": "کنترل دقیق سرعت حرکت پیستون جک‌های پنوماتیک و جلوگیری از کوبش در انتهای کورس، توسط شیرهای کنترل جریان یک‌طرفه (One-way Flow Control Valves) انجام می‌شود. مجموعه فلوکنترل‌های سرسیلندری (Meter-out)، شیرهای کنترل سرعت بین‌راهی شیلنگی (HVFF) و فلوکنترل‌های تابلویی سری ASC برند JPC به همراه اتصالات زانویی و پنلی مرتبط در این صفحه قابل بررسی و استعلام هستند.",
        "matchCategoryIds": ["pneumatic-kits"],
        "matchFamilies": ["jpc-hvff", "festo-qslv", "festo-qsl-h", "festo-qssf"],
        "subcategoriesFa": ["فلوکنترل سرسیلندری (SL / GRLA)", "فلوکنترل بین‌راهی شیلنگی (HVFF)", "شیر کنترل جریان خطی (ASC)", "اتصالات زانویی گردان سرسیلندری (QSLV)"],
        "faqs": [
            ("چرا در جک‌های پنوماتیک دوکاره از روش کنترل خروجی (Meter-Out) استفاده می‌شود؟", "در روش Meter-Out، هوای در حال تخلیه از جلوی پیستون محدود می‌شود؛ این کار یک پشت‌بند هوایی ایجاد کرده و حرکت پیستون را حتی در برابر تغییرات ناگهانی بار کاملاً یکنواخت و بدون پرش (Stick-Slip) نگه می‌دارد."),
            ("آیا امکان سفارش جداگانه فلوکنترل‌های سری SL و ASC از مجموعه JPC وجود دارد؟", "بله؛ کد JPC-HVFF-ASC-SET نماینده خانواده اتصالات و کنترل جریان JPC است و هر یک از سایزها (M5 تا G1/2 و شیلنگ ۴ تا ۱۲ میلی‌متر) به‌صورت مجزا در سبد استعلام قابل سفارش هستند."),
        ],
    },
    {
        "slug": "pressure-regulators",
        "uiCategory": "frl-accessories",
        "h1Fa": "رگلاتورهای فشار، فیلتر رگلاتور و واحدهای تثبیت فشار پنوماتیک",
        "titleSeo": "رگلاتور فشار هوا و فیلتر رگلاتور پنوماتیک (JPC و Norgren Excelon) | استعلام قیمت",
        "metaDesc": "بررسی مشخصات و استعلام قیمت رگلاتور فشار و فیلتر رگلاتور پنوماتیک برند JPC (سری AR / AW / AC4010) و واحدهای Excelon نورگرن (BL72، BL73، BL74) با گیج فشار.",
        "introFa": "تثبیت فشار کاری مدار پنوماتیک در مقدار بهینه (معمولاً ۶ بار) علاوه بر جلوگیری از آسیب به قطعات و پکینگ‌ها، مصرف انرژی کمپرسور را به شکل چشمگیری کاهش می‌دهد. در این بخش، واحدهای فیلتر رگلاتور و مجموعه‌های تنظیم فشار JPC و سری‌های صنعتی Norgren Excelon در سایزهای G1/4، G3/8 و G1/2 همراه با راهنمای انتخاب ارائه شده‌اند.",
        "matchCategoryIds": ["air-preparation-frl"],
        "matchFamilies": ["jpc-ac4010", "norgren-bl72", "norgren-bl73", "norgren-bl74"],
        "subcategoriesFa": ["فیلتر رگلاتور و روغن‌زن سایز G1/4 (BL72)", "فیلتر رگلاتور و روغن‌زن سایز G3/8 (BL73)", "فیلتر رگلاتور و روغن‌زن سایز G1/2 (AC4010 / BL74)"],
        "faqs": [
            ("منظور از رگلاتور فشار نوع Relieving (تخلیه‌دار) چیست؟", "در رگلاتورهای Relieving، اگر شما فشار تنظیمی را از مثلاً ۷ بار به ۵ بار کاهش دهید، فشار اضافی حبس‌شده در خط خروجی (Downstream) به‌صورت خودکار از سوراخ تخلیه رگلاتور به اتمسفر آزاد می‌شود تا فشار خط بلافاصله به ۵ بار برسد."),
            ("فشار کاری پیشنهادی برای اکثر شیرها و جک‌های پنوماتیک صنعتی چند بار است؟", "اکثر تجهیزات استاندارد پنوماتیک برای عملکرد بهینه در فشار ۶ بار (0.6 MPa) طراحی شده‌اند؛ بالا بردن غیرضروری فشار به ۸ یا ۱۰ بار تنها استهلاک آب‌بندها و مصرف هوای فشرده را افزایش می‌دهد."),
        ],
    },
    {
        "slug": "silencers-exhaust",
        "uiCategory": "frl-accessories",
        "h1Fa": "صداخفه‌کن (سایلنسر) برنزی و اگزوز تخلیه شیرهای برقی پنوماتیک",
        "titleSeo": "سایلنسر و صداخفه‌کن برنزی پنوماتیک (سری T40 نورگرن و JPC) | سایز G1/8 تا G1/2",
        "metaDesc": "کاتالوگ فنی و استعلام قیمت صداخفه‌کن و سایلنسر برنزی پنوماتیک Norgren سری T40 (رزوه G و R از ۱/۸ تا ۱/۲ اینچ) و سایلنسرهای شیر برقی JPC جهت کاهش صدای تخلیه.",
        "introFa": "نصب صداخفه‌کن (Pneumatic Silencer / Exhaust Muffler) روی پورت‌های تخلیه (R و S) شیرهای برقی پنوماتیک علاوه بر کاهش تراز صوتی کارگاه به زیر حد مجاز بهداشت حرفه‌ای، از ورود گردوغبار و براده‌های محیط به داخل اسپول شیر جلوگیری می‌کند. این بخش شامل ۸ مدل سایلنسر برنزی متخلخل (Sintered Bronze) برند Norgren سری T40 با رزوه‌های موازی (G1/8 تا G1/2) و مخروطی (R1/8 تا R1/2) است.",
        "matchCategoryIds": ["silencers-exhaust"],
        "matchFamilies": ["norgren-t40", "jpc-hvff"],
        "subcategoriesFa": ["سایلنسر برنزی رزوه موازی BSPP (T40C - G1/8..G1/2)", "سایلنسر برنزی رزوه مخروطی BSPT (T40B - R1/8..R1/2)"],
        "faqs": [
            ("تفاوت سایلنسرهای سری T40C و T40B نورگرن در چیست؟", "مدل‌های T40C دارای رزوه موازی استاندارد ISO 228-1 (G1/8 تا G1/2) هستند، در حالی که مدل‌های T40B دارای رزوه مخروطی استاندارد ISO 7-1 (R1/8 تا R1/2) می‌باشند."),
            ("چرا گرفتگی سایلنسرهای برنزی باعث کند شدن حرکت جک پنوماتیک می‌شود؟", "انباشته شدن ذرات روغن و گردوغبار در منافذ برنز متخلخل باعث ایجاد فشار برگشتی (Back-pressure) در پورت تخلیه شیر برقی شده و سرعت تخلیه هوای جک را کاهش می‌دهد؛ لذا شست‌وشو یا تعویض دوره‌ای سایلنسرها ضروری است."),
        ],
    },
]


def render_product_summary_card(p: dict, base_prefix: str) -> str:
    """
    Render a rich product card for catalog/category/brand/series grids.
    If the product is `published`, includes a direct crawlable link to `/product/<slug>/index.html`.
    """
    is_jpc = p["brand"] == "JPC"
    is_pub = p["publicationStatus"] == "published"
    p_slug = get_product_slug(p)
    pdp_href = f"{base_prefix}product/{esc(p_slug)}/index.html" if is_pub else ""
    svg_markup = get_schematic_svg(p.get("schematicType", "cylinder-iso"))
    ta = p.get("technicalAttributes", {})

    third_val = (
        f"{ta.get('boreMm')}×{ta.get('strokeMm')} mm ({ta.get('cushioning') or 'ISO'})"
        if (ta.get("boreMm") and ta.get("strokeMm"))
        else (ta.get("valveFunction") or (f"شیلنگ {ta.get('tubeOdMm')} mm" if ta.get("tubeOdMm") else p["subCategory"]))
    )

    title_inner = (
        f'<a href="{pdp_href}" style="color: inherit; text-decoration: none;">{esc(p["titleFa"])}</a>'
        if is_pub
        else esc(p["titleFa"])
    )

    detail_action_html = (
        f'<a href="{pdp_href}" class="product-pdf-link" style="font-weight: 800; color: #087F8C;">مشاهده صفحه تخصصی محصول ←</a>'
        if is_pub
        else f'<button type="button" class="product-pdf-link js-spec-trigger" data-id="{esc(p["id"])}">مشاهده جدول مشخصات سریع ←</button>'
    )

    return f"""          <article class="product-card {'is-jpc-brand' if is_jpc else ''}" id="card-{esc(p['id'])}" data-product-id="{esc(p['id'])}">
            <div>
              <div class="product-card-top">
                <span class="brand-badge {'badge-jpc' if is_jpc else 'badge-euro'}">{esc(p['brandFa'])}</span>
                <span class="status-badge {'status-available' if is_jpc else 'status-inquiry'}">{esc(p['availabilityFa'])}</span>
              </div>

              <div class="product-schematic-box">
                <div class="schematic-svg-wrap">
                  {svg_markup}
                </div>
                <div class="schematic-meta">
                  <div class="product-code-row">
                    <button type="button" class="copy-code-btn js-copy-btn" data-copy="{esc(p['modelCode'])}" title="کپی کد فنی">
                      <span>کپی</span>
                    </button>
                    <span class="product-code-pill" dir="ltr">{esc(p['modelCode'])}</span>
                  </div>
                  <span class="product-cat-label">{esc(p['subCategory'])}</span>
                </div>
              </div>

              <div class="product-card-body">
                <h3 class="product-title-fa">{title_inner}</h3>
                <div class="product-specs-table">
                  <div class="spec-cell">
                    <span class="spec-key">سایز پورت / اتصال</span>
                    <span class="spec-val mono" dir="ltr">{esc(p['portSize'])}</span>
                  </div>
                  <div class="spec-cell">
                    <span class="spec-key">فشار کاری</span>
                    <span class="spec-val mono" dir="ltr">{esc(p['pressureRange'])}</span>
                  </div>
                  <div class="spec-cell spec-cell-wide">
                    <span class="spec-key">مشخصه کلیدی / سری</span>
                    <span class="spec-val">{esc(third_val)}</span>
                  </div>
                </div>
              </div>
            </div>

            <div class="product-card-footer">
              <div class="product-card-actions">
                <button type="button" class="btn btn-amber btn-sm js-quote-trigger" data-id="{esc(p['id'])}">
                  درخواست استعلام قیمت
                </button>
                <button type="button" class="btn btn-rfq-add btn-sm js-add-rfq-btn" data-id="{esc(p['id'])}">
                  + افزودن به لیست استعلام
                </button>
              </div>
              <div class="product-sub-links">
                {detail_action_html}
                <a href="{base_prefix}series/{esc(p['familyId'])}/index.html" class="product-pdf-link">
                  سری <span dir="ltr" class="mono">{esc(p['family'])}</span>
                </a>
              </div>
            </div>
          </article>"""


def render_main_catalog_hub(all_products: list, families: list, manufacturers: list) -> str:
    """
    Generate `/products/index.html` (`depth=1`, `base_prefix="../"`).
    """
    base_prefix = "../"
    canonical_url = f"{SITE_DOMAIN}/products/"
    published_products = [p for p in all_products if p["publicationStatus"] == "published"]

    breadcrumbs = [
        ("صفحه اصلی", f"{SITE_DOMAIN}/"),
        ("کاتالوگ جامع محصولات پنوماتیک", canonical_url),
    ]

    item_list_ld = {
        "@type": "ItemList",
        "@id": f"{canonical_url}#catalog-list",
        "name": "کاتالوگ جامع تجهیزات پنوماتیک صنعتی شرکت جلالی پنوماتیک (JPC)",
        "numberOfItems": len(published_products),
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": idx + 1,
                "url": f"{SITE_DOMAIN}/product/{get_product_slug(p)}/",
                "name": p["titleFa"],
            }
            for idx, p in enumerate(published_products)
        ],
    }

    jsonld_str = build_base_jsonld_graph(
        canonical_url=canonical_url,
        breadcrumbs=breadcrumbs,
        extra_nodes=[item_list_ld],
    )

    cat_cards_html = "\n".join(
        f"""        <a href="{esc(c['slug'])}/index.html" style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 12px; padding: 1.15rem; text-decoration: none; color: #10243A; display: flex; flex-direction: column; justify-content: space-between; gap: 0.6rem; transition: border-color 0.2s;">
          <div>
            <span style="font-size: 0.72rem; font-weight: 800; color: #087F8C; background: #E6F4F6; padding: 0.2rem 0.55rem; border-radius: 999px;">گروه تخصصی</span>
            <h3 style="font-size: 0.98rem; font-weight: 800; color: #10243A; margin: 0.5rem 0 0.35rem;">{esc(c['h1Fa'].split('(')[0].strip())}</h3>
            <p style="font-size: 0.8rem; color: #475569; line-height: 1.7; margin: 0;">{esc(c['metaDesc'][:115])}...</p>
          </div>
          <span style="font-size: 0.8rem; font-weight: 800; color: #087F8C;">مشاهده محصولات گروه ←</span>
        </a>"""
        for c in CATEGORY_PAGES_SPEC
    )

    brand_cards_html = "\n".join(
        f"""        <a href="{base_prefix}brands/{esc(m['id'])}/index.html" style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 12px; padding: 1.15rem; text-decoration: none; color: #10243A;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.45rem;">
            <strong style="font-size: 1rem; color: #10243A;">{esc(m['nameFa'])}</strong>
            <span class="mono" dir="ltr" style="font-size: 0.76rem; color: #087F8C; font-weight: 800;">{esc(m['code'])}</span>
          </div>
          <p style="font-size: 0.78rem; color: #475569; line-height: 1.7; margin: 0;">{esc(m['disclaimerFa'])}</p>
        </a>"""
        for m in manufacturers
    )

    series_pills_html = "\n".join(
        f"""        <a href="{base_prefix}series/{esc(f['id'])}/index.html" style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 8px; padding: 0.55rem 0.85rem; text-decoration: none; color: #10243A; font-size: 0.82rem; display: flex; justify-content: space-between; align-items: center; gap: 0.5rem;">
          <span><strong>{esc(f['brand'])}</strong> · سری <span dir="ltr" class="mono" style="color:#087F8C; font-weight:800;">{esc(f['code'])}</span></span>
          <span class="mono" dir="ltr" style="font-size: 0.74rem; background: #E2E8F0; padding: 0.12rem 0.45rem; border-radius: 999px;">{f['skuCount']} SKU</span>
        </a>"""
        for f in families
    )

    ssr_cards_html = "\n".join(render_product_summary_card(p, base_prefix) for p in published_products)

    main_html = f"""
    <nav aria-label="مسیر راهنما (Breadcrumb)" style="background: #F1F5F9; border-bottom: 1px solid #E1E7EE; padding: 0.75rem 0; font-size: 0.82rem;">
      <div class="container" style="display: flex; flex-wrap: wrap; align-items: center; gap: 0.45rem; color: #475569;">
        <a href="{base_prefix}index.html" style="color: #087F8C; font-weight: 700;">صفحه اصلی</a>
        <span aria-hidden="true">←</span>
        <strong style="color: #10243A;">کاتالوگ جامع محصولات پنوماتیک (۵۰۰ کد فنی)</strong>
      </div>
    </nav>

    <section class="section" style="background: linear-gradient(135deg, #10243A 0%, #19344F 100%); color: #FFFFFF; padding: 2.5rem 0;">
      <div class="container">
        <span style="display: inline-block; background: rgba(8,127,140,0.28); color: #38BDF8; font-size: 0.78rem; font-weight: 800; padding: 0.3rem 0.75rem; border-radius: 999px; margin-bottom: 0.75rem;">
          بانک اطلاعات فنی ۵۰۰ تجهیز پنوماتیک صنعتی · ۴۰ مدل منتخب + ۴۶۰ ردیف جستجوی فنی
        </span>
        <h1 style="font-size: clamp(1.45rem, 3.5vw, 2.15rem); font-weight: 900; color: #FFFFFF; margin-bottom: 0.65rem;">
          کاتالوگ جامع محصولات و کدهای فنی شرکت جلالی پنوماتیک (JPC)
        </h1>
        <p style="font-size: 0.95rem; color: #CBD5E1; max-width: 820px; line-height: 1.85; margin-bottom: 1.25rem;">
          جستجوی دقیق بر اساس کد مدل سازنده (<span dir="ltr" class="mono">DSBC-32-100-PPVA-N3</span>، <span dir="ltr" class="mono">JPC-4V210-08-24DC</span>، <span dir="ltr" class="mono">V61B513A-A213JB</span>)، شماره سفارش (<span dir="ltr" class="mono">1376426</span>)، قطر پیستون، کورس و سایز رزوه با امکان افزودن مستقیم به سبد استعلام چندقلمی (RFQ).
        </p>

        <!-- 8-TIER SEARCH BAR -->
        <div id="primary-tech-search-hub" style="background: #FFFFFF; border-radius: 12px; padding: 1rem; color: #10243A; position: relative;">
          <form id="hero-quick-search-form" role="search" aria-label="جستجوی کد فنی در ۵۰۰ تجهیز کاتالوگ" style="display: flex; gap: 0.65rem; flex-wrap: wrap;">
            <label for="hero-quick-search-input" class="sr-only">جستجوی کد فنی، شماره سفارش یا مشخصات پنوماتیک</label>
            <input
              type="search"
              id="hero-quick-search-input"
              class="form-input"
              placeholder="جستجوی کد فنی (مثلاً DSBC-32-100، 1376426، 4V210-08، V61B513A، QS-8، جک قطر ۶۳)..."
              autocomplete="off"
              aria-autocomplete="list"
              aria-controls="hero-tech-autocomplete"
              aria-expanded="false"
              style="flex: 1; min-width: 240px;"
            />
            <button type="button" id="hero-quick-search-clear" class="btn btn-outline-tech btn-sm" aria-label="پاک کردن جستجو">پاکسازی</button>
            <button type="submit" class="btn btn-amber">جستجو در ۵۰۰ کد فنی</button>
          </form>
          <div id="hero-tech-autocomplete" class="tech-autocomplete-panel" role="listbox" aria-label="پیشنهادهای کد فنی"></div>
        </div>
      </div>
    </section>

    <!-- 8 CATEGORY DIRECTORIES -->
    <section class="section" style="padding: 2.25rem 0 1rem;">
      <div class="container">
        <div class="section-header" style="margin-bottom: 1.25rem;">
          <span class="section-eyebrow">مرور مهندسی بر اساس گروه کالایی</span>
          <h2 class="section-title">۸ گروه تخصصی تجهیزات پنوماتیک صنعتی</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
{cat_cards_html}
        </div>
      </div>
    </section>

    <!-- 4 BRAND PAGES -->
    <section class="section" style="padding: 1.5rem 0;">
      <div class="container">
        <div class="section-header" style="margin-bottom: 1.15rem;">
          <span class="section-eyebrow">تفکیک شفاف برند اختصاصی، تأمین بین‌المللی و نمایه کدهای تاریخی</span>
          <h2 class="section-title">مرور کاتالوگ بر اساس برند و سازنده</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem;">
{brand_cards_html}
        </div>
      </div>
    </section>

    <!-- 30 PRODUCT SERIES / FAMILIES -->
    <section class="section" style="padding: 1.5rem 0;">
      <div class="container">
        <div class="section-header" style="margin-bottom: 1.15rem;">
          <span class="section-eyebrow">۳۰ خانواده و سری استاندارد پنوماتیک</span>
          <h2 class="section-title">مرور سریع سری‌های فنی (Product Families &amp; Series)</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.65rem;">
{series_pills_html}
        </div>
      </div>
    </section>

    <!-- INTERACTIVE FILTERABLE 500-PRODUCT CATALOG GRID -->
    <section class="section" id="catalog" style="padding: 2rem 0;">
      <div class="container">
        <div class="section-header" style="margin-bottom: 1.25rem;">
          <span class="section-eyebrow">فیلتر زنده و افزودن به سبد استعلام (RFQ)</span>
          <h2 class="section-title">لیست محصولات منتخب و بانک جستجوی ۵۰۰ کد فنی</h2>
        </div>

        <div class="catalog-controls" style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 12px; padding: 1.15rem; margin-bottom: 1.25rem;">
          <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; justify-content: space-between; align-items: center; margin-bottom: 0.85rem;">
            <div class="filter-pills-group" role="group" aria-label="فیلتر دسته کالایی" style="display: flex; flex-wrap: wrap; gap: 0.45rem;">
              <button type="button" class="filter-pill active" data-category-filter="all">همه دسته‌ها (۵۰۰)</button>
              <button type="button" class="filter-pill" data-category-filter="cylinders">جک و سیلندر (۳۰۴)</button>
              <button type="button" class="filter-pill" data-category-filter="valves">شیر برقی و کنترل جهت (۴۸)</button>
              <button type="button" class="filter-pill" data-category-filter="frl-accessories">واحد مراقبت، اتصالات و جانبی (۱۴۸)</button>
            </div>
            <div class="filter-pills-group" role="group" aria-label="فیلتر برند" style="display: flex; flex-wrap: wrap; gap: 0.45rem;">
              <button type="button" class="filter-pill active" data-brand-filter="all">همه برندها</button>
              <button type="button" class="filter-pill" data-brand-filter="JPC">JPC (۱۰)</button>
              <button type="button" class="filter-pill" data-brand-filter="Festo">Festo (۴۰۰)</button>
              <button type="button" class="filter-pill" data-brand-filter="Norgren">Norgren (۵۵)</button>
              <button type="button" class="filter-pill" data-brand-filter="Bosch Rexroth">Bosch Rexroth / AVENTICS (۳۵)</button>
            </div>
          </div>

          <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center; justify-content: space-between;">
            <div style="flex: 1; min-width: 240px; position: relative;">
              <label for="catalog-search-input" class="sr-only">فیلتر فوری کد فنی یا مشخصات</label>
              <input
                type="search"
                id="catalog-search-input"
                class="form-input"
                placeholder="فیلتر فوری کد مدل، شماره سفارش، قطر پیستون، سایز پورت..."
              />
              <button type="button" id="search-clear-btn" class="search-clear-btn" aria-label="پاک کردن">✕</button>
            </div>
            <div id="catalog-result-counter" style="font-size: 0.85rem; color: #475569;">
              نمایش <strong>{len(published_products)}</strong> مدل منتخب از <strong>500</strong> تجهیز کاتالوگ
            </div>
          </div>
        </div>

        <div class="products-grid" id="catalog-products-grid">
{ssr_cards_html}
        </div>
      </div>
    </section>
"""

    return render_full_html_page(
        title="کاتالوگ جامع محصولات پنوماتیک صنعتی (۵۰۰ کد فنی JPC، فستو، نورگرن و رکسروت)",
        meta_description="مرجع جستجوی فنی و استعلام قیمت ۵۰۰ تجهیز پنوماتیک صنعتی شامل جک ISO 15552 فستو DSBC، شیر برقی JPC و نورگرن V60/V61، واحد مراقبت هوا و اتصالات QS در لاله‌زار تهران.",
        canonical_url=canonical_url,
        base_prefix=base_prefix,
        active_section="products",
        jsonld_str=jsonld_str,
        main_html=main_html,
        page_category_attr="all",
    )


def render_category_directory_page(cat_spec: dict, all_products: list, families: list) -> str:
    """
    Generate `/products/<cat-slug>/index.html` (`depth=2`, `base_prefix="../../"`).
    """
    base_prefix = "../../"
    slug = cat_spec["slug"]
    canonical_url = f"{SITE_DOMAIN}/products/{slug}/"

    matching_all = [
        p for p in all_products
        if p["categoryId"] in cat_spec["matchCategoryIds"] or p["familyId"] in cat_spec["matchFamilies"]
    ]
    matching_pub = [p for p in matching_all if p["publicationStatus"] == "published"]
    display_products = matching_pub if matching_pub else matching_all[:12]

    matching_families = [
        f for f in families
        if f["id"] in cat_spec["matchFamilies"] or f["categoryId"] in cat_spec["matchCategoryIds"]
    ]

    breadcrumbs = [
        ("صفحه اصلی", f"{SITE_DOMAIN}/"),
        ("محصولات", f"{SITE_DOMAIN}/products/"),
        (cat_spec["h1Fa"].split("(")[0].strip(), canonical_url),
    ]

    faq_ld = {
        "@type": "FAQPage",
        "@id": f"{canonical_url}#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in cat_spec["faqs"]
        ],
    }

    item_list_ld = {
        "@type": "ItemList",
        "@id": f"{canonical_url}#itemlist",
        "name": cat_spec["h1Fa"],
        "numberOfItems": len(display_products),
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": idx + 1,
                "url": (
                    f"{SITE_DOMAIN}/product/{get_product_slug(p)}/"
                    if p["publicationStatus"] == "published"
                    else f"{SITE_DOMAIN}/series/{p['familyId']}/"
                ),
                "name": p["titleFa"],
            }
            for idx, p in enumerate(display_products)
        ],
    }

    jsonld_str = build_base_jsonld_graph(
        canonical_url=canonical_url,
        breadcrumbs=breadcrumbs,
        extra_nodes=[item_list_ld, faq_ld],
    )

    subcat_badges = "\n".join(
        f'<span style="background: #F1F5F9; border: 1px solid #CBD5E1; color: #1E293B; font-size: 0.78rem; font-weight: 700; padding: 0.3rem 0.7rem; border-radius: 999px;">{esc(sc)}</span>'
        for sc in cat_spec["subcategoriesFa"]
    )

    family_links_html = "\n".join(
        f"""        <a href="{base_prefix}series/{esc(f['id'])}/index.html" style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 10px; padding: 0.9rem 1rem; text-decoration: none; color: #10243A; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <strong style="font-size: 0.9rem; color: #10243A;">سری <span dir="ltr" class="mono" style="color: #087F8C;">{esc(f['code'])}</span> ({esc(f['brand'])})</strong>
            <div style="font-size: 0.76rem; color: #64748B; margin-top: 0.15rem;">{esc(f['titleFa'])}</div>
          </div>
          <span class="mono" dir="ltr" style="font-size: 0.75rem; font-weight: 800; color: #087F8C; background: #E6F4F6; padding: 0.2rem 0.55rem; border-radius: 999px;">{f['skuCount']} کد ←</span>
        </a>"""
        for f in matching_families
    )

    cards_html = "\n".join(render_product_summary_card(p, base_prefix) for p in display_products)

    faqs_html = "\n".join(
        f"""        <details class="faq-item" {'open' if idx == 0 else ''} style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem 1.15rem; margin-bottom: 0.75rem;">
          <summary style="font-weight: 800; color: #10243A; cursor: pointer; font-size: 0.94rem;">{esc(q)}</summary>
          <p style="margin-top: 0.65rem; font-size: 0.87rem; color: #475569; line-height: 1.85;">{esc(a)}</p>
        </details>"""
        for idx, (q, a) in enumerate(cat_spec["faqs"])
    )

    other_cats_html = "\n".join(
        f'<a href="{base_prefix}products/{esc(c["slug"])}/index.html" class="btn btn-outline-tech btn-xs">{esc(c["h1Fa"].split("(")[0].strip())}</a>'
        for c in CATEGORY_PAGES_SPEC
        if c["slug"] != slug
    )

    main_html = f"""
    <nav aria-label="مسیر راهنما (Breadcrumb)" style="background: #F1F5F9; border-bottom: 1px solid #E1E7EE; padding: 0.75rem 0; font-size: 0.82rem;">
      <div class="container" style="display: flex; flex-wrap: wrap; align-items: center; gap: 0.45rem; color: #475569;">
        <a href="{base_prefix}index.html" style="color: #087F8C; font-weight: 700;">صفحه اصلی</a>
        <span aria-hidden="true">←</span>
        <a href="{base_prefix}products/index.html" style="color: #087F8C; font-weight: 700;">محصولات</a>
        <span aria-hidden="true">←</span>
        <strong style="color: #10243A;">{esc(cat_spec['h1Fa'].split('(')[0].strip())}</strong>
      </div>
    </nav>

    <section class="section" style="background: #FFFFFF; border-bottom: 1px solid #E1E7EE; padding: 2.25rem 0;">
      <div class="container">
        <span class="section-eyebrow">گروه تخصصی محصولات پنوماتیک · بانک اطلاعات فنی JPC</span>
        <h1 style="font-size: clamp(1.35rem, 3.2vw, 1.95rem); font-weight: 900; color: #10243A; margin: 0.35rem 0 0.75rem;">
          {esc(cat_spec['h1Fa'])}
        </h1>
        <p style="font-size: 0.92rem; color: #334155; line-height: 1.9; max-width: 900px; margin-bottom: 1rem;">
          {esc(cat_spec['introFa'])}
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 0.45rem; margin-bottom: 1rem;">
{subcat_badges}
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
          {other_cats_html}
        </div>
      </div>
    </section>

    <section class="section" style="padding: 1.75rem 0 0.75rem;">
      <div class="container">
        <h2 style="font-size: 1.15rem; font-weight: 800; color: #10243A; margin-bottom: 0.9rem;">
          خانواده‌ها و سری‌های فنی مرتبط در این گروه ({len(matching_families)} سری · {len(matching_all)} کد فنی)
        </h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 0.85rem;">
{family_links_html}
        </div>
      </div>
    </section>

    <section class="section" style="padding: 1.75rem 0;">
      <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.1rem;">
          <div>
            <span class="section-eyebrow">مدل‌های شاخص و پرکاربرد صنعتی</span>
            <h2 style="font-size: 1.2rem; font-weight: 800; color: #10243A; margin-top: 0.2rem;">
              فهرست محصولات منتخب این گروه کالایی
            </h2>
          </div>
          <a href="{base_prefix}products/index.html" class="btn btn-outline-tech btn-sm">
            جستجو در کل ۵۰۰ کد فنی کاتالوگ ←
          </a>
        </div>
        <div class="products-grid">
{cards_html}
        </div>
      </div>
    </section>

    <section class="section" style="padding: 1rem 0 2.25rem;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.25rem, 3vw, 1.85rem);">
          <span class="section-eyebrow">راهنمای فنی و پرسش‌های متداول</span>
          <h2 style="font-size: 1.15rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 1rem;">
            نکات مهندسی در انتخاب {esc(cat_spec['h1Fa'].split('(')[0].strip())}
          </h2>
{faqs_html}
        </div>
      </div>
    </section>
"""

    return render_full_html_page(
        title=cat_spec["titleSeo"],
        meta_description=cat_spec["metaDesc"],
        canonical_url=canonical_url,
        base_prefix=base_prefix,
        active_section=cat_spec["uiCategory"],
        jsonld_str=jsonld_str,
        main_html=main_html,
        page_category_attr=cat_spec["uiCategory"],
    )


def render_brand_page(brand_meta: dict, all_products: list, families: list) -> str:
    """
    Generate `/brands/<brand-slug>/index.html` (`depth=2`, `base_prefix="../../"`).
    Explicitly states brand role & legal attribution (including historical Rexroth/AVENTICS legacy notice).
    """
    base_prefix = "../../"
    brand_id = brand_meta["id"]
    canonical_url = f"{SITE_DOMAIN}/brands/{brand_id}/"

    brand_products = [p for p in all_products if p["manufacturerId"] == brand_id]
    brand_published = [p for p in brand_products if p["publicationStatus"] == "published"]
    brand_families = [f for f in families if f["manufacturerId"] == brand_id]

    breadcrumbs = [
        ("صفحه اصلی", f"{SITE_DOMAIN}/"),
        ("محصولات", f"{SITE_DOMAIN}/products/"),
        (f"برند {brand_meta['nameFa']}", canonical_url),
    ]

    item_list_ld = {
        "@type": "ItemList",
        "@id": f"{canonical_url}#itemlist",
        "name": f"کاتالوگ تجهیزات پنوماتیک {brand_meta['nameFa']} در شرکت جلالی پنوماتیک",
        "numberOfItems": len(brand_published),
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": idx + 1,
                "url": f"{SITE_DOMAIN}/product/{get_product_slug(p)}/",
                "name": p["titleFa"],
            }
            for idx, p in enumerate(brand_published)
        ],
    }

    jsonld_str = build_base_jsonld_graph(
        canonical_url=canonical_url,
        breadcrumbs=breadcrumbs,
        extra_nodes=[item_list_ld],
    )

    role_badge_map = {
        "proprietary_brand": ("برند تجاری اختصاصی شرکت جلالی پنوماتیک", "#0D9488", "#CCFBF1"),
        "international_sourcing_and_cross_reference": ("تأمین بازرگانی و مرجع معادل‌یابی فنی (بدون ادعای نمایندگی انحصاری)", "#1D4ED8", "#DBEAFE"),
        "historical_legacy_sourcing_reference": ("نمایه کدهای تاریخی جهت شناسایی، تأمین یا جایگزینی مهندسی", "#B45309", "#FEF3C7"),
    }
    r_label, r_color, r_bg = role_badge_map.get(
        brand_meta["sourcingRole"], ("مرجع کاتالوگ فنی", "#475569", "#F1F5F9")
    )

    legacy_banner = ""
    if brand_meta.get("isLegacy"):
        legacy_banner = """
        <div style="margin-top: 1rem; padding: 1rem 1.2rem; background: #FFFBEB; border-right: 4px solid #F28C28; border-radius: 8px; font-size: 0.86rem; color: #92400E; line-height: 1.85;">
          <strong>شفاف‌سازی حقوقی و فنی برند تاریخی (Bosch Rexroth / AVENTICS Legacy Index):</strong>
          بخش پنوماتیک صنعتی Bosch Rexroth در سال‌های گذشته تحت عنوان <strong>Rexroth Pneumatics</strong> و سپس <strong>AVENTICS</strong> فعالیت داشته است. ۳۵ کد فنی درج‌شده در این بخش (از خانواده جزیره شیر <span dir="ltr" class="mono">HF03-LG</span> با پیش‌شماره‌های <span dir="ltr" class="mono">0820...</span> و <span dir="ltr" class="mono">R412...</span>) از کاتالوگ‌های تاریخی استخراج شده‌اند تا مهندسان تعمیر و نگهداری بتوانند قطعات قدیمی خطوط تولید را شناسایی و استعلام نمایند. شرکت جلالی پنوماتیک هیچ‌گونه ادعای نمایندگی رسمی از Bosch Rexroth یا AVENTICS ندارد.
        </div>"""

    families_html = "\n".join(
        f"""        <a href="{base_prefix}series/{esc(f['id'])}/index.html" style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem; text-decoration: none; color: #10243A; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <strong style="font-size: 0.95rem; color: #10243A;">سری <span dir="ltr" class="mono" style="color: #087F8C;">{esc(f['code'])}</span></strong>
            <div style="font-size: 0.78rem; color: #64748B; margin-top: 0.2rem;">{esc(f['titleFa'])}</div>
          </div>
          <span class="mono" dir="ltr" style="font-size: 0.76rem; font-weight: 800; color: #087F8C; background: #E6F4F6; padding: 0.22rem 0.6rem; border-radius: 999px;">
            {f['skuCount']} کد فنی ←
          </span>
        </a>"""
        for f in brand_families
    )

    cards_html = "\n".join(render_product_summary_card(p, base_prefix) for p in brand_published)

    main_html = f"""
    <nav aria-label="مسیر راهنما (Breadcrumb)" style="background: #F1F5F9; border-bottom: 1px solid #E1E7EE; padding: 0.75rem 0; font-size: 0.82rem;">
      <div class="container" style="display: flex; flex-wrap: wrap; align-items: center; gap: 0.45rem; color: #475569;">
        <a href="{base_prefix}index.html" style="color: #087F8C; font-weight: 700;">صفحه اصلی</a>
        <span aria-hidden="true">←</span>
        <a href="{base_prefix}products/index.html" style="color: #087F8C; font-weight: 700;">محصولات</a>
        <span aria-hidden="true">←</span>
        <strong style="color: #10243A;">برند {esc(brand_meta['nameFa'])}</strong>
      </div>
    </nav>

    <section class="section" style="background: #FFFFFF; border-bottom: 1px solid #E1E7EE; padding: 2.25rem 0;">
      <div class="container">
        <div style="display: flex; flex-wrap: wrap; gap: 0.6rem; align-items: center; margin-bottom: 0.65rem;">
          <span style="font-size: 0.76rem; font-weight: 800; color: {r_color}; background: {r_bg}; padding: 0.25rem 0.7rem; border-radius: 999px;">
            {esc(r_label)}
          </span>
          <span class="mono" dir="ltr" style="font-size: 0.78rem; color: #64748B;">
            انتساب سازنده: {esc(brand_meta['legalAttribution'])}
          </span>
        </div>

        <h1 style="font-size: clamp(1.35rem, 3.2vw, 1.95rem); font-weight: 900; color: #10243A; margin-bottom: 0.65rem;">
          کاتالوگ تجهیزات پنوماتیک {esc(brand_meta['nameFa'])} — مشخصات فنی، استعلام و معادل‌یابی
        </h1>
        <p style="font-size: 0.92rem; color: #334155; line-height: 1.9; max-width: 900px;">
          {esc(brand_meta['disclaimerFa'])} در بانک اطلاعات فنی شرکت جلالی پنوماتیک، مجموعاً <strong>{len(brand_products)} کد فنی</strong> در <strong>{len(brand_families)} خانواده محصول</strong> برای برند {esc(brand_meta['name'])} ثبت و ساختاردهی شده است.
        </p>
        {legacy_banner}
      </div>
    </section>

    <section class="section" style="padding: 1.75rem 0 0.75rem;">
      <div class="container">
        <h2 style="font-size: 1.15rem; font-weight: 800; color: #10243A; margin-bottom: 0.9rem;">
          خانواده‌ها و سری‌های فنی {esc(brand_meta['name'])} ({len(brand_families)} سری)
        </h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 0.85rem;">
{families_html}
        </div>
      </div>
    </section>

    <section class="section" style="padding: 1.75rem 0 2.5rem;">
      <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.1rem;">
          <div>
            <span class="section-eyebrow">صفحات محصول منتشرشده در فاز پایلوت</span>
            <h2 style="font-size: 1.2rem; font-weight: 800; color: #10243A; margin-top: 0.2rem;">
              مدل‌های شاخص {esc(brand_meta['nameFa'])} ({len(brand_published)} مدل منتخب از {len(brand_products)} کد)
            </h2>
          </div>
          <a href="{base_prefix}products/index.html" class="btn btn-outline-tech btn-sm">
            جستجوی تمام {len(brand_products)} کد {esc(brand_meta['code'])} در کاتالوگ ←
          </a>
        </div>
        <div class="products-grid">
{cards_html}
        </div>
      </div>
    </section>
"""

    return render_full_html_page(
        title=f"کاتالوگ پنوماتیک {brand_meta['nameFa']} ({len(brand_products)} کد فنی) | استعلام و معادل‌یابی JPC",
        meta_description=f"مشخصات فنی، سری‌های کاتالوگ و استعلام قیمت تجهیزات پنوماتیک {brand_meta['nameFa']} ({brand_meta['legalAttribution']}) در شرکت جلالی پنوماتیک لاله‌زار تهران.",
        canonical_url=canonical_url,
        base_prefix=base_prefix,
        active_section="brands",
        jsonld_str=jsonld_str,
        main_html=main_html,
        page_category_attr="all",
    )


def render_series_page(family: dict, all_products: list) -> str:
    """
    Generate `/series/<family-id>/index.html` (`depth=2`, `base_prefix="../../"`).
    Explains the series architecture, supported configurations, selection parameters,
    and lists all variants in that series (linking published variants to `/product/<slug>/`).
    """
    base_prefix = "../../"
    fam_id = family["id"]
    canonical_url = f"{SITE_DOMAIN}/series/{fam_id}/"

    fam_products = [p for p in all_products if p["familyId"] == fam_id]
    fam_published = [p for p in fam_products if p["publicationStatus"] == "published"]

    breadcrumbs = [
        ("صفحه اصلی", f"{SITE_DOMAIN}/"),
        ("محصولات", f"{SITE_DOMAIN}/products/"),
        (f"برند {family['brand']}", f"{SITE_DOMAIN}/brands/{family['manufacturerId']}/"),
        (f"سری {family['code']}", canonical_url),
    ]

    item_list_ld = {
        "@type": "ItemList",
        "@id": f"{canonical_url}#series-list",
        "name": family["titleFa"],
        "numberOfItems": len(fam_published) if fam_published else len(fam_products),
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": idx + 1,
                "url": (
                    f"{SITE_DOMAIN}/product/{get_product_slug(p)}/"
                    if p["publicationStatus"] == "published"
                    else canonical_url
                ),
                "name": p["titleFa"],
            }
            for idx, p in enumerate(fam_published if fam_published else fam_products[:25])
        ],
    }

    jsonld_str = build_base_jsonld_graph(
        canonical_url=canonical_url,
        breadcrumbs=breadcrumbs,
        extra_nodes=[item_list_ld],
    )

    # Summarize variant ranges in this series
    bores = sorted({p["technicalAttributes"]["boreMm"] for p in fam_products if p["technicalAttributes"]["boreMm"] is not None})
    strokes = sorted({p["technicalAttributes"]["strokeMm"] for p in fam_products if p["technicalAttributes"]["strokeMm"] is not None})
    ports = sorted({p["technicalAttributes"]["portSize"] for p in fam_products if p["technicalAttributes"]["portSize"]})
    tubes = sorted({str(p["technicalAttributes"]["tubeOdMm"]) for p in fam_products if p["technicalAttributes"]["tubeOdMm"]})
    funcs = sorted({p["technicalAttributes"]["valveFunction"] for p in fam_products if p["technicalAttributes"]["valveFunction"]})

    config_bullets = []
    if bores:
        config_bullets.append(("قطرهای پیستون در این سری (Bore Ø)", " · ".join(f"{b}mm" for b in bores)))
    if strokes:
        config_bullets.append(("کورس‌های استاندارد (Stroke)", " · ".join(f"{s}mm" for s in strokes)))
    if ports:
        config_bullets.append(("سایز پورت و رزوه‌ها", " · ".join(ports[:8])))
    if tubes:
        config_bullets.append(("سایز شیلنگ‌های سازگار (Tube OD)", " · ".join(f"{t}mm" for t in tubes)))
    if funcs:
        config_bullets.append(("آرایش‌ها و توابع شیر", " · ".join(funcs)))
    config_bullets.append(("استاندارد مرجع", " / ".join(family.get("standards") or ["ISO"])))

    config_grid_html = "\n".join(
        f"""        <div style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 0.85rem 1rem;">
          <div style="font-size: 0.75rem; color: #64748B; margin-bottom: 0.25rem;">{esc(k)}</div>
          <div class="mono" dir="ltr" style="font-size: 0.88rem; font-weight: 800; color: #10243A;">{esc(v)}</div>
        </div>"""
        for k, v in config_bullets
    )

    # Complete HTML table of all variants in this series
    variant_rows_html = []
    for p in fam_products:
        is_pub = p["publicationStatus"] == "published"
        p_slug = get_product_slug(p)
        ta = p["technicalAttributes"]
        key_spec = (
            f"Ø{ta['boreMm']} × {ta['strokeMm']} mm ({ta.get('cushioning') or 'ISO'})"
            if (ta.get("boreMm") and ta.get("strokeMm"))
            else (ta.get("valveFunction") or (f"Tube {ta.get('tubeOdMm')} mm" if ta.get("tubeOdMm") else p["subCategory"]))
        )
        model_cell = (
            f'<a href="{base_prefix}product/{esc(p_slug)}/index.html" class="mono" dir="ltr" style="font-weight: 800; color: #087F8C;">{esc(p["modelCode"])}</a>'
            if is_pub
            else f'<span class="mono" dir="ltr" style="font-weight: 700; color: #10243A;">{esc(p["modelCode"])}</span>'
        )
        action_cell = (
            f'<div style="display:flex; gap:0.4rem; flex-wrap:wrap;">'
            f'<a href="{base_prefix}product/{esc(p_slug)}/index.html" class="btn btn-outline-tech btn-xs">صفحه محصول</a>'
            f'<button type="button" class="btn btn-rfq-add btn-xs js-add-rfq-btn" data-id="{esc(p["id"])}">+ استعلام</button>'
            f'</div>'
            if is_pub
            else f'<div style="display:flex; gap:0.4rem; flex-wrap:wrap;">'
                 f'<button type="button" class="btn btn-outline-tech btn-xs js-spec-trigger" data-id="{esc(p["id"])}">مشخصات</button>'
                 f'<button type="button" class="btn btn-rfq-add btn-xs js-add-rfq-btn" data-id="{esc(p["id"])}">+ استعلام</button>'
                 f'</div>'
        )
        variant_rows_html.append(f"""              <tr>
                <td>{model_cell}</td>
                <td class="mono" dir="ltr">{esc(p['articleNumber'] or '—')}</td>
                <td>{esc(p['titleFa'])}</td>
                <td class="mono" dir="ltr">{esc(key_spec)}</td>
                <td class="mono" dir="ltr">{esc(p['portSize'])}</td>
                <td>{action_cell}</td>
              </tr>""")

    variants_table_body = "\n".join(variant_rows_html)

    main_html = f"""
    <nav aria-label="مسیر راهنما (Breadcrumb)" style="background: #F1F5F9; border-bottom: 1px solid #E1E7EE; padding: 0.75rem 0; font-size: 0.82rem;">
      <div class="container" style="display: flex; flex-wrap: wrap; align-items: center; gap: 0.45rem; color: #475569;">
        <a href="{base_prefix}index.html" style="color: #087F8C; font-weight: 700;">صفحه اصلی</a>
        <span aria-hidden="true">←</span>
        <a href="{base_prefix}products/index.html" style="color: #087F8C; font-weight: 700;">محصولات</a>
        <span aria-hidden="true">←</span>
        <a href="{base_prefix}brands/{esc(family['manufacturerId'])}/index.html" style="color: #087F8C; font-weight: 700;">برند {esc(family['brand'])}</a>
        <span aria-hidden="true">←</span>
        <strong style="color: #10243A;">سری <span dir="ltr" class="mono">{esc(family['code'])}</span></strong>
      </div>
    </nav>

    <section class="section" style="background: #FFFFFF; border-bottom: 1px solid #E1E7EE; padding: 2.25rem 0;">
      <div class="container">
        <span class="section-eyebrow">مرجع مهندسی خانواده محصول · {esc(family['brand'])}</span>
        <h1 style="font-size: clamp(1.35rem, 3.2vw, 1.9rem); font-weight: 900; color: #10243A; margin: 0.35rem 0 0.65rem;">
          {esc(family['titleFa'])} — مشخصات، پیکربندی و جدول {family['skuCount']} کد فنی
        </h1>
        <p style="font-size: 0.92rem; color: #334155; line-height: 1.9; max-width: 900px; margin-bottom: 1.25rem;">
          خانواده <strong class="mono" dir="ltr">{esc(family['code'])}</strong> از برند <strong>{esc(family['brand'])}</strong> شامل <strong>{family['skuCount']} واریانت و کد فنی</strong> در کاتالوگ شرکت جلالی پنوماتیک (JPC) است. در جدول زیر می‌توانید تمامی کدهای مدل، شماره سفارش سازنده (Article No.)، ابعاد، سایز پورت و وضعیت استعلام هر واریانت را بررسی و به سبد استعلام (RFQ) اضافه نمایید.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem;">
{config_grid_html}
        </div>

        <div style="margin-top: 1rem; display: flex; flex-wrap: wrap; gap: 0.65rem; align-items: center;">
          <a href="{esc(family['sourceUrl'])}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-tech btn-sm">
            📄 مشاهده مستند مرجع سازنده برای سری {esc(family['code'])} ↗
          </a>
          <a href="{base_prefix}festo-cross-reference.html" class="btn btn-outline-tech btn-sm">
            🔄 تطبیق و معادل‌یابی با برند JPC
          </a>
        </div>
      </div>
    </section>

    <section class="section" style="padding: 2rem 0;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.15rem, 3vw, 1.75rem);">
          <h2 style="font-size: 1.15rem; font-weight: 800; color: #10243A; margin-bottom: 1rem;">
            جدول کامل کدهای فنی و واریانت‌های سری <span dir="ltr" class="mono">{esc(family['code'])}</span> ({len(fam_products)} مدل)
          </h2>
          <div class="table-responsive">
            <table class="tech-comparison-table" aria-label="جدول کدهای فنی سری {esc(family['code'])}">
              <thead>
                <tr>
                  <th scope="col">کد مدل سازنده</th>
                  <th scope="col">شماره سفارش (Article No.)</th>
                  <th scope="col">عنوان و شرح فارسی</th>
                  <th scope="col">مشخصه فنی / سایز</th>
                  <th scope="col">پورت / اتصال</th>
                  <th scope="col">عملیات و استعلام</th>
                </tr>
              </thead>
              <tbody>
{variants_table_body}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
"""

    return render_full_html_page(
        title=f"{family['titleFa']} | جدول {family['skuCount']} کد فنی و استعلام قیمت | JPC Iran",
        meta_description=f"راهنمای انتخاب، جدول مشخصات فنی و استعلام قیمت {family['skuCount']} مدل از {family['titleFa']} در شرکت جلالی پنوماتیک لاله‌زار تهران.",
        canonical_url=canonical_url,
        base_prefix=base_prefix,
        active_section=family["uiCategory"],
        jsonld_str=jsonld_str,
        main_html=main_html,
        page_category_attr=family["uiCategory"],
    )
