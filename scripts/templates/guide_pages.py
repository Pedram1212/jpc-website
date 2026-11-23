"""
Phase 3 Engineering Knowledge Hub Templates (`/guides/`)
======================================================
Generates the 2 remaining Engineering Knowledge Hubs (`depth=2`, `base_prefix="../../"`):
1. `/guides/frl-air-preparation-guide/index.html`
   «مرکز جامع انتخاب و محاسبه واحد مراقبت هوای فشرده (FRL)»
2. `/guides/pneumatic-troubleshooting-guide/index.html`
   «مرکز عیبیابی مدارهای پنوماتیک و راهنمای تشخیص و جایگزینی قطعات»

Together with `pneumatic-cylinder-buying-guide.html` and `solenoid-valve-guide.html`,
these complete all 4 Engineering Knowledge Clusters on `jpciran.com`.
"""

from .common import (
    SITE_DOMAIN,
    build_base_jsonld_graph,
    esc,
    render_full_html_page,
)

GUIDE_PAGES_SPEC = [
    {
        "slug": "frl-air-preparation-guide",
        "titleSeo": "مرکز جامع انتخاب و محاسبه واحد مراقبت هوای فشرده (FRL: فیلتر، رگلاتور و روغن‌زن) | JPC",
        "metaDesc": "راهنمای مهندسی انتخاب واحد مراقبت پنوماتیک FRL بر اساس استاندارد خلوص هوای ISO 8573-1، فیلتراسیون ۵ در برابر ۴۰ میکرون، محاسبه افت فشار رگلاتور، قواعد روغن‌زن و تخلیه اتوماتیک.",
        "h1Fa": "مرکز جامع انتخاب و محاسبه واحد مراقبت هوای فشرده (FRL)",
        "eyebrowFa": "دانشنامه مهندسی آماده‌سازی هوای فشرده · استاندارد ISO 8573-1",
        "activeSection": "frl-accessories",
        "tldrFa": "بیش از ۷۰٪ خرابی زودهنگام شیرهای برقی (گیرکردن اسپول) و پوسیدگی پکینگ جک‌های پنوماتیک ناشی از رطوبت تقطیرشده، ذرات زنگ لوله و نوسان فشار خط است. انتخاب صحیح واحد مراقبت (Filter + Regulator + Lubricator) نیازمند تطبیق دبی مصرفی سیستم (L/min) با سایز پورت (G1/4 تا G1/2)، انتخاب دقت فیلتراسیون (۴۰ میکرون عمومی یا ۵ میکرون ابزار دقیق) و انتخاب مکانیزم تخلیه اتوماتیک رطوبت است.",
        "sections": [
            {
                "id": "iso-8573-1",
                "eyebrow": "۱. استاندارد کیفیت هوای فشرده",
                "title": "کلاس‌های خلوص هوای فشرده طبق استاندارد ISO 8573-1",
                "intro": "استاندارد بین‌المللی ISO 8573-1 کیفیت هوای فشرده را با سه عدد (کلاس ذرات جامد : کلاس رطوبت/نقطه شبنم : کلاس روغن) تعریف می‌کند. برای خطوط اتوماسیون عمومی (جک‌های ISO 15552 و شیرهای 4V/MFH) معمولاً کلاس [7:4:4] یا [6:4:4] و برای شیرهای سروو/ابزار دقیق کلاس [5:4:3] یا بالاتر الزامی است.",
                "tableHeaders": ["کلاس ISO 8573-1", "حداکثر اندازه ذرات جامد", "کاربرد صنعتی پیشنهادی", "تجهیز مورد نیاز در واحد مراقبت"],
                "tableRows": [
                    ("کلاس ۷ (عمومی کارگاهی)", "تا ۴۰ میکرون (40 µm)", "جک‌های پنوماتیک استاندارد، شیرهای برقی 4V / V60 / MFH", "فیلتر رگلاتور استاندارد ۴۰ میکرون (مانند سری JPC AC4010)"),
                    ("کلاس ۶ (اتوماسیون دقیق)", "تا ۵ میکرون (5 µm)", "شیرهای کامپکت VUVG، رگلاتورهای دقیق، جزیره شیرها", "المان فیلتر ۵ میکرون (مانند Norgren Excelon سری BL72/BL74)"),
                    ("کلاس ۱ تا ۳ (هوای بدون روغن)", "۰.۰۱ تا ۱ میکرون", "صنایع غذایی، دارویی، رنگ‌پاشی و ابزار دقیق آزمایشگاهی", "فیلترهای کوالسینگ (Coalescing) چندمرحله‌ای + خشک‌کن تبریدی/جذبی"),
                ],
            },
            {
                "id": "filtration-5-vs-40",
                "eyebrow": "۲. دقت فیلتراسیون",
                "title": "فیلتر ۵ میکرون در برابر ۴۰ میکرون: کدام یک را انتخاب کنیم؟",
                "intro": "انتخاب فیلتر بیش از حد ریز بدون پیش‌فیلتر باعث افت فشار سریع و گرفتگی زودهنگام کارتریج می‌شود. قاعده طلایی طراحی مدار، استفاده از فیلتر ۴۰ میکرون در ورودی کلکتور و فیلتر ۵ میکرون پیش از شیرهای حساس است.",
                "bullets": [
                    ("فیلتر ۴۰ میکرون (40 µm — فیلتراسیون استاندارد):", "مناسب جک‌های چهارمیل SC، جک‌های پروفیلی DNC/DSBC و شیرهای اسپول استاندارد. افت فشار بسیار پایین و عمر طولانی المان برنزی متخلخل دارد."),
                    ("فیلتر ۵ میکرون (5 µm — فیلتراسیون دقیق):", "مناسب شیرهای پایلوتی کامپکت (مانند Festo VUVG)، رگلاتورهای تناسبی (Proportional) و مدارهایی که احتمال ورود غبار ریز اکسید آهن از لوله‌کشی گالوانیزه قدیمی وجود دارد."),
                    ("نکته نگهداری کارتریج:", "در صورت عبور اختلاف فشار از دو طرف فیلتر به بیش از ۰.۷ بار، المان فیلتر باید شست‌وشو (در نوع برنزی متخلخل) یا تعویض شود."),
                ],
            },
            {
                "id": "regulator-sizing",
                "eyebrow": "۳. محاسبه سایز پورت و افت فشار",
                "title": "سایزینگ رگلاتور بر اساس دبی (Flow Rate) و افت فشار مجاز",
                "intro": "انتخاب سایز واحد مراقبت صرفاً بر اساس سایز لوله خط اصلی اشتباه است؛ اگر مجموع مصرف لحظه‌ای جک‌ها از ظرفیت اسمی رگلاتور بیشتر باشد، در لحظه حرکت همزمان جک‌ها فشار خط افت شدید (Pressure Sag) پیدا می‌کند.",
                "tableHeaders": ["سایز پورت (BSPP)", "دبی اسمی پیشنهادی (در ۶ بار با افت ≤ 0.5 bar)", "سری مرجع JPC و Norgren / Festo", "دامنه کاربرد"],
                "tableRows": [
                    ("G1/4 (سری 2000 / MS4)", "۸۰۰ تا ۱,۲۰۰ لیتر بر دقیقه", "Norgren BL72-201G / Festo MS4", "ماشین‌آلات تکی، میزهای مونتاژ، ۲ تا ۳ جک قطر ۲۵ تا ۴۰ میلی‌متر"),
                    ("G3/8 (سری 3000 / MS6)", "۱,۸۰۰ تا ۲,۶۰۰ لیتر بر دقیقه", "Norgren BL73-301G / Festo MS6-3/8", "خطوط بسته‌بندی متوسط، ۴ تا ۸ جک قطر ۴۰ تا ۶۳ میلی‌متر"),
                    ("G1/2 (سری 4000 / MS6)", "۳,۰۰۰ تا ۴,۲۰۰ لیتر بر دقیقه", "JPC-AC4010-04-D / Norgren BL74-401G / Festo MS6-LFR-1/2", "تابلوهای اصلی خط تولید، تغذیه جک‌های Ø80 تا Ø125 و منیفولدهای بزرگ"),
                ],
            },
            {
                "id": "lubricator-and-autodrain",
                "eyebrow": "۴. قواعد روغن‌زن و تخلیه رطوبت",
                "title": "اصول روغن‌کاری (Lubricator) و انتخاب نوع تخلیه کاسه (Drain)",
                "intro": "تمام شیرها و جک‌های مدرن امروزی با گریس کارخانه (Pre-lubricated) آب‌بندی شده‌اند؛ بنابراین تصمیم برای نصب یا حذف روغن‌زن در واحد مراقبت (FRL سه‌تکه در برابر FR دوتکه) حیاتی است.",
                "bullets": [
                    ("چه زمانی از روغن‌زن استفاده کنیم؟", "برای خطوط پرسرعت صنعتی سنگین، ابزارهای بادی (بکس و دریل بادی) و جک‌های کارکرد پیوسته. توجه: اگر خطی یک‌بار با روغن‌زن کار کرد، گریس فابریک قطعات شسته می‌شود و از آن پس روغن‌زن نباید هرگز خالی بماند."),
                    ("چه زمانی روغن‌زن را حذف کنیم؟", "در صنایع غذایی، دارویی، رنگ‌پاشی، سیستم‌های خلأ و شیرهای کامپکت/پایلوت‌دار حساس که در دیتاشیت آن‌ها «Unlubricated Compressed Air» قید شده است (استفاده از واحد دوتکه FR یعنی فیلتر-رگلاتور)."),
                    ("نوع روغن استاندارد:", "تنها از روغن‌های معدنی رقیق ویژه پنوماتیک با ویسکوزیته ISO VG 32 استفاده کنید. هرگز روغن موتور یا روغن هیدرولیک غلیظ داخل کاسه نریزید."),
                    ("تخلیه دستی، نیمه‌اتوماتیک و اتوماتیک (-D):", "در تخلیه اتوماتیک (مانند JPC-AC4010-04-D)، شناور داخلی بدون نیاز به قطع باد و به‌محض جمع شدن آب در کاسه، رطوبت را تخلیه می‌کند که برای مناطقی با رطوبت بالا یا کمپرسورهای فاقد درایر ضروری است."),
                ],
            },
        ],
        "relatedLinks": [
            ("مقایسه فنی واحد مراقبت Festo MS با سری JPC AC4010", "compare/festo-ms-vs-jpc-frl-air-preparation/index.html"),
            ("صفحه تخصصی واحد مراقبت سه‌تکه JPC-AC4010-04-D", "product/jpc-ac4010-04-d/index.html"),
            ("صفحه تخصصی واحد مراقبت Norgren BL72-201GA (G1/4)", "product/norgren-bl72-201ga/index.html"),
            ("صفحه تخصصی واحد مراقبت Norgren BL74-401G (G1/2)", "product/norgren-bl74-401g/index.html"),
            ("کاتالوگ واحدهای مراقبت و آماده‌سازی هوا (FRL)", "products/air-preparation/index.html"),
            ("کاتالوگ رگلاتورهای فشار پنوماتیک", "products/pressure-regulators/index.html"),
            ("راهنمای عیبیابی مدارهای پنوماتیک", "guides/pneumatic-troubleshooting-guide/index.html"),
            ("جدول جامع معادل‌یابی JPC و فستو", "festo-cross-reference.html"),
        ],
        "faqs": [
            (
                "فشار استاندارد تنظیمی روی رگلاتور واحد مراقبت FRL برای اکثر ماشین‌آلات چند بار است؟",
                "فشار کاری بهینه برای اکثر جک‌ها و شیرهای برقی پنوماتیک ۶ بار (0.6 MPa / 87 PSI) است. تنظیم رگلاتور روی فشارهای بالاتر (۸ تا ۱۰ بار) در حالی که مدار به آن نیاز ندارد، تنها مصرف هوای کمپرسور و استهلاک پکینگ‌ها را افزایش می‌دهد."
            ),
            (
                "تفاوت رگلاتور نوع Relieving (تخلیه‌دار) با Non-Relieving در چیست؟",
                "در رگلاتورهای Relieving (که مدل استاندارد واحدهای JPC AC4010 و Norgren BL است)، هنگام کاهش فشار تنظیمی، هوای محبوس‌شده با فشار بالاتر در خط خروجی به‌طور خودکار به اتمسفر تخلیه می‌شود تا فشار مدار بلافاصله پایین بیاید."
            ),
            (
                "آیا واحد مراقبت JPC AC4010-04-D می‌تواند جایگزین Festo MS6-LFR-1/2 شود؟",
                "در کاربری‌های عمومی خطی با پورت G1/2 و فیلتراسیون استاندارد، بله؛ اما پیش از جایگزینی باید دقت فیلتراسیون مورد نیاز (۴۰ در برابر ۵ میکرون) و نحوه نصب براکت دیواری روی تابلو کنترل شود. جزئیات کامل در صفحه مقایسه Festo MS و JPC AC درج شده است."
            ),
        ],
    },
    {
        "slug": "pneumatic-troubleshooting-guide",
        "titleSeo": "مرکز عیبیابی مدارهای پنوماتیک و راهنمای تشخیص و جایگزینی قطعات | JPC",
        "metaDesc": "راهنمای عملی عیبیابی تجهیزات پنوماتیک صنعتی: رفع کندی حرکت و کوبش جک، علت سوختن بوبین شیر برقی و نشتی اگزوز، تشخیص رزوه BSPP/BSPT و شناسایی پلاک قطعات با هوش مصنوعی.",
        "h1Fa": "مرکز عیبیابی مدارهای پنوماتیک و راهنمای تشخیص و جایگزینی قطعات",
        "eyebrowFa": "دانشنامه نگهداری و تعمیرات (PM) و عیبیابی خطوط تولید پنوماتیک",
        "activeSection": "all",
        "tldrFa": "در عیبیابی مدارهای پنوماتیک، علامت خرابی روی یک قطعه (مثلاً کند شدن جک یا نشتی دائمی از اگزوز شیر برقی) اغلب ریشه در قطعه دیگری دارد (مانند خرابی کاسه‌نمد پیستون جک که باد را به اگزوز شیر برقی می‌فرستد، یا گرفتگی سایلنسر برنزی که سرعت جک را نصف می‌کند). پیش از تعویض قطعه، ۴ تست ایزوله‌سازی زیر را انجام دهید و برای قطعات فاقد کد خوانا از دستیار پلاک‌خوان هوشمند JPC استفاده کنید.",
        "sections": [
            {
                "id": "cylinder-faults",
                "eyebrow": "۱. عیبیابی عملگرها",
                "title": "عیبیابی کندی حرکت، حرکت پرشی (Stick-Slip) و ضربه‌گیر جک پنوماتیک",
                "intro": "اگر جک پنوماتیک در مسیر حرکت گیرپاژ می‌کند، سرعت آن کاهش یافته یا در انتهای کورس به کله‌گی می‌کوبد، پیش از باز کردن جک موارد زیر را کنترل کنید:",
                "tableHeaders": ["نشانه خرابی در خط تولید", "علت‌های محتمل مهندسی", "تست سریع تشخیص", "اقدام اصلاحی / قطعه جایگزین"],
                "tableRows": [
                    ("خروج مداوم باد از اگزوز شیر برقی حتی بدون تغییر فرمان", "۱) پارگی یا سایش کاسه‌نمد (پکینگ) پیستون جک و عبور باد از محفظه رفت به برگشت\n۲) خرابی اورینگ‌های اسپول شیر برقی", "شیلنگ خروجی جک را زمانی که تحت فشار است باز کنید؛ اگر از پورت مخالف باد خارج شد، پکینگ جک خراب است.", "تعویض کیت پکینگ یا جایگزینی جک استاندارد ISO 15552 (سری JPC DNC / Festo DSBC)"),
                    ("کوبش شدید پیستون در انتهای کورس", "۱) باز بودن بیش از حد پیچ ضربه‌گیر PPV\n۲) فرسودگی رینگ آب‌بند ضربه‌گیر\n۳) نبود فلوکنترل سرسیلندری", "پیچ سوزنی PPV روی کله‌گی جک را ببندید و نیم دور باز کنید؛ اگر تغییر نکرد رینگ ضربه‌گیر فرسوده است.", "نصب فلوکنترل یک‌طرفه (Meter-out) روی پورت‌های جک یا بررسی سری‌های DNC / DSBC"),
                    ("حرکت پرشی و لرزشی (Stick-Slip) در سرعت پایین", "استفاده از فلوکنترل به‌صورت Meter-in (کنترل ورودی) به جای Meter-out، یا خشکی بیش از حد بدنه و کمبود فشار", "جهت فلش فلوکنترل روی جک را چک کنید؛ باید جریان خروجی از جک خفه شود.", "تغییر فلوکنترل به حالت Meter-out و بررسی سلامت واحد مراقبت FRL"),
                ],
            },
            {
                "id": "valve-faults",
                "eyebrow": "۲. عیبیابی شیرهای برقی",
                "title": "علت سوختن بوبین، عمل نکردن شیر و گرفتگی پورت اگزوز",
                "intro": "شیرهای برقی ۵/۲ و ۳/۲ از نوع پایلوت داخلی (Internal Pilot) برای تغییر وضعیت اسپول به حداقل ۱.۵ بار فشار هوا نیاز دارند.",
                "bullets": [
                    ("سوختن متوالی بوبین 220V AC:", "برخلاف بوبین 24V DC، در بوبین‌های 220V AC اگر اسپول مکانیکی به دلیل وجود رطوبت یا ذرات زنگ‌زدگی داخل بدنه گیر کند و هسته متحرک (Plunger) نتواند تا انتها بالا برود، جریان هجومی سیم‌پیچ بالا مانده و بوبین ظرف چند دقیقه می‌سوزد. راهکار: تمیزکاری/تعویض شیر + نصب فیلتر هوا."),
                    ("عمل نکردن شیر در فشار پایین (< 1.5 bar):", "شیرهای پایلوتی مثل 4V210 و MFH با فشار هوای ورودی تغییر وضعیت می‌دهند. اگر فشار خط در لحظه تحریک افت کند، شیر عمل نمی‌کند. از صحت رگلاتور FRL اطمینان حاصل کنید."),
                    ("کاهش ناگهانی سرعت جک به دلیل گرفتگی سایلنسر:", "ذرات روغن سوخته و گردوغبار کارگاه منافذ سایلنسر برنزی متخلخل (پورت R و S) را مسدود کرده و فشار برگشتی (Back-pressure) ایجاد می‌کنند. سایلنسرها را باز کرده و با سایلنسر نو سری T40 جایگزین کنید."),
                ],
            },
            {
                "id": "thread-identification",
                "eyebrow": "۳. تشخیص سایز رزوه و پورت",
                "title": "جدول سریع تشخیص سایز رزوه‌های پنوماتیک (G / BSPP در برابر R / BSPT و NPT)",
                "intro": "یکی از رایج‌ترین خطاها هنگام سفارش آنلاین یا تلفنی تجهیزات پنوماتیک، اشتباه گرفتن سایز واقعی رزوه با عنوان اینچی آن است (مثلاً رزوه 1/4 اینچ حدود ۱۳.۱ میلی‌متر قطر خارجی دارد، نه ۶.۳۵ میلی‌متر!).",
                "tableHeaders": ["نام اسمی رزوه", "قطر خارجی رزوه نری (OD با کولیس)", "گام رزوه (تعداد دنده در اینچ)", "کاربرد متداول در کاتالوگ JPC"],
                "tableRows": [
                    ("M5", "5.0 mm", "0.8 mm (متریک)", "شیرهای مینیاتوری، جک‌های قلمی Ø12-16 و اتصالات سری QS-M5"),
                    ("G1/8 (1/8\")", "9.7 mm", "28 TPI", "پورت جک Ø32، شیر 3V210 / 4V110 / V60، اگزوز 4V210 و سری QS-1/8"),
                    ("G1/4 (1/4\")", "13.1 mm", "19 TPI", "پورت جک Ø40-50، شیرهای 4V210-08 / MFH-5-1/4 / V61 و سری QS-1/4"),
                    ("G3/8 (3/8\")", "16.6 mm", "19 TPI", "پورت جک Ø63-80، شیرهای 4V310-10 / 4V330C-10 و واحد مراقبت BL73"),
                    ("G1/2 (1/2\")", "20.9 mm", "14 TPI", "پورت جک Ø100-125، شیر 4V410-15 و واحد مراقبت JPC-AC4010-04-D / BL74"),
                ],
            },
            {
                "id": "ai-plate-scanner",
                "eyebrow": "۴. شناسایی هوشمند قطعات قدیمی و مخدوش",
                "title": "استفاده از دستیار هوشمند تشخیص پلاک AI و مرکز مقایسه فنی JPC",
                "intro": "در ماشین‌آلات اروپایی قدیمی (مانند Bosch Rexroth / AVENTICS سری HF03-LG یا سری‌های قدیمی Festo)، ممکن است کد حک‌شده روی بدنه یا لیبل کمرنگ شده باشد. می‌توانید تصویر پلاک قطعه را برای دستیار هوشمند تشخیص پلاک JPC ارسال کنید تا کد دقیق، مشخصات فنی و گزینه‌های جایگزین استخراج شود.",
                "bullets": [
                    ("گام اول — عکسبرداری واضح از پلاک:", "در نور مناسب از کد مدل (مانند DSBC-63-200 یا 0820055051) و شماره سفارش (Part No.) عکس بگیرید و در ai.jpciran.com آپلود کنید."),
                    ("گام دوم — بررسی چک‌لیست جایگزینی در /compare/:", "قبل از خرید قطعه جایگزین، حتماً فایل مقایسه فنی مرتبط (مثلاً تفاوت منیفولد HF03-LG یا شیار سنسور DSBC) را مطالعه کنید."),
                    ("گام سوم — تأیید نهایی با کارشناسان لاله‌زار:", "کد یا عکس پلاک را در واتساپ 09121305167 ارسال کنید تا انطباق ۱۰۰٪ با شاسی و برق دستگاه شما تأیید شود."),
                ],
            },
        ],
        "relatedLinks": [
            ("دستیار هوشمند تشخیص پلاک قطعات پنوماتیک (AI)", "https://ai.jpciran.com"),
            ("مرکز معادل‌یابی و مقایسه فنی تجهیزات پنوماتیک", "compare/index.html"),
            ("مقایسه جک Festo DSBC با استاندارد ISO 15552 (JPC DNC)", "compare/festo-dsbc-vs-iso-15552-cylinders/index.html"),
            ("مقایسه شیر برقی Festo MFH با سری JPC 4V", "compare/festo-mfh-vs-jpc-4v-solenoid-valves/index.html"),
            ("مقایسه شیر کامپکت Festo VUVG با شیرهای منیفولدی", "compare/festo-vuvg-vs-compact-manifold-valves/index.html"),
            ("راهنمای جایگزینی Rexroth / AVENTICS HF03-LG (0820055051)", "compare/rexroth-aventics-hf03-lg-0820055051-replacement/index.html"),
            ("مرکز جامع انتخاب واحد مراقبت هوای فشرده (FRL)", "guides/frl-air-preparation-guide/index.html"),
            ("کاتالوگ صداخفه‌کن و سایلنسر برنزی (سری T40)", "products/silencers-exhaust/index.html"),
        ],
        "faqs": [
            (
                "چرا از پورت اگزوز (R یا S) شیر برقی به‌طور مداوم باد خارج می‌شود؟",
                "دو علت اصلی وجود دارد: ۱) پکینگ پیستون جک پنوماتیک آسیب دیده و هوای پرفشار از یک طرف پیستون به طرف دیگر و از آنجا به اگزوز شیر برقی نشت می‌کند (رایج‌ترین علت). ۲) اورینگ‌های داخلی اسپول شیر برقی بر اثر رطوبت یا نبود فیلتراسیون فرسوده شده‌اند."
            ),
            (
                "چگونه بفهمیم رزوه روی قطعه پنوماتیک G (موازی) است یا R/NPT (مخروطی)؟",
                "در رزوه موازی BSPP (سری G)، قطر رزوه در ابتدا و انتها یکسان است و آب‌بندی توسط واشر یا اورینگ زیر گلویی اتصالات انجام می‌شود. در رزوه‌های مخروطی BSPT (سری R) و NPT، قطر رزوه به سمت سر پیچ باریک‌تر می‌شود و آب‌بندی با نوار تفلون یا چسب رزوه انجام می‌گیرد."
            ),
            (
                "اگر کد فنی روی پلاک شیر یا جک مخدوش باشد چگونه قطعه جایگزین را پیدا کنیم؟",
                "کافی است عکس واضح از قطعه و پلاک آن را در دستیار هوشمند تشخیص پلاک JPC (ai.jpciran.com) بارگذاری کنید یا به واتساپ فنی 09121305167 بفرستید تا با اندازه‌گیری قطر شفت، فاصله پیچ‌ها و سایز پورت، کد دقیق یا معادل آن مشخص شود."
            ),
        ],
    },
]


