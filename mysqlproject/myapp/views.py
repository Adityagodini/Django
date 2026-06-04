from django.shortcuts import render
from myapp.models import Product

# Create your views here.
def prodView(request):
    s=Product.objects.all()
    ctx= {'prod':s}
    return render(request,'index.html',ctx)