"""yagna_student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from yagna_student.api_views import Register, Login, LogoutUser, CheckUserLogin, ChangePassword, StudentCourseManagement
from yagna_student.admin_views import AdminCourseManagement, AdminManagedbyStudent,RemoveStudent, GetAllStudents

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/register/', Register.as_view()),
    url(r'^api/accounts/login/', Login.as_view()),
    url(r'^api/accounts/logout/', LogoutUser.as_view()),
    url(r'^api/accounts/checklogin/', CheckUserLogin.as_view()),
    url(r'^api/accounts/change-password/', ChangePassword.as_view()),
    url(r'^api/admin/add-course/', AdminCourseManagement.as_view()),
    url(r'^api/admin/remove-course/', AdminCourseManagement.as_view()),
    url(r'^api/get-all/', AdminCourseManagement.as_view()),
    url(r'^api/student/enroll-course/', StudentCourseManagement.as_view()),
    url(r'^api/student/get-enroll-courses-by-student/', StudentCourseManagement.as_view()),
    url(r'^api/admin/remove-student-course/', AdminManagedbyStudent.as_view()),
    url(r'^api/admin/remove-student/', RemoveStudent.as_view()),
    url(r'^api/admin/get-enrolled-students/', AdminManagedbyStudent.as_view()),
    url(r'^api/admin/get-students/',GetAllStudents.as_view()),
    url(r'^api/admin/add-to-course/',AdminCourseManagement.as_view()),
]
