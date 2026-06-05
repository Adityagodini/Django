import django
import os
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakeproject.settings')
django.setup()


from faker import Faker
from myapp.models import Employee

f = Faker('en-IN')

def populate(n):
    for i in range(n):
        fname = f.name()
        fdob = f.date_of_birth()
        fplace = f.address()
        femail = f.email()
        fsalary = round(random.uniform(25000,90000),2)
        fjob = f.job()
        s = Employee.objects.get_or_create(name=fname,dob=fdob,place=fplace,email=femail, salary=fsalary, job=fjob)

populate(20)

