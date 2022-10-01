from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Student,StudentMarks,Teacher,StudentsInClass,MessageToTeacher,ClassNotice,ClassAssignment,SubmitAssignment

# Register your models here..

admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(StudentMarks)
admin.site.register(Teacher)
admin.site.register(StudentsInClass)
admin.site.register(MessageToTeacher)
admin.site.register(ClassNotice)
admin.site.register(ClassAssignment)
admin.site.register(SubmitAssignment)

admin.site.site_header = 'Ali'