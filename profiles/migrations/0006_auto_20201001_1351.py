# Generated by Django 3.1.1 on 2020-10-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_athleteprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athleteprofile',
            name='dateofbirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]