from django.shortcuts import render
from myapp.models import Student

# Create your views here.
def student(request):
    s = Student.objects.all()
    ctx = ('stud',ctx)
    return render(request,ctx)