def _render_section_block(sec: dict) -> str:
    table_html = ""
    if sec.get("tableHeaders") and sec.get("tableRows"):
        ths = "\n".join(f'                <th scope="col">{esc(h)}</th>' for h in sec["tableHeaders"])
        trs = []
        for row in sec["tableRows"]:
            tds = "\n".join(f'                  <td>{esc(cell)}</td>' for cell in row)
            trs.append(f"                <tr>\n{tds}\n                </tr>")
        tbody = "\n".join(trs)
        table_html = f"""
          <div class="table-responsive" style="margin-top: 1rem;">
            <table class="tech-comparison-table" aria-label="{esc(sec['title'])}">
              <thead>
                <tr>
{ths}
                </tr>
              </thead>
              <tbody>
{tbody}
              </tbody>
            </table>
          </div>"""

    bullets_html = ""
    if sec.get("bullets"):
        b_items = "\n".join(
            f"""            <li style="background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 10px; padding: 0.9rem 1.05rem;">
              <strong style="color: #10243A; font-size: 0.92rem; display: block; margin-bottom: 0.3rem;">{esc(title)}</strong>
              <span style="color: #475569; font-size: 0.86rem; line-height: 1.85;">{esc(desc)}</span>
            </li>"""
            for title, desc in sec["bullets"]
        )
        bullets_html = f"""
          <ul style="list-style: none; padding: 0; margin: 1rem 0 0; display: grid; gap: 0.75rem;">
{b_items}
          </ul>"""

    return f"""
    <section class="section" id="{esc(sec['id'])}" style="padding: 1.1rem 0;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.2rem, 3vw, 1.85rem);">
          <span class="section-eyebrow">{esc(sec['eyebrow'])}</span>
          <h2 style="font-size: 1.2rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 0.75rem;">
            {esc(sec['title'])}
          </h2>
          <p style="font-size: 0.9rem; color: #334155; line-height: 1.9; margin: 0;">
            {esc(sec['intro'])}
          </p>{table_html}{bullets_html}
        </div>
      </div>
    </section>"""


