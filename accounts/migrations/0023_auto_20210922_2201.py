# Generated by Django 2.2.13 on 2021-09-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_merge_20210915_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationrecord',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
