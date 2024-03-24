
// Bootstrap popover enable
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl);
});

// To allow attribute in pop over
const myDefaultAllowList = bootstrap.Tooltip.Default.allowList

// To allow button elements
myDefaultAllowList.button = ["onclick"]





// Modal image preview
var exampleModal = document.getElementById('exampleModal')
exampleModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget;
    // Extract info from data-bs-* attributes
    var src = button.getAttribute('data-bs-src');
    var alt = button.getAttribute('data-bs-alt');
    var desc = button.getAttribute('data-bs-desc');
    var price = button.getAttribute('data-bs-price');

    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    var modalImg = exampleModal.querySelector('.modal-Img');
    var modalTitle = exampleModal.querySelector('.modal-title');
    var modalDesc = exampleModal.querySelector('.modal-desc');
    var modalPrice = exampleModal.querySelector('.modal-price');

    modalImg.src = src;
    modalImg.alt = alt;
    modalTitle.innerHTML = alt;
    modalDesc.innerHTML = desc;
    modalPrice.innerHTML = price;
})


// make cart on startup
function makeCart() {
    if (localStorage.getItem("cart") == null) {
        var cart = {};
        // Display Cart Items
        showCartItems(cart)
        updateCart(cart)
    }
    else {
        cart = JSON.parse(localStorage.getItem("cart"));
        // Display Cart Items
        showCartItems(cart)
        updateCart(cart)
    };
    return cart

}
var cart = makeCart()

// If the add to cart/plus button is clicked, add/increment the item
function addCart(itsId) {
    let cart = makeCart()
    if (cart[itsId] != undefined) {
        cart[itsId][0] = cart[itsId][0] + 1;
    }
    else {
        let qty = 1;
        let name = document.getElementById(`name${itsId}`).innerHTML
        let price = parseInt(document.getElementById(`price${itsId}`).innerHTML)
        cart[itsId] = [qty, name, price]
    };
    console.log(cart)
    localStorage.setItem('cart', JSON.stringify(cart));

    // Display Cart Items
    showCartItems(cart)
    updateCart(cart)
};

// If the minus  button is clicked, minus the item
function removeCart(itsId) {
    let cart = makeCart()
    if (cart[itsId][0] > 0) {
        cart[itsId][0] = cart[itsId][0] - 1

        // Display Cart Items
        showCartItems(cart)
        updateCart(cart)

        // delete item from cart
        if (cart[itsId][0] == 0) {
            delete cart[itsId]

        };
    };

    if (cart[itsId] == undefined) {
        document.getElementById(`div${itsId}`).innerHTML = `<button class="btn btn-dark cart" onclick="addCart(this.id)"
            id="${itsId}">Add to Cart</button>`
    }


    console.log(cart)
    localStorage.setItem('cart', JSON.stringify(cart));


};

// Show Cart Items
function showCartItems(cart) {
    let cartItems = 0;
    for (let value of Object.values(cart)) {
        cartItems += value[0];
    };
    document.getElementById('cart-items').innerText = cartItems;
};

// Update The Cart
function updateCart(cart) {
    if (cart != undefined) {
        for (var item in cart) {
            document.getElementById(`div${item}`).innerHTML = `<button id="minus${item}" class="btn btn-dark" onclick="removeCart(this.id.slice(5,))">-</button>
                    <span id="val${item}">${cart[item][0]}</span>
                    <button id="plus${item}" class="btn btn-dark" onclick="addCart(this.id.slice(4,))">+</button>`
        };
    } else {
        return cart
    }
    console.log(localStorage.cart)
    updatePopover(cart)

};


// Clear cart
function clearCart() {
    let cart = JSON.parse(localStorage.getItem("cart"))
    for (item in cart) {
        document.getElementById(`div${item}`).innerHTML = `<button class="btn btn-dark cart" onclick="addCart(this.id)" id="${item}">Add to Cart</button>`
    }
    const list = document.getElementById("popoverItems");

    while (list.hasChildNodes()) {
        list.removeChild(list.firstChild);
    }
    localStorage.clear();
    cart = {};
    updateCart(cart);
    showCartItems(cart);

}


// Pop Cart
function updatePopoverBoot(content) {
    const popCart = document.getElementById('popcart');
    const popover = new bootstrap.Popover(popCart, {
        content: content,
        // trigger: "focus",
        container: "body"
    }
    );
    // popover.Popover('show')

};

// Product View
function productView(itsId) {
    window.location = `productview/${itsId.slice(3,)}`
}

// Update Popover
function updatePopover(cart) {
    var popStr = "";
    popStr += `<h5 class="mb-4"> Cart for your items in my shopping cart </h5><div id="popoverItems"`;
    var i = 1;
    for (var item in cart) {
        popStr += `<div class="my-2"><b>${i}</b>. ${cart[item][1]}... <b>Qty:</b> ${cart[item][0]}</div> <br>`
        i++
    };
    popStr += `</div><div class="d-flex justify-content-evenly"><button class="btn btn-outline-dark" id="clearCart" onclick="clearCart()">Clear Cart</button><a class="btn btn-dark" href="checkout/">Checkout</a></div>`
    updatePopoverBoot(popStr)

};
