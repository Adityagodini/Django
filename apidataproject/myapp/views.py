from urllib import request

from django.shortcuts import render
from myapp.models import Student
from django.views.generic import View
from django.http import HttpResponse
import json


# Create your views here.
class studentDetails(View):
    def get(self,request,id,*args,**kwargs):
        stud = Student.objects.get(id=id)
        stud_data= {
        'name': stud.name,
        'age': stud.age,
        'email':stud.email,
        'place' : stud.place
    }

        json_data = json.dumps(stud_data)

        return HttpResponse(json_data, content_type='application/json')

    