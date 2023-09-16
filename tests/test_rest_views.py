import pytest
from rest_framework.test import APIClient
from restaurant.models import Restaurant, Menu
from django.contrib.auth.models import User
from employee.models import Employee, Vote
from datetime import date


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def sample_data(db):
    data = {}
    data['restaurant'] = Restaurant.objects.create(
        name="Test Restaurant", address="123 Test St", phone="1234567890")
    data['menu'] = Menu.objects.create(
        restaurant=data['restaurant'],
        date=date.today(),
        items="Chicken, Pizza, Water")
    data['user'] = User.objects.create_user(
        username="testuser", password="testpassword")
    data['employee'] = Employee.objects.create(
        user=data['user'], employee_id="E12345")
    return data


def test_restaurant_list_create(api_client, sample_data, db):
    # Authenticate the client
    api_client.force_authenticate(user=sample_data['user'])

    # Test GET
    response = api_client.get('/api/v1/restaurants/')
    assert response.status_code == 200

    # Test POST
    data = {
        "name": "New Restaurant",
        "address": "456 New St",
        "phone": "9876543210"}
    response = api_client.post('/api/v1/restaurants/', data=data)
    assert response.status_code == 201


def test_current_day_menu(api_client, sample_data, db):
    # Authenticate the client
    api_client.force_authenticate(user=sample_data['user'])

    # Create a vote for the menu
    Vote.objects.create(
        menu=sample_data['menu'],
        employee=sample_data['employee'])

    response = api_client.get('/api/v1/restaurants/current-day-menu/')
    assert response.status_code == 200

# ... Add more tests for other views ...
