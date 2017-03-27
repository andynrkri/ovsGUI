var tree;
tree = document.querySelectorAll('ul.tree a:not(:last-child)');
for (var i = 0; i < tree.length; i++) {
    tree[i].addEventListener('click', function (e) {
        var parent = e.target.parentElement;
        var classList = parent.classList;
        if (classList.contains("open")) {
            classList.remove('open');
            var opensubs = parent.querySelectorAll(':scope .open');
            for (var i = 0; i < opensubs.length; i++) {
                opensubs[i].classList.remove('open');
            }
        } else {
            classList.add('open');
        }
    });
}
function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false);
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function myFunction1() {
    document.getElementById("demo1").innerHTML = httpGet("/getbridges")
}
function myFunction2() {
    document.getElementById("demo2").innerHTML = httpGet("/getbridges")
}
function myFunction3() {
    document.getElementById("demo3").innerHTML = httpGet("/getbridges")
}
function myFunction4() {
    document.getElementById("demo4").innerHTML = httpGet("/getbridges")
}
