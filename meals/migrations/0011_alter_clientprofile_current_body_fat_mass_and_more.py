# Generated by Django 4.1.2 on 2022-11-01 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0010_alter_clientprofile_current_body_fat_mass_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='current_body_fat_mass',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='current_body_fat_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='current_height',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='current_skeletul_muscle_mass',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='current_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='starting_body_fat_mass',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='starting_body_fat_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='starting_height',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='starting_skeletul_muscle_mass',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='starting_weight',
            field=models.FloatField(default=0),
        ),
    ]
