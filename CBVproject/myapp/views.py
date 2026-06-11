from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from myapp.models import Student
from django.urls import reverse_lazy
# Create your views here.
class StudentList(ListView):
    model = Student
    # default templates: student_list.html
    # default context : student_list

class StudentDetails(DetailView):
    model = Student

    # default templates: student_detail.html
    # default context : student


class StudentUpdate(UpdateView):
    model = Student
    fields = "__all__"
    


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students')
   
   
    # default templates: student_confirm_delete.html
    # default context : student