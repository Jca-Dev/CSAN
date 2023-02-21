$(document).ready(function () {
    $(".show").click(function () {
        $(".half-content").hide(),
            $(".full-content").show();
    });
    $(".hide").click(function () {
        $(".full-content").hide(),
            $(".half-content").show();
    });

    $(document).on('click', '.confirm-delete', function(){
        return confirm('Are you sure you want to delete {{ product.name }}?'
        );
})});