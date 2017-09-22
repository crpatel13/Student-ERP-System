from django.contrib import admin
from myApp.models import Author, Book, Student, Course, Topic

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Topic)