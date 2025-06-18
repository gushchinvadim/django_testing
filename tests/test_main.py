
import pytest
from rest_framework import status

from students.models import Course

pytestmark = pytest.mark.django_db

BASE_URL = "http://localhost:8000/api/v1/courses/"  # замените на ваш URL


# --- 1. Проверка получения одного курса (retrieve) ---
def test_retrieve_course(api_client, course_factory):
    course = course_factory(name="Django Advanced")

    url = f"{BASE_URL}{course.id}/"
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == course.id
    assert response.data['name'] == "Django Advanced"


# --- 2. Проверка получения списка курсов (list) ---
def test_list_courses(api_client, course_factory):
    course_factory(name="Python Basics")
    course_factory(name="JavaScript Intro")

    url = BASE_URL
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    course_names = [course['name'] for course in response.data]
    assert "Python Basics" in course_names
    assert "JavaScript Intro" in course_names


# --- 3. Проверка фильтрации по id ---
def test_filter_courses_by_id(api_client, course_factory):
    course1 = course_factory(name="Course A")
    course2 = course_factory(name="Course B")

    url = f"{BASE_URL}?id={course1.id}"
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['id'] == course1.id


# --- 4. Проверка фильтрации по name ---
def test_filter_courses_by_name(api_client, course_factory):
    course1 = course_factory(name="Mathematics")
    course2 = course_factory(name="Literature")

    url = f"{BASE_URL}?name=Mathematics"
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == course1.name


# --- 5. Тест успешного создания курса ---
def test_create_course(api_client):
    data = {"name": "New Course"}

    url = BASE_URL
    response = api_client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Course.objects.count() == 1
    assert Course.objects.first().name == "New Course"


# --- 6. Тест успешного обновления курса ---
def test_update_course(api_client, course_factory):
    course = course_factory(name="Old Name")
    updated_data = {"name": "New Name"}

    url = f"{BASE_URL}{course.id}/"
    response = api_client.patch(url, updated_data)

    assert response.status_code == status.HTTP_200_OK
    course.refresh_from_db()
    assert course.name == "New Name"


# --- 7. Тест успешного удаления курса ---
def test_delete_course(api_client, course_factory):
    course = course_factory(name="ToDelete")

    url = f"{BASE_URL}{course.id}/"
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Course.objects.count() == 0