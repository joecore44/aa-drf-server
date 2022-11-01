from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class TrainerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=10, default='trainer')
    username = models.CharField(max_length=100)
    country = models.CharField(max_length=4, default='USA')
    contact = models.CharField(max_length=16, default='(555) 555-5555')
    email = models.EmailField(max_length=100)
    currentPlan = models.CharField(max_length=100, default='enterprise')
    status = models.CharField(max_length=24, default='active')
    avatar = models.CharField(max_length=100, default='https://personal-portfolio-v2-ae3h.vercel.app/images/formal-image-joe-s.png')
    avatarColor = models.CharField(max_length=25, default='primary')

    def __str__(self):
        return f'{self.fullName}'

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=10, default='client')
    username = models.CharField(max_length=100)
    country = models.CharField(max_length=4, default='USA')
    contact = models.CharField(max_length=16, default='(555) 555-5555')
    email = models.EmailField(max_length=100)
    currentPlan = models.CharField(max_length=100, default='enterprise')
    status = models.CharField(max_length=24, default='active')
    avatar = models.CharField(max_length=100, default='https://personal-portfolio-v2-ae3h.vercel.app/images/formal-image-joe-s.png')
    avatarColor = models.CharField(max_length=25, default='primary')

    def __str__(self):
        return f'{self.fullName}'


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ManyToManyField('Food', blank=True)

    date = models.DateField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    total_calories = models.FloatField(null=True)
    total_protein = models.FloatField(null=True)
    total_carbs = models.FloatField(null=True)
    total_fat = models.FloatField(null=True)
    order = models.IntegerField()

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
