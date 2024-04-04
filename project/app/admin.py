from django.contrib import admin
from .models import DeparmentModel,StudentModel


# Register your models here.
# @admin.register(DeparmentModel)
# class DeparmentAdmin(admin.ModelAdmin):
#     list_display=['id','Dep_name']

# @admin.register(StudentModel)
# class StudentAdmin(admin.ModelAdmin):
#     list_display=['stu_name','stu_deparment','stu_class']

class Student(admin.ModelAdmin):
    list_display=['id','stu_deparment']
admin.site.register(StudentModel,Student)

class Department(admin.ModelAdmin):
    list_display=['id','Dep_name']
admin.site.register(DeparmentModel,Department)

# admin.site.register(StudentModel)
# admin.site.register(DeparmentModel)