# Generated by Django 4.1.2 on 2022-11-04 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0017_alter_clientmedicalcontitions_client'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientMedicalContitions',
            new_name='ClientMedicalCondition',
        ),
    ]