$(document).ready(function () {

    $('.increment-btn').click(function (e) { 
        e.preventDefault();

        var inc_value = $(this).closest('.product-data').find('.qnt-input').val();
        var value = parseInt(inc_value, 6);
        value = isNaN(value) ? 0 : value;
        if (value < 5)
        {
            value++;
            $(this).closest('.product-data').find('.qnt-input').val(value);
        }
        
    });

    $('.decrement-btn').click(function (e) { 
        e.preventDefault();

        var dec_value = $(this).closest('.product-data').find('.qnt-input').val();
        var value = parseInt(dec_value, 6);
        value = isNaN(value) ? 0 : value;
        if (value > 1)
        {
            value--;
            $(this).closest('.product-data').find('.qnt-input').val(value);
        }
        
    });




    $('.add-to-cart').click(function (e) { 
        e.preventDefault();
    
        var product_id = $(this).closest('.product-data').find('.prod_id').val();
        var product_qty =  $(this).closest('.product-data').find('.qnt-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        $.ajax({
            method: "POST",
            url: "/add-to-cart/",
            data: {
                'product_id' : product_id,
                'product_qty' : product_qty,
                csrfmiddlewaretoken : token,
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status);
            }
        });

    });


    $('.wishlist').click(function (e) { 
        e.preventDefault();
        
        var product_id = $(this).closest('.product-data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-wishlist/",
            data: {
                'product_id' : product_id,
                csrfmiddlewaretoken : token,
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status);
            }
        });

    });


    $('.changeQuantity').click(function (e) { 
        e.preventDefault();
    
        var product_id = $(this).closest('.product-data').find('.prod_id').val();
        var product_qty =  $(this).closest('.product-data').find('.qnt-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

    
        $.ajax({
            method: "POST",
            url: "/update-cart/",
            data: {
                'product_id' : product_id,
                'product_qty' : product_qty,
                csrfmiddlewaretoken : token,
            },
            success: function (response) {
                alertify.success(response.status);
            }
        });

    });


    $(document).on('click', '.delete-cart-item', function (e) {
        e.preventDefault();
    
        var $deleteButton = $(this);
        var product_id = $deleteButton.closest('.product-data').find('.prod_id').val();               // var product_id = $(this).closest('.product-data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        $.ajax({
            method: "POST",
            url: "/delete-cart-item/",
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken': token,
            },
            success: function (response) {
                console.log("Server response: " + response.status);           //check in console what the server response return in string and pass in here in response.status
                if (response.status === "Removed Item Successfully") {
                    // alertify.success("Product removed successfully");      // never show the remove message to the user.
                    $deleteButton.closest('.cart-item').remove();            // remove function remove the product of the nearest class cart-item on every click without refreshing the whole page.
                } else {
                    alertify.error("Failed to remove the product");
                }
            },
            error: function () {
                alertify.error("An error occurred while removing the product");
            }
        });
    });


    $(document).on('click', '.delete-wishlist-item', function (e) {
        e.preventDefault();
    
        var $deleteButton = $(this);
        var product_id = $deleteButton.closest('.product-data').find('.prod_id').val();               // var product_id = $(this).closest('.product-data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
    
        $.ajax({
            method: "POST",
            url: "/delete-from-wishlist/",
            data: {
                'product_id': product_id,   
                'csrfmiddlewaretoken': token,
            },
            success: function (response) {
                console.log("Server response: " + response.status);           //check in console what the server response return in string and pass in here in response.status
                if (response.status === "Product Removed from Wishlist") {
                    // alertify.success("Product removed successfully");      // never show the remove message to the user.
                    $deleteButton.closest('.wishlist-item').remove();            // remove function remove the product of the nearest class cart-item on every click without refreshing the whole page.
                } else {
                    alertify.error("Failed to remove the product");
                }
            },
            error: function () {
                alertify.error("An error occurred while removing the product");
            }
        });
    });
    

});

// ----------------------------------------------------------------------------------------------------------------------

// ---------------- this jquery function is used to check the availability of the COD payemts and delivery available by entering the pincode --------------------------
$(document).ready(function () {
    $('#Pincode').click(function (e) { 
        e.preventDefault();

        var pincode = $('#inputPincode').val();  // Use the correct ID here
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'POST',
            url: '/check-delivery-area/',  // Replace with the actual URL
            data: { 
                'pincode': pincode,
                'csrfmiddlewaretoken': token, 
              },
            success: function (data) {
                if (isNaN(pincode)){
                    var deliveryText = "<span style='color: red;font-weight:500;'>Invalid Pincode</span>";
                    var codText = "";
                    var deliveryHeading = "";
                    var CODHeading = '';
                }else if(pincode === "" || pincode === null){
                    var deliveryText = "";
                    var codText = "";
                    var deliveryHeading = "";
                    var CODHeading = '';
                }else if (data.delivery_available) {
                    var deliveryHeading = "Delivery";
                    var CODHeading = "COD";
                    var deliveryText = 'This item can be <span style="color: green;">Delivered</span> to your location';
                    var codText = data.cod_available ? 'is <span style="color: green;">available</span> for this item' : 'is <span style="color: red;">not available</span> for this item.';
                } else {
                    var deliveryText = 'Sorry, Delivery is <span style="color: red;">not available</span> to this Pincode.';
                    var deliveryHeading = "Delivery";
                    var codText = '';
                    var CODHeading = '';
                }
                $('.left-half-right-for-delivery p').html(deliveryText);
                $('.left-half-right-for-delivery h3').html(deliveryHeading);
                $('.right-half-right-for-COD p').html(codText);
                $('.right-half-right-for-COD h3').html(CODHeading);
            }
        });
    });

    
});












// add to cart js and jsquery code with harry


// if (localStorage.getItem('cart') == null){
//     var cart = {};
// }else{
//     cart = JSON.parse(localStorage.getItem('cart'));
//     document.getElementById("cart").innerText = Object.keys(cart).length;
// }

// $('.cart').click(function () { 
    
//     var idstr = this.id.toString();
//     console.log(idstr);

//     if (cart[idstr] != undefined){
//         cart[idstr] = cart[idstr] + 1;
//     }else{
//         cart[idstr] = 1;
//     }
//     console.log(cart);
//     localStorage.setItem('cart', JSON.stringify(cart));
//     document.getElementById("cart").innerText = Object.keys(cart).length;


// });




// // message add to cart
// const addtocartmessage = document.getElementById("addcartmessage");
// console.log(addtocartmessage);
// const cartbtn = document.querySelector('add-to-cart');

// function doubleclick(){
//   addtocartmessage.innerHTML="Added To Cart!";
//   console.log("clicked")
// }


