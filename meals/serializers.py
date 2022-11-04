from django.contrib.auth.models import User, Group
from .models import Meal, Food, TrainerProfile, ClientProfile
from .models import ClientCheckin, Condition
from rest_framework import serializers

class TrainerProfileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = TrainerProfile
        fields = '__all__'

class ConditionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Condition
        fields = '__all__'
        

class ClientProfileSerializer(serializers.ModelSerializer):
    condition_set = ConditionSerializer(many=True)
    class Meta:
        model = ClientProfile
        fields = fields = [
            'id',
            'public',
            'fullName',
            'company',
            'role',
            'username',
            'country',
            'contact',
            'email',
            'currentPlan',
            'status',
            'avatar',
            'starting_weight',
            'starting_height',
            'starting_body_fat_mass',
            'starting_body_fat_percentage',
            'starting_skeletul_muscle_mass',
            'current_weight',
            'current_height',
            'current_body_fat_mass',
            'current_body_fat_percentage',
            'current_skeletul_muscle_mass',
            'user',
            'trainer',
            'condition_set'
        ]

class ClientCheckinSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ClientCheckin
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullName', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    food_set = FoodSerializer(many=True)
    class Meta:
        model = Meal
        fields = ['id',
         'date',
         'title', 
         'description',
         'image',
         'total_calories',
         'total_protein',
         'total_carbs',
         'total_fat',
         'client',
         'trainer',
         'order',
         'food_set'
         ]

    def create(self, validated_data):
        food_data = validated_data.pop('food_set')
        meal = Meal.objects.create(**validated_data)
        for food in food_data:
            Food.objects.create(meal=meal, **food)
        return meal