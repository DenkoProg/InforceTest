import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from employee.models import Employee, Vote
from restaurant.models import Menu, Restaurant


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def sample_data(db):
    data = {}
    data['user'] = User.objects.create_user(
        username="testuser", password="testpassword")
    data['employee'] = Employee.objects.create(
        user=data['user'], employee_id="E12345")

    # Create a Restaurant object
    data['restaurant'] = Restaurant.objects.create(
        name="Test Restaurant",
        address="Bandera Street",
    )

    # Create a Menu object using the Restaurant object
    data['menu'] = Menu.objects.create(
        restaurant=data['restaurant'],
        date="2023-09-15",
        items="Pizza, Pasta, Salad",
        description="Today's special menu"
    )
    return data


def test_employee_list_create(api_client, sample_data):
    # Authenticate the client
    api_client.force_authenticate(user=sample_data['user'])

    # Test GET
    response = api_client.get('/api/v1/employees/')
    assert response.status_code == 200
    assert len(response.data) == 1

    # Create a new user for the new employee
    new_user = User.objects.create_user(
        username="testuser2", password="testpassword2")

    # Test POST
    data = {"user": new_user.id, "employee_id": "E67890", "department": "AI"}
    response = api_client.post('/api/v1/employees/', data=data)
    assert response.status_code == 201
    assert Employee.objects.count() == 2


def test_employee_retrieve_update_destroy(api_client, sample_data):
    # Authenticate the client
    api_client.force_authenticate(user=sample_data['user'])

    # Test GET (Retrieve)
    response = api_client.get(f'/api/v1/employees/{sample_data["employee"].id}/')
    assert response.status_code == 200
    assert response.data['employee_id'] == "E12345"

    # Test PUT (Update)
    data = {"user": sample_data['user'].id, "employee_id": "E54321"}
    response = api_client.put(
        f'/api/v1/employees/{sample_data["employee"].id}/',
        data=data)
    assert response.status_code == 200
    updated_employee = Employee.objects.get(id=sample_data['employee'].id)
    assert updated_employee.employee_id == "E54321"

    # Test DELETE
    response = api_client.delete(f'/api/v1/employees/{sample_data["employee"].id}/')
    assert response.status_code == 204
    assert Employee.objects.count() == 0


def test_vote_create(api_client, sample_data):
    # Authenticate the client
    api_client.force_authenticate(user=sample_data['user'])

    # Test POST
    data = {"menu": sample_data['menu'].id,
            "employee": sample_data['employee'].id}
    response = api_client.post('/api/v1/employees/vote/', data=data)
    print(response.data)
    assert response.status_code == 201
    assert Vote.objects.count() == 1
    assert Vote.objects.first().employee == sample_data['employee']
