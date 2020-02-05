from django.urls import path
from . views import (
    ItemListView,
    ItemDetailView,
    add_to_cart,
    decreaseCart,
    remove_from_cart,
    CartView,
)
from . import views


app_name ='shop'

urlpatterns = [
    path('', views.home, name='fashion-home'),
    path('contact/', views.contact, name='fashion-contact'),
    path('sale/', views.SalesView, name='fashion-sales'),
    path('product/<slug>/', ItemDetailView.as_view(), name='single-product'),
    path('category/<category_slug>/', views.display_by_category, name='category_display'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('decrease-from-cart/<slug>/', decreaseCart, name='decrease-from-cart'),
    path('delete-from-cart/<slug>/', remove_from_cart, name='delete-from-cart'),
    path('cart/', CartView, name='cart-view'),
]
