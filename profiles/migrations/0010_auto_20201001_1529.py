# Generated by Django 3.1.1 on 2020-10-01 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20201001_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racehubfriends',
            name='racehubfriends',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.athleteprofile'),
        ),
    ]