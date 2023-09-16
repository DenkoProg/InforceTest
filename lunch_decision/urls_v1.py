from django.urls import path, include

app_name = 'v1'

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('restaurants/', include('restaurant.urls')),
    path('employees/', include('employee.urls')),
]

