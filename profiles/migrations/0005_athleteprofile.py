# Generated by Django 3.1.1 on 2020-10-01 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0004_remove_userprofile_eanumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthleteProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eanumber', models.CharField(blank=True, max_length=80, null=True)),
                ('eaverified', models.BooleanField(default=True)),
                ('dateofbirth', models.DateTimeField(blank=True, null=True)),
                ('emergencycontactname', models.CharField(blank=True, max_length=60, null=True)),
                ('emergencycontactphone', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F'), ('N', 'Prefer not to say')], max_length=2, null=True)),
                ('tshirtsize', models.CharField(choices=[('Small', 'Small'), ('Med', 'Medium'), ('Large', 'Large')], default='Med', max_length=5)),
                ('club', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clubs.club')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userprofile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
        ),
    ]
