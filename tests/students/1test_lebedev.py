import pytest
import rest_framework.authtoken.models
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from students.models import Student


@pytest.fixture
def student():
    return APIClient()



@pytest.mark.django_db
def test_example(student):
# assert False, "Just test example"
    # Arrange
    student = APIClient()
    User.objects.create_user('admin')
    Student.objects.create(name='Stud111')
    # Act
    response = student.get('/courses/')
    # Assert
    assert response.status_code == 404
    data = response.json()
    assert len(data) == 0



# @pytest.mark.django_db
# def test_create_student(student):
#     User.objects.create_user('admin')
#     response = student.post('/courses/', data={'user': 1, 'name': 'biology'}, format='json')
#
#     assert response.status_code == 201