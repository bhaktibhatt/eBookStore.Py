from django.shortcuts import render, HttpResponseRedirect
from .models import CartItems, Ebook
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def store_view(request):
    ebooks = {'eBooks' : Ebook.objects.all()}
    return render(request,'Store\index.html',ebooks)

def cart_view(request):
    CART_ITEMS = CartItems.objects.all()
    cart_total = 0
    for item in CART_ITEMS:
        cart_total += item.price
    return render(request, 'Store\cart.html', {
        'cart_items' : CART_ITEMS,
        'cart_total' : cart_total
        })


@csrf_exempt
def add_cart_items(request):
    book_id = request.POST['book_id']
    title = Ebook.objects.get(pk=book_id).title
    price = Ebook.objects.get(pk=book_id).price
    item = CartItems.objects.create(title = title, price = price)
    return HttpResponseRedirect('/store')
    