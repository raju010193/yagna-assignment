from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser
from rest_framework import status
from .models import EnrollCourse,Course


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

    def delete_course_to_student(self, enroll_id):
        try:
            en_course = EnrollCourse.objects.get(id=enroll_id)
            en_course.delete()
            if en_course.course.isAvailable is False:
                course_update = Course.objects.get(id=en_course.course.id)
                course_update.isAvailable = True
                course_update.save()
            return status.HTTP_200_OK
        except Exception as e:
            return status.HTTP_400_BAD_REQUEST

    def get_course_details(self,courseId):
        try:
            course = Course.objects.get(id=courseId.id)
            return {"id":course.id,"title":course.title,"days":course.days,"author":course.author}
        except Exception as e:
            return None
    def get_student_details(self,student):
        try:
            student = User.objects.get(id=student.id)
            return {"id":student.id,"userName":student.username,"email":student.email}
        except Exception as e:
            return None

    def get_all_enrolled_students(self):
        try:
            enroll_students = EnrollCourse.objects.all()
            courses = list()
            if enroll_students:
                for each_enroll in enroll_students:
                    courses.append({"student":self.get_student_details(each_enroll.student),"course":self.get_course_details(each_enroll.course),"enId":each_enroll.id})

            return courses
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
            users = User.objects.filter(is_superuser=False)
            users_details = list()
            if users:
                for each_user in users:
                   count = EnrollCourse.objects.filter(student=each_user).count()
                   users_details.append({"id":each_user.id,"userName":each_user.username,"email":each_user.email,"total":count})

            return users_details
        except Exception as e:
            return None
