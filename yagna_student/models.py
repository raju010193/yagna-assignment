from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework import status


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    else:
        token = Token.objects.get(user=instance)


class UserSerialization(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "username", 'password', 'email')


class Course(models.Model):
    title = models.CharField(max_length=50)
    courseDetails = models.TextField()
    days = models.IntegerField(max_length=50)
    isAvailable = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.utcnow())
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def update_course_availabilty(self, course):
        try:
            course = Course.objects.get(id=course.id)
            course.isAvailable = False
            course.save()
            return True
        except Exception as e:
            return False

    def get_course(self, course_id):
        try:
            return Course.objects.get(id=course_id)
        except Exception as e:
            return None


class CourseSerialization(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("title", "courseDetails", "days", "author")


class EnrollCourse(models.Model):
    student = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    date = models.DateTimeField(default=datetime.utcnow())

    def __str__(self):
        return self.course.title

    def check_course_avaialbility(self, course):
        try:
            if EnrollCourse.objects.filter(course=course).count() == settings.EACH_COURSE_ENROLL:
                Course().update_course_availabilty(course)
                return False
            return Course.objects.get(id=course.id).isAvailable
        except Exception as e:
            return False

    def check_user_already_enrolled_not(self, course, student):
        try:
            EnrollCourse.objects.get(course=course, student=student)
            return False
        except Exception as e:
            return True

    def enroll_course(self, course, student):
        try:
            if self.check_user_already_enrolled_not(course, student):
                if self.check_course_avaialbility(course):
                    self.student = student
                    self.course = course
                    self.save()
                    self.check_course_avaialbility()
                    return status.HTTP_200_OK
                return status.HTTP_306_RESERVED
            return status.HTTP_207_MULTI_STATUS
        except Exception as e:
            return status.HTTP_400_BAD_REQUEST

    def get_enrolled_course_by_user(self, student):
        try:
            course = list()
            enroll = EnrollCourse.objects.filter(student=student)
            if enroll:
                for each_course in enroll:
                    each = Course().get_course(each_course.course.id)
                    course.append({"id":each.id,"title":each.title,"days":each.days,"author":each.author,"courseDetails":each.courseDetails})
            return course
        except Exception as e:
            return None
