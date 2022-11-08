from django.contrib import admin
from .models import Meal, Food, TrainerProfile, ClientProfile, ClientCheckin
from .models import Condition, FoodInventory
admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(TrainerProfile)
admin.site.register(ClientProfile)
admin.site.register(ClientCheckin)
admin.site.register(Condition)
admin.site.register(FoodInventory)