# Generated by Django 3.1.1 on 2020-10-01 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
        ('profiles', '0015_auto_20201001_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonracehubfriends',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.club'),
        ),
    ]