function openMenu() {
  document.getElementsById('slidemenu').style.marginleft = '0';
  document.getElementsById('main').style.marginleft = '250px';
  document.body.style.backgroundcolor = 'rgba(0,0,0,0.4)';
}
function closeMenu() {
  document.getElementsById('slidemenu').style.marginleft = '-250px';
  document.getElementsById('main').style.marginleft = '0';
  document.body.style.backgroundcolor = '#fff';
}
