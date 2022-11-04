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
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE, default='1')
    public = models.BooleanField(default=True)
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
    starting_weight = models.FloatField(default=0)
    starting_height = models.FloatField(default=0)
    starting_body_fat_mass = models.FloatField(default=0)
    starting_body_fat_percentage = models.FloatField(default=0)
    starting_skeletul_muscle_mass = models.FloatField(default=0)
    current_weight = models.FloatField(default=0)
    current_height = models.FloatField(default=0)
    current_body_fat_mass = models.FloatField(default=0)
    current_body_fat_percentage = models.FloatField(default=0)
    current_skeletul_muscle_mass = models.FloatField(default=0)


    def __str__(self):
        return f'{self.fullName}'


class ClientCheckin(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
    checkin_date = models.DateField(auto_now_add=True)
    checkin_mood = models.CharField(choices=(('1', '1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')), max_length=1, default='5')
    public = models.BooleanField(default=True)
    back_photo = models.CharField(max_length=100, default='https://personal-portfolio-v2-ae3h.vercel.app/images/formal-image-joe-s.png', null=True)
    front_photo = models.CharField(max_length=100, default='https://personal-portfolio-v2-ae3h.vercel.app/images/formal-image-joe-s.png', null=True)
    side_photo = models.CharField(max_length=100, default='https://personal-portfolio-v2-ae3h.vercel.app/images/formal-image-joe-s.png', null=True)
    weight = models.FloatField()
    body_fat_mass = models.FloatField(null=True)
    body_fat_percentage = models.FloatField(null=True)
    skeletul_muscle_mass = models.FloatField(null=True)

    def __str__(self):
        return f'{self.client}'

class Meal(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, default=1)
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500, default='https://images.immediate.co.uk/production/volatile/sites/30/2020/08/american-style-pancakes-34d56dc.jpg?quality=90&resize=440,400')
    total_calories = models.FloatField(null=True)
    total_protein = models.FloatField(null=True)
    total_carbs = models.FloatField(null=True)
    total_fat = models.FloatField(null=True)
    order = models.IntegerField()

    def __str__(self):
        return self.name

class Food(models.Model):
    meal = models.ForeignKey(Meal, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    calories = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Condition(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name