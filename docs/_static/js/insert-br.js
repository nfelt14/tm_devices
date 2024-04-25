document.addEventListener('DOMContentLoaded', function () {
    var properties = document.querySelectorAll('details.quote');
    properties.forEach(function (prop) {
        var numberOfBreaks = 1; // Number of <br> elements you want to insert
        for (var i = 0; i < numberOfBreaks; i++) {
            var br = document.createElement('br');
            prop.parentNode.insertBefore(br, prop.nextSibling);
        }
    });
});
