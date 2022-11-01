# Generated by Django 4.1.2 on 2022-10-31 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='foods/images/')),
                ('calories', models.FloatField()),
                ('protein', models.FloatField()),
                ('carbs', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='meals/images/')),
                ('total_calories', models.FloatField()),
                ('total_protein', models.FloatField()),
                ('total_carbs', models.FloatField()),
                ('order', models.IntegerField()),
                ('food', models.ManyToManyField(to='meals.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]