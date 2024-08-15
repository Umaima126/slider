from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    products=Product.objects.all()
    n=len(products)
    nSlides= n//4 
    print(products)
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'index.html',params)
