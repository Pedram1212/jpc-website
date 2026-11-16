/**
 * Jalali Pneumatic Company (JPC) - Interactive B2B Application Engine
 * شامل:
 * ۱. سبد استعلام قیمت چندقلمی (Multi-Item RFQ Drawer) با ذخیره‌سازی محلی
 * ۲. سیستم معادل‌یابی فنی برند JPC (Technical Cross-Reference)
 * ۳. ماشین‌حساب مهندسی محاسبه نیروی جک پنوماتیک (Cylinder Force Calculator)
 * ۴. نرمال‌ساز هوشمند جستجوی فارسی/انگلیسی و کپی تک‌کلیکی کدهای فنی
 */

(function () {
  "use strict";

  const initialCategory =
    document.body.getAttribute("data-page-category") || "all";

  // Application State
  const state = {
    category: initialCategory,
    brand: "all",
    searchQuery: "",
    selectedProduct: null,
    theme: localStorage.getItem("jpc_theme") || "light",
    rfqItems: loadRfqFromStorage(),
    rfqCustomerNote: localStorage.getItem("jpc_rfq_note") || "",
    calc: {
      bore: 63,
      rod: 20,
      pressure: 6
    }
  };

  // Standard ISO Rod Diameter Map (Bore mm -> Standard Rod mm)
  const STANDARD_ROD_MAP = {
    12: 6,
    16: 6,
    20: 8,
    25: 10,
    32: 12,
    40: 16,
    50: 20,
    63: 20,
    80: 25,
    100: 25,
    125: 32,
    160: 40,
    200: 40
  };

  function loadRfqFromStorage() {
    try {
      const raw = localStorage.getItem("jpc_rfq_items");
      if (!raw) return [];
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) {
      return [];
    }
  }

  function saveRfqToStorage() {
    try {
      localStorage.setItem("jpc_rfq_items", JSON.stringify(state.rfqItems));
      localStorage.setItem("jpc_rfq_note", state.rfqCustomerNote || "");
    } catch (e) {
      // ignore storage errors
    }
  }

  function syncOverlayOpenState() {
    const anyModalOpen = Array.from(
      document.querySelectorAll(".modal-backdrop")
    ).some((el) => el.classList.contains("open"));
    const rfqDrawer = document.getElementById("rfq-drawer");
    const mobileDrawer = document.getElementById("mobile-drawer");
    const anyDrawerOpen =
      (rfqDrawer && rfqDrawer.classList.contains("open")) ||
      (mobileDrawer && mobileDrawer.classList.contains("open"));
    document.body.classList.toggle(
      "overlay-open",
      Boolean(anyModalOpen || anyDrawerOpen)
    );
  }

  /**
   * Smart Persian/Arabic/English Text & Digit Normalizer
   */
  function normalizeSearchText(input) {
    if (!input) return "";
    const persianDigits = "۰۱۲۳۴۵۶۷۸۹";
    const arabicDigits = "٠١٢٣٤٥٦٧٨٩";

    let out = String(input);

    for (let i = 0; i < 10; i++) {
      out = out.replace(new RegExp(persianDigits[i], "g"), String(i));
      out = out.replace(new RegExp(arabicDigits[i], "g"), String(i));
    }

    out = out
      .replace(/ي/g, "ی")
      .replace(/ى/g, "ی")
      .replace(/ك/g, "ک")
      .replace(/ة/g, "ه")
      .replace(/ؤ/g, "و")
      .replace(/[إأآ]/g, "ا")
      .replace(/\u200c/g, " ") // convert ZWNJ to space
      .toLowerCase();

    return out.replace(/\s+/g, " ").trim();
  }

  function normalizeCompact(input) {
    return normalizeSearchText(input).replace(/[\s\-_/."']+/g, "");
  }

  /**
   * Show Toast Feedback ("کپی شد")
   */
  let toastTimer = null;
  function showToast(message) {
    let toast = document.getElementById("jpc-copy-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "jpc-copy-toast";
      toast.className = "copy-toast";
      document.body.appendChild(toast);
    }
    toast.innerHTML = `
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2.5">
        <polyline points="20 6 9 17 4 12"></polyline>
      </svg>
      <span>${message}</span>
    `;
    toast.classList.add("show");
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.remove("show");
    }, 2400);
  }

  /**
   * Copy text to clipboard with button state feedback
   */
  function copyTextToClipboard(text, buttonEl) {
    if (!text) return;
    const done = () => {
      showToast(`کپی شد: ${text}`);
      if (buttonEl) {
        const originalHtml = buttonEl.getAttribute("data-orig-html") || buttonEl.innerHTML;
        if (!buttonEl.getAttribute("data-orig-html")) {
          buttonEl.setAttribute("data-orig-html", originalHtml);
        }
        buttonEl.classList.add("copied");
        buttonEl.innerHTML = `<span>کپی شد ✓</span>`;
        setTimeout(() => {
          buttonEl.classList.remove("copied");
          buttonEl.innerHTML = originalHtml;
        }, 1600);
      }
    };

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done).catch(() => {
        fallbackCopy(text);
        done();
      });
    } else {
      fallbackCopy(text);
      done();
    }
  }

  function fallbackCopy(text) {
    const ta = document.createElement("textarea");
    ta.value = text;
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
    } catch (e) {}
    document.body.removeChild(ta);
  }

  /**
   * Generate clean ISO-inspired SVG Pneumatic Schematics for each component type
   */
  function getSchematicSvg(schematicType) {
    switch (schematicType) {
      case "valve-5-2":
      case "valve-5-2-double":
      case "valve-5-3":
        return `
          <svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
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
          </svg>`;

      case "valve-3-2":
        return `
          <svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="24" y="14" width="36" height="36" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="60" y="14" width="36" height="36" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="10" y="22" width="14" height="20" rx="1" stroke="#F59E0B" stroke-width="2"/>
            <line x1="12" y1="38" x2="21" y2="26" stroke="#F59E0B" stroke-width="1.8"/>
            <line x1="42" y1="50" x2="42" y2="14" stroke="currentColor" stroke-width="1.8"/>
            <polygon points="42,14 39,20 45,20" fill="currentColor"/>
            <line x1="74" y1="38" x2="82" y2="38" stroke="#F59E0B" stroke-width="2"/>
            <line x1="78" y1="38" x2="78" y2="50" stroke="#F59E0B" stroke-width="2"/>
            <path d="M96 28L102 22L106 34L110 22L114 28" stroke="currentColor" stroke-width="1.8"/>
          </svg>`;

      case "cylinder-double":
      case "cylinder-tierod":
        return `
          <svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="14" y="14" width="72" height="36" rx="3" stroke="currentColor" stroke-width="2"/>
            <line x1="46" y1="14" x2="46" y2="50" stroke="#F59E0B" stroke-width="3"/>
            <line x1="46" y1="32" x2="112" y2="32" stroke="currentColor" stroke-width="4"/>
            <rect x="108" y="25" width="6" height="14" rx="1" fill="#F59E0B"/>
            <line x1="22" y1="14" x2="22" y2="6" stroke="currentColor" stroke-width="2"/>
            <line x1="78" y1="14" x2="78" y2="6" stroke="currentColor" stroke-width="2"/>
            <line x1="14" y1="20" x2="86" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
            <line x1="14" y1="44" x2="86" y2="44" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
          </svg>`;

      case "cylinder-compact":
      case "cylinder-mini":
        return `
          <svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="24" y="12" width="52" height="40" rx="3" stroke="currentColor" stroke-width="2"/>
            <line x1="50" y1="12" x2="50" y2="52" stroke="#F59E0B" stroke-width="3"/>
            <line x1="50" y1="32" x2="104" y2="32" stroke="currentColor" stroke-width="4.5"/>
            <circle cx="34" cy="22" r="2.5" fill="currentColor"/>
            <circle cx="66" cy="22" r="2.5" fill="currentColor"/>
            <circle cx="34" cy="42" r="2.5" fill="currentColor"/>
            <circle cx="66" cy="42" r="2.5" fill="currentColor"/>
          </svg>`;

      case "cylinder-rodless":
        return `
          <svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="10" y="24" width="100" height="22" rx="2" stroke="currentColor" stroke-width="2"/>
            <rect x="44" y="12" width="32" height="12" rx="2" stroke="#F59E0B" stroke-width="2"/>
            <line x1="60" y1="24" x2="60" y2="46" stroke="#F59E0B" stroke-width="2.5"/>
            <line x1="18" y1="35" x2="102" y2="35" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
          </svg>`;

      case "frl-unit":
      default:
        return `
          <svg viewBox="0 0 120 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <rect x="18" y="12" width="26" height="40" rx="2" stroke="currentColor" stroke-width="2"/>
            <line x1="31" y1="12" x2="31" y2="52" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3 3"/>
            <circle cx="60" cy="32" r="14" stroke="#F59E0B" stroke-width="2"/>
            <line x1="60" y1="32" x2="67" y2="24" stroke="#F59E0B" stroke-width="2" stroke-linecap="round"/>
            <rect x="76" y="12" width="26" height="40" rx="2" stroke="currentColor" stroke-width="2"/>
            <line x1="8" y1="32" x2="18" y2="32" stroke="currentColor" stroke-width="2"/>
            <line x1="44" y1="32" x2="46" y2="32" stroke="currentColor" stroke-width="2"/>
            <line x1="74" y1="32" x2="76" y2="32" stroke="currentColor" stroke-width="2"/>
            <line x1="102" y1="32" x2="112" y2="32" stroke="currentColor" stroke-width="2"/>
          </svg>`;
    }
  }

  /**
   * Build WhatsApp URL using SITE_CONFIG.whatsappNumber
   */
  function buildWhatsAppUrl(product, customText) {
    const waNumber =
      (window.SITE_CONFIG &&
        (window.SITE_CONFIG.whatsappNumber ||
          (window.SITE_CONFIG.contact &&
            window.SITE_CONFIG.contact.whatsappNumber))) ||
      "989121305167";
    const base = `https://wa.me/${waNumber}`;

    let message = "";
    if (customText) {
      message = customText;
    } else if (product) {
      message =
        `سلام، جهت استعلام قیمت و موجودی تجهیز زیر از وب‌سایت شرکت جلالی پنوماتیک (JPC) پیام می‌دهم:\n` +
        `• نام محصول: ${product.nameFa}\n` +
        `• کد فنی: ${product.code}\n` +
        `• برند: ${product.brand}`;
    } else if (state.rfqItems.length > 0) {
      message = formatRfqWhatsAppMessage();
    } else {
      message =
        "سلام، جهت استعلام قیمت تجهیزات پنوماتیک و دریافت مشاوره فنی از وب‌سایت شرکت جلالی پنوماتیک (JPC) پیام می‌دهم.";
    }
    return `${base}?text=${encodeURIComponent(message)}`;
  }

  /**
   * Build Telegram URL using SITE_CONFIG.telegramUsername
   */
  function buildTelegramUrl(customText) {
    const tgUser =
      (window.SITE_CONFIG &&
        (window.SITE_CONFIG.telegramUsername ||
          (window.SITE_CONFIG.contact &&
            window.SITE_CONFIG.contact.telegramUsername))) ||
      "JalaliPneumatic_Sales";
    if (!customText) {
      return `https://t.me/${tgUser}`;
    }
    return `https://t.me/${tgUser}?text=${encodeURIComponent(customText)}`;
  }

  /**
   * Multi-Item RFQ List Management
   */
  function isProductInRfq(productId) {
    return state.rfqItems.some((item) => item.id === productId);
  }

  function addToRfqList(product, customNote) {
    if (!product) return;
    const existing = state.rfqItems.find((item) => item.id === product.id);
    if (existing) {
      existing.qty += 1;
      if (customNote) existing.note = customNote;
    } else {
      state.rfqItems.push({
        id: product.id,
        code: product.code,
        nameFa: product.nameFa,
        brand: product.brand,
        brandFa: product.brandFa,
        portSize: product.portSize,
        qty: 1,
        note: customNote || ""
      });
    }
    saveRfqToStorage();
    renderRfqUI();
    renderCatalog();
    showToast(`به لیست استعلام اضافه شد: ${product.code}`);
  }

  function updateRfqItemQty(productId, newQty) {
    const qty = Math.max(1, parseInt(newQty, 10) || 1);
    const item = state.rfqItems.find((i) => i.id === productId);
    if (item) {
      item.qty = qty;
      saveRfqToStorage();
      renderRfqUI();
    }
  }

  function removeRfqItem(productId) {
    state.rfqItems = state.rfqItems.filter((i) => i.id !== productId);
    saveRfqToStorage();
    renderRfqUI();
    renderCatalog();
  }

  function clearRfqList() {
    state.rfqItems = [];
    state.rfqCustomerNote = "";
    saveRfqToStorage();
    renderRfqUI();
    renderCatalog();
    showToast("لیست استعلام پاک شد");
  }

  function formatRfqWhatsAppMessage() {
    if (state.rfqItems.length === 0) {
      return "سلام، جهت استعلام قیمت تجهیزات پنوماتیک از وب‌سایت شرکت جلالی پنوماتیک (JPC) پیام می‌دهم.";
    }
    const lines = state.rfqItems.map(
      (item, idx) =>
        `${idx + 1}. [${item.code}] — ${item.nameFa} | برند: ${item.brand} | تعداد: ${item.qty} عدد${
          item.note ? ` (${item.note})` : ""
        }`
    );
    const noteSection =
      state.rfqCustomerNote && state.rfqCustomerNote.trim()
        ? `\n\nتوضیحات تکمیلی خریدار:\n${state.rfqCustomerNote.trim()}`
        : "";
    return (
      `سلام، درخواست استعلام قیمت لیست اقلام زیر (BOM) را از وب‌سایت شرکت جلالی پنوماتیک (JPC) دارم:\n\n` +
      lines.join("\n") +
      noteSection +
      `\n\nلطفاً موجودی و پیش‌فاکتور را اعلام فرمایید.`
    );
  }

  function formatRfqForFormText() {
    const itemsText = state.rfqItems
      .map(
        (item, idx) =>
          `${idx + 1}) کد فنی: ${item.code} | شرح: ${item.nameFa} | برند: ${item.brand} | تعداد: ${item.qty} عدد${
            item.note ? ` | توضیح: ${item.note}` : ""
          }`
      )
      .join("\n");
    if (state.rfqCustomerNote && state.rfqCustomerNote.trim()) {
      return `${itemsText}\n\nتوضیحات تکمیلی: ${state.rfqCustomerNote.trim()}`;
    }
    return itemsText;
  }

  function updateRfqActionLinks() {
    const waSendBtn = document.getElementById("rfq-send-whatsapp-btn");
    const tgSendBtn = document.getElementById("rfq-send-telegram-btn");
    if (waSendBtn) {
      waSendBtn.href = buildWhatsAppUrl(null, formatRfqWhatsAppMessage());
    }
    if (tgSendBtn) {
      tgSendBtn.href = buildTelegramUrl(formatRfqWhatsAppMessage());
    }
  }

  function renderRfqUI() {
    const totalItems = state.rfqItems.reduce((acc, i) => acc + i.qty, 0);
    const uniqueCount = state.rfqItems.length;

    // Update header & floating badges
    document.querySelectorAll(".js-rfq-count").forEach((el) => {
      el.textContent = String(uniqueCount);
    });

    const drawerBody = document.getElementById("rfq-drawer-body");
    const formPopulateBtn = document.getElementById("rfq-populate-form-btn");
    const clearBtn = document.getElementById("rfq-clear-btn");

    updateRfqActionLinks();

    if (!drawerBody) return;

    if (state.rfqItems.length === 0) {
      drawerBody.innerHTML = `
        <div style="text-align: center; padding: 2.5rem 1rem; color: var(--text-muted);">
          <div style="font-size: 1rem; font-weight: 800; color: var(--text-primary); margin-bottom: 0.5rem;">
            لیست استعلام چندقلمی شما خالی است
          </div>
          <p style="font-size: 0.85rem; line-height: 1.7;">
            برای استعلام همزمان چند قطعه (BOM پروژه)، روی دکمه <strong>«+ افزودن به لیست استعلام»</strong> در کارت محصولات کلیک کنید.
          </p>
        </div>
      `;
      if (formPopulateBtn) formPopulateBtn.disabled = true;
      if (clearBtn) clearBtn.style.display = "none";
      updateFloatingWhatsApp(state.selectedProduct);
      return;
    }

    if (formPopulateBtn) formPopulateBtn.disabled = false;
    if (clearBtn) clearBtn.style.display = "inline-flex";

    drawerBody.innerHTML = `
      <div style="display:flex; align-items:center; justify-content:space-between; font-size:0.8rem; color:var(--text-muted); padding-bottom:0.4rem; border-bottom:1px solid var(--border-tech);">
        <span>اقلام انتخاب‌شده: <strong>${uniqueCount} ردیف کالا</strong></span>
        <span>مجموع تعداد: <strong>${totalItems} عدد</strong></span>
      </div>
      ${state.rfqItems
        .map(
          (item) => `
        <div class="rfq-item-card" data-rfq-id="${item.id}">
          <div class="rfq-item-top">
            <div>
              <span class="mono" style="font-size:0.76rem; font-weight:800; color:var(--steel-accent);">${item.code}</span>
              <div class="rfq-item-title">${item.nameFa}</div>
              ${
                item.note
                  ? `<div style="font-size:0.74rem; color:var(--amber-hover); margin-top:0.15rem;">مشخصه انتخابی: ${item.note}</div>`
                  : ""
              }
            </div>
            <button type="button" class="rfq-item-remove js-rfq-remove" data-id="${item.id}" aria-label="حذف از لیست">
              حذف ✕
            </button>
          </div>
          <div class="rfq-item-bottom">
            <span class="brand-badge ${item.brand === "JPC" ? "badge-jpc" : "badge-euro"}" style="font-size:0.7rem;">
              ${item.brand}
            </span>
            <div style="display:flex; align-items:center; gap:0.45rem;">
              <span style="font-size:0.76rem; color:var(--text-muted);">تعداد:</span>
              <div class="rfq-qty-controls">
                <button type="button" class="rfq-qty-btn js-rfq-dec" data-id="${item.id}" aria-label="کاهش تعداد">−</button>
                <input type="number" inputmode="numeric" min="1" class="rfq-qty-input js-rfq-qty-input" data-id="${item.id}" value="${item.qty}" aria-label="تعداد" />
                <button type="button" class="rfq-qty-btn js-rfq-inc" data-id="${item.id}" aria-label="افزایش تعداد">+</button>
              </div>
            </div>
          </div>
        </div>
      `
        )
        .join("")}
      <div class="rfq-notes-box">
        <label for="rfq-customer-notes">توضیحات تکمیلی سفارش (ولتاژ، کورس جک، نام شرکت یا شرایط ارسال):</label>
        <textarea
          id="rfq-customer-notes"
          class="rfq-notes-input"
          rows="2"
          placeholder="مثال: بوبین 24V DC، ارسال به شهرک صنعتی..."
        >${state.rfqCustomerNote || ""}</textarea>
      </div>
    `;

    drawerBody.querySelectorAll(".js-rfq-remove").forEach((btn) => {
      btn.addEventListener("click", () =>
        removeRfqItem(btn.getAttribute("data-id"))
      );
    });

    drawerBody.querySelectorAll(".js-rfq-inc").forEach((btn) => {
      btn.addEventListener("click", () => {
        const id = btn.getAttribute("data-id");
        const found = state.rfqItems.find((i) => i.id === id);
        if (found) updateRfqItemQty(id, found.qty + 1);
      });
    });

    drawerBody.querySelectorAll(".js-rfq-dec").forEach((btn) => {
      btn.addEventListener("click", () => {
        const id = btn.getAttribute("data-id");
        const found = state.rfqItems.find((i) => i.id === id);
        if (found && found.qty > 1) updateRfqItemQty(id, found.qty - 1);
      });
    });

    drawerBody.querySelectorAll(".js-rfq-qty-input").forEach((inp) => {
      inp.addEventListener("change", () => {
        updateRfqItemQty(inp.getAttribute("data-id"), inp.value);
      });
    });

    const notesTextarea = document.getElementById("rfq-customer-notes");
    if (notesTextarea) {
      notesTextarea.addEventListener("input", () => {
        state.rfqCustomerNote = notesTextarea.value;
        saveRfqToStorage();
        updateRfqActionLinks();
        updateFloatingWhatsApp(state.selectedProduct);
      });
    }

    updateFloatingWhatsApp(state.selectedProduct);
  }

  function toggleRfqDrawer(open) {
    const drawer = document.getElementById("rfq-drawer");
    const backdrop = document.getElementById("rfq-drawer-backdrop");
    if (!drawer || !backdrop) return;
    drawer.classList.toggle("open", open);
    backdrop.classList.toggle("open", open);
    drawer.setAttribute("aria-hidden", open ? "false" : "true");
    syncOverlayOpenState();
  }

  function populateMainFormFromRfq() {
    toggleRfqDrawer(false);
    const inquirySection = document.getElementById("inquiry");
    const reqTypeSelect = document.getElementById("b2b-request-type");
    const techCodeInput = document.getElementById("b2b-tech-code");
    const qtyInput = document.getElementById("b2b-quantity");
    const notesInput = document.getElementById("b2b-notes");
    const bomBanner = document.getElementById("rfq-bom-form-banner");

    if (!inquirySection) {
      // If on a category page without #inquiry form, redirect to index.html#inquiry
      window.location.href = "index.html#inquiry";
      return;
    }

    if (reqTypeSelect) {
      reqTypeSelect.value = "سفارش عمده / تامین لیست پروژه (B2B)";
    }
    if (techCodeInput) {
      techCodeInput.value = state.rfqItems
        .map((i) => `${i.code} (×${i.qty})`)
        .join(" ، ");
    }
    if (qtyInput) {
      const total = state.rfqItems.reduce((acc, i) => acc + i.qty, 0);
      qtyInput.value = `${state.rfqItems.length} ردیف کالا (مجموعاً ${total} عدد)`;
    }
    if (notesInput) {
      notesInput.value =
        `لیست اقلام انتخابی جهت پیش‌فاکتور (BOM):\n` + formatRfqForFormText();
    }
    if (bomBanner) {
      bomBanner.classList.add("active");
      bomBanner.innerHTML = `
        <div style="display:flex; align-items:center; justify-content:space-between; gap:1rem; flex-wrap:wrap;">
          <div>
            <strong style="color:var(--text-primary);">لیست استعلام چندقلمی (${state.rfqItems.length} ردیف کالا) به فرم منتقل شد.</strong>
            <div style="font-size:0.8rem; color:var(--text-secondary);">کدهای فنی و تعداد هر ردیف در بخش شرح اقلام درج گردید.</div>
          </div>
          <button type="button" class="btn btn-outline-tech btn-xs" id="edit-bom-drawer-btn">ویرایش لیست اقلام</button>
        </div>
      `;
      const editBtn = document.getElementById("edit-bom-drawer-btn");
      if (editBtn) {
        editBtn.addEventListener("click", () => toggleRfqDrawer(true));
      }
    }

    inquirySection.scrollIntoView({ behavior: "smooth" });
  }

  /**
   * Update the Floating RTL WhatsApp button & Mobile Quick-Action Bar to carry the active product code or RFQ count
   */
  function updateFloatingWhatsApp(product) {
    const waLink = document.getElementById("floating-whatsapp-btn");
    const waBadge = document.getElementById("floating-wa-code-badge");
    const waLabel = document.getElementById("floating-wa-label");
    const targetUrl = buildWhatsAppUrl(product);

    document.querySelectorAll(".js-mobile-quick-wa").forEach((el) => {
      el.href = targetUrl;
    });

    if (!waLink) return;

    waLink.href = targetUrl;
    if (product && waBadge) {
      waBadge.textContent = product.code;
      waBadge.classList.add("active");
      if (waLabel) waLabel.textContent = "استعلام واتساپ:";
    } else if (state.rfqItems.length > 0 && waBadge) {
      waBadge.textContent = `${state.rfqItems.length} قلم`;
      waBadge.classList.add("active");
      if (waLabel) waLabel.textContent = "ارسال لیست در واتساپ";
    } else if (waBadge) {
      waBadge.textContent = "";
      waBadge.classList.remove("active");
      if (waLabel) waLabel.textContent = "استعلام سریع واتساپ";
    }
  }

  /**
   * Filter products using Smart Persian/English Normalizer & Cross-Reference matching
   */
  function getFilteredProducts() {
    const products = window.PRODUCTS_DATA || [];
    const normQuery = normalizeSearchText(state.searchQuery);
    const compactQuery = normalizeCompact(state.searchQuery);

    return products.filter((item) => {
      const matchCategory =
        state.category === "all" || item.category === state.category;
      const matchBrand =
        state.brand === "all" ||
        item.brand.toLowerCase() === state.brand.toLowerCase();

      if (!matchCategory || !matchBrand) return false;
      if (!normQuery) return true;

      const fields = [
        item.code,
        item.nameFa,
        item.nameEn,
        item.brand,
        item.brandFa,
        item.categoryTitleFa,
        item.portSize,
        item.pressureRange,
        item.voltage || "",
        item.valveConfiguration || "",
        item.cylinderType || "",
        item.boreStrokeSpec || "",
        item.accessoryType || "",
        item.applicationsFa || "",
        ...(item.equivalentTo || []),
        ...(item.keywords || [])
      ].join(" ");

      const normFields = normalizeSearchText(fields);
      const compactFields = normalizeCompact(fields);

      return (
        normFields.includes(normQuery) ||
        (compactQuery.length >= 2 && compactFields.includes(compactQuery))
      );
    });
  }

  /**
   * Render Product Cards Grid with JPC Cross-Reference Badges, Copy Code, and Add to RFQ
   */
  function renderCatalog() {
    const grid = document.getElementById("catalog-products-grid");
    const counter = document.getElementById("catalog-result-counter");
    if (!grid) return;

    const filtered = getFilteredProducts();
    const total = (window.PRODUCTS_DATA || []).length;

    if (counter) {
      counter.innerHTML = `نمایش <strong>${filtered.length}</strong> مدل از <strong>${total}</strong> تجهیز کاتالوگ`;
    }

    if (filtered.length === 0) {
      grid.innerHTML = `
        <div class="catalog-empty-state">
          <div style="font-size: 1.1rem; font-weight: 800; color: var(--text-primary);">
            مدلی با فیلتر یا کد فنی جستجو شده در لیست نمونه یافت نشد
          </div>
          <p style="font-size: 0.9rem; color: var(--text-secondary); max-width: 540px;">
            شما می‌توانید کد فنی دقیق قطعه مورد نظر خود را مستقیماً در فرم استعلام قیمت ثبت نمایید تا کارشناسان جلالی پنوماتیک موجودی یا معادل ابعادی برند <strong>JPC</strong> آن را بررسی کنند.
          </p>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; justify-content: center;">
            <button type="button" class="btn btn-outline-tech btn-sm" id="reset-catalog-filters-btn">
              نمایش همه محصولات کاتالوگ
            </button>
            <button type="button" class="btn btn-amber btn-sm" id="empty-state-inquiry-btn">
              استعلام مستقیم این کد فنی
            </button>
          </div>
        </div>
      `;

      const resetBtn = document.getElementById("reset-catalog-filters-btn");
      if (resetBtn) {
        resetBtn.addEventListener("click", resetFilters);
      }
      const emptyInquiryBtn = document.getElementById("empty-state-inquiry-btn");
      if (emptyInquiryBtn) {
        emptyInquiryBtn.addEventListener("click", () => {
          openQuickQuoteModal({
            code: state.searchQuery.trim() || "CUSTOM-CODE",
            nameFa: `استعلام کد فنی: ${state.searchQuery.trim() || "تجهیز پنوماتیک"}`,
            brand: state.brand === "all" ? "تأمین چندبرنده / JPC" : state.brand
          });
        });
      }
      return;
    }

    grid.innerHTML = filtered
      .map((product) => {
        const isJpc = product.brand === "JPC";
        const inRfq = isProductInRfq(product.id);
        const badgeClass = isJpc ? "badge-jpc" : "badge-euro";
        const statusClass =
          product.availabilityStatus === "available"
            ? "status-available"
            : "status-inquiry";

        const thirdSpecLabel =
          product.category === "valves"
            ? "ولتاژ بوبین / آرایش"
            : product.category === "cylinders"
            ? "مشخصات کورس و سیلندر"
            : "مشخصات فنی / دبی";

        const thirdSpecValue =
          product.category === "valves"
            ? `${product.voltage} | ${product.valveConfiguration}`
            : product.category === "cylinders"
            ? product.boreStrokeSpec || product.cylinderType
            : product.accessoryType || product.flowRate;

        // JPC Equivalent Cross-Reference Banner
        let crossRefHtml = "";
        if (!isJpc && product.jpcAlternativeId) {
          crossRefHtml = `
            <div class="jpc-equivalent-banner">
              <span class="jpc-equivalent-text">
                معادل ابعادی و فنی موجود در برند اختصاصی JPC
              </span>
              <button
                type="button"
                class="jpc-equivalent-switch-btn js-switch-to-jpc"
                data-target-id="${product.jpcAlternativeId}"
                title="مشاهده معادل ابعادی و فنی در برند اختصاصی JPC"
              >
                ${product.jpcAlternativeCode || "مشاهده JPC"} ←
              </button>
            </div>
          `;
        } else if (isJpc && product.equivalentTo && product.equivalentTo.length > 0) {
          const sampleEquiv = product.equivalentTo.slice(0, 3).join(" · ");
          crossRefHtml = `
            <div class="equivalent-codes-strip">
              <span>کدهای هم‌ابعاد و معادل فنی:</span>
              <span class="mono" style="font-weight:700; color:var(--steel-accent);">${sampleEquiv}</span>
            </div>
          `;
        }

        return `
          <article class="product-card ${isJpc ? "is-jpc-brand" : ""}" id="card-${product.id}" data-product-id="${product.id}">
            <div>
              <div class="product-card-top">
                <span class="brand-badge ${badgeClass}">${product.brandFa}</span>
                <span class="status-badge ${statusClass}">${product.availabilityFa}</span>
              </div>

              <div class="product-schematic-box">
                <div class="schematic-svg-wrap">
                  ${getSchematicSvg(product.schematicType)}
                </div>
                <div class="schematic-meta">
                  <div class="product-code-row">
                    <button
                      type="button"
                      class="copy-code-btn js-copy-btn"
                      data-copy="${product.code}"
                      title="کپی کد فنی"
                    >
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                      </svg>
                      <span>کپی</span>
                    </button>
                    <span class="product-code-pill">${product.code}</span>
                  </div>
                  <span class="product-cat-label">${product.categoryTitleFa}</span>
                </div>
              </div>

              <div class="product-card-body">
                <h3 class="product-title-fa">${product.nameFa}</h3>

                ${crossRefHtml}

                <div class="product-specs-table">
                  <div class="spec-cell">
                    <span class="spec-key">سایز پورت (Port)</span>
                    <span class="spec-val mono">${product.portSize}</span>
                  </div>
                  <div class="spec-cell">
                    <span class="spec-key">فشار کاری (Pressure)</span>
                    <span class="spec-val mono">${product.pressureRange}</span>
                  </div>
                  <div class="spec-cell spec-cell-wide">
                    <span class="spec-key">${thirdSpecLabel}</span>
                    <span class="spec-val">${thirdSpecValue}</span>
                  </div>
                </div>
              </div>
            </div>

            <div class="product-card-footer">
              <div class="product-card-actions">
                <button
                  type="button"
                  class="btn btn-amber btn-sm js-quote-trigger"
                  data-id="${product.id}"
                >
                  درخواست استعلام قیمت
                </button>
                <button
                  type="button"
                  class="btn btn-rfq-add btn-sm js-add-rfq-btn ${inRfq ? "in-list" : ""}"
                  data-id="${product.id}"
                >
                  ${inRfq ? "✓ در لیست استعلام (+۱)" : "+ افزودن به لیست استعلام"}
                </button>
              </div>
              <div class="product-sub-links">
                <button
                  type="button"
                  class="product-pdf-link js-spec-trigger"
                  data-id="${product.id}"
                >
                  مشاهده مشخصات فنی و کدهای معادل ←
                </button>
                <a
                  href="${product.datasheetUrl}"
                  download
                  class="product-pdf-link"
                >
                  دانلود PDF
                </a>
              </div>
            </div>
          </article>
        `;
      })
      .join("");

    // Attach listeners to newly rendered buttons
    grid.querySelectorAll(".js-quote-trigger").forEach((btn) => {
      btn.addEventListener("click", () => {
        const prod = findProductById(btn.getAttribute("data-id"));
        if (prod) openQuickQuoteModal(prod);
      });
    });

    grid.querySelectorAll(".js-add-rfq-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const prod = findProductById(btn.getAttribute("data-id"));
        if (prod) addToRfqList(prod);
      });
    });

    grid.querySelectorAll(".js-spec-trigger").forEach((btn) => {
      btn.addEventListener("click", () => {
        const prod = findProductById(btn.getAttribute("data-id"));
        if (prod) openTechDetailModal(prod);
      });
    });

    grid.querySelectorAll(".js-copy-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        copyTextToClipboard(btn.getAttribute("data-copy"), btn);
      });
    });

    grid.querySelectorAll(".js-switch-to-jpc").forEach((btn) => {
      btn.addEventListener("click", () => {
        const targetId = btn.getAttribute("data-target-id");
        switchToJpcEquivalent(targetId);
      });
    });
  }

  /**
   * Switch to / Highlight JPC Equivalent Product
   */
  function switchToJpcEquivalent(targetId) {
    const targetProduct = findProductById(targetId);
    if (!targetProduct) return;

    // Ensure filters allow showing the JPC product
    if (state.brand !== "all" && state.brand !== "JPC") {
      state.brand = "all";
    }
    if (
      state.category !== "all" &&
      state.category !== targetProduct.category
    ) {
      state.category = "all";
    }
    state.searchQuery = "";
    const searchInput = document.getElementById("catalog-search-input");
    if (searchInput) searchInput.value = "";

    syncFilterPillsUI();
    renderCatalog();

    const cardEl = document.getElementById(`card-${targetId}`);
    if (cardEl) {
      cardEl.scrollIntoView({ behavior: "smooth", block: "center" });
      cardEl.classList.add("highlight-pulse");
      setTimeout(() => cardEl.classList.remove("highlight-pulse"), 2600);
    } else {
      openTechDetailModal(targetProduct);
    }
  }

  function findProductById(id) {
    return (window.PRODUCTS_DATA || []).find((p) => p.id === id) || null;
  }

  function resetFilters() {
    state.category = initialCategory;
    state.brand = "all";
    state.searchQuery = "";

    const searchInput = document.getElementById("catalog-search-input");
    const clearBtn = document.getElementById("search-clear-btn");
    if (searchInput) searchInput.value = "";
    if (clearBtn) clearBtn.classList.remove("visible");

    syncFilterPillsUI();
    renderCatalog();
  }

  function syncFilterPillsUI() {
    document.querySelectorAll("[data-category-filter]").forEach((pill) => {
      const val = pill.getAttribute("data-category-filter");
      pill.classList.toggle("active", val === state.category);
    });

    document.querySelectorAll("[data-brand-filter]").forEach((pill) => {
      const val = pill.getAttribute("data-brand-filter");
      pill.classList.toggle("active", val === state.brand);
    });
  }

  /**
   * Interactive Pneumatic Cylinder Force Calculator
   * F_ext (N) = (pi * D^2 / 4) * P(bar) * 0.1
   * F_ret (N) = (pi * (D^2 - d^2) / 4) * P(bar) * 0.1
   * 1 kgf = 9.80665 N
   */
  function initCylinderCalculator() {
    const boreInput = document.getElementById("calc-bore-input");
    const rodInput = document.getElementById("calc-rod-input");
    const pressureInput = document.getElementById("calc-pressure-input");
    const pressureSlider = document.getElementById("calc-pressure-slider");
    const presetButtons = document.querySelectorAll("[data-bore-preset]");

    if (!boreInput || !rodInput || !pressureInput) return;

    function updateCalculation() {
      const D = Math.max(6, parseFloat(boreInput.value) || 63);
      let d = Math.max(2, parseFloat(rodInput.value) || 20);
      if (d >= D) {
        d = Math.round(D * 0.35);
        rodInput.value = String(d);
      }
      const P = Math.min(16, Math.max(0.5, parseFloat(pressureInput.value) || 6));

      state.calc.bore = D;
      state.calc.rod = d;
      state.calc.pressure = P;

      // Highlight matching bore preset button
      presetButtons.forEach((btn) => {
        const bVal = parseFloat(btn.getAttribute("data-bore-preset"));
        btn.classList.toggle("active", bVal === D);
      });

      const areaExtMm2 = (Math.PI * D * D) / 4;
      const areaRetMm2 = (Math.PI * (D * D - d * d)) / 4;

      // Force in Newtons (1 bar = 0.1 N/mm^2)
      const forceExtN = areaExtMm2 * P * 0.1;
      const forceRetN = areaRetMm2 * P * 0.1;

      const forceExtKgf = forceExtN / 9.80665;
      const forceRetKgf = forceRetN / 9.80665;

      const extNEl = document.getElementById("calc-ext-n");
      const extKgfEl = document.getElementById("calc-ext-kgf");
      const retNEl = document.getElementById("calc-ret-n");
      const retKgfEl = document.getElementById("calc-ret-kgf");
      const summarySpecEl = document.getElementById("calc-formula-summary");

      if (extNEl) extNEl.textContent = `${Math.round(forceExtN).toLocaleString("en-US")} N`;
      if (extKgfEl) extKgfEl.textContent = `≈ ${forceExtKgf.toFixed(1)} kgf`;
      if (retNEl) retNEl.textContent = `${Math.round(forceRetN).toLocaleString("en-US")} N`;
      if (retKgfEl) retKgfEl.textContent = `≈ ${forceRetKgf.toFixed(1)} kgf`;
      if (summarySpecEl) {
        summarySpecEl.textContent = `Ø${D}mm Bore | Ø${d}mm Rod | ${P} bar`;
      }

      renderRecommendedCylinders(D, P);
    }

    function renderRecommendedCylinders(boreMm, pressureBar) {
      const container = document.getElementById("calc-recommended-cylinders");
      if (!container) return;

      const allCylinders = (window.PRODUCTS_DATA || []).filter(
        (p) => p.category === "cylinders"
      );

      // Match cylinders whose supportedBores includes boreMm, or closest match
      let matched = allCylinders.filter(
        (p) => Array.isArray(p.supportedBores) && p.supportedBores.includes(boreMm)
      );
      if (matched.length === 0) {
        matched = allCylinders.slice(0, 3);
      }

      container.innerHTML = matched
        .slice(0, 3)
        .map(
          (cyl) => `
          <div class="calc-rec-card">
            <div>
              <div style="display:flex; align-items:center; justify-content:space-between; gap:0.5rem; margin-bottom:0.45rem;">
                <span class="brand-badge ${cyl.brand === "JPC" ? "badge-jpc" : "badge-euro"}" style="font-size:0.7rem;">
                  ${cyl.brandFa}
                </span>
                <span class="mono" style="font-size:0.76rem; font-weight:700; color:var(--steel-accent);">
                  Ø${boreMm}mm
                </span>
              </div>
              <div style="font-size:0.88rem; font-weight:800; color:var(--text-primary); margin-bottom:0.25rem;">
                ${cyl.nameFa}
              </div>
              <div class="mono" style="font-size:0.74rem; color:var(--text-muted);">
                ${cyl.code}
              </div>
            </div>
            <div style="display:flex; gap:0.45rem; flex-wrap:wrap;">
              <button
                type="button"
                class="btn btn-rfq-add btn-xs js-calc-add-rfq"
                data-id="${cyl.id}"
                data-bore="${boreMm}"
                data-pressure="${pressureBar}"
              >
                + افزودن به لیست استعلام (Ø${boreMm}mm)
              </button>
              <button
                type="button"
                class="btn btn-outline-tech btn-xs js-calc-quote"
                data-id="${cyl.id}"
              >
                استعلام فوری
              </button>
            </div>
          </div>
        `
        )
        .join("");

      container.querySelectorAll(".js-calc-add-rfq").forEach((btn) => {
        btn.addEventListener("click", () => {
          const prod = findProductById(btn.getAttribute("data-id"));
          const b = btn.getAttribute("data-bore");
          const pr = btn.getAttribute("data-pressure");
          if (prod) {
            addToRfqList(prod, `قطر پیستون Ø${b}mm | فشار کاری ${pr} bar`);
          }
        });
      });

      container.querySelectorAll(".js-calc-quote").forEach((btn) => {
        btn.addEventListener("click", () => {
          const prod = findProductById(btn.getAttribute("data-id"));
          if (prod) openQuickQuoteModal(prod);
        });
      });
    }

    presetButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const bVal = parseInt(btn.getAttribute("data-bore-preset"), 10);
        boreInput.value = String(bVal);
        if (STANDARD_ROD_MAP[bVal]) {
          rodInput.value = String(STANDARD_ROD_MAP[bVal]);
        }
        updateCalculation();
      });
    });

    boreInput.addEventListener("input", () => {
      const bVal = parseInt(boreInput.value, 10);
      if (STANDARD_ROD_MAP[bVal]) {
        rodInput.value = String(STANDARD_ROD_MAP[bVal]);
      }
      updateCalculation();
    });

    rodInput.addEventListener("input", updateCalculation);

    pressureSlider.addEventListener("input", () => {
      pressureInput.value = pressureSlider.value;
      updateCalculation();
    });

    pressureInput.addEventListener("input", () => {
      pressureSlider.value = pressureInput.value;
      updateCalculation();
    });

    updateCalculation();
  }

  /**
   * Open Quick Quote Modal & pre-fill both Modal Form and Main B2B Inquiry Form
   */
  function openQuickQuoteModal(product) {
    state.selectedProduct = product;
    updateFloatingWhatsApp(product);

    const mainCodeInput = document.getElementById("b2b-tech-code");
    const mainBrandSelect = document.getElementById("b2b-brand-select");
    const mainNotesInput = document.getElementById("b2b-notes");

    if (mainCodeInput && product.code) {
      mainCodeInput.value = `${product.code} — ${product.nameFa}`;
    }
    if (mainBrandSelect && product.brand) {
      const options = Array.from(mainBrandSelect.options).map((o) => o.value);
      if (options.includes(product.brand)) {
        mainBrandSelect.value = product.brand;
      }
    }
    if (mainNotesInput && !mainNotesInput.value) {
      mainNotesInput.value = `درخواست استعلام قیمت و زمان تحویل برای مدل ${product.code} (${product.nameFa})`;
    }

    const modal = document.getElementById("quick-quote-modal");
    const prodTitleEl = document.getElementById("modal-prefill-name");
    const prodCodeEl = document.getElementById("modal-prefill-code");
    const modalCodeInput = document.getElementById("modal-tech-code-input");
    const modalWaDirectBtn = document.getElementById("modal-wa-direct-btn");
    const modalFeedback = document.getElementById("modal-form-feedback");

    if (prodTitleEl) prodTitleEl.textContent = product.nameFa;
    if (prodCodeEl) prodCodeEl.textContent = product.code;
    if (modalCodeInput) {
      modalCodeInput.value = `${product.code} | ${product.nameFa}`;
    }
    if (modalWaDirectBtn) {
      modalWaDirectBtn.href = buildWhatsAppUrl(product);
    }
    if (modalFeedback) {
      modalFeedback.className = "form-feedback";
      modalFeedback.textContent = "";
    }

    if (modal) {
      modal.classList.add("open");
      modal.setAttribute("aria-hidden", "false");
      syncOverlayOpenState();
    }
  }

  /**
   * Open Technical Specification Detail Modal (with Add to RFQ + Cross-Reference + Sticky Mobile Footer)
   */
  function openTechDetailModal(product) {
    state.selectedProduct = product;
    updateFloatingWhatsApp(product);

    const modal = document.getElementById("tech-detail-modal");
    const body = document.getElementById("tech-detail-modal-body");
    const footer = document.getElementById("tech-detail-modal-footer");
    const title = document.getElementById("tech-detail-modal-title");
    if (!modal || !body) return;

    if (title) {
      title.textContent = `${product.nameFa}`;
    }

    const highlightsHtml = (product.highlightsFa || [])
      .map((h) => `<li>${h}</li>`)
      .join("");

    const equivHtml =
      product.equivalentTo && product.equivalentTo.length > 0
        ? `
      <div style="background: var(--bg-tertiary); border: 1px solid var(--border-strong); padding: 0.75rem 1rem; border-radius: var(--radius-sm); margin-bottom: 1.15rem; font-size: 0.82rem;">
        <div style="font-weight: 800; color: var(--text-primary); margin-bottom: 0.3rem;">
          کدهای فنی هم‌ابعاد و قابل معادل‌یابی (Cross-Reference):
        </div>
        <div class="mono" style="color: var(--steel-accent); font-weight: 700;">
          ${product.equivalentTo.join(" , ")}
        </div>
      </div>`
        : "";

    const jpcSwitchBanner =
      product.brand !== "JPC" && product.jpcAlternativeId
        ? `
      <div class="jpc-equivalent-banner" style="margin-bottom: 1.15rem; padding: 0.75rem 1rem;">
        <span class="jpc-equivalent-text">
          معادل ابعادی و فنی موجود در برند اختصاصی JPC (${product.jpcAlternativeCode})
        </span>
        <button type="button" class="jpc-equivalent-switch-btn" id="modal-switch-jpc-btn">
          مشاهده معادل JPC ←
        </button>
      </div>`
        : "";

    const actionsMarkup = `
      <div style="display: flex; align-items: center; justify-content: space-between; gap: 0.65rem; flex-wrap: wrap; width: 100%;">
        <div style="display:flex; gap:0.55rem; flex-wrap:wrap; flex: 1;">
          <button type="button" class="btn btn-amber btn-sm" id="spec-modal-to-quote-btn" style="flex: 1;">
            درخواست استعلام قیمت
          </button>
          <button type="button" class="btn btn-rfq-add btn-sm" id="spec-modal-add-rfq-btn" style="flex: 1;">
            + افزودن به لیست استعلام
          </button>
        </div>
        <a href="${product.datasheetUrl}" download class="btn btn-outline-tech btn-sm">
          دانلود کاتالوگ PDF
        </a>
      </div>
    `;

    body.innerHTML = `
      <div class="prefilled-product-banner">
        <div>
          <div style="font-size: 0.76rem; color: var(--text-muted);">کد فنی مدل (Technical Code)</div>
          <div style="display:flex; align-items:center; gap:0.5rem; margin-top:0.15rem;">
            <span class="mono" style="font-size: 1.02rem; font-weight: 800; color: var(--steel-accent);">${product.code}</span>
            <button type="button" class="copy-code-btn" id="modal-copy-code-btn" data-copy="${product.code}">
              کپی کد
            </button>
          </div>
        </div>
        <span class="brand-badge ${product.brand === "JPC" ? "badge-jpc" : "badge-euro"}">${product.brandFa}</span>
      </div>

      ${jpcSwitchBanner}

      <div class="product-specs-table" style="margin-bottom: 1.15rem;">
        <div class="spec-cell">
          <span class="spec-key">دسته تجهیز</span>
          <span class="spec-val">${product.categoryTitleFa}</span>
        </div>
        <div class="spec-cell">
          <span class="spec-key">سایز پورت</span>
          <span class="spec-val mono">${product.portSize}</span>
        </div>
        <div class="spec-cell">
          <span class="spec-key">محدوده فشار کاری</span>
          <span class="spec-val mono">${product.pressureRange}</span>
        </div>
        <div class="spec-cell">
          <span class="spec-key">دمای کاری</span>
          <span class="spec-val mono">${product.operatingTemp}</span>
        </div>
        <div class="spec-cell spec-cell-wide">
          <span class="spec-key">جنس بدنه و ساختار آب‌بندی</span>
          <span class="spec-val">${product.bodyMaterial}</span>
        </div>
        <div class="spec-cell spec-cell-wide">
          <span class="spec-key">دبی / ویژگی عملکردی</span>
          <span class="spec-val">${product.flowRate}</span>
        </div>
      </div>

      ${equivHtml}

      <div style="margin-bottom: 1.15rem;">
        <h4 style="font-size: 0.88rem; font-weight: 800; margin-bottom: 0.45rem;">ویژگی‌های فنی و مهندسی:</h4>
        <ul class="pillar-feature-list" style="padding-top: 0.45rem;">
          ${highlightsHtml}
        </ul>
      </div>

      <div style="background: var(--bg-primary); border: 1px solid var(--border-tech); padding: 0.8rem 1rem; border-radius: var(--radius-sm); margin-bottom: 0.5rem; font-size: 0.83rem;">
        <strong>کاربردهای صنعتی:</strong> ${product.applicationsFa}
      </div>

      ${footer ? "" : `<div style="margin-top: 1rem;">${actionsMarkup}</div>`}
    `;

    if (footer) {
      footer.innerHTML = actionsMarkup;
    }

    const copyBtn = document.getElementById("modal-copy-code-btn");
    if (copyBtn) {
      copyBtn.addEventListener("click", () =>
        copyTextToClipboard(product.code, copyBtn)
      );
    }

    const switchJpcBtn = document.getElementById("modal-switch-jpc-btn");
    if (switchJpcBtn && product.jpcAlternativeId) {
      switchJpcBtn.addEventListener("click", () => {
        const altProd = findProductById(product.jpcAlternativeId);
        if (altProd) openTechDetailModal(altProd);
      });
    }

    const toQuoteBtn = document.getElementById("spec-modal-to-quote-btn");
    if (toQuoteBtn) {
      toQuoteBtn.addEventListener("click", () => {
        closeAllModals();
        openQuickQuoteModal(product);
      });
    }

    const addRfqBtn = document.getElementById("spec-modal-add-rfq-btn");
    if (addRfqBtn) {
      addRfqBtn.addEventListener("click", () => {
        addToRfqList(product);
      });
    }

    modal.classList.add("open");
    modal.setAttribute("aria-hidden", "false");
    syncOverlayOpenState();
  }

  function closeAllModals() {
    document.querySelectorAll(".modal-backdrop").forEach((m) => {
      m.classList.remove("open");
      m.setAttribute("aria-hidden", "true");
    });
    syncOverlayOpenState();
  }

  /**
   * Theme Management (Default Light Engineering, Toggleable Dark Slate)
   */
  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("jpc_theme", theme);
  }

  /**
   * Handle B2B Inquiry Form & Quick Quote Modal Form Submissions
   */
  function initForms() {
    const fileInput = document.getElementById("b2b-pdf-upload");
    const fileStatus = document.getElementById("file-upload-status");
    const fileZone = document.getElementById("file-upload-zone");

    if (fileZone && fileInput) {
      fileZone.addEventListener("click", () => fileInput.click());
      fileInput.addEventListener("change", () => {
        const file = fileInput.files && fileInput.files[0];
        if (!file) {
          if (fileStatus)
            fileStatus.textContent =
              "فایلی انتخاب نشده است (حداکثر ۱۵ مگابایت - PDF)";
          return;
        }
        if (!file.name.toLowerCase().endsWith(".pdf")) {
          if (fileStatus) {
            fileStatus.textContent =
              "خطا: لطفاً فقط فایل با فرمت PDF بارگذاری نمایید.";
            fileStatus.style.color = "#EF4444";
          }
          fileInput.value = "";
          return;
        }
        const sizeMB = (file.size / (1024 * 1024)).toFixed(2);
        if (fileStatus) {
          fileStatus.textContent = `فایل انتخاب شده: ${file.name} (${sizeMB} MB)`;
          fileStatus.style.color = "var(--status-success)";
        }
      });
    }

    const b2bForm = document.getElementById("b2b-inquiry-form");
    const b2bFeedback = document.getElementById("b2b-form-feedback");

    if (b2bForm) {
      b2bForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const formData = new FormData(b2bForm);
        const payload = {
          requestType: formData.get("requestType"),
          companyName: formData.get("companyName"),
          contactPerson: formData.get("contactPerson"),
          phone: formData.get("phone"),
          brandPreference: formData.get("brandPreference"),
          technicalCodes: formData.get("technicalCodes"),
          quantity: formData.get("quantity"),
          notes: formData.get("notes"),
          attachedPdf:
            fileInput && fileInput.files[0] ? fileInput.files[0].name : null
        };

        const refCode = `JPC-${Math.floor(100000 + Math.random() * 900000)}`;
        const endpoint =
          window.SITE_CONFIG &&
          window.SITE_CONFIG.endpoints &&
          window.SITE_CONFIG.endpoints.inquirySubmitUrl;

        if (b2bFeedback) {
          const waText =
            `درخواست استعلام B2B (${refCode}) - شرکت جلالی پنوماتیک\n` +
            `• نام شرکت/کارگاه: ${payload.companyName}\n` +
            `• نام درخواست‌کننده: ${payload.contactPerson}\n` +
            `• شماره تماس: ${payload.phone}\n` +
            `• نوع سفارش: ${payload.requestType}\n` +
            `• برند مدنظر: ${payload.brandPreference}\n` +
            `• کد فنی / شرح اقلام: ${payload.technicalCodes}\n` +
            `• تعداد: ${payload.quantity || "طبق لیست"}\n` +
            (payload.notes ? `• جزئیات:\n${payload.notes}` : "");

          const waUrl = buildWhatsAppUrl(null, waText);
          const tgUrl = buildTelegramUrl(waText);

          b2bFeedback.className = "form-feedback success";
          b2bFeedback.innerHTML = `
            <div style="display:flex; flex-direction:column; gap:0.65rem;">
              <div>
                درخواست استعلام شما با کد پیگیری <span class="mono">${refCode}</span> در سامانه ثبت گردید (${endpoint}). کارشناسان فروش جلالی پنوماتیک در کوتاه‌ترین زمان پیش‌فاکتور و مشخصات فنی را ارسال خواهند کرد.
              </div>
              <div style="display:flex; gap:0.65rem; flex-wrap:wrap;">
                <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-amber btn-sm">
                  ارسال همزمان در واتساپ فروش
                </a>
                <a href="${tgUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-telegram btn-sm">
                  ارسال در تلگرام مهندسی فروش
                </a>
              </div>
            </div>
          `;
        }
      });
    }

    // Quick Quote Modal Form
    const modalForm = document.getElementById("quick-quote-form");
    const modalFeedback = document.getElementById("modal-form-feedback");

    if (modalForm) {
      modalForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const fd = new FormData(modalForm);
        const techCode = fd.get("modalTechCode");
        const company = fd.get("modalCompany");
        const phone = fd.get("modalPhone");
        const qty = fd.get("modalQty");
        const refCode = `JPC-Q${Math.floor(10000 + Math.random() * 90000)}`;

        const waMsg =
          `استعلام سریع محصول (${refCode}) - جلالی پنوماتیک\n` +
          `• کد فنی و محصول: ${techCode}\n` +
          `• تعداد درخواستی: ${qty}\n` +
          `• نام مجموعه: ${company}\n` +
          `• شماره تماس/واتساپ: ${phone}`;

        const waUrl = buildWhatsAppUrl(null, waMsg);

        if (modalFeedback) {
          modalFeedback.className = "form-feedback success";
          modalFeedback.innerHTML = `
            <div style="display:flex; flex-direction:column; gap:0.6rem;">
              <div>
                استعلام قیمت برای <span class="mono">${techCode}</span> با کد <span class="mono">${refCode}</span> ثبت شد.
              </div>
              <div>
                <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-amber btn-sm">
                  ادامه گفتگو و دریافت فوری قیمت در واتساپ
                </a>
              </div>
            </div>
          `;
        }
      });
    }
  }

  /**
   * Interactive Cross-Reference Quick Finder in #cross-reference section
   */
  function initCrossReferenceFinder() {
    const input = document.getElementById("crossref-finder-input");
    const resultBox = document.getElementById("crossref-finder-result");
    if (!input || !resultBox) return;

    function runLookup(rawVal) {
      const q = normalizeSearchText(rawVal);
      const compact = normalizeCompact(rawVal);
      if (!q || q.length < 2) {
        resultBox.style.display = "none";
        resultBox.innerHTML = "";
        return;
      }

      const products = window.PRODUCTS_DATA || [];
      const matches = products.filter((p) => {
        const hay = [
          p.code,
          p.nameFa,
          p.nameEn,
          p.brand,
          p.portSize,
          ...(p.equivalentTo || []),
          ...(p.keywords || [])
        ].join(" ");
        return (
          normalizeSearchText(hay).includes(q) ||
          (compact.length >= 2 && normalizeCompact(hay).includes(compact))
        );
      });

      resultBox.style.display = "block";
      if (matches.length === 0) {
        resultBox.innerHTML = `
          <div style="padding:0.75rem 0.9rem; background:var(--bg-primary); border:1px solid var(--border-tech); border-radius:var(--radius-sm); font-size:0.83rem;">
            کد <strong>${rawVal}</strong> در جدول نمونه یافت نشد؛ برای استعلام معادل دقیق در برند <strong>JPC</strong> یا تأمین اروپایی، مستقیماً در واتساپ پیام دهید:
            <div style="margin-top:0.55rem;">
              <a href="${buildWhatsAppUrl(null, `سلام، درخواست بررسی و معادل‌یابی کد فنی ${rawVal} را دارم.`)}" target="_blank" rel="noopener noreferrer" class="btn btn-amber btn-xs">
                استعلام کد در واتساپ (0912 130 5167)
              </a>
            </div>
          </div>
        `;
        return;
      }

      resultBox.innerHTML = matches
        .slice(0, 3)
        .map((m) => {
          const jpcAlt =
            m.brand === "JPC"
              ? m
              : m.jpcAlternativeId
              ? findProductById(m.jpcAlternativeId)
              : null;
          return `
            <div style="padding:0.75rem 0.9rem; background:var(--bg-primary); border:1px solid var(--border-strong); border-radius:var(--radius-sm); margin-bottom:0.5rem; display:flex; align-items:center; justify-content:space-between; gap:0.75rem; flex-wrap:wrap;">
              <div>
                <div style="font-size:0.84rem; font-weight:800; color:var(--text-primary);">
                  <span class="mono" style="color:var(--steel-accent);">${m.code}</span> — ${m.nameFa}
                </div>
                <div style="font-size:0.76rem; color:var(--text-secondary); margin-top:0.2rem;">
                  سایز پورت: <span class="mono">${m.portSize}</span> | فشار: <span class="mono">${m.pressureRange}</span>
                  ${
                    jpcAlt
                      ? ` | <strong style="color:var(--amber-hover);">معادل ابعادی JPC: <span class="mono">${jpcAlt.code}</span></strong>`
                      : ""
                  }
                </div>
              </div>
              <div style="display:flex; gap:0.45rem; flex-wrap:wrap;">
                <button type="button" class="btn btn-rfq-add btn-xs js-xref-add" data-id="${(jpcAlt || m).id}">
                  + افزودن ${(jpcAlt || m).code} به استعلام
                </button>
                <button type="button" class="btn btn-outline-tech btn-xs js-xref-spec" data-id="${m.id}">
                  مشخصات فنی
                </button>
              </div>
            </div>
          `;
        })
        .join("");

      resultBox.querySelectorAll(".js-xref-add").forEach((btn) => {
        btn.addEventListener("click", () => {
          const prod = findProductById(btn.getAttribute("data-id"));
          if (prod) addToRfqList(prod);
        });
      });

      resultBox.querySelectorAll(".js-xref-spec").forEach((btn) => {
        btn.addEventListener("click", () => {
          const prod = findProductById(btn.getAttribute("data-id"));
          if (prod) openTechDetailModal(prod);
        });
      });
    }

    input.addEventListener("input", () => runLookup(input.value));
  }

  /**
   * Initialize Event Listeners & UI Components
   */
  function init() {
    applyTheme(state.theme);

    // Theme Toggle Button
    const themeBtn = document.getElementById("theme-toggle-btn");
    if (themeBtn) {
      themeBtn.addEventListener("click", () => {
        applyTheme(state.theme === "light" ? "dark" : "light");
      });
    }

    // Mobile Drawer Menu
    const mobileMenuBtn = document.getElementById("mobile-menu-btn");
    const mobileCloseBtn = document.getElementById("mobile-drawer-close");
    const mobileBackdrop = document.getElementById("mobile-drawer-backdrop");
    const mobileDrawer = document.getElementById("mobile-drawer");

    function toggleMobileDrawer(open) {
      if (!mobileDrawer || !mobileBackdrop) return;
      mobileDrawer.classList.toggle("open", open);
      mobileBackdrop.classList.toggle("open", open);
      mobileDrawer.setAttribute("aria-hidden", open ? "false" : "true");
      syncOverlayOpenState();
    }

    if (mobileMenuBtn) {
      mobileMenuBtn.addEventListener("click", () => toggleMobileDrawer(true));
    }
    if (mobileCloseBtn) {
      mobileCloseBtn.addEventListener("click", () => toggleMobileDrawer(false));
    }
    if (mobileBackdrop) {
      mobileBackdrop.addEventListener("click", () => toggleMobileDrawer(false));
    }
    document.querySelectorAll(".mobile-nav-link").forEach((link) => {
      link.addEventListener("click", () => toggleMobileDrawer(false));
    });

    // RFQ Drawer Open/Close & Action Buttons
    document.querySelectorAll(".js-open-rfq-drawer").forEach((btn) => {
      btn.addEventListener("click", () => toggleRfqDrawer(true));
    });

    const rfqCloseBtn = document.getElementById("rfq-drawer-close");
    const rfqBackdrop = document.getElementById("rfq-drawer-backdrop");
    const rfqClearBtn = document.getElementById("rfq-clear-btn");
    const rfqPopulateBtn = document.getElementById("rfq-populate-form-btn");

    if (rfqCloseBtn) {
      rfqCloseBtn.addEventListener("click", () => toggleRfqDrawer(false));
    }
    if (rfqBackdrop) {
      rfqBackdrop.addEventListener("click", () => toggleRfqDrawer(false));
    }
    if (rfqClearBtn) {
      rfqClearBtn.addEventListener("click", clearRfqList);
    }
    if (rfqPopulateBtn) {
      rfqPopulateBtn.addEventListener("click", populateMainFormFromRfq);
    }

    // Static Copy Buttons (Phone Numbers, Contacts, etc.)
    document.querySelectorAll(".js-static-copy-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        copyTextToClipboard(btn.getAttribute("data-copy"), btn);
      });
    });

    // Category Filter Pills
    document.querySelectorAll("[data-category-filter]").forEach((pill) => {
      pill.addEventListener("click", () => {
        state.category = pill.getAttribute("data-category-filter");
        syncFilterPillsUI();
        renderCatalog();
      });
    });

    // Brand Filter Pills
    document.querySelectorAll("[data-brand-filter]").forEach((pill) => {
      pill.addEventListener("click", () => {
        state.brand = pill.getAttribute("data-brand-filter");
        syncFilterPillsUI();
        renderCatalog();
      });
    });

    // Brand Matrix interactive cards (scroll + filter catalog by brand)
    document.querySelectorAll("[data-select-brand]").forEach((card) => {
      card.addEventListener("click", () => {
        const brandVal = card.getAttribute("data-select-brand");
        state.brand = brandVal;
        syncFilterPillsUI();
        renderCatalog();
        const catalogSection = document.getElementById("catalog");
        if (catalogSection) {
          catalogSection.scrollIntoView({ behavior: "smooth" });
        }
      });
    });

    // Live Search Input
    const searchInput = document.getElementById("catalog-search-input");
    const clearBtn = document.getElementById("search-clear-btn");

    if (searchInput) {
      searchInput.addEventListener("input", () => {
        state.searchQuery = searchInput.value;
        if (clearBtn) {
          clearBtn.classList.toggle(
            "visible",
            state.searchQuery.trim().length > 0
          );
        }
        renderCatalog();
      });
    }

    if (clearBtn && searchInput) {
      clearBtn.addEventListener("click", () => {
        searchInput.value = "";
        state.searchQuery = "";
        clearBtn.classList.remove("visible");
        renderCatalog();
        searchInput.focus();
      });
    }

    // Hero Quick Search Form (Above the fold on mobile/desktop)
    const heroSearchForm = document.getElementById("hero-quick-search-form");
    const heroSearchInput = document.getElementById("hero-quick-search-input");
    if (heroSearchForm && heroSearchInput) {
      heroSearchForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const q = heroSearchInput.value.trim();
        state.searchQuery = q;
        if (searchInput) {
          searchInput.value = q;
        }
        if (clearBtn) {
          clearBtn.classList.toggle("visible", q.length > 0);
        }
        renderCatalog();
        const catalogSection = document.getElementById("catalog");
        if (catalogSection) {
          catalogSection.scrollIntoView({ behavior: "smooth" });
        }
      });
    }

    // Modal close triggers
    document.querySelectorAll("[data-close-modal]").forEach((btn) => {
      btn.addEventListener("click", closeAllModals);
    });

    document.querySelectorAll(".modal-backdrop").forEach((backdrop) => {
      backdrop.addEventListener("click", (e) => {
        if (e.target === backdrop) {
          closeAllModals();
        }
      });
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        closeAllModals();
        toggleMobileDrawer(false);
        toggleRfqDrawer(false);
      }
    });

    // Hero & Header Quick Inquiry Triggers
    document.querySelectorAll(".js-open-general-inquiry").forEach((btn) => {
      btn.addEventListener("click", (e) => {
        const targetId = btn.getAttribute("href");
        if (!targetId || targetId === "#") {
          e.preventDefault();
          openQuickQuoteModal({
            code: "JPC / MULTI-BRAND",
            nameFa: "استعلام قیمت و مشاوره فنی تجهیزات پنوماتیک",
            brand: "JPC"
          });
        }
      });
    });

    // Support ?q= query parameter from JSON-LD SearchAction
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const qParam = urlParams.get("q");
      if (qParam && qParam.trim()) {
        state.searchQuery = qParam.trim();
        if (searchInput) {
          searchInput.value = state.searchQuery;
        }
        if (clearBtn) {
          clearBtn.classList.add("visible");
        }
      }
    } catch (e) {
      // ignore URLSearchParams errors on older browsers
    }

    // Comparison Table quick-view / inquiry triggers
    document.querySelectorAll(".js-table-product-trigger").forEach((btn) => {
      btn.addEventListener("click", () => {
        const pid = btn.getAttribute("data-id");
        const prod = findProductById(pid);
        if (prod) {
          openTechDetailModal(prod);
        }
      });
    });

    // Standalone RFQ / Quote triggers (e.g., on SEO guide & cross-reference pages)
    document.querySelectorAll(".js-add-rfq-btn").forEach((btn) => {
      if (!btn.closest("#catalog-products-grid")) {
        btn.addEventListener("click", () => {
          const pid = btn.getAttribute("data-id");
          if (pid) {
            addToRfq(pid);
          }
        });
      }
    });

    document.querySelectorAll(".js-quote-trigger").forEach((btn) => {
      if (!btn.closest("#catalog-products-grid")) {
        btn.addEventListener("click", () => {
          const pid = btn.getAttribute("data-id");
          const prod = findProductById(pid);
          if (prod) {
            openQuickQuoteModal(prod);
          }
        });
      }
    });

    // Initialize Views
    syncFilterPillsUI();
    renderCatalog();
    renderRfqUI();
    initCylinderCalculator();
    initCrossReferenceFinder();
    updateFloatingWhatsApp(null);
    initForms();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
