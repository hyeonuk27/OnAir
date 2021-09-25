# Generated by Django 3.2.7 on 2021-09-24 09:18

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
            name='Airline',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('profile_url', models.TextField()),
                ('address', models.TextField()),
                ('phone_number', models.TextField()),
                ('site_url', models.TextField()),
                ('corona_url', models.TextField()),
                ('is_skypass', models.BooleanField(blank=True, null=True)),
                ('is_star', models.BooleanField(blank=True, null=True)),
                ('is_oneworld', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Arrival',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('airline', models.CharField(max_length=20)),
                ('arrival', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=10)),
                ('reason', models.CharField(blank=True, max_length=50, null=True)),
                ('passengers', models.IntegerField()),
                ('delayed_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('flight_at', models.DateField()),
                ('seat', models.CharField(max_length=10)),
                ('score', models.IntegerField()),
                ('seat_score', models.IntegerField(blank=True, null=True)),
                ('service_score', models.IntegerField(blank=True, null=True)),
                ('checkin_score', models.IntegerField(blank=True, null=True)),
                ('food_score', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='airlines.airline')),
                ('arrival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='airlines.arrival')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('reg_dt', models.DateTimeField(auto_now_add=True)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='airlines.airline')),
                ('arrival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='airlines.arrival')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]