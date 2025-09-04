from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


# Create your views here.

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо, {name}! <p>С вами скоро свяжутся.</p>')

    return render(request, 'catalog/contacts.html')


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'catalog/product.html', context)
