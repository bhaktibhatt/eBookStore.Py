from django.shortcuts import HttpResponse
def index(request):
    return HttpResponse('<i>This is my home page, in </i> <code>DJANGO</code>')