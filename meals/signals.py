from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import ClientProfile, ClientCheckin, TrainerProfile, Meal


@receiver(post_save, sender=ClientCheckin)
def create_client_checkin(sender, instance, created, **kwargs):
    if created:
        client = ClientProfile.objects.filter(pk=instance.client.id).first()
        client.current_height = client.starting_height
        client.current_weight = instance.weight
        client.current_body_fat_mass = instance.body_fat_mass
        client.current_body_fat_percentage = instance.body_fat_percentage
        client.current_skeletul_muscle_mass = instance.skeletul_muscle_mass
        
        client.save()

@receiver(post_save, sender=ClientCheckin)
def save_client_checkin(sender, instance,  **kwargs):
    client = ClientProfile.objects.filter(pk=instance.client.id).first()
    client.current_height = client.starting_height
    client.current_weight = instance.weight
    client.current_body_fat_mass = instance.body_fat_mass
    client.current_body_fat_percentage = instance.body_fat_percentage
    client.current_skeletul_muscle_mass = instance.skeletul_muscle_mass
    
    client.save()


@receiver(post_save, sender=Meal)
def create_meal(sender, instance, created, **kwargs):
    if created:
        meal = Meal.objects.filter(pk=instance.id).first()
        meal.title = meal.title + ' Calories: ' + str(instance.total_calories)
        meal.save()
