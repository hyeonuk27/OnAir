# Generated by Django 3.2.7 on 2021-09-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticsResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('under_10', models.FloatField()),
                ('under_30', models.FloatField()),
                ('over_30', models.FloatField()),
                ('delay_rate', models.FloatField()),
                ('delay_time', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='airline',
            old_name='is_skypass',
            new_name='is_skyteam',
        ),
    ]
