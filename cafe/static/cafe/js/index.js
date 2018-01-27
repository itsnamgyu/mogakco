$.fn.isInViewport = function() {
    var elementTop = $(this).offset().top;
    var elementBottom = elementTop + $(this).outerHeight();
    var viewportTop = $(window).scrollTop;
    var viewportBottom = viewportTop + $(window).height();
    return elementBottom > viewportTop && elementTop < viewportBottom;
};

function animate(highResTimestamp) {
    requestAnimationFrame(animate);


}

$(document).ready(function() {
    requestAnimationFrame(animate);
});
