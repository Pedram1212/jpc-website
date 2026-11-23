"""
Phase 2 Technical Cross-Reference & Brand Comparison Templates (`/compare/`)
===========================================================================
Generates:
- `/compare/index.html` (`depth=1`, `base_prefix="../"`): مرکز معادل‌یابی و مقایسه فنی تجهیزات پنوماتیک
- 5 High-Intent Engineering Comparison Pages (`depth=2`, `base_prefix="../../"`):
  1. `/compare/festo-dsbc-vs-iso-15552-cylinders/index.html`
  2. `/compare/festo-mfh-vs-jpc-4v-solenoid-valves/index.html`
  3. `/compare/festo-vuvg-vs-compact-manifold-valves/index.html`
  4. `/compare/festo-ms-vs-jpc-frl-air-preparation/index.html`
  5. `/compare/rexroth-aventics-hf03-lg-0820055051-replacement/index.html`
"""

import urllib.parse
from .common import (
    SITE_DOMAIN,
    build_base_jsonld_graph,
    esc,
    render_full_html_page,
)

COMPARE_PAGES_SPEC = [
    {
        "slug": "festo-dsbc-vs-iso-15552-cylinders",
        "activeSection": "cylinders",
        "titleSeo": "مقایسه فنی جک پنوماتیک Festo DSBC با جک‌های استاندارد ISO 15552 (سری DNC) | JPC",
        "metaDesc": "مقایسه مهندسی جک پنوماتیک فستو سری DSBC با سیلندرهای استاندارد ISO 15552 برند JPC سری DNC؛ بررسی ابعاد نصب، شیار سنسور T-Slot، ضربه‌گیر PPV/PPS و چک‌لیست جایگزینی.",
        "h1Fa": "مقایسه فنی جک پنوماتیک Festo DSBC با جک‌های استاندارد ISO 15552 (سری JPC DNC)",
        "eyebrowFa": "راهنمای تطبیق مهندسی سیلندرهای استاندارد ISO 15552 / VDMA 24562",
        "oemLabel": "Festo DSBC / DSBC-D3 (ISO 15552)",
        "jpcLabel": "JPC DNC Series (ISO 15552 / 6431)",
        "tldrViableFa": "جایگزینی مستقیم (Drop-in) زمانی امکان‌پذیر است که هر دو سیلندر دارای قطر پیستون (Bore) و کورس (Stroke) یکسان بوده و از پایه‌های نصب استاندارد ISO 15552 (مانند فلنج FNC، پایه رادیال LBG یا مفصل SNC) استفاده کنند؛ زیرا فاصله مرکز تا مرکز پیچ‌های سر و ته، قطر گژن‌پین و گام رزوه سرشفت (مثلاً M16x1.5 در قطر ۶۳ میلی‌متر) در استاندارد ISO 15552 کاملاً یکسان است.",
        "tldrMandatoryOemFa": "استفاده از کد اصلی Festo DSBC زمانی الزامی است که ماشین دارای ضربه‌گیر خودتنظیم دینامیکی PPS در سرعت‌های بسیار بالا، سنسورهای مگنتی T-Slot فابریک سری SMT-8M بدون براکت تبدیل، یا گواهینامه محیط‌های خاص (ATEX / صنایع غذایی با گریس NSF-H1) باشد.",
        "comparisonRows": [
            ("استاندارد ابعادی و نصب (Mounting Standard)", "ISO 15552 (جایگزین ISO 6431 / VDMA 24562)", "ISO 15552 / ISO 6431 / VDMA 24562", "تطابق کامل فاصله پیچ‌های کله‌گی و رزوه سرشفت"),
            ("قطرهای پیستون استاندارد (Bore Ø)", "32, 40, 50, 63, 80, 100, 125 mm", "32, 40, 50, 63, 80, 100, 125 mm", "هم‌اندازه در تمام قطرهای استاندارد ایزو"),
            ("سایز و نوع رزوه پورت (Port Thread)", "G1/8 (Ø32)، G1/4 (Ø40-50)، G3/8 (Ø63-80)، G1/2 (Ø100-125) — BSPP", "G1/8 (Ø32)، G1/4 (Ø40-50)، G3/8 (Ø63-80)، G1/2 (Ø100-125) — BSPP", "رزوه موازی استاندارد ISO 228-1 (G) در هر دو سری"),
            ("محدوده فشار کاری (Operating Pressure)", "0.6 – 12 bar", "1.0 – 10 bar", "در فشار استاندارد کارگاهی (۶ بار) کاملاً هم‌پوشان هستند"),
            ("سیستم ضربه‌گیر انتهایی (Cushioning)", "PPVA (پنوماتیک قابل تنظیم) یا PPSA (پنوماتیک خودتنظیم)", "PPV (پنوماتیک قابل تنظیم دوطرفه با پیچ سوزنی)", "در مدل‌های PPSA هنگام جایگزینی با PPV باید پیچ ضربه‌گیر دستی تنظیم شود"),
            ("شیار نصب سنسور مگنتی (Sensor Groove)", "شیار T-Slot یک‌طرفه (DSBC) یا سه‌طرفه (DSBC-D3) ویژه سنسور SMT-8M", "شیار پروفیل استاندارد DNC (نصب سنسور CS1-U /CS1-F یا رید سوییچ با بست)", "هشدار: تیپ سنسور مگنتی روی پروفیل باید پیش از تعویض بررسی شود"),
            ("قطر شفت و گام رزوه سرشفت (Piston Rod)", "Ø12 (M10x1.25) تا Ø32 (M27x2)", "Ø12 (M10x1.25) تا Ø32 (M27x2) استیل کروم سخت CK45", "چنگالی (SG) و سرشفت کروی (SGS) بین دو برند قابل جابه‌جایی است"),
        ],
        "checklistItems": [
            ("کنترل فاصله پیچ‌های کله‌گی و نوع پایه نصب (TG & Mounting):", "اطمینان حاصل کنید سیلندر فعلی شما سری ISO 15552 (DSBC یا DNC) است و با سیلندرهای چهارمیل آسیایی سری SC (که فاصله پیچ متفاوتی دارند) اشتباه گرفته نشده باشد."),
            ("بررسی شیار سنسور مگنتی (T-Slot vs Profile Groove):", "اگر روی جک فعلی سنسورهای فستو SMT-8M داخل شیار T-Slot نصب شده‌اند، هنگام جایگزینی با پروفیل DNC ممکن است به سنسور سازگار با شیار DNC نیاز داشته باشید."),
            ("تطبیق ضربه‌گیر انتهایی (PPS در برابر PPV):", "اگر کد فستو دارای پسوند PPSA (ضربه‌گیر خودتنظیم) است، در جک جایگزین PPV باید پیچ تنظیم ضربه‌گیر در دو انتهای کورس متناسب با سرعت بار تنظیم گردد."),
            ("بررسی فشار استارت و دمای محیط:", "فشار شروع حرکت در DSBC از 0.6 بار و در DNC از 1.0 بار است؛ در مدارهای فشار بسیار پایین (< 1 bar) یا دمای بالای ۸۰ درجه سانتی‌گراد (پکینگ وایتون پسوند A3)، کد اصلی اولویت دارد."),
        ],
        "relatedLinks": [
            ("صفحه محصول JPC-DNC-63-200-PPV-A", "product/jpc-dnc-63-200-ppv-a/index.html"),
            ("صفحه محصول Festo DSBC-63-200-PPVA-N3", "product/festo-dsbc-63-200-ppva-n3/index.html"),
            ("صفحه محصول Festo DSBC-32-100-PPVA-N3 (1376426)", "product/festo-dsbc-32-100-ppva-n3/index.html"),
            ("ماتریس ۲۲۸ کد فنی سری Festo DSBC", "series/festo-dsbc/index.html"),
            ("ماتریس ۷۲ کد فنی سری Festo DSBC-D3", "series/festo-dsbc-d3/index.html"),
            ("خانواده جک استاندارد JPC DNC", "series/jpc-dnc/index.html"),
            ("کاتالوگ جک و سیلندر پنوماتیک", "products/pneumatic-cylinders/index.html"),
            ("صفحه برند فستو (Festo)", "brands/festo/index.html"),
        ],
        "oemWaQuery": "سلام، درخواست استعلام قیمت و موجودی جک اصلی فستو سری Festo DSBC (ISO 15552) را دارم.",
        "jpcWaQuery": "سلام، درخواست استعلام قیمت جک جایگزین هم‌ابعاد ISO 15552 برند JPC سری DNC به جای Festo DSBC را دارم.",
        "modalProductId": "jpc-dnc-63-200",
        "faqs": [
            (
                "آیا پایه‌ها و اتصالات سرشفت جک Festo DSBC مستقیماً روی جک JPC DNC بسته می‌شوند؟",
                "بله؛ از آنجا که هر دو سری دقیقاً بر اساس جدول ابعادی استاندارد ISO 15552 ساخته می‌شوند، فاصله سوراخ‌های رزوه‌دار کله‌گی جلو و عقب و همچنین قطر و گام رزوه سرشفت (مثلاً M12x1.25 در قطر ۴۰ و M16x1.5 در قطر ۶۳) کاملاً یکسان بوده و پایه‌های فلنج، لولا و چنگالی بدون تغییر شاسی قابل استفاده هستند."
            ),
            (
                "تفاوت نیروی خروجی جک Festo DSBC و JPC DNC در فشار ۶ بار چقدر است؟",
                "نیروی خروجی سیلندر تنها به قطر پیستون، قطر شفت و فشار هوا وابسته است (F = P × A). بنابراین در قطر ۶۳ میلی‌متر و شفت ۲۰ میلی‌متر در فشار ۶ بار، هر دو سیلندر نیروی تئوری رفت ۱۸۷۰ نیوتن و نیروی عملیاتی مؤثر (با راندمان ۸۰٪) حدود ۱۴۹۶ نیوتن (۱۵۲.۵ کیلوگرم‌نیرو) تولید می‌کنند."
            ),
            (
                "در چه شرایطی نباید جک Festo DSBC را با برندهای جایگزین تعویض کرد؟",
                "در کاربردهای دارای دمای کاری خارج از محدوده استاندارد (-20 تا +80 درجه سانتی‌گراد)، محیط‌های اسیدی یا شست‌وشوی صنایع غذایی، یا جایی که در دفترچه نگهداری خط تولید استفاده از قطعه OEM با پارت‌نامبر فستو الزام قانونی دارد، باید کد اصلی فستو تأمین شود."
            ),
        ],
    },
    {
        "slug": "festo-mfh-vs-jpc-4v-solenoid-valves",
        "activeSection": "valves",
        "titleSeo": "مقایسه شیر برقی Festo سری MFH / JMFH با شیرهای سری 4V صنعتی JPC | راهنمای جایگزینی",
        "metaDesc": "بررسی فنی و مقایسه شیر برقی پنوماتیک فستو سری MFH / JMFH با شیرهای ۵/۲ و ۵/۳ سری 4V210، 4V220 و 4V330 برند JPC؛ مقایسه سایز پورت 1/8 تا 1/2، دبی Qn، فشار پایلوت و بوبین.",
        "h1Fa": "مقایسه و بررسی جایگزین شیر برقی Festo سری MFH با شیرهای سری 4V صنعتی JPC",
        "eyebrowFa": "تحلیل مهندسی شیرهای کنترل جهت ۵/۲ و ۳/۲ خطی (In-line Directional Control Valves)",
        "oemLabel": "Festo MFH / JMFH Tiger Classic (مثلاً MFH-5-1/4-B)",
        "jpcLabel": "JPC 4V / 3V Series (مثلاً JPC-4V210-08-24DC)",
        "tldrViableFa": "جایگزینی عملکردی در نصب‌های خطی و تکی (In-line / Stand-alone) زمانی کاملاً عملی است که سایز رزوه پورت‌های کاری (مثلاً G1/4 در MFH-5-1/4 و 4V210-08)، آرایش شیر (۵/۲ تک‌بوبین برگشت فنری یا ۵/۲ دوبوبین حافظه‌دار) و ولتاژ بوبین (24V DC یا 220V AC) یکسان باشند و شیر از طریق شیلنگ و فیتینگ به جک متصل شود.",
        "tldrMandatoryOemFa": "تأمین کد اصلی Festo MFH زمانی الزامی است که شیر فعلی روی منیفولد ریل‌پایه فابریک فستو (سری‌های PRS یا بلوک‌های PAL) بسته شده باشد (زیرا فاصله سوراخ‌های منیفولد MFH با منیفولد سری 4V متفاوت است) یا مدار نیاز به دبی لحظه‌ای بالاتر از ۱۰۰۰ لیتر بر دقیقه در سایز ۱/۴ اینچ داشته باشد.",
        "comparisonRows": [
            ("ساختار و مکانیزم داخلی (Valve Design)", "اسپول پیستونی با تحریک پایلوت داخلی (Poppet / Piston Spool)", "اسپول کشویی آلومینیوم آنودایز با پایلوت داخلی (Sliding Spool)", "هر دو نیازمند حداقل فشار پایلوت برای تغییر وضعیت هستند"),
            ("سایز پورت‌های کاری (P, A, B)", "G1/8 (MFH-5-1/8)، G1/4 (MFH-5-1/4)، G1/2 (MFH-5-1/2) — BSPP", "G1/8 (4V110-06)، G1/4 (4V210-08)، G3/8 (4V310-10)، G1/2 (4V410-15) — BSPP", "در سایز G1/4 پورت‌های تخلیه (R, S) در فستو G1/4 و در 4V210 سایز G1/8 است"),
            ("دبی اسمی عبوری (Nominal Flow Qn / Cv)", "حدود 1000 – 1600 L/min (در سایز G1/4 مدل MFH-5-1/4)", "حدود 890 L/min (Cv = 0.89 در مدل 4V210-08) تا 1680 L/min (در 4V310-10)", "برای سیلندرهای قطر بالای ۸۰ میلی‌متر با سرعت بالا، سایز 4V310-10 (G3/8) پیشنهاد می‌شود"),
            ("محدوده فشار کاری و حداقل فشار پایلوت", "1.5 – 8 bar (مدل استاندارد) / تا 10 bar", "1.5 – 8 bar (حداکثر فشار تست 12 bar)", "حداقل فشار ۱.۵ بار جهت فرمان‌پذیری پایلوت داخلی در هر دو الزامی است"),
            ("ولتاژ بوبین و نوع سوکت (Coil & Connector)", "بوبین سری F یا MSFG (24V DC, 220V AC — سفارش جداگانه بوبین)", "همراه با بوبین و سوکت چراغ‌دار استاندارد DIN 43650B (24V DC / 220V AC) با حفاظت IP65", "پین‌بندی سوکت ۳ پین باید هنگام تعویض بوبین کنترل شود"),
            ("نصب روی منیفولد (Manifold Mounting)", "سازگار با منیفولد اختصاصی فستو سری PAL / PRS", "سازگار با منیفولد اختصاصی سری 4V200 (از ۲ تا ۱۲ خانه)", "هشدار: شیر JPC 4V210 مستقیماً روی بلوک منیفولد فستو بسته نمی‌شود"),
        ],
        "checklistItems": [
            ("نصب خطی (تکی) در برابر نصب منیفولدی:", "اگر شیر فعلی به صورت تکی روی شاسی بسته شده و ورودی/خروجی آن شیلنگ خورده است، جایگزینی با JPC-4V210-08 به راحتی انجام می‌شود؛ اما اگر روی بلوک منیفولد چندتایی فستو بسته شده، یا باید کل بلوک منیفولد با منیفولد 4V جایگزین شود یا کد اصلی MFH تهیه گردد."),
            ("کنترل سایز سایلنسرهای تخلیه (پورت R و S):", "در شیر JPC-4V210-08 پورت‌های کار (P, A, B) سایز G1/4 و دو پورت اگزوز (R, S) سایز G1/8 هستند؛ هنگام جایگزینی دو عدد سایلنسر برنزی G1/8 نیز همراه شیر سفارش دهید."),
            ("تطبیق دبی عبوری (Qn) برای جک‌های قطور:", "اگر شیر فستو MFH-5-1/4 یک جک قطر ۱۰۰ یا ۱۲۵ میلی‌متر را با سرعت بالا تغذیه می‌کند، به جای 4V210-08 می‌توانید از سری بزرگ‌تر JPC-4V310-10 (پورت G3/8 با دبی 1680 L/min) با تبدیل رزوه استفاده کنید."),
            ("تأیید ولتاژ بوبین (24V DC در برابر 220V AC):", "پیش از ثبت سفارش، ولتاژ حک‌شده روی بوبین فعلی (24V DC یا 220V AC) را به واحد فروش اعلام فرمایید."),
        ],
        "relatedLinks": [
            ("صفحه محصول شیر ۵/۲ تک‌بوبین JPC-4V210-08-24DC", "product/jpc-4v210-08-24dc/index.html"),
            ("صفحه محصول شیر ۵/۲ دوبوبین JPC-4V220-08-220AC", "product/jpc-4v220-08-220ac/index.html"),
            ("صفحه محصول شیر ۵/۳ مرکز بسته JPC-4V330C-10-24DC", "product/jpc-4v330c-10-24dc/index.html"),
            ("صفحه محصول شیر ۳/۲ JPC-3V210-06-24DC", "product/jpc-3v210-06-24dc/index.html"),
            ("صفحه سری JPC 4V210", "series/jpc-4v210/index.html"),
            ("صفحه سری Norgren V61 (G1/4)", "series/norgren-v61/index.html"),
            ("کاتالوگ شیرهای برقی و کنترل جهت", "products/solenoid-valves/index.html"),
            ("راهنمای انتخاب شیر برقی ۵/۲ و ۵/۳", "solenoid-valve-guide.html"),
        ],
        "oemWaQuery": "سلام، درخواست استعلام قیمت و موجودی شیر برقی اصلی فستو مدل Festo MFH-5-1/4-B را دارم.",
        "jpcWaQuery": "سلام، درخواست استعلام قیمت شیر برقی جایگزین JPC-4V210-08-24DC (پورت G1/4) به جای Festo MFH را دارم.",
        "modalProductId": "jpc-4v210-08",
        "faqs": [
            (
                "تفاوت شیر فستو MFH-5-1/4 با JMFH-5-1/4 و معادل هر کدام در برند JPC چیست؟",
                "در کدگذاری فستو، MFH-5-1/4 شیر ۵/۲ تک‌بوبین (برگشت فنری) است که معادل عملکردی آن در برند JPC مدل JPC-4V210-08 می‌باشد؛ در حالی که JMFH-5-1/4 شیر ۵/۲ دوبوبین (حافظه‌دار Bistable) است که معادل عملکردی آن مدل JPC-4V220-08 است."
            ),
            (
                "آیا بوبین فستو MSFG-24 ولت روی شفت بوبین شیر JPC 4V210 نصب می‌شود؟",
                "خیر؛ قطر هسته آرمیچر و ابعاد مکانیکی بوبین‌های فستو با سری 4V متفاوت است. شیرهای سری JPC 4V به صورت کامل همراه با بوبین و سوکت چراغ‌دار فابریک خود در ولتاژ 24V DC یا 220V AC عرضه می‌شوند."
            ),
            (
                "چرا شیر برقی ۵/۲ پایلوت‌دار در فشار زیر ۱.۵ بار عمل نمی‌کند؟",
                "هم در شیرهای Festo MFH و هم در JPC 4V210، بوبین برقی تنها یک مجرای پایلوت کوچک را باز می‌کند و نیروی اصلی حرکت اسپول توسط فشار خود هوای ورودی پورت P تأمین می‌شود؛ بنابراین وجود حداقل ۱.۵ بار فشار در خط ورودی الزامی است."
            ),
        ],
    },
    {
        "slug": "festo-vuvg-vs-compact-manifold-valves",
        "activeSection": "valves",
        "titleSeo": "مقایسه شیرهای کامپکت Festo VUVG با شیرهای منیفولدی صنعتی (4V و Norgren V60/V61) | JPC",
        "metaDesc": "تحلیل فنی شیرهای برقی کامپکت فستو سری VUVG در مقایسه با شیرهای منیفولدی و خطی Norgren سری V60/V61 و JPC سری 4V؛ بررسی عرض بدنه، زیرشیری Sub-base، توان بوبین 24V DC و دبی.",
        "h1Fa": "مقایسه شیرهای کامپکت Festo VUVG با شیرهای منیفولدی صنعتی (Norgren V60/V61 و JPC 4V)",
        "eyebrowFa": "راهنمای مهندسی تابلوهای پنوماتیک، جزیره شیر و منیفولدهای چندخانه",
        "oemLabel": "Festo VUVG Compact Series (VUVG-L10 / L14 / L18)",
        "jpcLabel": "Norgren V60 / V61 Series & JPC 4V Manifold Series",
        "tldrViableFa": "جایگزینی در سطح مدار زمانی امکان‌پذیر است که فضای داخل تابلو پنوماتیک اجازه نصب شیرهای خطی یا منیفولدی استاندارد با عرض بدنه ۱۸ تا ۲۲ میلی‌متر (مانند Norgren V60 با پورت G1/8 یا JPC 4V210 با پورت G1/4) را بدهد و اتصال الکتریکی هر شیر به صورت مجزا (Individual Wiring) باشد.",
        "tldrMandatoryOemFa": "استفاده از کد اصلی Festo VUVG زمانی الزامی است که شیر به‌صورت نسخه زیرشیری (Sub-base مدل VUVG-B...) روی منیفولد فابریک VTUG با رابط شبکه صنعتی (Fieldbus / IO-Link / Multipin) نصب شده باشد یا محدودیت شدید عرض تابلو (۱۰ و ۱۴ میلی‌متر) وجود داشته باشد.",
        "comparisonRows": [
            ("نوع نصب و پیکربندی (Mounting Type)", "نسخه خطی (VUVG-L) یا نسخه زیرشیری منیفولدی (VUVG-B روی ریل VTUG)", "نصب خطی یا روی منیفولدهای ردیفی استاندارد (Norgren V60/V61 و JPC 4V)", "نسخه VUVG-B فاقد رزوه پورت روی بدنه شیر است و فقط روی منیفولد VTUG بسته می‌شود"),
            ("عرض بدنه و سایز پورت (Body Width & Port)", "10mm (M5/M7)، 14mm (G1/8)، 18mm (G1/4)", "Norgren V60 (G1/8)، Norgren V61 (G1/4)، JPC 4V110 (G1/8)، JPC 4V210 (G1/4)", "در سایز G1/8 و G1/4 امکان تطبیق پورت با سری‌های V60/V61 و 4V وجود دارد"),
            ("دبی عبوری (Flow Rate Qn)", "از 130 L/min (سایز M5) تا 1380 L/min (سایز G1/4 مدل VUVG-L18)", "Norgren V60: ~750 L/min | Norgren V61: ~1300 L/min | JPC 4V210: ~890 L/min", "سری Norgren V61 در سایز G1/4 دبی بسیار نزدیک به VUVG-L18 (1300 L/min) ارائه می‌دهد"),
            ("آرایش‌های شیر موجود (Valve Functions)", "2x3/2 NC/NO, 5/2 تک و دوبوبین، 5/3 مرکز بسته/باز/تحت فشار", "3/2 NC, 2x3/2 NO (در Norgren V60AB11A), 5/2 و 5/3 مرکز بسته/APB", "برای شیرهای دوبل 2x3/2 در یک بدنه، سری Norgren V60AB11A ساختار مشابهی دارد"),
            ("توان مصرفی و اتصال بوبین (Electrical Coil)", "24V DC کم‌مصرف (1W تا 2.5W با کابل E-Box بسیار ظریف)", "24V DC (حدود 3W تا 4.8W) یا 220V AC با سوکت DIN 43650", "حداکثر جریان خروجی کارت PLC هنگام جایگزینی با بوبین استاندارد بررسی شود"),
        ],
        "checklistItems": [
            ("تشخیص کد VUVG-L (خطی) از VUVG-B (زیرشیری):", "اگر کد فستو با VUVG-L شروع می‌شود (دارای رزوه G1/8 یا G1/4 روی بدنه)، می‌توان آن را به صورت تکی با شیرهای هم‌پورت جایگزین کرد؛ اما اگر با VUVG-B شروع می‌شود، شیر به صورت کتابی روی منیفولد VTUG پیچ شده و تنها با کد اصلی VUVG-B یا تعویض کامل مجموعه منیفولد قابل جایگزینی است."),
            ("بررسی شیرهای دوبل 2x3/2 در یک بدنه:", "بسیاری از مدل‌های VUVG دو شیر ۳/۲ مستقل در یک بدنه هستند؛ هرگز یک شیر ۵/۲ معمولی را بدون اصلاح مدار به جای شیر 2x3/2 نصب نکنید."),
            ("کنترل جریان خروجی کارت PLC (توان بوبین):", "بوبین‌های کامپکت VUVG توان بسیار پایینی (حدود ۱ تا ۱.۵ وات) دارند؛ در صورت جایگزینی چند شیر همزمان با بوبین‌های استاندارد ۳ تا ۴.۸ وات، مجموع جریان کشیده‌شده از کارت خروجی PLC را کنترل کنید."),
            ("فضای نصب و نوع سوکت:", "ارتفاع سوکت DIN 43650 در شیرهای صنعتی بیشتر از کانکتور تخت E-Box فستو است؛ عمق تابلو پنوماتیک را پیش از تغییر تیپ شیر اندازه بگیرید."),
        ],
        "relatedLinks": [
            ("صفحه محصول Norgren V60A513A-A213JB (5/2 G1/8)", "product/norgren-v60a513a-a213jb/index.html"),
            ("صفحه محصول Norgren V61B513A-A213JB (5/2 G1/4 - 1300 L/min)", "product/norgren-v61b513a-a213jb/index.html"),
            ("صفحه محصول Norgren V61B611A-A213JB (5/3 APB G1/4)", "product/norgren-v61b611a-a213jb/index.html"),
            ("صفحه محصول JPC-4V210-08-24DC (5/2 G1/4)", "product/jpc-4v210-08-24dc/index.html"),
            ("ماتریس ۱۵ کد فنی سری Norgren V60", "series/norgren-v60/index.html"),
            ("ماتریس ۱۸ کد فنی سری Norgren V61", "series/norgren-v61/index.html"),
            ("کاتالوگ شیرهای برقی و کنترل جهت", "products/solenoid-valves/index.html"),
            ("صفحه برند نورگرن (Norgren)", "brands/norgren/index.html"),
        ],
        "oemWaQuery": "سلام، درخواست استعلام قیمت و بررسی فنی شیر کامپکت فستو سری Festo VUVG را دارم.",
        "jpcWaQuery": "سلام، درخواست مشاوره و استعلام قیمت شیر جایگزین خطی/منیفولدی (Norgren V60/V61 یا JPC 4V) به جای Festo VUVG را دارم.",
        "modalProductId": "norgren-v61b513a",
        "faqs": [
            (
                "تفاوت VUVG-L14 و VUVG-L18 در سایز پورت و دبی چیست؟",
                "مدل VUVG-L14 دارای عرض بدنه ۱۴ میلی‌متر و پورت G1/8 با دبی حدود ۶۰۰ تا ۷۰۰ لیتر بر دقیقه است (هم‌رده با Norgren V60A513A با دبی 750 L/min)، در حالی که VUVG-L18 دارای عرض ۱۸ میلی‌متر و پورت G1/4 با دبی حدود ۱۳۰۰ لیتر بر دقیقه است (هم‌رده با Norgren V61B513A و JPC 4V210-08)."
            ),
            (
                "منظور از آرایش ۵/۳ با کد M53C، M53E و M53B در فستو VUVG چیست؟",
                "کد M53C نشان‌دهنده ۵/۳ مرکز بسته (Closed Center - مشابه JPC-4V330C)، کد M53E نشان‌دهنده ۵/۳ مرکز باز به تخلیه (Exhausted Center)، و کد M53B نشان‌دهنده ۵/۳ مرکز تحت فشار (Pressurized Center / APB - مشابه Norgren V61B611A) است."
            ),
        ],
    },
    {
        "slug": "festo-ms-vs-jpc-frl-air-preparation",
        "activeSection": "frl",
        "titleSeo": "مقایسه واحد مراقبت هوای فشرده Festo سری MS با واحدهای FRL صنعتی JPC و Norgren | JPC",
        "metaDesc": "مقایسه مهندسی واحد مراقبت هوای فشرده فستو سری MS (MS4 / MS6-LFR) با واحدهای FRL صنعتی JPC سری AC4010 و Norgren Excelon سری BL72/BL73/BL74؛ بررسی دقت فیلتر ۵ و ۴۰ میکرون، تخلیه اتوماتیک و دبی.",
        "h1Fa": "مقایسه واحد مراقبت هوای فشرده Festo سری MS با واحدهای FRL صنعتی JPC و Norgren Excelon",
        "eyebrowFa": "مهندسی آماده‌سازی هوای فشرده، فیلتراسیون، تثبیت فشار و روانکاری (Air Preparation FRL)",
        "oemLabel": "Festo MS Series (MS4 / MS6-LFR / MSB6)",
        "jpcLabel": "JPC AC Series (AC4010-04-D) & Norgren Excelon (BL72 / BL73 / BL74)",
        "tldrViableFa": "جایگزینی کامل واحد مراقبت در ورودی ماشین‌آلات زمانی کاملاً عملی و اقتصادی است که سایز رزوه ورودی و خروجی خط (مثلاً G1/4، G3/8 یا G1/2)، دبی هوای مصرفی خط، نوع تخلیه کندانس (تخلیه اتوماتیک شناوری در برابر دستی) و دقت فیلتراسیون مورد نیاز هم‌خوانی داشته باشند؛ زیرا واحد مراقبت یک ماژول مستقل در ابتدای خط تغذیه است.",
        "tldrMandatoryOemFa": "استفاده از کد اصلی Festo سری MS زمانی الزامی است که قصد تعویض تنها یک ماژول میانی در یک بلوک ماژولار موجود MS6 (مثلاً افزودن شیر استارت نرم MS6-DL یا سنسور فشار MS6-SFE به بلوک فستو موجود) را داشته باشید یا نیاز به فیلترهای میکرو ۰.۰۱ میکرون (MS6-LFM) جهت هوای تنفسی/ابزار دقیق حساس باشد.",
        "comparisonRows": [
            ("سایز پورت و رزوه اتصال (Port Thread)", "MS4 (G1/8, G1/4) | MS6 (G1/4, G3/8, G1/2) — BSPP", "JPC AC2010 (G1/4), AC3010 (G3/8), AC4010 (G1/2) | Norgren BL72 (G1/4), BL73 (G3/8), BL74 (G1/2)", "رزوه موازی استاندارد BSPP (G) در تمام سایزهای ۱/۴ تا ۱/۲ اینچ"),
            ("دقت فیلتراسیون المان (Filtration Grade)", "40 µm (کد D7) یا 5 µm (کد D6) + میکروفیلترهای 1 µm و 0.01 µm", "JPC AC4010: استاندارد 25 µm (قابل سفارش 5 µm) | Norgren Excelon: 40 µm یا 5 µm", "برای جک و شیر استاندارد، فیلتر ۲۵ تا ۴۰ میکرون و برای شیرهای حساس ۵ میکرون مناسب است"),
            ("سیستم تخلیه آب کاسه (Condensate Drain)", "دستی چرخشی (M)، نیمه‌اتوماتیک یا تمام‌اتوماتیک شناوری (D / V)", "تخلیه اتوماتیک شناوری (پسوند D در JPC-AC4010-04-D و کد GA در Norgren BL72-201GA)", "در خطوط بدون سرکشی روزانه اپراتور، حتماً مدل تخلیه اتوماتیک انتخاب شود"),
            ("محدوده تنظیم فشار رگلاتور (Pressure Range)", "0.5 – 12 bar (مدل D7) یا 0.3 – 7 bar (مدل D6)", "JPC AC4010: 0.5 – 10 bar | Norgren BL72..BL74: 0.3 – 10 bar", "مجهز به مکانیزم Relieving (تخلیه فشار مازاد خط خروجی) و کلاهک قفل‌شونده"),
            ("محافظ کاسه و ایمنی کارگاهی (Bowl Guard)", "کاسه پلی‌کربنات با گارد محافظ پلاستیکی/فلزی (AS) یا کاسه تمام‌فلزی (U)", "کاسه پلی‌کربنات شفاف مجهز به گارد محافظ فلزی صنعتی", "در محیط‌های دارای بخار حلال یا تینر، از کاسه فلزی استفاده شود"),
            ("دبی اسمی عبوری (Nominal Flow Rate)", "حدود 2200 – 4500 L/min (در سایز MS6 پورت G1/2)", "JPC AC4010-04-D: ~3500 L/min | Norgren BL74 (G1/2): ~4000 L/min", "تأمین کامل دبی خطوط تولید و ماشین‌آلات چندجکه"),
        ],
        "checklistItems": [
            ("جایگزینی بلوک کامل در برابر تک‌ماژول:", "کانسپت اتصال بین‌ماژولی Festo MS6 با بست‌های کوپلینگ اختصاصی فستو است؛ بنابراین یک رگلاتور JPC یا Norgren به تنهایی به فیلتر MS6 فستو کوپل نمی‌شود، اما کل مجموعه واحد مراقبت (FRL کامل) به راحتی در مسیر لوله‌کشی G1/4 تا G1/2 جایگزین می‌گردد."),
            ("بررسی نیاز یا عدم نیاز مدار به روغن‌زن (Lubricator):", "سیلندرها و شیرهای مدرن فستو دارای گریس مادام‌العمر هستند؛ اگر مدار فعلی شما فقط فیلتر-رگلاتور (LFR بدون روغن‌زن) دارد، هنگام جایگزینی مشخص کنید که آیا به ست دوتکه (فیلتر رگلاتور) نیاز دارید یا سه‌تکه (همراه با روغن‌زن)."),
            ("کنترل فضای عرضی و فاصله براکت نصب:", "عرض کل واحد مراقبت سه‌تکه (F+R+L) بیشتر از واحد دوتکه سوار بر هم (FR+L مانند AC4010 یا BL74) است؛ فضای روی شاسی دستگاه را پیش از سفارش اندازه بگیرید."),
            ("انتخاب تخلیه اتوماتیک (Auto-Drain):", "اگر واحد مراقبت در ارتفاع یا داخل کابین بسته نصب می‌شود، حتماً کد دارای تخلیه اتوماتیک (مانند JPC-AC4010-04-D یا Norgren BL72-201GA) را انتخاب نمایید."),
        ],
        "relatedLinks": [
            ("صفحه محصول واحد مراقبت JPC-AC4010-04-D (G1/2 اتوماتیک)", "product/jpc-ac4010-04-d/index.html"),
            ("صفحه محصول Norgren BL72-201GA (G1/4 اتوماتیک)", "product/norgren-bl72-201ga/index.html"),
            ("صفحه محصول Norgren BL74-401G (G1/2)", "product/norgren-bl74-401g/index.html"),
            ("صفحه سری JPC AC4010", "series/jpc-ac4010/index.html"),
            ("صفحه سری Norgren BL72 (G1/4)", "series/norgren-bl72/index.html"),
            ("صفحه سری Norgren BL73 (G3/8)", "series/norgren-bl73/index.html"),
            ("صفحه سری Norgren BL74 (G1/2)", "series/norgren-bl74/index.html"),
            ("کاتالوگ واحد مراقبت و آماده‌سازی هوا", "products/air-preparation/index.html"),
            ("کاتالوگ رگلاتورهای فشار", "products/pressure-regulators/index.html"),
        ],
        "oemWaQuery": "سلام، درخواست استعلام قیمت واحد مراقبت هوای فشرده فستو سری Festo MS6-LFR را دارم.",
        "jpcWaQuery": "سلام، درخواست استعلام قیمت واحد مراقبت جایگزین (JPC-AC4010-04-D یا Norgren Excelon BL72/BL74) به جای Festo MS را دارم.",
        "modalProductId": "jpc-ou-frl-1-2",
        "faqs": [
            (
                "تفاوت واحد مراقبت سه‌تکه (AC) با دوتکه (OU / BL) در چیست؟",
                "در مدل‌های دوتکه (مانند JPC AC4010 یا Norgren BL72/BL74)، فیلتر و رگلاتور در یک ستون واحد بالای یکدیگر ادغام شده‌اند (Filter-Regulator) و روغن‌زن در کنار آن قرار می‌گیرد؛ این طراحی ضمن حفظ کامل عملکرد سه‌گانه، حدود ۳۰٪ فضای افقی کمتری روی شاسی اشغال می‌کند."
            ),
            (
                "چه نوع روغنی باید در مخزن روغن‌زن واحد مراقبت پنوماتیک ریخته شود؟",
                "فقط از روغن پنوماتیک یا هیدرولیک سبک با گرانروی ISO VG 32 (مانند Tellus 32) استفاده کنید. استفاده از روغن موتور، روغن ترمز یا تینر باعث خوردگی کاسه پلی‌کربنات و تورم اورینگ‌های NBR شیر برقی می‌شود."
            ),
        ],
    },
    {
        "slug": "rexroth-aventics-hf03-lg-0820055051-replacement",
        "activeSection": "valves",
        "titleSeo": "راهنمای فنی و معادل‌یابی شیر برقی Bosch Rexroth / AVENTICS سری HF03-LG (کد 0820055051) | JPC",
        "metaDesc": "تحلیل مهندسی و راهنمای تعیین تکلیف و معادل‌یابی شیر کنترل جهت Bosch Rexroth / AVENTICS سری HF03-LG (کد 0820055051 و R412003484)؛ بررسی عملکرد ۵/۲، الگوی منیفولد و راهکارهای جایگزینی.",
        "h1Fa": "راهنمای فنی و معادل‌یابی شیر برقی Bosch Rexroth / AVENTICS سری HF03-LG (کد 0820055051)",
        "eyebrowFa": "مرجع شناسایی کدهای ۱۰ رقمی تاریخی Rexroth Pneumatics / AVENTICS در خطوط تولید",
        "oemLabel": "Bosch Rexroth / AVENTICS HF03-LG (کد 0820055051 و سری R412...)",
        "jpcLabel": "تأمین کد مرجع، بازطراحی بلوک منیفولد یا جایگزینی عملکردی خطی (Norgren V60/V61 و JPC 4V)",
        "tldrViableFa": "کد ۱۰ رقمی 0820055051 متعلق به سیستم شیرهای جزیره‌ای (Valve Manifold System) خانواده HF03-LG از کاتالوگ تاریخی Rexroth Pneumatics / AVENTICS است (و نباید با سری خطی CD07 اشتباه گرفته شود). اگر هدف شما جایگزینی یک عملکرد ۵/۲ مستقل در خارج از بلوک جزیره‌ای یا نوسازی کامل یک ایستگاه منیفولد قدیمی با یک منیفولد جدید استاندارد باشد، جایگزینی عملکردی با شیرهای ۵/۲ صنعتی (مانند JPC 4V210 یا Norgren V60/V61) کاملاً امکان‌پذیر است.",
        "tldrMandatoryOemFa": "اگر قصد دارید تنها یک اسلایس (Slice / Valve Module) معیوب را در میانه یک جزیره شیر موجود HF03-LG (متصل به بک‌پلین الکتریکی و صفحات اتصال R412003484 / R412005839) بدون تغییر سایر اسلایس‌ها تعویض کنید، هیچ شیر خطی استاندارد دیگری روی پروفیل منیفولد HF03-LG نصب نمی‌شود و باید دقیقاً کد مرجع سری HF03-LG جست‌وجو یا کل جزیره بازطراحی گردد.",
        "comparisonRows": [
            ("خانواده و معماری واقعی قطعه", "سیستم شیر جزیره‌ای ماژولار سری HF03-LG (کدهای 0820055... و R412...)", "شیرهای کنترل جهت خطی و منیفولدی استاندارد (JPC 4V210 / Norgren V60-V61)", "اصلاح خطای رایج بازار: کد 0820055051 متعلق به خانواده HF03-LG است، نه سری CD07"),
            ("انتساب حقوقی برند (Brand Lineage)", "Rexroth Pneumatics -> Bosch Rexroth -> AVENTICS (Emerson)", "JPC (برند اختصاصی جلالی پنوماتیک) و Norgren", "شفافیت: کدهای رکسروت/آونتیکس در کاتالوگ JPC یک نمایه مرجع تاریخی برای مهندسان نت است"),
            ("آرایش و عملکرد مدار (Valve Function)", "شیر کنترل جهت اسپول ۵/۲ یا ۲×۳/۲ ماژولار پایلوتی در بلوک جزیره", "۵/۲ تک‌بوبین (4V210 / V61B513A)، ۵/۲ دوبوبین (4V220) و ۵/۳ مرکز بسته (4V330C)", "از نظر منطق مدار پنوماتیک (فرمان به جک دوکاره)، عملکرد ۵/۲ کاملاً معادل است"),
            ("نحوه اتصال هوا و برق (Pneumatic & Electrical)", "کانال‌های هوای مشترک داخلی در بلوک جزیره + اتصال الکتریکی Multipin / Fieldbus یا فیش مجزا", "پورت‌های رزوه‌دار استاندارد G1/8 و G1/4 + سوکت برق استاندارد DIN 43650", "برای جایگزینی تکی، باید تغذیه P و خروجی‌های A/B به صورت شیلنگی منشعب شوند"),
            ("قطعات جانبی منیفولد در بانک ۵۰۰ کد JPC", "شامل ۳۵ کد مرجع HF03-LG (شیرهای 0820055201..5502 و قطعات اتصال R412003484..5839)", "منیفولدهای ردیفی استاندارد سری 4V همراه با فیتینگ و سایلنسر کامل", "امکان استعلام کدهای ۱۰ رقمی یا دریافت پیشنهاد نوسازی کامل منیفولد"),
        ],
        "checklistItems": [
            ("تأیید خانواده صحیح روی پلاک (HF03-LG در برابر CD07):", "کد 0820055051 در مستندات رسمی رکسروت/آونتیکس متعلق به سیستم جزیره‌ای HF03-LG است؛ پیش از هر اقدامی عکس واضح از پلاک شیر و بلوک زیرین آن تهیه کنید."),
            ("تصمیم‌گیری بین «تأمین تک‌اسلایس» یا «ایزوله‌سازی / نوسازی منیفولد»:", "در خطوط تولیدی که قطعات یدکی جزیره قدیمی HF03-LG کمیاب یا دارای زمان تحویل طولانی هستند، مهندسان نت می‌توانند خروجی شیلنگ همان ایستگاه را به یک شیر برقی خطی ۲۴ ولت استاندارد (مانند JPC-4V210-08-24DC) منتقل کنند یا کل منیفولد را با یک بلوک منیفولد جدید جایگزین نمایند."),
            ("بررسی ولتاژ و قطبیت تحریک بوبین:", "در سیستم‌های جزیره‌ای رکسروت، مشترک برق (Common) روی برد منیفولد ممکن است PNP (مثبت مشترک یا منفی مشترک) باشد؛ هنگام انشعاب سیم فرمان به شیر جایگزین، ولتاژ 24V DC را با مولتی‌متر کنترل کنید."),
            ("استفاده از دستیار هوش مصنوعی پلاک‌خوان JPC:", "برای شناسایی دقیق کدهای ۱۰ رقمی که با 0820 یا R412 شروع می‌شوند، تصویر پلاک را در ai.jpciran.com بارگذاری하거나 به واتساپ فنی ارسال فرمایید."),
        ],
        "relatedLinks": [
            ("صفحه مرجع کد Bosch Rexroth / AVENTICS 0820055051", "product/bosch-rexroth-aventics-0820055051/index.html"),
            ("صفحه مرجع کد Bosch Rexroth / AVENTICS 0820055201", "product/bosch-rexroth-aventics-0820055201/index.html"),
            ("صفحه مرجع قطعه منیفولد R412003484", "product/bosch-rexroth-aventics-r412003484/index.html"),
            ("صفحه مرجع رابط پنوماتیک 2123208000", "product/bosch-rexroth-aventics-2123208000/index.html"),
            ("ماتریس کامل ۳۵ کد فنی سری HF03-LG", "series/rexroth-hf03-lg/index.html"),
            ("صفحه برند Bosch Rexroth / AVENTICS", "brands/bosch-rexroth/index.html"),
            ("صفحه شیر جایگزین خطی JPC-4V210-08-24DC", "product/jpc-4v210-08-24dc/index.html"),
            ("صفحه شیر Norgren V61B513A-A213JB", "product/norgren-v61b513a-a213jb/index.html"),
        ],
        "oemWaQuery": "سلام، درخواست بررسی تامین یا استعلام قطعه Bosch Rexroth / AVENTICS سری HF03-LG با کد 0820055051 را دارم.",
        "jpcWaQuery": "سلام، درخواست مشاوره مهندسی جهت جایگزینی عملکردی یا نوسازی منیفولد Bosch Rexroth HF03-LG (0820055051) با شیرهای JPC / Norgren را دارم.",
        "modalProductId": "rexroth-581-iso1",
        "faqs": [
            (
                "چرا در برخی لیست‌های بازار کد 0820055051 به اشتباه سری CD07 نامیده شده است؟",
                "هر دو سری CD07 و HF03-LG از پیش‌شماره کدهای ۱۰ رقمی قدیمی Rexroth Pneumatics (0820...) استفاده می‌کنند؛ اما بر اساس جدول کاتالوگ مرجع Bosch Rexroth / AVENTICS، کدهای خانواده 0820055051 تا 0820055502 ماژول‌های شیر سیستم جزیره‌ای سری HF03-LG هستند و در بانک اطلاعاتی JPC با انتساب دقیق HF03-LG ثبت شده‌اند."
            ),
            (
                "چگونه می‌توان یک خانه معیوب از جزیره شیر قدیمی HF03-LG را در صورت عدم دسترسی فوری به اسلایس اصلی راه‌اندازی کرد؟",
                "در تعمیرات اضطراری خط تولید، می‌توان پورت‌های خروجی خانه معیوب را کور (Blind Plug) کرد، دو رشته سیم تحریک ۲۴ ولت همان بوبین را از ترمینال خارج نمود و به یک شیر برقی ۵/۲ خطی استاندارد (مانند JPC-4V210-08-24DC یا Norgren V60/V61) که در کنار منیفولد نصب شده متصل کرد تا توقف خط تولید برطرف شود."
            ),
        ],
    },
]


