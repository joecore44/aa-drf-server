# Generated by Django 4.1.2 on 2022-11-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_trainerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainerprofile',
            name='fullName',
            field=models.CharField(max_length=50, null=True),
        ),
    ]