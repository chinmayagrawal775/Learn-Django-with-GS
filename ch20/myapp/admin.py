from django.contrib import admin
from .models import Student, Teacher, ExamCenter, Examinee, MyExamCenter

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'fees']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'salary']

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']

@admin.register(Examinee)
class ExamineeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'cname', 'city']

@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']
    ordering = ['id']