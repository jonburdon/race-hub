# Generated by Django 3.1.1 on 2020-10-03 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_auto_20200928_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='athletefirstname',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='athletesurname',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
