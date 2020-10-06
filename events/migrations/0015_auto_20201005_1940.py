# Generated by Django 3.1.1 on 2020-10-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_event_isvirtual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='isvirtual',
        ),
        migrations.AddField(
            model_name='eventinstance',
            name='isvirtual',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
