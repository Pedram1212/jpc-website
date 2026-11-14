/**
 * Jalali Pneumatic Company (JPC) - Site Configuration
 * شرکت جلالی پنوماتیک - تنظیمات پایه وب‌سایت و درگاه‌های ارتباطی
 */
const SITE_CONFIG = {
  company: {
    nameFa: "شرکت جلالی پنوماتیک",
    shortNameFa: "جلالی پنوماتیک",
    nameEn: "Jalali Pneumatic Company",
    brandCode: "JPC",
    taglineFa: "واردکننده، تأمین‌کننده و توزیع‌کننده تجهیزات پنوماتیک صنعتی و اتوماسیون هوای فشرده",
    descriptionFa:
      "تأمین تخصصی شیرهای برقی، جک‌های پنوماتیک، واحدهای مراقبت هوا و اتصالات صنعتی از برندهای معتبر اروپایی (Festo, Norgren, Bosch Rexroth)، خطوط تأمین منتخب آسیایی و برند اختصاصی JPC.",
    workingHoursFa: "شنبه تا چهارشنبه: ۹:۰۰ الی ۱۷:۳۰ | پنج‌شنبه: ۹:۰۰ الی ۱۳:۳۰",
    locationFa: "تهران، قطب صنعتی و تجاری تجهیزات اتوماسیون و پنوماتیک"
  },

  contact: {
    // شماره واتساپ جهت استعلام سریع (قابل تغییر به شماره رسمی مجموعه)
    whatsappNumber: "989120000000",
    whatsappBaseUrl: "https://wa.me/989120000000",
    phoneDisplay: "۰۲۱-۳۳۹۰۰۰۰۰",
    phoneTel: "+982133900000",
    salesMobileDisplay: "۰۹۱۲-۰۰۰-۰۰۰۰",
    email: "info@jalalipneumatic.ir",
    salesEmail: "sales@jalalipneumatic.ir"
  },

  endpoints: {
    // آدرس وب‌هوک یا API دریافت فرم استعلام قیمت و سفارش عمده B2B
    inquirySubmitUrl: "https://api.jalalipneumatic.ir/v1/b2b-inquiry",
    // در صورت عدم اتصال بک‌اند، حالت شبیه‌سازی و ارسال مستقیم به واتساپ/ایمیل فعال است
    enableMockSubmission: true,
    maxUploadSizeMB: 15,
    allowedFileTypes: [".pdf"]
  },

  catalogs: {
    jpcGeneralCatalogPdf: "assets/docs/jpc-general-catalog.pdf",
    valvesCatalogPdf: "assets/docs/jpc-solenoid-valves-datasheet.pdf",
    cylindersCatalogPdf: "assets/docs/jpc-pneumatic-cylinders-datasheet.pdf",
    frlAccessoriesCatalogPdf: "assets/docs/jpc-frl-accessories-datasheet.pdf"
  },

  brands: [
    {
      id: "JPC",
      nameEn: "JPC",
      nameFa: "جی‌پی‌سی (برند اختصاصی)",
      originFa: "برند تجاری اختصاصی جلالی پنوماتیک",
      tierFa: "تأمین مستقیم با کنترل کیفی دقیق و ارزش خرید بالا"
    },
    {
      id: "Festo",
      nameEn: "Festo",
      nameFa: "فستو (Festo)",
      originFa: "مهندسی آلمان / اروپا",
      tierFa: "سیستم‌های اتوماسیون و پنوماتیک دقیق صنعتی"
    },
    {
      id: "Norgren",
      nameEn: "Norgren",
      nameFa: "نورگرن (Norgren)",
      originFa: "مهندسی بریتانیا / اروپا",
      tierFa: "تجهیزات کنترل سیالات و مراقبت هوای فشرده سنگین"
    },
    {
      id: "Bosch Rexroth",
      nameEn: "Bosch Rexroth",
      nameFa: "بوش و بوش رکسروت (Bosch Rexroth)",
      originFa: "مهندسی آلمان / اروپا",
      tierFa: "شیرآلات و عملگرهای صنعتی خطوط تولید پیوسته"
    }
  ]
};

window.SITE_CONFIG = SITE_CONFIG;
