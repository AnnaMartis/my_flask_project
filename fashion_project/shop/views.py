from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import (
    Product,
    Category,
    Order,
    Cart,
    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'shop/home.html')


def contact(request):
    return render(request, 'shop/contact.html')


def display_by_category(request, category_slug):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    template = 'shop/gender.html'
    context = {'categories':categories, 'products':products, 'category':category}
    return render(request, template, context)


class ItemListView(ListView):
    model = Product
    template_name = 'shop/gender.html'


class ItemDetailView(DetailView):
    model =  Product
    template_name = 'shop/single-product.html'


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.order_items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, f"{item.title} quantity has updated.")
            return redirect('shop:cart-view')
        else:
            order.order_items.add(order_item)
            messages.info(request, f"{item.title} has added to your cart.")
            return redirect('shop:cart-view')
    else:
        order = Order.objects.create(user=request.user)
        order.order_items.add(order_item)
        messages.info(request, f"{item.title} has added to your cart.")
        return redirect('shop:cart-view')

# # Cart View

@login_required
def CartView(request):
    user = request.user

    carts = Cart.objects.filter(user=user, purchased=False)
    orders = Order.objects.filter(user=user, ordered=False)

    if carts.exists():
        if orders.exists():
            order = orders[0]
            return render(request, 'shop/cart.html', {"carts": carts, 'order': order})
        else:
            messages.warning(request, "You do not have any item in your Cart")
            return redirect('fashion-home')

    else:
        messages.warning(request, "You do not have any item in your Cart")
        return redirect('shop:fashion-home')


@staff_member_required
def SalesView(request):
    carts_ord = Cart.objects.filter( purchased=False)
    prod_all = Product.objects.all()
    income = 0
    if carts_ord.exists():
        for cart in carts_ord:
            income += cart.get_total()
            quant_remained = cart.item.quantity - cart.quantity
    else:
        income=0
        quant_remained = 5
    return render(request, 'shop/sales.html', {'carts_ord':carts_ord, 'prod_all':prod_all, 'income':income,
                                               'quant_remained':quant_remained})




# Decrease the quantity of the cart :

@login_required
def decreaseCart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.order_items.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.order_items.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{item.title} has removed from your cart.")
            messages.info(request, f"{item.title} quantity has updated.")
            return redirect('shop:cart-view')
        else:
            messages.info(request, f"{item.title} quantity has updated.")
            return redirect('shop:shop:cart-view')
    else:
        messages.info(request, "You do not have an active order")
        return redirect("shop:fashion-home")


def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.order_items.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.order_items.remove(order_item)
            messages.warning(request, "This item was removed from your cart.")
            return redirect("shop:cart-view")
        else:
            messages.warning(request, "This item was not in your cart")
            return redirect("shop:cart-view")
    else:
        messages.warning(request, "You do not have an active order")
        return redirect("shop:fashion-home")


