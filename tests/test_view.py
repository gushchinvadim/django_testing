import pytest
from rest_framework import status

from students.models import Student, Course


# === ТЕСТЫ ДЛЯ КУРСОВ ===

@pytest.mark.django_db
def test_course_list(api_client, course_factory):
    # Создаем несколько курсов
    course_factory.create_batch(3)

    response = api_client.get('/courses/')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3


@pytest.mark.django_db
def test_course_detail(api_client, course_factory):
    course = course_factory()

    response = api_client.get(f'/courses/{course.id}/')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == course.name


@pytest.mark.django_db
def test_create_course(api_client):
    data = {
        "name": "Math Basics",
        "description": "Introduction to Math"
    }

    response = api_client.post('/courses/', data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Course.objects.filter(name="Math Basics").exists()


# === ТЕСТЫ ДЛЯ СТУДЕНТОВ ===

@pytest.mark.django_db
def test_student_list(api_client, student_factory):
    student_factory.create_batch(5)

    response = api_client.get('/students/')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5


@pytest.mark.django_db
def test_student_detail(api_client, student_factory):
    student = student_factory()

    response = api_client.get(f'/students/{student.id}/')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['first_name'] == student.first_name


@pytest.mark.django_db
def test_create_student(api_client):
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "date_of_birth": "2000-01-01"
    }

    response = api_client.post('/students/', data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Student.objects.filter(first_name="John").exists()