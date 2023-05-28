function allowDrop(event) {
    event.preventDefault();
}
function drop(event) {
    event.preventDefault();
    var product_id = event.dataTransfer.getData("text/plain");
    window.location.href=`assign/${product_id}`
}
// =====================================================================================
function allowDropbill(event) {
    event.preventDefault();
}
function dropbill(event) {
    event.preventDefault();
    var product_id = event.dataTransfer.getData("text/plain");
    window.location.href=`billable/${product_id}`
}
// ============================================================================================
function allowDropAvailable(event) {
    event.preventDefault();
}
function dropAvailable(event) {
    event.preventDefault();
    var product_id = event.dataTransfer.getData("text/plain");
    window.location.href=`billed-remove/${product_id}`
}
var products = document.querySelectorAll('.product');
products.forEach(function(product) {
    product.addEventListener('dragstart', function(event)
    {
        event.dataTransfer.setData("text/plain", event.target.id);
    });
});

// ======================menu script=====================================

function open_list(){
    var cancel = document.getElementById("cancel");
    var list = document.getElementById("list");
    var list_menu =  document.getElementById("list_menu");
    list.style.display="none";
    cancel.style.display="block";
    list_menu.style.display="block"
}
function close_list(){
    var cancel = document.getElementById("cancel");
    var list = document.getElementById("list");
    var list_menu =  document.getElementById("list_menu");
    list.style.display="block"
    cancel.style.display="none"
    list_menu.style.display="none"
}