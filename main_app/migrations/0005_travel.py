# Generated by Django 5.0.6 on 2024-06-06 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_journal_id_entry_journal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('body', models.CharField(max_length=1000)),
                ('notes', models.CharField(max_length=300)),
                ('mood_tracker', models.CharField(max_length=25)),
                ('location', models.CharField(max_length=50)),
                ('food', models.CharField(max_length=50)),
                ('weather', models.CharField(choices=[('S', 'Sunny ☀️'), ('C', 'Cloudy ☁️'), ('R', 'Rainy 🌧️'), ('T', 'Thunderstorm ⛈️'), ('N', 'Snowy ❄️'), ('W', 'Windy 🌬️'), ('F', 'Foggy 🌫️')], default='S', max_length=1)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.journal')),
            ],
        ),
    ]
