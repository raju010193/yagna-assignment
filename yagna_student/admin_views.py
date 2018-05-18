from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core import serializers

from django.contrib.auth.models import User
from .models import CourseSerialization, Course, EnrollCourse
from .utils import UserManagement
from django.contrib.auth import authenticate, login, logout


class AdminCourseManagement(APIView):
    def post(self, request):
        try:
            serializer = CourseSerialization(data=request.data)
            if serializer.is_valid():
                if request.user.is_authenticated and request.user.is_superuser:
                    serializer.save()

                    return Response(serializer.errors, status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_403_FORBIDDEN)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            if request.user.is_authenticated and request.user.is_superuser:
                course_info = Course.objects.get(id=request.data.get('courseId'))
                course_info.delete()
                return Response(status.HTTP_200_OK,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:

            course_details = Course.objects.all().values()
            return Response(course_details, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):

        try:
            if request.user.is_authenticated and request.user.is_superuser:

                try:
                    user = User.objects.get(id=request.data.get("studentId"))
                    course = Course.objects.get(id=request.data.get("courseId"))
                except Exception as e:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                status_code = EnrollCourse().enroll_course(course, user)
                if status_code is status.HTTP_200_OK:
                    return Response(status_code,status=status_code)
                return Response(status=status_code)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class AdminManagedbyStudent(APIView):

    def delete(self, request):
        try:
            if request.user.is_authenticated and request.user.is_superuser:
                status_code = UserManagement().delete_course_to_student(request.data.get('enrollId'))
                if status_code is status.HTTP_200_OK:
                    return Response(status_code,status=status_code)

                return Response(status=status_code)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            if request.user.is_superuser and request.user.is_authenticated:
                course_students = UserManagement().get_all_enrolled_students()
                return Response(course_students, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetAllStudents(APIView):
    def get(self, request):
        try:
            if request.user.is_authenticated and request.user.is_superuser:
                get_all_students = UserManagement().get_all_students()
                return Response(get_all_students, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RemoveStudent(APIView):
    def delete(self, request):
        try:
            if request.user.is_authenticated and request.user.is_superuser:
                status_code = UserManagement().delete_student(request.data.get('studentId'))
                if status_code is status.HTTP_200_OK:
                    return Response(status_code,status=status_code)
                return Response(status=status_code)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
