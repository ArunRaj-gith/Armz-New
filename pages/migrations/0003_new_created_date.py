# Generated by Django 4.2.5 on 2023-09-22 07:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
