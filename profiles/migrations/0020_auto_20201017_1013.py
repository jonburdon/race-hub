# Generated by Django 3.1.1 on 2020-10-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_auto_20201007_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonracehubfriends',
            name='emergencycontactname',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='nonracehubfriends',
            name='emergencycontactphone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
