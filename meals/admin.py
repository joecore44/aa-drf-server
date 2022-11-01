from django.contrib import admin
from .models import Meal, Food, TrainerProfile, ClientProfile, ClientCheckin

admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(TrainerProfile)
admin.site.register(ClientProfile)
admin.site.register(ClientCheckin)