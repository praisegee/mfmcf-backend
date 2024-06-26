# Generated by Django 4.2.1 on 2023-05-05 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SpotLight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Prefix the name with a title (Bro|Sis) e.g Bro PraiseGod.', max_length=100, verbose_name='Name')),
                ('description', models.CharField(help_text='A short description of the person.', max_length=500, verbose_name='Description')),
                ('birthdate', models.CharField(help_text='Just the day and the month; in the formart `DD-MM`.', max_length=20, verbose_name='Date')),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('engaged', 'Engaged'), ('married', 'Married')], default='Single', max_length=10, verbose_name='Marital status')),
                ('hobby', models.CharField(max_length=50, verbose_name='Hobby')),
                ('picture', models.ImageField(upload_to='', verbose_name='Picture')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Auth User')),
            ],
        ),
        migrations.CreateModel(
            name='BirthdayCelebrant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Prefix the name with a title (Bro|Sis) e.g Bro PraiseGod.', max_length=100, verbose_name='Name')),
                ('birthdate', models.CharField(help_text='Just the day and the month; in the formart `DD-MM`.', max_length=20, verbose_name='Date')),
                ('picture', models.ImageField(upload_to='', verbose_name='Picture')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Auth User')),
            ],
        ),
    ]
