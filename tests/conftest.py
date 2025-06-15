import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from students.models import Course, Student
import factory
from factory.django import DjangoModelFactory


# === ФАБРИКИ ===

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user_{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')


class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.Sequence(lambda n: f'Course {n}')
    description = factory.Faker('sentence')
    instructor = factory.SubFactory(UserFactory)


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    date_of_birth = factory.Faker('date_of_birth', minimum_age=18, maximum_age=30)


# === ФИКСТУРЫ ===

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    return CourseFactory


@pytest.fixture
def student_factory():
    return StudentFactory