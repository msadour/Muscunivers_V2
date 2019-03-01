$(function() {
    $(".color_hover").hover(
    function() {
        $(this).css('background-color', '#D8FEEC')
    }, function() {
        $(this).css('background-color', '')
    });
}
)