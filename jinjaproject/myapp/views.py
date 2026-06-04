from django.shortcuts import render

# Create your views here.
def index(request):
    name="rama"
    place="banglore"

    ctx={'NAME':name,'PLACE':place}

    return render (request,'index.html',ctx)
