/**
 * Jalali Pneumatic Company (JPC) - Site Configuration & B2B E-E-A-T Signals
 * شرکت جلالی پنوماتیک (JPC) با مدیریت امیر جلالی - تنظیمات پایه وب‌سایت، اطلاعات تماس و سیگنال‌های مکانی و تجاری
 */
const SITE_CONFIG = {
  // دسترسی مستقیم در سطح اول جهت سازگاری با اسکریپت‌ها و کامپوننت‌های استعلام
  whatsappNumber: "989121305167",
  phoneInternational: "00989121305167",
  phoneE164: "+989121305167",
  phoneDisplayLtr: "0912 130 5167",
  phoneIntlDisplayLtr: "0098 912 130 5167",
  telegramUsername: "JalaliPneumatic_Sales",
  landlinePhone: "021-33900000",
  founderFa: "امیر جلالی",
  founderEn: "Amir Jalali",
  ownershipTitleFa: "شرکت جلالی پنوماتیک (JPC) — با مدیریت امیر جلالی",
  addressFa: "تهران، محدوده بازار صنعتی / لالهزار (تأمین و ارسال به سراسر کشور)",
  workingHoursFa: "شنبه تا چهارشنبه: ۸:۳۰ الی ۱۷:۳۰ | پنجشنبه: ۸:۳۰ الی ۱۳:۳۰",

  company: {
    nameFa: "شرکت جلالی پنوماتیک",
    fullTitleFa: "شرکت جلالی پنوماتیک (JPC) — با مدیریت امیر جلالی",
    shortNameFa: "جلالی پنوماتیک",
    nameEn: "Jalali Pneumatic Company",
    brandCode: "JPC",
    founderFa: "امیر جلالی",
    founderEn: "Amir Jalali",
    domains: ["jpciran.com", "jalalipneumatic.ir"],
    taglineFa: "واردکننده، تأمین‌کننده و توزیع‌کننده تجهیزات پنوماتیک صنعتی و اتوماسیون هوای فشرده (با مدیریت امیر جلالی)",
    descriptionFa:
      "شرکت جلالی پنوماتیک (JPC) با مدیریت امیر جلالی؛ تأمین تخصصی شیرهای برقی، جک‌های پنوماتیک، واحدهای مراقبت هوا و اتصالات صنعتی از برندهای معتبر اروپایی (Festo, Norgren, Bosch Rexroth)، خطوط تأمین منتخب آسیایی و برند اختصاصی JPC.",
    addressFa: "تهران، محدوده بازار صنعتی / لالهزار (تأمین و ارسال به سراسر کشور)",
    addressEn: "Tehran Industrial & Commercial Automation District (Lalehzar), Tehran, Iran",
    workingHoursFa: "شنبه تا چهارشنبه: ۸:۳۰ الی ۱۷:۳۰ | پنجشنبه: ۸:۳۰ الی ۱۳:۳۰",
    workingHoursIso: "Sa-We 08:30-17:30, Th 08:30-13:30",
    locationFa: "تهران، محدوده بازار صنعتی / لالهزار (تأمین و ارسال به سراسر کشور)"
  },

  contact: {
    whatsappNumber: "989121305167",
    whatsappBaseUrl: "https://wa.me/989121305167",
    telegramUsername: "JalaliPneumatic_Sales",
    telegramBaseUrl: "https://t.me/JalaliPneumatic_Sales",
    landlinePhone: "021-33900000",
    phoneDisplay: "0912 130 5167",
    phoneIntlDisplay: "0098 912 130 5167",
    phoneDisplayFa: "۰۹۱۲ ۱۳۰ ۵۱۶۷",
    phoneTel: "+989121305167",
    landlineTel: "+982133900000",
    salesMobileDisplay: "0912 130 5167",
    salesMobileDisplayFa: "۰۹۱۲ ۱۳۰ ۵۱۶۷",
    salesMobileRaw: "00989121305167",
    email: "info@jalalipneumatic.ir",
    salesEmail: "sales@jalalipneumatic.ir",
    addressFa: "تهران، محدوده بازار صنعتی / لالهزار (تأمین و ارسال به سراسر کشور)",
    workingHoursFa: "شنبه تا چهارشنبه: ۸:۳۰ الی ۱۷:۳۰ | پنجشنبه: ۸:۳۰ الی ۱۳:۳۰"
  },

  endpoints: {
    inquirySubmitUrl: "https://api.jalalipneumatic.ir/v1/b2b-inquiry",
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

  pages: {
    home: "index.html",
    valves: "solenoid-valves.html",
    cylinders: "pneumatic-cylinders.html",
    frlAccessories: "frl-accessories.html"
  },

  brands: [
    {
      id: "JPC",
      nameEn: "JPC",
      nameFa: "جی‌پی‌سی (برند اختصاصی)",
      originFa: "برند تجاری اختصاصی شرکت جلالی پنوماتیک (با مدیریت امیر جلالی)",
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
