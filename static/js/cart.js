$(document).ready(function () {
    $('.btt-link').click(function(e) {
        window.scrollTo(0,0)
    })
    $('.update-cart').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    })
});