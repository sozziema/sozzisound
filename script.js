const menuButton = document.querySelector('.menu-button');
const menu = document.querySelector('.menu');

if (menuButton && menu) {
  menuButton.addEventListener('click', () => {
    const isOpen = menu.classList.toggle('open');
    menuButton.setAttribute('aria-expanded', isOpen);
    menuButton.textContent = isOpen ? '×' : '☰';
  });

  menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
    menu.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.textContent = '☰';
  }));
}

const yearEl = document.querySelector('#year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

const contactForm = document.querySelector('#contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const subject = encodeURIComponent(`Richiesta di consulenza acustica - ${formData.get('nome')}`);
    const body = encodeURIComponent(`Nome: ${formData.get('nome')}\nEmail: ${formData.get('email')}\n\nRichiesta:\n${formData.get('messaggio')}`);
    window.location.href = `mailto:info@sozzisound.it?subject=${subject}&body=${body}`;
  });
}

// Consenso cookie (Google Consent Mode v2)
const CONSENT_KEY = 'sozzisound-cookie-consent';
const banner = document.querySelector('#cookie-banner');

function applyConsent(granted) {
  if (typeof gtag !== 'function') return;
  const state = granted ? 'granted' : 'denied';
  gtag('consent', 'update', {
    ad_storage: state,
    ad_user_data: state,
    ad_personalization: state,
    analytics_storage: state,
  });
}

// Pulsante flottante WhatsApp
const whatsappLink = document.createElement('a');
whatsappLink.id = 'whatsapp-button';
whatsappLink.href = 'https://wa.me/393348748771?text=' + encodeURIComponent('Ciao, vorrei richiedere una consulenza acustica.');
whatsappLink.target = '_blank';
whatsappLink.rel = 'noopener noreferrer';
whatsappLink.setAttribute('aria-label', 'Contattaci su WhatsApp');
whatsappLink.innerHTML = '<svg viewBox="0 0 32 32" width="30" height="30" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.004 3C9.383 3 4 8.373 4 15c0 2.393.7 4.623 1.902 6.5L4 29l7.71-1.863A11.9 11.9 0 0 0 16.004 27C22.625 27 28 21.627 28 15S22.625 3 16.004 3zm0 21.6c-1.98 0-3.822-.55-5.395-1.5l-.386-.23-4.57 1.104 1.14-4.457-.25-.398A9.55 9.55 0 0 1 5.4 15c0-5.302 4.31-9.6 9.604-9.6 5.293 0 9.6 4.298 9.6 9.6 0 5.302-4.307 9.6-9.6 9.6zm5.29-7.19c-.29-.146-1.716-.847-1.982-.943-.266-.097-.46-.146-.654.146-.194.291-.75.943-.92 1.137-.17.194-.34.218-.63.073-.29-.146-1.224-.451-2.332-1.44-.862-.769-1.444-1.72-1.613-2.01-.17-.29-.018-.447.128-.592.13-.13.29-.34.435-.51.146-.17.194-.291.29-.485.097-.194.049-.364-.024-.51-.073-.146-.654-1.576-.897-2.158-.236-.567-.477-.49-.654-.5l-.557-.01c-.194 0-.51.073-.777.364-.267.291-1.02.996-1.02 2.428 0 1.432 1.044 2.816 1.19 3.01.146.194 2.055 3.14 4.98 4.404.696.3 1.24.48 1.663.615.699.222 1.334.19 1.837.115.56-.084 1.716-.702 1.958-1.38.243-.68.243-1.262.17-1.38-.072-.12-.266-.194-.556-.34z"/></svg>';
document.body.appendChild(whatsappLink);

function keepWhatsappAboveBanner() {
  if (banner && !banner.hidden) {
    const bannerTop = banner.getBoundingClientRect().top;
    const clearance = Math.max(0, window.innerHeight - bannerTop) + 14;
    whatsappLink.style.bottom = clearance + 'px';
  } else {
    whatsappLink.style.bottom = '';
  }
}

function hideBanner() {
  if (banner) banner.hidden = true;
  keepWhatsappAboveBanner();
}

const storedConsent = localStorage.getItem(CONSENT_KEY);
if (storedConsent) {
  applyConsent(storedConsent === 'granted');
} else if (banner) {
  banner.hidden = false;
}
keepWhatsappAboveBanner();
window.addEventListener('resize', keepWhatsappAboveBanner);

document.querySelector('#cookie-accept')?.addEventListener('click', () => {
  localStorage.setItem(CONSENT_KEY, 'granted');
  applyConsent(true);
  hideBanner();
});

document.querySelector('#cookie-reject')?.addEventListener('click', () => {
  localStorage.setItem(CONSENT_KEY, 'denied');
  applyConsent(false);
  hideBanner();
});

document.querySelector('#cookie-manage')?.addEventListener('click', (event) => {
  event.preventDefault();
  localStorage.removeItem(CONSENT_KEY);
  if (banner) banner.hidden = false;
  keepWhatsappAboveBanner();
});
