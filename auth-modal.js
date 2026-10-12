/* ============================================================
   DELI & SANDWICH - AUTH & ORDER NOW MODAL INTERACTIVE LOGIC
   ============================================================ */

(function () {
  // Global modal state & references
  let isDelivery = true;
  let basePrice = 12.99;
  let deliveryFee = 2.99;
  let quantity = 1;

  // DOM Elements
  const modalOverlay = document.getElementById('authModalOverlay');
  const modalClose = document.getElementById('authModalClose');
  const modalTitle = document.getElementById('modalTitle');
  const modalSubtitle = document.getElementById('modalSubtitle');
  
  const tabBtns = document.querySelectorAll('.auth-tab-btn');
  const tabPanes = document.querySelectorAll('.auth-tab-pane');

  const orderItemSelect = document.getElementById('orderItem');
  const qtyVal = document.getElementById('qtyVal');
  const qtyMinus = document.getElementById('qtyMinus');
  const qtyPlus = document.getElementById('qtyPlus');

  const summarySubtotal = document.getElementById('summarySubtotal');
  const summaryDelivery = document.getElementById('summaryDelivery');
  const summaryTotal = document.getElementById('summaryTotal');

  const orderTypeOptions = document.querySelectorAll('.order-type-option');
  const addressGroup = document.getElementById('addressGroup');

  // ---------- OPEN & CLOSE MODAL ----------
  window.openAuthModal = function (targetTab) {
    if (!modalOverlay) return;
    modalOverlay.classList.add('open');
    modalOverlay.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    if (targetTab) {
      switchTab(targetTab);
    }
  };

  window.closeAuthModal = function () {
    if (!modalOverlay) return;
    modalOverlay.classList.remove('open');
    modalOverlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  };

  // Close handlers
  if (modalClose) {
    modalClose.addEventListener('click', closeAuthModal);
  }

  if (modalOverlay) {
    modalOverlay.addEventListener('click', function (e) {
      if (e.target === modalOverlay) {
        closeAuthModal();
      }
    });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modalOverlay && modalOverlay.classList.contains('open')) {
      closeAuthModal();
    }
  });

  // Attach listeners to Order Now & Login buttons
  function attachButtonTriggers() {
    const path = window.location.pathname.toLowerCase();
    const isOrderPage = path.includes('login.html') || path.includes('order.html');

    if (isOrderPage) {
      // On standalone order page, clicking Order Now switches to order tab and scrolls to form
      const pageOrderTriggers = document.querySelectorAll('.order-btn, .mobile-order-btn, [href="#order"]');
      pageOrderTriggers.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
          e.preventDefault();
          switchTab('tabOrder');
          const card = document.querySelector('.standalone-card-container');
          if (card) card.scrollIntoView({ behavior: 'smooth' });
        });
      });
    } else {
      // On other pages, if any order button is a <button>, navigate to login.html on click
      const orderButtons = document.querySelectorAll('button.order-btn, button.mobile-order-btn');
      orderButtons.forEach(function (btn) {
        btn.addEventListener('click', function () {
          window.location.href = 'login.html';
        });
      });
    }

    // Modal triggers only for elements explicitly requesting popup modal
    const modalOrderTriggers = document.querySelectorAll('[data-open-modal="order"]');
    modalOrderTriggers.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        window.openAuthModal('tabOrder');
      });
    });

    const modalLoginTriggers = document.querySelectorAll('[data-open-modal="login"]');
    modalLoginTriggers.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        window.openAuthModal('tabLogin');
      });
    });
  }

  // Handle URL hash on load (e.g. login.html#login)
  function handleUrlHash() {
    const hash = window.location.hash;
    if (hash === '#login') {
      switchTab('tabLogin');
    } else if (hash === '#register') {
      switchTab('tabRegister');
    } else if (hash === '#order') {
      switchTab('tabOrder');
    }
  }

  // ---------- TAB SWITCHING ----------
  window.switchTab = function switchTab(tabId) {
    tabBtns.forEach(function (btn) {
      const isTarget = btn.getAttribute('data-tab') === tabId;
      btn.classList.toggle('active', isTarget);
      btn.setAttribute('aria-selected', isTarget ? 'true' : 'false');
    });

    tabPanes.forEach(function (pane) {
      pane.classList.toggle('active', pane.id === tabId);
    });

    // Update modal header text based on active tab
    if (tabId === 'tabOrder') {
      if (modalTitle) modalTitle.innerText = 'Order Fresh Sandwiches';
      if (modalSubtitle) modalSubtitle.innerText = 'Customize your sandwich & get fast delivery to your doorstep';
    } else if (tabId === 'tabLogin') {
      if (modalTitle) modalTitle.innerText = 'Welcome Back!';
      if (modalSubtitle) modalSubtitle.innerText = 'Sign in to access your saved orders & exclusive rewards';
    } else if (tabId === 'tabRegister') {
      if (modalTitle) modalTitle.innerText = 'Create an Account';
      if (modalSubtitle) modalSubtitle.innerText = 'Join Deli & Sandwich to earn points on every bite';
    }
  }

  tabBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      const tabId = this.getAttribute('data-tab');
      switchTab(tabId);
    });
  });

  // ---------- PRICE CALCULATION & ORDER LOGIC ----------
  function updatePrices() {
    if (orderItemSelect) {
      basePrice = parseFloat(orderItemSelect.value) || 12.99;
    }
    const subtotal = basePrice * quantity;
    const currentDelivery = isDelivery ? deliveryFee : 0.00;
    const total = subtotal + currentDelivery;

    if (summarySubtotal) summarySubtotal.innerText = '$' + subtotal.toFixed(2);
    if (summaryDelivery) summaryDelivery.innerText = isDelivery ? '$' + currentDelivery.toFixed(2) : 'FREE';
    if (summaryTotal) summaryTotal.innerText = '$' + total.toFixed(2);
  }

  if (orderItemSelect) {
    orderItemSelect.addEventListener('change', updatePrices);
  }

  if (qtyMinus) {
    qtyMinus.addEventListener('click', function () {
      if (quantity > 1) {
        quantity--;
        if (qtyVal) qtyVal.innerText = quantity;
        updatePrices();
      }
    });
  }

  if (qtyPlus) {
    qtyPlus.addEventListener('click', function () {
      quantity++;
      if (qtyVal) qtyVal.innerText = quantity;
      updatePrices();
    });
  }

  // Delivery vs Pickup selection
  orderTypeOptions.forEach(function (opt) {
    opt.addEventListener('click', function () {
      orderTypeOptions.forEach(o => o.classList.remove('active'));
      this.classList.add('active');
      const radio = this.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;

      isDelivery = radio.value === 'delivery';
      if (addressGroup) {
        addressGroup.style.display = isDelivery ? 'flex' : 'none';
      }
      updatePrices();
    });
  });

  // ---------- FORM SUBMIT HANDLERS ----------
  window.handleOrderSubmit = function () {
    const name = document.getElementById('orderName')?.value || 'Customer';
    const itemOption = orderItemSelect?.options[orderItemSelect.selectedIndex];
    const itemName = itemOption ? itemOption.getAttribute('data-name') : 'Sandwich';
    const total = summaryTotal ? summaryTotal.innerText : '$15.98';

    showToast(`🎉 Thank you, ${name}! Your order for ${quantity}x ${itemName} (${total}) has been placed!`, 'success');
    closeAuthModal();
  };

  window.handleLoginSubmit = function () {
    const email = document.getElementById('loginEmail')?.value || 'User';
    showToast(`🔑 Welcome back! Signed in as ${email}`, 'success');
    closeAuthModal();
  };

  window.handleRegisterSubmit = function () {
    const name = document.getElementById('regName')?.value || 'Friend';
    showToast(`✨ Welcome aboard, ${name}! Your account has been created.`, 'success');
    closeAuthModal();
  };

  window.handleSocialLogin = function (provider) {
    showToast(`🌐 Signed in with ${provider} successfully!`, 'success');
    closeAuthModal();
  };

  // Password Visibility Toggle
  window.togglePasswordVisibility = function (inputId, btn) {
    const input = document.getElementById(inputId);
    if (!input) return;
    const icon = btn.querySelector('i');
    if (input.type === 'password') {
      input.type = 'text';
      if (icon) icon.className = 'fas fa-eye-slash';
    } else {
      input.type = 'password';
      if (icon) icon.className = 'fas fa-eye';
    }
  };

  // ---------- TOAST NOTIFICATIONS ----------
  window.showToast = function (message, type) {
    let container = document.getElementById('toastContainer');
    if (!container) {
      container = document.createElement('div');
      container.id = 'toastContainer';
      container.className = 'toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `toast ${type === 'success' ? 'toast-success' : ''}`;
    toast.innerHTML = `<i class="fas fa-check-circle"></i> <span>${message}</span>`;
    container.appendChild(toast);

    setTimeout(function () {
      toast.classList.add('toast-hiding');
      setTimeout(function () {
        if (toast.parentNode) toast.parentNode.removeChild(toast);
      }, 300);
    }, 4000);
  };

  // Initialize triggers on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      attachButtonTriggers();
      updatePrices();
      handleUrlHash();
    });
  } else {
    attachButtonTriggers();
    updatePrices();
    handleUrlHash();
  }

})();
