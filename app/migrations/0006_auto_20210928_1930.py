# Generated by Django 3.2.6 on 2021-09-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_patient_patient_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('medicinename', models.CharField(max_length=70)),
                ('medicinetiming', models.IntegerField()),
                ('medicineprice', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='patient_number',
        ),
    ]
