# Generated by Django 4.1.2 on 2022-11-03 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0012_clientcheckin_public_clientprofile_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='food',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='user',
        ),
        migrations.AddField(
            model_name='food',
            name='meal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meals.meal'),
        ),
        migrations.AddField(
            model_name='meal',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meals.clientprofile'),
        ),
        migrations.AddField(
            model_name='meal',
            name='trainer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meals.trainerprofile'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.CharField(default='https://images.immediate.co.uk/production/volatile/sites/30/2020/08/american-style-pancakes-34d56dc.jpg?quality=90&resize=440,400', max_length=500),
        ),
    ]
