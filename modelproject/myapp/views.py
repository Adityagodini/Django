from django.shortcuts import render
from myapp.models import Student
# Create your views here.
def Studview(request):
    s=Student.objects.all()
    ctx= {'stud':s}
    return render(request,'index.html',ctx)