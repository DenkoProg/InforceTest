from django.urls import path
from .views import RestaurantListCreate, RestaurantRetrieveUpdateDestroy, MenuListCreate, MenuRetrieveUpdateDestroy, CurrentDayMenu, VotingResults

urlpatterns = [
    path(
        '',
        RestaurantListCreate.as_view(),
        name='restaurant-list-create'),
    path(
        '<int:pk>/',
        RestaurantRetrieveUpdateDestroy.as_view(),
        name='restaurant-detail'),
    path(
        'menus/',
        MenuListCreate.as_view(),
        name='menu-list-create'),
    path(
        'menus/<int:pk>/',
        MenuRetrieveUpdateDestroy.as_view(),
        name='menu-detail'),
    path(
        'current-day-menu/',
        CurrentDayMenu.as_view(),
        name='current-day-menu'),
    path(
        'voting-results/',
        VotingResults.as_view(),
        name='voting-results'),
]
