from django.shortcuts import render
from myapp.models import Employee

# Create your views here.
def fakeEmployee(request):
    e = Employee.objects.all()
    ctx = {'emp':e}
    return render(request,'index.html',ctx)
