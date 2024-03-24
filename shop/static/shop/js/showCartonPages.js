// make cart on startup
function makeCart() {
    if (localStorage.getItem("cart") == null) {
        var cart = {};
        // Display Cart Items
        showCartItems(cart)
    }
    else {
        cart = JSON.parse(localStorage.getItem("cart"));
        // Display Cart Items
        showCartItems(cart)
    };
    return cart

}
var cart = makeCart()



// Show Cart Items
function showCartItems(cart) {
    let cartItems = 0;
    for (let value of Object.values(cart)) {
        cartItems += value[0];
    };
    document.getElementById('cart-items').innerText = cartItems;
};

function addCart(itsId) {
    let cart = makeCart()
    if (cart[itsId] != undefined) {
        cart[itsId][0] = cart[itsId][0] + 1;
    }
    else {
        let qty = 1;
        let name = document.getElementById(`name${itsId}`).innerHTML.slice(0,40) + "..."
        let price = parseInt(document.getElementById(`price${itsId}`).innerHTML)
        cart[itsId] = [qty, name, price]
    };
    // console.log(cart)
    localStorage.setItem('cart', JSON.stringify(cart));

    // Display Cart Items
    showCartItems(cart)
};

document.getElementById("popcart").addEventListener("pointerdown", () => {
    window.location.href = "/shop/checkout/";
});