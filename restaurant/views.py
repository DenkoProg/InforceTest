from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer
from .models import Menu
from .serializers import MenuSerializer
from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from employee.models import Vote


class RestaurantListCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class CurrentDayMenu(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        today_votes = Vote.objects.filter(timestamp__date=date.today())
        top_menu = today_votes.values('menu').annotate(
            vote_count=Count('menu')).order_by('-vote_count').first()

        if top_menu:
            return Menu.objects.filter(id=top_menu['menu'], date=date.today())
        else:
            return Menu.objects.none()


class VotingResults(APIView):

    def get(self):
        today_votes = Vote.objects.filter(timestamp__date=date.today())
        results = today_votes.values('menu__items').annotate(
            vote_count=Count('menu')).order_by('-vote_count')
        return Response(results)
