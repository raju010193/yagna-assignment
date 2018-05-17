from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core import serializers

from django.contrib.auth.models import User
from .models import UserSerialization, EnrollCourse, Course
from rest_framework.authtoken.models import Token
from .utils import UserManagement
from django.contrib.auth import authenticate, login, logout


class Register(APIView):
    def post(self, request):
        try:
            serializer = UserSerialization(data=request.data)
            if serializer.is_valid():
                if UserManagement().already_exists(request.data.get("username")):
                    user = UserManagement().save_user(request.data)
                    if user is not None:
                        return Response(serializer.errors, status=status.HTTP_201_CREATED)
                    return Response(serializer.error_messages, status=status.HTTP_204_NO_CONTENT)
                return Response(serializer.errors, status=status.HTTP_207_MULTI_STATUS)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Login(APIView):
    def post(self, request):
        try:
            user = authenticate(username=request.data["username"], password=request.data["password"], type='user')
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

            login(request, user)
            token = Token.objects.get(user=user)

            return Response(
                {"user": {"id": user.id, "username": user.username, "email": user.email, "is_superuser":user.is_superuser,"token": token.key}},
                status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogoutUser(APIView):
    def get(self, request):
        try:
            logout(request)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"result": "error"}, 500)


class CheckUserLogin(APIView):
    def get(self, request):
        try:
            email = request.user.email
            return Response({"success": email}, 200)
        except:
            return Response({"error": "user is not logged in"}, 500)


class ChangePassword(APIView):
    def put(self, request):
        if request.user.is_authenticated:
            new_password = request.data.get("newPassword")
            username = request.user.username
            old_password = request.data.get("oldPassword")
            try:
                user = authenticate(username=username, password=old_password, type='user')
                if user:
                    update_password = User.objects.get(username=username)
                    update_password.set_password(new_password)
                    update_password.save()
                    user = authenticate(username=username, password=new_password, type='user')
                    login(request, user)
                    token = Token.objects.get(user=user)
                    return Response({"token":token.key},status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            except Exception as e:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class StudentCourseManagement(APIView):
    def put(self, request):
        try:
            if request.user.is_authenticated:
                course = Course().get_course(request.data.get("courseId"))
                if course is not None:
                    status_code = EnrollCourse().enroll_course(course,request.user)
                return Response(status=status_code)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        try:
            if request.user.is_authenticated:
                course_details = EnrollCourse().get_enrolled_course_by_user(request.user)
                return Response(course_details,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)