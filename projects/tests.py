from django.test import TestCase
from .models import Project, Tags


# Create your tests here.

class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(name='test projects', description='Description test', url_project_online='www.test.com')

    def test_title_content(self):
        todo = Project.objects.get(name='test projects')
        expected_object_name = f'{todo.name}'
        self.assertEquals(expected_object_name, 'test projects')