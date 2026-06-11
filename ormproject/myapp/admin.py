from django.contrib import admin
from myapp.models import Student

# Register your models here.
admin.site.register(Student)


# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['name','age','place','marks','email']
# admin.site.register(StudentAdmin,Student)
