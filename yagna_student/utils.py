from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser
from rest_framework import status
from .models import EnrollCourse


class UserManagement:

    def already_exists(self, username):
        try:
            User.objects.get(username=username)
            return False
        except Exception as e:
            return True

    def save_user(self, data):
        user = None
        try:
            user = User(username=data["username"], email=data["email"])
            user.set_password(data["password"])
            user.save()
            return user
        except Exception as e:
            return user

    def delete_course_to_student(self, student_id, course_id):
        try:
            en_course = EnrollCourse.objects.get(student=student_id, course=course_id)
            en_course.delete()
            return status.HTTP_200_OK
        except Exception as e:
            return status.HTTP_400_BAD_REQUEST

    def get_all_enrolled_students(self):
        try:
            all_enrolled_students = EnrollCourse.objects.all().values()
            return all_enrolled_students
        except Exception as e:
            return None

    def delete_student(self, student_id):
        try:
            student = User.objects.get(id=student_id)
            student.delete()
            return status.HTTP_200_OK
        except Exception as e:
            return status.HTTP_400_BAD_REQUEST

    def get_all_students(self):
        try:
            return User.objects.filter(is_superuser=False).values()
        except Exception as e:
            return None
