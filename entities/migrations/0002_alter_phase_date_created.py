# Generated by Django 4.1 on 2022-08-11 17:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phase',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
