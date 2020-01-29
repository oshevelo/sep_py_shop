var order = document.getElementById("order");
var xmlhttp = new XMLHttpRequest();
var url = "http://127.0.0.1:8000/shipments/";
var search = '?search=';
var buttonElement = document.getElementById("button");

buttonElement.addEventListener("click", function(event) {
  
  var ordercode = getInputValue();

  xmlhttp.open("GET", url + search + ordercode, true);
  xmlhttp.responseType = 'json';
  xmlhttp.send();

  xmlhttp.onload = function() {
    var shipmentInfo = xmlhttp.response;

    if (Object.keys(shipmentInfo.results).length === 0) { // Order not found
      OrderNotFound();
    } else if (Object.keys(shipmentInfo.results).length === 1) { // Ruturn order
      showOrder(shipmentInfo);
    } else {
      OrderNotFound();
    }
  };


function getInputValue(){
  var inputVal = document.getElementById('get_order').value;
  return inputVal;
}

function OrderNotFound () {
  var myH1;
  if (order.hasChildNodes()) {
    console.log(order.hasChildNodes(), order.childNodes);
    order.removeChild(order.childNodes[0]);
    console.log(order.hasChildNodes(), order.childNodes);
    myH1 = document.createElement('h1');
    myH1.textContent = "Order not found";
} else {
    console.log(order.hasChildNodes(), order.childNodes);
    myH1 = document.createElement('h1');
    myH1.textContent = "Order not found";
    order.appendChild(myH1);
  }

}

function showOrder(jsonObj) {
  var myArticle = document.createElement('article');
  var myH1 = document.createElement('h1');

  myH1.textContent = "Order: " + jsonObj.results[0].public_id.id;

  myArticle.appendChild(myH1);

  var myP = document.createElement('p');
  myP.textContent = "Phone: " + jsonObj.results[0].public_id.phone;
  myArticle.appendChild(myP);

  var myP2 = document.createElement('p');
  myP2.textContent = "Date of order: " + jsonObj.results[0].public_id.date_of_order.substr(0, 10);
  myArticle.appendChild(myP2);

  var shipmentDetails = jsonObj.results[0];

  var shipmentDetailHeader = document.createElement('h1');
  shipmentDetailHeader.textContent = "Shipment details: ";

  myArticle.appendChild(shipmentDetailHeader);

  var myList = document.createElement('ul');

    for (var i = 1; i < Object.keys(shipmentDetails).length-1; i++) {
      var listItem = document.createElement('li');
      var element = Object.keys(shipmentDetails)[i];
      listItem.textContent = element+ ": " + shipmentDetails[element];
      myList.appendChild(listItem);
    }
  myArticle.appendChild(myList);

  order.appendChild(myArticle);

  //   if (order.hasChildNodes) {
  //     order.removeChild(order.childNodes[0]);
  //   } else {
  //   order.appendChild(myArticle);
  // }
}
});
