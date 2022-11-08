from django.contrib.auth.models import User, Group
from .models import Meal, Food, TrainerProfile, ClientProfile
from .models import ClientCheckin, Condition, FoodInventory
from rest_framework import serializers

class TrainerProfileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = TrainerProfile
        fields = '__all__'

class ConditionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Condition
        fields = '__all__'
    def create(self, validated_data):
        return Condition.objects.create(**validated_data)
        

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

    def update(self, instance, validated_data):
 
        food_data = validated_data.pop('food_set')
        foods = (instance.food_set).all()
        foods = list(foods)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.total_calories = validated_data.get('total_calories', instance.total_calories)
        instance.total_protein = validated_data.get('total_protein', instance.total_protein)
        instance.total_carbs = validated_data.get('total_carbs', instance.total_carbs)
        instance.total_fat = validated_data.get('total_fat', instance.total_fat)
        instance.client = validated_data.get('client', instance.client)
        instance.trainer = validated_data.get('trainer', instance.trainer)
        instance.order = validated_data.get('order', instance.order)
        instance.save()

        for food in food_data:
            food_instance = foods.pop(0)
            food_instance.name = food.get('name', food_instance.name)
            food_instance.calories = food.get('calories', food_instance.calories)
            food_instance.protein = food.get('protein', food_instance.protein)
            food_instance.carbs = food.get('carbs', food_instance.carbs)
            food_instance.fats = food.get('fats', food_instance.fats)
            food_instance.quantity = food.get('quantity', food_instance.quantity)
            food_instance.save()
        return instance

class FoodInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodInventory
        fields = '__all__'

    
    