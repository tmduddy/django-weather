function darkModeSwap() {

  const fullPage = document.querySelector('body');

  const existing_class = fullPage.getAttribute('class');
  if (existing_class.includes('dark-mode-off')) {
    fullPage.setAttribute('class', existing_class.replace('dark-mode-off', 'dark-mode-on'));
  } else {
    fullPage.setAttribute('class', existing_class.replace('dark-mode-on', 'dark-mode-off'));
  }
}