def render_compare_hub_page() -> str:
    """
    Generate `/compare/index.html` (`depth=1`, `base_prefix="../"`).
    """
    base_prefix = "../"
    canonical_url = f"{SITE_DOMAIN}/compare/"

    breadcrumbs = [
        ("صفحه اصلی", f"{SITE_DOMAIN}/"),
        ("مرکز معادل‌یابی و مقایسه فنی تجهیزات پنوماتیک", canonical_url),
    ]

    item_list_ld = {
        "@type": "ItemList",
        "@id": f"{canonical_url}#compare-guides",
        "name": "مرکز معادل‌یابی و مقایسه فنی تجهیزات پنوماتیک صنعتی (Festo، Norgren، Bosch Rexroth و JPC)",
        "numberOfItems": len(COMPARE_PAGES_SPEC),
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": idx + 1,
                "url": f"{SITE_DOMAIN}/compare/{c['slug']}/",
                "name": c["h1Fa"],
            }
            for idx, c in enumerate(COMPARE_PAGES_SPEC)
        ],
    }

    hub_faqs = [
        (
            "تفاوت «جایگزین مستقیم (Drop-in)»، «سازگار مشروط» و «مشابه عملکردی» در معادل‌یابی پنوماتیک چیست؟",
            "۱) جایگزین مستقیم (Drop-in): قطعه از نظر استاندارد ابعاد نصب، فاصله پیچ‌ها، سایز رزوه، ولتاژ و فشار کاملاً منطبق است (مانند دو جک استاندارد ISO 15552 با پایه یکسان). ۲) سازگار مشروط: ابعاد اصلی نصب یکسان است اما جزئیاتی مانند شیار سنسور مگنتی (T-Slot) یا سایز سایلنسر اگزوز باید تطبیق داده شود. ۳) مشابه عملکردی: قطعه همان کار مدار (مثلاً شیر ۵/۲ با پورت G1/4) را انجام می‌دهد اما الگوی منیفولد یا ابعاد بدنه متفاوت است."
        ),
        (
            "چرا شرکت جلالی پنوماتیک بدون بررسی ۴ پارامتر فنی هیچ معادلی را قطعی اعلام نمی‌کند؟",
            "در مهندسی پنوماتیک، صرفاً تشابه ظاهر یا نام قطعه برای جایگزینی کافی نیست. تطابق استاندارد ابعاد نصب (ISO)، نوع رزوه (G موازی در برابر R/NPT مخروطی)، دبی عبوری (Qn/Cv) در فشار ۶ بار و مشخصات الکتریکی بوبین (24V DC / 220V AC) باید پیش از صدور پیش‌فاکتور کنترل شود تا ایمنی و راندمان خط تولید تضمین گردد."
        ),
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
            for q, a in hub_faqs
        ],
    }

    jsonld_str = build_base_jsonld_graph(
        canonical_url=canonical_url,
        breadcrumbs=breadcrumbs,
        extra_nodes=[item_list_ld, faq_ld],
    )

    cards_html = "\n".join(
        f"""        <article style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: 1.4rem; display: flex; flex-direction: column; justify-content: space-between; gap: 1rem;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 0.6rem;">
              <span style="font-size: 0.74rem; font-weight: 800; color: #087F8C; background: #E6F4F6; padding: 0.22rem 0.65rem; border-radius: 999px;">
                {esc(c['eyebrowFa'])}
              </span>
              <span class="mono" dir="ltr" style="font-size: 0.74rem; color: #64748B;">{esc(c['oemLabel'].split('(')[0].strip())}</span>
            </div>
            <h2 style="font-size: 1.08rem; font-weight: 800; color: #10243A; line-height: 1.5; margin-bottom: 0.55rem;">
              <a href="{esc(c['slug'])}/index.html" style="color: inherit; text-decoration: none;">{esc(c['h1Fa'])}</a>
            </h2>
            <p style="font-size: 0.85rem; color: #475569; line-height: 1.8; margin: 0;">
              {esc(c['metaDesc'])}
            </p>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; padding-top: 0.85rem; border-top: 1px solid #E1E7EE;">
            <a href="{esc(c['slug'])}/index.html" class="btn btn-amber btn-sm">
              مشاهده جدول مقایسه و چک‌لیست جایگزینی ←
            </a>
            <span class="mono" dir="ltr" style="font-size: 0.75rem; color: #087F8C; font-weight: 700;">4-Step Engineering Check</span>
          </div>
        </article>"""
        for c in COMPARE_PAGES_SPEC
    )

    faqs_html = "\n".join(
        f"""        <details class="faq-item" {'open' if idx == 0 else ''} style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem 1.15rem; margin-bottom: 0.75rem;">
          <summary style="font-weight: 800; color: #10243A; cursor: pointer; font-size: 0.94rem;">{esc(q)}</summary>
          <p style="margin-top: 0.65rem; font-size: 0.87rem; color: #475569; line-height: 1.85;">{esc(a)}</p>
        </details>"""
        for idx, (q, a) in enumerate(hub_faqs)
    )

    main_html = f"""
    <nav aria-label="مسیر راهنما (Breadcrumb)" style="background: #F1F5F9; border-bottom: 1px solid #E1E7EE; padding: 0.75rem 0; font-size: 0.82rem;">
      <div class="container" style="display: flex; flex-wrap: wrap; align-items: center; gap: 0.45rem; color: #475569;">
        <a href="{base_prefix}index.html" style="color: #087F8C; font-weight: 700;">صفحه اصلی</a>
        <span aria-hidden="true">←</span>
        <strong style="color: #10243A;">مرکز معادل‌یابی و مقایسه فنی تجهیزات پنوماتیک</strong>
      </div>
    </nav>

    <section class="section" style="background: linear-gradient(135deg, #10243A 0%, #19344F 100%); color: #FFFFFF; padding: 2.5rem 0;">
      <div class="container">
        <span style="display: inline-block; background: rgba(8,127,140,0.3); color: #38BDF8; font-size: 0.78rem; font-weight: 800; padding: 0.3rem 0.75rem; border-radius: 999px; margin-bottom: 0.75rem;">
          مرجع مهندسی تطبیق، مقایسه ابعادی و جایگزینی قطعات پنوماتیک صنعتی
        </span>
        <h1 style="font-size: clamp(1.45rem, 3.4vw, 2.1rem); font-weight: 900; color: #FFFFFF; margin-bottom: 0.65rem;">
          مرکز معادل‌یابی و مقایسه فنی تجهیزات پنوماتیک (Festo، Norgren، Bosch Rexroth و JPC)
        </h1>
        <p style="font-size: 0.94rem; color: #CBD5E1; max-width: 860px; line-height: 1.9; margin-bottom: 1.25rem;">
          در این مرکز، مقایسه‌های فنی خط‌به‌خط میان سری‌های پرکاربرد اروپایی (<span dir="ltr" class="mono">Festo DSBC, MFH, VUVG, MS6</span> و کدهای تاریخی <span dir="ltr" class="mono">Bosch Rexroth / AVENTICS HF03-LG</span>) با سری‌های صنعتی <strong dir="ltr" class="mono">JPC</strong> و <strong dir="ltr" class="mono">Norgren</strong> به همراه چک‌لیست‌های الزامی پیش از جایگزینی تدوین شده است.
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 0.65rem;">
          <a href="{base_prefix}products/index.html" class="btn btn-amber btn-sm">جستجو در بانک ۵۰۰ کد فنی کاتالوگ ←</a>
          <a href="{base_prefix}festo-cross-reference.html" class="btn btn-outline-light btn-sm">جدول جامع معادل‌یابی کدها</a>
          <a href="https://ai.jpciran.com" target="_blank" rel="noopener noreferrer" class="btn btn-ai-scan btn-sm">✦ دستیار هوشمند تشخیص پلاک (AI)</a>
        </div>
      </div>
    </section>

    <section class="section" style="padding: 2.25rem 0 1.25rem;">
      <div class="container">
        <div class="section-header" style="margin-bottom: 1.25rem;">
          <span class="section-eyebrow">۵ پرونده تخصصی مقایسه و جایگزینی مهندسی</span>
          <h2 class="section-title">راهنماهای مقایسه فنی و چک‌لیست‌های تطبیق استاندارد</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: 1.25rem;">
{cards_html}
        </div>
      </div>
    </section>

    <section class="section" style="padding: 1.25rem 0 2.5rem;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.25rem, 3vw, 1.85rem);">
          <span class="section-eyebrow">اصول مهندسی معادل‌یابی در شرکت جلالی پنوماتیک</span>
          <h2 style="font-size: 1.15rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 1rem;">
            سؤالات پرتکرار درباره سطح‌بندی سازگاری و جایگزینی قطعات
          </h2>
{faqs_html}
        </div>
      </div>
    </section>
"""

    return render_full_html_page(
        title="مرکز معادل‌یابی و مقایسه فنی تجهیزات پنوماتیک (فستو، نورگرن، رکسروت و JPC) | جلالی پنوماتیک",
        meta_description="مرجع مهندسی مقایسه فنی جک Festo DSBC با ISO 15552، شیر برقی MFH و VUVG با سری 4V و V60/V61، واحد مراقبت MS با FRL صنعتی و کدهای Bosch Rexroth HF03-LG (0820055051).",
        canonical_url=canonical_url,
        base_prefix=base_prefix,
        active_section="products",
        jsonld_str=jsonld_str,
        main_html=main_html,
        page_category_attr="all",
    )


