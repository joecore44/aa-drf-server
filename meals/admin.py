from django.contrib import admin
from .models import Meal, Food, TrainerProfile, ClientProfile

admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(TrainerProfile)
admin.site.register(ClientProfile)
