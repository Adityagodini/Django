from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import StudentForm

# Create your views here.
def feedView(request):
    f = StudentForm()
    if request.method == 'POST':
        f = StudentForm(request.POST)
        if f.is_valid():
            f.save()
            # return HttpResponse("Data is stored in database suceessfully")

            name = f.cleaned_data['name']
            age = f.cleaned_data['age']
            email = f.cleaned_data['email']
            course = f.cleaned_data['course']
            feedback = f.cleaned_data['feedback']
            d = {'name': name, 'age': age, 'email': email, 'course': course, 'feedback': feedback}
            return render(request, 'output.html', d)
    d={'form':f}
    return render(request, 'form.html',d)