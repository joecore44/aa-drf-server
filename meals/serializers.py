from django.contrib.auth.models import User, Group
from .models import Meal, Food, TrainerProfile, ClientProfile
from rest_framework import serializers

class TrainerProfileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = TrainerProfile
        fields = '__all__'

class ClientProfileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ClientProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullName', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
