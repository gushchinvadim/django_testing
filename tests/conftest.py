
import pytest
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return Course.objects.create(*args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return Student.objects.create(*args, **kwargs)
    return factory






