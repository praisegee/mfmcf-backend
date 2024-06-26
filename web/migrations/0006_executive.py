# Generated by Django 4.2.1 on 2023-05-06 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_spotlight_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, verbose_name='Full name')),
                ('campus', models.CharField(choices=[('oye', 'Oye'), ('ikole', 'Ikole')], default='Oye', max_length=10, verbose_name='Campus')),
                ('position', models.CharField(help_text='Office post', max_length=50, verbose_name='Position')),
                ('picture', models.ImageField(upload_to='', verbose_name='Picture')),
                ('facebook', models.URLField(verbose_name='Facebook profile link')),
                ('twitter', models.URLField(verbose_name='Twitter profile link')),
                ('linked_in', models.URLField(verbose_name='LinkedIn profile link')),
                ('instagram', models.URLField(verbose_name='Instagram profile link')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
