from django.contrib import admin

from yagna_student.models import Course,EnrollCourse

admin.site.register(Course)
admin.site.register(EnrollCourse)