$(document).ready(function () {
    glowCookies.start('en', { 
        style: 1,
        analytics: 'G-FH87DE17XF', 
        facebookPixel: '990955817632355',
        policyLink: 'https://www.privacypolicygenerator.info/live.php?token=cXfHIKF1soN81fZF1OQKU1J8PuaA3C4K'
    });
    var toastElList = [].slice
      .call(document.querySelectorAll('.toast'));
    var toastList = toastElList.map(function (toastEl) {
      return new bootstrap.Toast(toastEl, {delay: 2000});
    });
    toastList.forEach(toast => toast.show());
});