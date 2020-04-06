var product = document.getElementById('product');
var xmlhttp = new XMLHttpRequest();
var host = "http://0.0.0.0:8000/products/";
var pagination = "?limit=20&offset=20";
var url = host + pagination;
var search = '?search=';
var buttonPrevious = document.getElementById("previous");
var buttonNext = document.getElementById("next");
var pagination_previous;
var pagination_next;


window.addEventListener("load", function(event) {
    buttonPrevious.addEventListener('click', function(event) {
        pagination = pagination_previous;
        console.log(pagination);
    });

    buttonNext.addEventListener('click', function(event) {
        pagination = pagination_next;
        console.log(pagination);
    });

    GetProductsFromApi();
    

function GetProductsFromApi () {
    xmlhttp.open("GET", url, true);
    xmlhttp.responseType = 'json';
    xmlhttp.send();

    xmlhttp.onload = function() {
        var products = xmlhttp.response;
        var products_results = products.results;
        pagination_next = products.next;
        pagination_previous = product.previous;
        showProducts(products_results);
    };

function showProducts(jsonObj) {
    var newArticle;
    var paragraphItem = document.createElement('a');
    var bookimg = document.createElement('img');
    var element;

    for (var i=0; i<Object.keys(jsonObj).length;i++){
        newArticle = document.createElement('article');
        element = jsonObj[i].attributes;
        bookimg = document.createElement('img') ;
        bookimg.src = element.medium_image_URL;

        paragraphItem = document.createElement('a');

        paragraphItem.innerHTML = '<h5>' + element.author + '<br>' + element.book_title + '<br></h5>' + 'ISBN: ' + element.ISBN + '<br>' + element.publisher;
        paragraphItem.href = url + jsonObj[i].id;
        
        newArticle.appendChild(bookimg);
        newArticle.appendChild(paragraphItem);
        product.appendChild(newArticle);
    }
    
}
}
});