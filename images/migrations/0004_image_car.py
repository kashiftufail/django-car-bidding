# Generated by Django 5.2.3 on 2025-07-09 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
        ('images', '0003_image_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='cars.car'),
        ),
    ]
