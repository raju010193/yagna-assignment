from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Course

class CoursesTest(APITestCase):


    def post_course(self):
        Course(title='java',days=20,courseDetails='its java base',author='sidhu').save()
        self.assertEqual(status.HTTP_200_OK)


    def get_courses(self):

        # First check for the default behavior
        response = self.client.get('/api/get-all/',{},format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print(response.data)

