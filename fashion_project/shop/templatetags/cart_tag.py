from django import template
from ..models import Order

register = template.Library()

@register.filter
def cart_quantity_total(user):
    order = Order.objects.filter(user=user, ordered=False)

    if order.exists():
        return order[0].order_items.count()
    else:
        return 0

