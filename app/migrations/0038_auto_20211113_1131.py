# Generated by Django 3.2.6 on 2021-11-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_blooddonation_bloodgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonation',
            name='bloodgroup',
            field=models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='O+', max_length=10),
        ),
        migrations.AlterField(
            model_name='blooddonation',
            name='healthissue',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
