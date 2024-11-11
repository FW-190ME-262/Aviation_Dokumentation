import requests
from django.test import TestCase
from app_name.models import Course


class CourseAPITestCase(TestCase):

    def setUp(self):
        self.course = Course.objects.create(title='Test Course', description='Test Description')

    def test_get_course(self):
        url = f'http://127.0.0.1:8000/courses/{self.course.pk}/'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_course_not_found(self):
        url = 'http://127.0.0.1:8000/courses/999/'  # Не существующий ID
        response = requests.get(url)
        self.assertEqual(response.status_code, 404)
