# Generated by Django 3.2.6 on 2021-11-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20211111_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_lastname',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_middlename',
            field=models.CharField(default='', max_length=70),
        ),
    ]