def render_guide_page(spec: dict) -> str:
    """
    Generate `/guides/<slug>/index.html` (`depth=2`, `base_prefix="../../"`).
    Includes TechArticle + FAQPage + BreadcrumbList JSON-LD (zero fabricated prices/offers).
    """
    base_prefix = "../../"
    slug = spec["slug"]
    canonical_url = f"{SITE_DOMAIN}/guides/{slug}/"

    breadcrumbs = [
        ("صفحه اصلی", f"{SITE_DOMAIN}/"),
        ("مقالات و راهنماهای تخصصی", f"{SITE_DOMAIN}/what-is-pneumatics-jpc.html"),
        (spec["h1Fa"], canonical_url),
    ]

    tech_article_ld = {
        "@type": "TechArticle",
        "@id": f"{canonical_url}#article",
        "headline": spec["h1Fa"],
        "description": spec["metaDesc"],
        "inLanguage": "fa-IR",
        "mainEntityOfPage": {"@id": f"{canonical_url}#webpage"},
        "author": {"@id": f"{SITE_DOMAIN}/#organization"},
        "publisher": {"@id": f"{SITE_DOMAIN}/#organization"},
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

    sections_html = "\n".join(_render_section_block(sec) for sec in spec["sections"])

    related_links_html = "\n".join(
        f"""            <a href="{esc(href) if href.startswith('http') else base_prefix + esc(href)}" {'target="_blank" rel="noopener noreferrer"' if href.startswith('http') else ''} style="display: flex; justify-content: space-between; align-items: center; padding: 0.65rem 0.9rem; background: #F8FAFC; border: 1px solid #E1E7EE; border-radius: 8px; text-decoration: none; color: #10243A; font-size: 0.84rem; font-weight: 700;">
              <span>{esc(label)}</span>
              <span style="color: #087F8C;">←</span>
            </a>"""
        for label, href in spec["relatedLinks"]
    )

    faqs_html = "\n".join(
        f"""        <details class="faq-item" {'open' if idx == 0 else ''} style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 10px; padding: 1rem 1.15rem; margin-bottom: 0.75rem;">
          <summary style="font-weight: 800; color: #10243A; cursor: pointer; font-size: 0.94rem;">{esc(q)}</summary>
          <p style="margin-top: 0.65rem; font-size: 0.87rem; color: #475569; line-height: 1.85;">{esc(a)}</p>
        </details>"""
        for idx, (q, a) in enumerate(spec["faqs"])
    )

    main_html = f"""
    <nav aria-label="مسیر راهنما (Breadcrumb)" style="background: #F1F5F9; border-bottom: 1px solid #E1E7EE; padding: 0.75rem 0; font-size: 0.82rem;">
      <div class="container" style="display: flex; flex-wrap: wrap; align-items: center; gap: 0.45rem; color: #475569;">
        <a href="{base_prefix}index.html" style="color: #087F8C; font-weight: 700;">صفحه اصلی</a>
        <span aria-hidden="true">←</span>
        <a href="{base_prefix}what-is-pneumatics-jpc.html" style="color: #087F8C; font-weight: 700;">مقالات و راهنماهای تخصصی</a>
        <span aria-hidden="true">←</span>
        <strong style="color: #10243A;">{esc(spec['h1Fa'])}</strong>
      </div>
    </nav>

    <section class="section" style="background: linear-gradient(135deg, #10243A 0%, #19344F 100%); color: #FFFFFF; padding: 2.35rem 0;">
      <div class="container">
        <span style="display: inline-block; background: rgba(8,127,140,0.3); color: #38BDF8; font-size: 0.78rem; font-weight: 800; padding: 0.3rem 0.75rem; border-radius: 999px; margin-bottom: 0.75rem;">
          {esc(spec['eyebrowFa'])}
        </span>
        <h1 style="font-size: clamp(1.38rem, 3.2vw, 2.02rem); font-weight: 900; color: #FFFFFF; line-height: 1.45; margin-bottom: 0.85rem;">
          {esc(spec['h1Fa'])}
        </h1>
        <p style="font-size: 0.92rem; color: #CBD5E1; max-width: 880px; line-height: 1.85; margin-bottom: 1.15rem;">
          تدوین‌شده توسط واحد مهندسی فروش شرکت جلالی پنوماتیک (<strong dir="ltr" class="mono">JPC</strong>) — لاله‌زار جنوبی تهران.
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 0.6rem;">
          <a href="https://ai.jpciran.com" target="_blank" rel="noopener noreferrer" class="btn btn-ai-scan btn-sm">✦ دستیار هوشمند تشخیص پلاک (AI)</a>
          <a href="{base_prefix}compare/index.html" class="btn btn-amber btn-sm">مرکز معادل‌یابی و مقایسه فنی ←</a>
          <a href="{base_prefix}products/index.html" class="btn btn-outline-light btn-sm">بانک ۵۰۰ کد فنی کاتالوگ</a>
        </div>
      </div>
    </section>

    <!-- QUICK ENGINEERING SUMMARY (TL;DR BOX) -->
    <section class="section" style="padding: 1.5rem 0 0.5rem;">
      <div class="container">
        <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-right: 4px solid #087F8C; border-radius: 12px; padding: 1.25rem 1.4rem;">
          <span style="font-size: 0.78rem; font-weight: 800; color: #087F8C; display: block; margin-bottom: 0.35rem;">خلاصه مهندسی (Quick Engineering Answer)</span>
          <p style="font-size: 0.9rem; color: #1E293B; line-height: 1.9; margin: 0;">
            {esc(spec['tldrFa'])}
          </p>
        </div>
      </div>
    </section>

{sections_html}

    <!-- RELATED LINKS & CLUSTER NAVIGATION -->
    <section class="section" style="padding: 1.25rem 0;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.2rem, 3vw, 1.8rem);">
          <span class="section-eyebrow">دسترسی به محصولات، سری‌ها و راهنماهای مرتبط</span>
          <h2 style="font-size: 1.12rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 0.95rem;">
            مسیرهای تخصصی مرتبط در کاتالوگ جلالی پنوماتیک
          </h2>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 0.65rem;">
{related_links_html}
          </div>
        </div>
      </div>
    </section>

    <!-- TECHNICAL FAQ -->
    <section class="section" style="padding: 1rem 0 2.5rem;">
      <div class="container">
        <div style="background: #FFFFFF; border: 1px solid #E1E7EE; border-radius: 14px; padding: clamp(1.2rem, 3vw, 1.8rem);">
          <span class="section-eyebrow">پرسش و پاسخ مهندسی (Technical Q&amp;A)</span>
          <h2 style="font-size: 1.15rem; font-weight: 800; color: #10243A; margin: 0.25rem 0 1rem;">
            سؤالات پرتکرار مهندسان درباره {esc(spec['h1Fa'])}
          </h2>
{faqs_html}
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
