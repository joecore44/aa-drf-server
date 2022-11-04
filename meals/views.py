from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from .serializers import MealSerializer, FoodSerializer
from .serializers import TrainerProfileSerializer, ClientProfileSerializer
from .serializers import ClientCheckinSerializer, ConditionSerializer
from .models import Meal, Food, TrainerProfile, ClientProfile
from .models import ClientCheckin, Condition


class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientProfileViewSet(viewsets.ModelViewSet):
    trainer_id = 1 # id(1 | 3) TODO turn this into a filter on autheniticated.trainer
    queryset = ClientProfile.objects.filter(trainer=trainer_id)
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ClientMedicalConditionViewSet(viewsets.ModelViewSet):
  
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ClientCheckinViewSet(viewsets.ModelViewSet):
    
    queryset = ClientCheckin.objects.all()
    serializer_class = ClientCheckinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TrainerProfileViewSet(viewsets.ModelViewSet):
    
    queryset = TrainerProfile.objects.all()
    serializer_class = TrainerProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class MealViewSet(viewsets.ModelViewSet):

    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FoodViewSet(viewsets.ModelViewSet):

    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=True, methods=['get'])
    def foods(self, request, pk=None):
        meal = self.get_object()
        foods = meal.foods.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_food(self, request, pk=None):
        meal = self.get_object()
        food = Food.objects.get(pk=request.data['food_id'])
        meal.foods.add(food)
        return Response(status=204)


