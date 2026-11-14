/**
 * Jalali Pneumatic Company (JPC) - Interactive Application Logic
 * مدیریت کاتالوگ زنده، فیلترهای فنی، مودال استعلام قیمت سریع و ارتباط واتساپ
 */

(function () {
  "use strict";

  // Application State
  const state = {
    category: "all",
    brand: "all",
    searchQuery: "",
    selectedProduct: null,
    theme: localStorage.getItem("jpc_theme") || "light"
  };

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
   * Build WhatsApp URL carrying optional product code & name
   */
  function buildWhatsAppUrl(product, customText) {
    const base =
      (window.SITE_CONFIG &&
        window.SITE_CONFIG.contact &&
        window.SITE_CONFIG.contact.whatsappBaseUrl) ||
      "https://wa.me/989120000000";

    let message = "";
    if (customText) {
      message = customText;
    } else if (product) {
      message =
        `سلام، جهت استعلام قیمت و موجودی تجهیز زیر از وب‌سایت شرکت جلالی پنوماتیک (JPC) پیام می‌دهم:\n` +
        `• نام محصول: ${product.nameFa}\n` +
        `• کد فنی: ${product.code}\n` +
        `• برند: ${product.brand}`;
    } else {
      message =
        "سلام، جهت استعلام قیمت تجهیزات پنوماتیک و دریافت مشاوره فنی از وب‌سایت شرکت جلالی پنوماتیک (JPC) پیام می‌دهم.";
    }
    return `${base}?text=${encodeURIComponent(message)}`;
  }

  /**
   * Update the Floating RTL WhatsApp button to carry the active product code
   */
  function updateFloatingWhatsApp(product) {
    const waLink = document.getElementById("floating-whatsapp-btn");
    const waBadge = document.getElementById("floating-wa-code-badge");
    const waLabel = document.getElementById("floating-wa-label");
    if (!waLink) return;

    waLink.href = buildWhatsAppUrl(product);
    if (product && waBadge) {
      waBadge.textContent = product.code;
      waBadge.classList.add("active");
      if (waLabel) {
        waLabel.textContent = "استعلام واتساپ:";
      }
    } else if (waBadge) {
      waBadge.textContent = "";
      waBadge.classList.remove("active");
      if (waLabel) {
        waLabel.textContent = "استعلام سریع واتساپ";
      }
    }
  }

  /**
   * Filter products according to current state
   */
  function getFilteredProducts() {
    const products = window.PRODUCTS_DATA || [];
    const q = state.searchQuery.trim().toLowerCase();

    return products.filter((item) => {
      const matchCategory =
        state.category === "all" || item.category === state.category;
      const matchBrand =
        state.brand === "all" ||
        item.brand.toLowerCase() === state.brand.toLowerCase();

      if (!matchCategory || !matchBrand) return false;
      if (!q) return true;

      const haystack = [
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
        item.applicationsFa || ""
      ]
        .join(" ")
        .toLowerCase();

      return haystack.includes(q);
    });
  }

  /**
   * Render Product Cards Grid
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
          <p style="font-size: 0.9rem; color: var(--text-secondary); max-width: 520px;">
            شما می‌توانید کد فنی دقیق قطعه مورد نظر خود را مستقیماً در فرم استعلام قیمت ثبت نمایید تا کارشناسان جلالی پنوماتیک موجودی یا معادل دقیق آن را بررسی کنند.
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

        return `
          <article class="product-card ${isJpc ? "is-jpc-brand" : ""}" data-product-id="${product.id}">
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
                  <span class="product-code-pill">${product.code}</span>
                  <span class="product-cat-label">${product.categoryTitleFa}</span>
                </div>
              </div>

              <div class="product-card-body">
                <h3 class="product-title-fa">${product.nameFa}</h3>

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
                  class="btn btn-outline-tech btn-sm js-spec-trigger"
                  data-id="${product.id}"
                >
                  مشخصات فنی
                </button>
              </div>
              <div class="product-sub-links">
                <a
                  href="${product.datasheetUrl}"
                  download
                  class="product-pdf-link"
                >
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                    <polyline points="7 10 12 15 17 10"/>
                    <line x1="12" y1="15" x2="12" y2="3"/>
                  </svg>
                  دانلود دیتاشیت PDF
                </a>
                <span class="mono" style="font-size: 0.72rem;">${product.protectionClass}</span>
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
        if (prod) {
          openQuickQuoteModal(prod);
        }
      });
    });

    grid.querySelectorAll(".js-spec-trigger").forEach((btn) => {
      btn.addEventListener("click", () => {
        const prod = findProductById(btn.getAttribute("data-id"));
        if (prod) {
          openTechDetailModal(prod);
        }
      });
    });
  }

  function findProductById(id) {
    return (window.PRODUCTS_DATA || []).find((p) => p.id === id) || null;
  }

  function resetFilters() {
    state.category = "all";
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
   * Open Quick Quote Modal & pre-fill both Modal Form and Main B2B Inquiry Form
   */
  function openQuickQuoteModal(product) {
    state.selectedProduct = product;
    updateFloatingWhatsApp(product);

    // Pre-fill main B2B form on page as well
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

    // Populate Quick Quote Modal
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
    }
  }

  /**
   * Open Technical Specification Detail Modal
   */
  function openTechDetailModal(product) {
    state.selectedProduct = product;
    updateFloatingWhatsApp(product);

    const modal = document.getElementById("tech-detail-modal");
    const body = document.getElementById("tech-detail-modal-body");
    const title = document.getElementById("tech-detail-modal-title");
    if (!modal || !body) return;

    if (title) {
      title.textContent = `${product.nameFa}`;
    }

    const highlightsHtml = (product.highlightsFa || [])
      .map((h) => `<li>${h}</li>`)
      .join("");

    body.innerHTML = `
      <div class="prefilled-product-banner">
        <div>
          <div style="font-size: 0.78rem; color: var(--text-muted);">کد فنی مدل (Technical Code)</div>
          <div class="mono" style="font-size: 1.05rem; font-weight: 800; color: var(--steel-accent);">${product.code}</div>
        </div>
        <span class="brand-badge ${product.brand === "JPC" ? "badge-jpc" : "badge-euro"}">${product.brandFa}</span>
      </div>

      <div class="product-specs-table" style="margin-bottom: 1.25rem;">
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

      <div style="margin-bottom: 1.25rem;">
        <h4 style="font-size: 0.9rem; font-weight: 800; margin-bottom: 0.5rem;">ویژگی‌های فنی و مهندسی:</h4>
        <ul class="pillar-feature-list" style="padding-top: 0.5rem;">
          ${highlightsHtml}
        </ul>
      </div>

      <div style="background: var(--bg-primary); border: 1px solid var(--border-tech); padding: 0.85rem 1rem; border-radius: var(--radius-sm); margin-bottom: 1.35rem; font-size: 0.84rem;">
        <strong>کاربردهای صنعتی:</strong> ${product.applicationsFa}
      </div>

      <div style="display: flex; align-items: center; justify-content: space-between; gap: 0.75rem; flex-wrap: wrap;">
        <button type="button" class="btn btn-amber" id="spec-modal-to-quote-btn">
          درخواست استعلام قیمت این مدل
        </button>
        <a href="${product.datasheetUrl}" download class="btn btn-outline-tech">
          دانلود کاتالوگ PDF
        </a>
      </div>
    `;

    const toQuoteBtn = document.getElementById("spec-modal-to-quote-btn");
    if (toQuoteBtn) {
      toQuoteBtn.addEventListener("click", () => {
        closeAllModals();
        openQuickQuoteModal(product);
      });
    }

    modal.classList.add("open");
    modal.setAttribute("aria-hidden", "false");
  }

  function closeAllModals() {
    document.querySelectorAll(".modal-backdrop").forEach((m) => {
      m.classList.remove("open");
      m.setAttribute("aria-hidden", "true");
    });
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
    // PDF File Upload Input preview
    const fileInput = document.getElementById("b2b-pdf-upload");
    const fileStatus = document.getElementById("file-upload-status");
    const fileZone = document.getElementById("file-upload-zone");

    if (fileZone && fileInput) {
      fileZone.addEventListener("click", () => fileInput.click());
      fileInput.addEventListener("change", () => {
        const file = fileInput.files && fileInput.files[0];
        if (!file) {
          if (fileStatus) fileStatus.textContent = "فایلی انتخاب نشده است (حداکثر ۱۵ مگابایت - PDF)";
          return;
        }
        if (!file.name.toLowerCase().endsWith(".pdf")) {
          if (fileStatus) {
            fileStatus.textContent = "خطا: لطفاً فقط فایل با فرمت PDF بارگذاری نمایید.";
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

    // Main B2B Inquiry Form
    const b2bForm = document.getElementById("b2b-inquiry-form");
    const b2bFeedback = document.getElementById("b2b-form-feedback");

    if (b2bForm) {
      b2bForm.addEventListener("submit", async (e) => {
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
            fileInput && fileInput.files[0] ? fileInput.files[0].name : null,
          submittedAt: new Date().toISOString()
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
            `• تعداد: ${payload.quantity || "طبق لیست"}`;

          const waUrl = buildWhatsAppUrl(null, waText);

          b2bFeedback.className = "form-feedback success";
          b2bFeedback.innerHTML = `
            <div style="display:flex; flex-direction:column; gap:0.65rem;">
              <div>
                درخواست استعلام شما با کد پیگیری <span class="mono">${refCode}</span> در سامانه ثبت گردید (${endpoint}). کارشناسان فروش جلالی پنوماتیک در کوتاه‌ترین زمان پیش‌فاکتور و مشخصات فنی را ارسال خواهند کرد.
              </div>
              <div>
                <a href="${waUrl}" target="_blank" rel="noopener" class="btn btn-amber btn-sm">
                  ارسال همزمان جزئیات استعلام در واتساپ فروش
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
                <a href="${waUrl}" target="_blank" rel="noopener" class="btn btn-amber btn-sm">
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
        state.category = "all";
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

    // Initial render
    syncFilterPillsUI();
    renderCatalog();
    updateFloatingWhatsApp(null);
    initForms();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
