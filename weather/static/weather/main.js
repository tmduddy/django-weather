const getCookieValue = (name) => (
  document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop()
)

function assignDarkMode() {
  const fullPage = document.querySelector('body');
  const dark_mode_preference = getCookieValue('dark_mode') || 'dark-mode-on';
  console.log('cookie value onLoad: ' + getCookieValue('dark_mode'))

  fullPage.setAttribute('class', dark_mode_preference)

  
}

function darkModeSwap() {

  const fullPage = document.querySelector('body');

  const existing_class = fullPage.getAttribute('class') || '';

  if (existing_class.includes('dark-mode-off')) {
    document.cookie = 'dark_mode=dark-mode-on; path=/';
    fullPage.setAttribute('class', 'dark-mode-on');
  } else {
    document.cookie = 'dark_mode=dark-mode-off; path=/';
    fullPage.setAttribute('class', 'dark-mode-off');
  }

  console.log('cookie value onClick ' + getCookieValue('dark_mode'))
}