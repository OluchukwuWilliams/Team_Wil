# Generated by Django 4.2.2 on 2023-06-13 12:18

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(default='ad', max_length=100)),
                ('last_Name', models.CharField(default='ad', max_length=100)),
                ('pix', models.ImageField(default='avatar.png', upload_to='Profile')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=150)),
                ('dob', models.CharField(default='a', max_length=20)),
                ('nationality', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
