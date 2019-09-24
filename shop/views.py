from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("About shops")

def contact(request):
    return HttpResponse("Contact shop's")

def tracker(request):
    return HttpResponse("Tracker Shops")

def search(request):
    return HttpResponse("Search Product Shop")

def productview(request):
    return HttpResponse("ProductVies in the Shop")

def checkout(request):
    return HttpResponse("CheckOut from Shop")
