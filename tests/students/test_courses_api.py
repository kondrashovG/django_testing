import pytest
from django.contrib.auth.models import User
from model_bakery import baker
from students.models import Course, Student
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_cource(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=1)
    print(courses[0].name)

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    print(response.status_code)
    assert response.status_code == 200
    # data = response.json()
    # print(data)
    # assert len(data) == len(courses)
    # for i, m in enumerate(data):
    #     assert m['name'] == courses[i].name