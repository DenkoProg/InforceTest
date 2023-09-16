# tests/test_auth_views.py

import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_register_user(client):
    # Including the version namespace in the reverse function
    url = reverse('v1:register')
    data = {
        'username': 'testuser',
        'password': 'testpassword123'
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1
    assert User.objects.first().username == 'testuser'


@pytest.mark.django_db
def test_login_user(client):
    user = User.objects.create_user(
        username='testuser',
        password='testpassword123')
    # Including the version namespace in the reverse function
    url = reverse('v1:login')
    data = {
        'username': 'testuser',
        'password': 'testpassword123'
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert 'refresh' in response.data
    assert 'access' in response.data