def render_compare_detail_page(spec: dict) -> str:
    """
    Generate `/compare/<slug>/index.html` (`depth=2`, `base_prefix="../../"`).
    """
    base_prefix = "../../"
    slug = spec["slug"]
    canonical_url = f"{SITE_DOMAIN}/compare/{slug}/"

    breadcrumbs = [
        ("صفحه اصلی", f"{SITE_DOMAIN}/"),
        ("مرکز معادل‌یابی و مقایسه فنی", f"{SITE_DOMAIN}/compare/"),
        (spec["h1Fa"], canonical_url),
    ]

    tech_article_ld = {
        "@type": "TechArticle",
        "@id": f"{canonical_url}#tech-article",
        "headline": spec["h1Fa"],
        "description": spec["metaDesc"],
        "inLanguage": "fa-IR",
        "mainEntityOfPage": canonical_url,
        "author": {
            "@type": "Organization",
            "@id": "https://jpciran.com/#organization",
            "name": "شرکت جلالی پنوماتیک (JPC)",
        },
        "publisher": {"@id": "https://jpciran.com/#organization"},
        "proficiencyLevel": "Expert",
    }

    faq_ld = {
        "@type": "FAQPage",
        "@id": f"{canonical_url}#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in spec["faqs"]
        ],
    }

    jsonld_str = build_base_jsonld_graph(
        canonical_url=canonical_url,
        breadcrumbs=breadcrumbs,
        extra_nodes=[tech_article_ld, faq_ld],
    )

    table_rows_html = "\n".join(
        f"""              <tr>
                <th scope="row" style="background: #F8FAFC; font-weight: 800; color: #10243A; width: 22%;">{esc(param)}</th>
                <td style="width: 26%; font-variant-numeric: tabular-nums;">{esc(oem_val)}</td>
                <td style="width: 26%; font-variant-numeric: tabular-nums;">{esc(jpc_val)}</td>
                <td style="width: 26%; color: #334155; font-size: 0.83rem;">{esc(note)}</td>
              </tr>"""
        for param, oem_val, jpc_val, note in spec["comparisonRows"]
    )

    checklist_html = "\n".join(
        f"""            <div style="background: #FFFBEB; border: 1px solid #FDE68A; border-right: 4px solid #F28C28; border-radius: 10px; padding: 0.95rem 1.1rem;">
              <div style="font-weight: 800; color: #92400E; font-size: 0.9rem; margin-bottom: 0.3rem;">✓ {esc(title)}</div>
              <p style="font-size: 0.84rem; color: #78350F; line-height: 1.8; margin: 0;">{esc(desc)}</p>
            </div>"""
        for title, desc in spec["checklistItems"]
    )

    related_links_html = "\n".join(
        f"""            <a href="{base_prefix}{esc(rel_path)}" style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 0.8rem 1rem; text-decoration: none; color: #10243A; font-size: 0.85rem; font-weight: 700; display: flex; justify-content: space-between; align-items: center;">
              <span>{esc(lbl)}</span>
              <span style="color: #087F8C; font-weight: 800;">←</span>
            </a>"""
        for lbl, rel_path in spec["relatedLinks"]
    )

    other_compares_html = "\n".join(
        f"""            <a href="{base_prefix}compare/{esc(c['slug'])}/index.html" class="btn btn-outline-tech btn-xs">{esc(c['h1Fa'][:55])}...</a>"""
        for c in COMPARE_PAGES_SPEC
        if c["slug"] != slug
    )

    faqs_html = "\n".join(
        f"""        <details class="faq-item" {'open' if idx == 0 else ''} style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem 1.15rem; margin-bottom: 0.75rem;">
          <summary style="font-weight: 800; color: #10243A; cursor: pointer; font-size: 0.94rem;">{esc(q)}</summary>
          <p style="margin-top: 0.65rem; font-size: 0.87rem; color: #475569; line-height: 1.85;">{esc(a)}</p>
        </details>"""
        for idx, (q, a) in enumerate(spec["faqs"])
    )

    oem_wa_url = f"https://wa.me/989121305167?text={urllib.parse.quote(spec['oemWaQuery'])}"
    jpc_wa_url = f"https://wa.me/989121305167?text={urllib.parse.quote(spec['jpcWaQuery'])}"

    main_html = f"""
    <!-- A. BREADCRUMB NAVIGATION -->
    <nav aria-label="مسیر راهنما (Breadcrumb)" style="background: #F1F5F9; border-bottom: 1px solid #E1E7EE; padding: 0.75rem 0; font-size: 0.82rem;">
      <div class="container" style="display: flex; flex-wrap: wrap; align-items: center; gap: 0.45rem; color: #475569;">
        <a href="{base_prefix}index.html" style="color: #087F8C; font-weight: 700;">صفحه اصلی</a>
        <span aria-hidden="true">←</span>
        <a href="{base_prefix}compare/index.html" style="color: #087F8C; font-weight: 700;">مرکز معادل‌یابی و مقایسه فنی</a>
        <span aria-hidden="true">←</span>
        <strong style="color: #10243A;">{esc(spec['h1Fa'])}</strong>
      </div>
    </nav>

    <!-- HERO & B. QUICK ENGINEERING ANSWER (TL;DR BOX) -->
    <section class="section" style="background: #FFFFFF; border-bottom: 1px solid #E1E7EE; padding: 2.25rem 0;">
      <div class="container">
        <span class="section-eyebrow">{esc(spec['eyebrowFa'])}</span>
        <h1 style="font-size: clamp(1.3rem, 3vw, 1.85rem); font-weight: 900; color: #10243A; line-height: 1.45; margin: 0.35rem 0 1.15rem;">
          {esc(spec['h1Fa'])}
        </h1>

        <!-- TL;DR QUICK ENGINEERING ANSWER BOX -->
        <div style="background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 14px; padding: clamp(1.15rem, 2.5vw, 1.65rem);">
          <div style="font-size: 0.82rem; font-weight: 800; color: #087F8C; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.4rem;">
            <span>⚡ پاسخ سریع مهندسی (Quick Engineering Answer — TL;DR)</span>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 310px), 1fr)); gap: 1rem;">
            <div style="background: #ECFDF5; border: 1px solid #A7F3D0; border-right: 4px solid #059669; border-radius: 10px; padding: 1rem;">
              <strong style="color: #065F46; font-size: 0.9rem; display: block; margin-bottom: 0.35rem;">
                ✓ چه زمانی جایگزینی با سری صنعتی JPC / هم‌استاندارد امکان‌پذیر است؟
              </strong>
              <p style="font-size: 0.85rem; color: #064E3B; line-height: 1.85; margin: 0;">
                {esc(spec['tldrViableFa'])}
              </p>
            </div>
            <div style="background: #FEF2F2; border: 1px solid #FECACA; border-right: 4px solid #DC2626; border-radius: 10px; padding: 1rem;">
              <strong style="color: #991B1B; font-size: 0.9rem; display: block; margin-bottom: 0.35rem;">
                ⚠️ چه زمانی تأمین دقیق کد اصلی سازنده (OEM Exact-Match) الزامی است؟
              </strong>
              <p style="font-size: 0.85rem; color: #7F1D1D; line-height: 1.85; margin: 0;">
                {esc(spec['tldrMandatoryOemFa'])}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- C. SIDE-BY-SIDE TECHNICAL COMPARISON TABLE -->
    <section class="section" style="padding: 2rem 0 1.25rem;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.2rem, 3vw, 1.8rem);">
          <span class="section-eyebrow">مقایسه پارامتر به پارامتر کاتالوگ</span>
          <h2 style="font-size: 1.2rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 1rem;">
            جدول مقایسه مشخصات فنی: <span dir="ltr" class="mono">{esc(spec['oemLabel'])}</span> در برابر <span dir="ltr" class="mono">{esc(spec['jpcLabel'])}</span>
          </h2>
          <div class="table-responsive">
            <table class="tech-comparison-table" aria-label="جدول مقایسه فنی {esc(spec['h1Fa'])}">
              <thead>
                <tr>
                  <th scope="col">پارامتر فنی و مهندسی</th>
                  <th scope="col"><span dir="ltr" class="mono">{esc(spec['oemLabel'])}</span></th>
                  <th scope="col"><span dir="ltr" class="mono">{esc(spec['jpcLabel'])}</span></th>
                  <th scope="col">تحلیل مهندسی و ملاحظات تطبیق</th>
                </tr>
              </thead>
              <tbody>
{table_rows_html}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- D. MANDATORY PRE-REPLACEMENT VERIFICATION CHECKLIST -->
    <section class="section" style="padding: 1.25rem 0;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.2rem, 3vw, 1.8rem);">
          <span class="section-eyebrow">الزامات ایمنی و مهندسی پیش از جایگزینی</span>
          <h2 style="font-size: 1.18rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 0.5rem;">
            چک‌لیست الزامی ۴مرحله‌ای پیش از جایگزینی قطعه در خط تولید
          </h2>
          <p style="font-size: 0.87rem; color: #475569; margin-bottom: 1rem; line-height: 1.8;">
            هیچ‌گاه جایگزینی مستقیم (Drop-in) نباید بدون کنترل چهار محور زیر (ابعاد مرکزبه‌مرکز نصب، گام رزوه پورت، الگوی منیفولد و مشخصات دبی/ولتاژ) فرض شود:
          </p>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 0.9rem;">
{checklist_html}
          </div>
        </div>
      </div>
    </section>

    <!-- E. DIRECT LINKS & DUAL RFQ ACTIONS -->
    <section class="section" style="padding: 1.25rem 0;">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr)); gap: 1.35rem;">
          <!-- DUAL RFQ WORKSTATION -->
          <div style="background: #10243A; color: #FFFFFF; border-radius: 14px; padding: 1.5rem;">
            <span style="font-size: 0.76rem; font-weight: 800; color: #38BDF8;">استعلام همزمان کد اصلی یا جایگزین مهندسی</span>
            <h2 style="font-size: 1.15rem; font-weight: 800; color: #FFFFFF; margin: 0.3rem 0 0.75rem;">
              دریافت پیش‌فاکتور کد OEM یا معادل اقتصادی JPC
            </h2>
            <p style="font-size: 0.84rem; color: #CBD5E1; line-height: 1.8; margin-bottom: 1.1rem;">
              واحد فروش و مهندسی شرکت جلالی پنوماتیک در لاله‌زار تهران امکان اعلام قیمت و زمان تحویل هم برای کد اصلی سازنده و هم برای جایگزین هم‌استاندارد JPC را فراهم کرده است:
            </p>
            <div style="display: flex; flex-direction: column; gap: 0.65rem;">
              <a href="{esc(jpc_wa_url)}" target="_blank" rel="noopener noreferrer" class="btn btn-amber" style="width: 100%; justify-content: center; font-weight: 800;">
                استعلام قیمت جایگزین JPC / هم‌استاندارد در واتساپ
              </a>
              <a href="{esc(oem_wa_url)}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="width: 100%; justify-content: center;">
                استعلام تأمین کد اصلی سازنده (OEM) در واتساپ
              </a>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
                <button type="button" class="btn btn-rfq-add btn-sm js-add-rfq-btn" data-id="{esc(spec['modalProductId'])}">
                  + افزودن به سبد استعلام
                </button>
                <button type="button" class="btn btn-outline-light btn-sm js-quote-trigger" data-id="{esc(spec['modalProductId'])}">
                  فرم استعلام سریع
                </button>
              </div>
            </div>
          </div>

          <!-- DIRECT PRODUCT, SERIES & BRAND LINKS -->
          <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: 1.5rem;">
            <span class="section-eyebrow">دسترسی یک‌کلیکی به صفحات محصول و سری فنی</span>
            <h2 style="font-size: 1.12rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 0.9rem;">
              صفحات تخصصی محصولات، سری‌ها و برندهای مرتبط
            </h2>
            <div style="display: grid; grid-template-columns: 1fr; gap: 0.55rem;">
{related_links_html}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- F. TECHNICAL FAQ & RELATED ENGINEERING GUIDES -->
    <section class="section" style="padding: 1.25rem 0 2.5rem;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.2rem, 3vw, 1.8rem);">
          <span class="section-eyebrow">پرسش و پاسخ مهندسی (Technical Q&amp;A)</span>
          <h2 style="font-size: 1.18rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 1rem;">
            سؤالات پرتکرار مهندسان درباره {esc(spec['h1Fa'])}
          </h2>
{faqs_html}
          <div style="margin-top: 1.15rem; padding-top: 1rem; border-top: 1px solid #E1E7EE; display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center;">
            <span style="font-size: 0.8rem; font-weight: 700; color: #64748B;">سایر مقایسه‌های فنی:</span>
{other_compares_html}
          </div>
        </div>

        <div style="background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 14px; padding: clamp(1.15rem, 3vw, 1.6rem); margin-top: 1.25rem;">
          <span class="section-eyebrow">دانشنامه مهندسی و عیبیابی JPC</span>
          <h2 style="font-size: 1.1rem; font-weight: 800; color: #10243A; margin: 0.2rem 0 0.85rem;">
            راهنماهای مهندسی مرتبط
          </h2>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 0.65rem;">
            <a href="{base_prefix}pneumatic-cylinder-buying-guide.html" style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 8px; padding: 0.75rem 0.9rem; text-decoration: none; color: #10243A; font-size: 0.83rem; font-weight: 700;">📘 راهنمای انتخاب جک پنوماتیک (ISO 15552 و SC) ←</a>
            <a href="{base_prefix}solenoid-valve-guide.html" style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 8px; padding: 0.75rem 0.9rem; text-decoration: none; color: #10243A; font-size: 0.83rem; font-weight: 700;">⚡ راهنمای انتخاب شیر برقی ۵/۲، ۳/۲ و ۵/۳ ←</a>
            <a href="{base_prefix}guides/frl-air-preparation-guide/index.html" style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 8px; padding: 0.75rem 0.9rem; text-decoration: none; color: #10243A; font-size: 0.83rem; font-weight: 700;">🌬️ مرکز جامع انتخاب واحد مراقبت هوا (FRL) ←</a>
            <a href="{base_prefix}guides/pneumatic-troubleshooting-guide/index.html" style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 8px; padding: 0.75rem 0.9rem; text-decoration: none; color: #10243A; font-size: 0.83rem; font-weight: 700;">🛠️ مرکز عیبیابی مدارهای پنوماتیک و تشخیص رزوه ←</a>
          </div>
        </div>
      </div>
    </section>
"""

    return render_full_html_page(
        title=spec["titleSeo"],
        meta_description=spec["metaDesc"],
        canonical_url=canonical_url,
        base_prefix=base_prefix,
        active_section=spec["activeSection"],
        jsonld_str=jsonld_str,
        main_html=main_html,
        page_category_attr=spec["activeSection"],
    )
