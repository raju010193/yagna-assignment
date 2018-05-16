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
from yagna_student.admin_views import AdminCourseManagement, AdminManagedbyStudent,RemoveStudent

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', Register.as_view()),
    url(r'^login/', Login.as_view()),
    url(r'^logout/', LogoutUser.as_view()),
    url(r'^checklogin/', CheckUserLogin.as_view()),
    url(r'^change-password/', ChangePassword.as_view()),
    url(r'^add-course/', AdminCourseManagement.as_view()),
    url(r'^remove-course/', AdminCourseManagement.as_view()),
    url(r'^get-all', AdminCourseManagement.as_view()),
    url(r'^enroll-course/', StudentCourseManagement.as_view()),
    url(r'^get-enroll-courses-by-student', StudentCourseManagement.as_view()),
    url(r'^remove-student-course', AdminManagedbyStudent.as_view()),
    url(r'^remove-student', RemoveStudent.as_view()),
    url(r'^get-enrolled-students', AdminManagedbyStudent.as_view()),
]
