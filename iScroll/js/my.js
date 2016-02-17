var myScroll;
$(document).ready(function () {
    myScroll = new IScroll('#wrapper', {
        mouseWheel: true
    });
});
//document.addEventListener('touchmove', function (e) { e.preventDefault(); }, false);
