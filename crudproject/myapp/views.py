from django.shortcuts import render,redirect
from myapp.models import Student
from myapp.forms import StudentForm

# Create your views here.

def student(request):
    s = Student.objects.all()
    ctx = {'stud':s}
    return render(request,'index.html',ctx)


def insert_view(request):

    f = StudentForm()
    if request.method == "POST":
        f = StudentForm(request.POST)

        if f.is_valid():
            f.save(commit = True)

            return redirect('/')
        
    d = {'form':f}
    return render(request, 'form.html',d)
    



def update_view(request,id):
    s = Student.objects.get(id = id)
    if request.method == "POST":
        f  = StudentForm(request.POST, instance=s)

        if f.is_valid():
            f.save()
            return redirect('/')
        
    f = StudentForm(instance=s)
    d = {'form':f}
    return render(request,'form.html',d)

def delete_view(request,id):
    s = Student.objects.get(id=id)
    s.delete()
    return redirect('/')
        

