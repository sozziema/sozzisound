const menuButton = document.querySelector('.menu-button');
const menu = document.querySelector('.menu');

menuButton.addEventListener('click', () => {
  const isOpen = menu.classList.toggle('open');
  menuButton.setAttribute('aria-expanded', isOpen);
  menuButton.textContent = isOpen ? '×' : '☰';
});

document.querySelectorAll('.menu a').forEach((link) => link.addEventListener('click', () => {
  menu.classList.remove('open');
  menuButton.setAttribute('aria-expanded', 'false');
  menuButton.textContent = '☰';
}));

document.querySelector('#year').textContent = new Date().getFullYear();

document.querySelector('#contact-form').addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(event.currentTarget);
  const subject = encodeURIComponent(`Richiesta di consulenza acustica - ${formData.get('nome')}`);
  const body = encodeURIComponent(`Nome: ${formData.get('nome')}\nEmail: ${formData.get('email')}\n\nRichiesta:\n${formData.get('messaggio')}`);
  window.location.href = `mailto:sozzisoundsrl@gmail.com?subject=${subject}&body=${body}`;
});
