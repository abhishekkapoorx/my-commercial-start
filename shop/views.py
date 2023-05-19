from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse  # For testing the app routing
from shop.models import Product, Contact, Order, OrderUpdate
from math import ceil
from datetime import datetime
import json
from django.contrib import messages

# Create your views here.
def index(request):
    allProds = []
    subcatprods = Product.objects.values('subcategory', 'id')
    subcats = {item["subcategory"] for item in subcatprods}
    for subcat in subcats:
        prod = Product.objects.filter(subcategory=subcat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name').title()
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        dateAdded = datetime.now().strftime(r"%Y-%m-%d")
        contact = Contact(
            name = name,
            email = email,
            phone = phone,
            desc = desc,
            dateAdded = dateAdded
        )
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, "shop/contact.html")


def tracker(request):
    if request.method == 'POST':
        # decoding data from request
        data = json.loads(request.body.decode("utf-8"))
        orderId = data["orderId"]
        email = data["email"]

        try:
            order = Order.objects.filter(order_id = orderId, email = email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(orderId = orderId)
                updates = []
                for item in update:
                    updates.append({"text":item.updateDesc, "date":item.timestamp.strftime("%a, %d %b %Y, %I:%M%p %Z")})
                response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")
        except Exception as e:
            return HttpResponse("{}")
    return render(request, "shop/tracker.html")


def search(request):
    return render(request, "shop/search.html")


def productView(request, myid):
    product = Product.objects.get(id = myid)
    return render(request, "shop/productview.html", {"product":product})


def checkout(request):
    if request.method == "POST":
        items_JSON = request.POST.get('items_JSON')
        name = request.POST.get('name').title()
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        phone = request.POST.get('phone')
        dateAdded = datetime.now().strftime(r"%Y-%m-%d")
        order = Order(
            items_json = items_JSON,
            name = name,
            email = email,
            address1 = address1,
            address2 = address2,
            city = city,
            state = state,
            zip_code = zip,
            phone = phone,
            dateAdded = dateAdded
        )
        order.save()

        # Push update
        update = OrderUpdate(orderId = order.order_id, updateDesc = "Your Order has been placed!")
        update.save()

        thank = True
        id = order.order_id
        messages.success(request, f"Thanks for ordering with us. Your order id is: {id}. Use it to track your order.")
        # return redirect("ShopHome")
        return render(request, "shop/checkout.html", {"thank":thank, "id":id})

    return render(request, "shop/checkout.html")


def data(request):
    dataset = Product.objects.all()
    prod = {"products": dataset}
    return render(request, "shop/data.html", prod)