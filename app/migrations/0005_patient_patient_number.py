# Generated by Django 3.2.6 on 2021-09-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210918_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_number',
            field=models.IntegerField(null=True),
        ),
    ]
