# Generated by Django 3.2.7 on 2021-09-29 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0006_merge_20210929_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statisticsresult',
            old_name='over_30',
            new_name='over_60',
        ),
        migrations.RenameField(
            model_name='statisticsresult',
            old_name='under_10',
            new_name='under_60',
        ),
    ]
