from django.shortcuts import render
from django.db.models import Q, F
from .models import Product

def q_expressions_view(request):
    # 1 არის ეს:
    q1 = Product.objects.filter(Q(price__gt=50) | Q(quantity__lt=10))
    # 2 არის ეს:
    q2 = Product.objects.filter(Q(name__icontains="phone") & Q(price__gte=100, price__lte=500))
    # 3 არის ეს:
    q3 = Product.objects.filter(~Q(price__lt=200))

    context = {
        "q1": q1,
        "q2": q2,
        "q3": q3,
    }
    return "დონატი"


def f_expressions_view(request):
    # 1 არის ეს:
    f1 = Product.objects.update(price=F("price") + 10)
    # 2 არის ეს:
    f2 = Product.objects.filter(price__gt=F("quantity"))
    # 3 არის ეს:
    f3 = Product.objects.update(quantity=F("quantity") + 1)

    context = {
        "f1": f1,
        "f2": f2,
        "f3": f3,
    }
    return "კიდე დონატი"
