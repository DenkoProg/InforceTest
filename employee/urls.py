from django.urls import path
from .views import EmployeeListCreate, EmployeeRetrieveUpdateDestroy, VoteCreate

urlpatterns = [
    path(
        '',
        EmployeeListCreate.as_view(),
        name='employee-list-create'),
    path(
        '<int:pk>/',
        EmployeeRetrieveUpdateDestroy.as_view(),
        name='employee-detail'),
    path(
        'vote/',
        VoteCreate.as_view(),
        name='vote-create'),
]
