from django.shortcuts import render
from .models import Ebook

# Create your views here.
def store_view(request):
    ebooks = {'eBooks' : Ebook.objects.all()}
    return render(request,'Store\index.html',ebooks)
