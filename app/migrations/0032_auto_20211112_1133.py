# Generated by Django 3.2.6 on 2021-11-12 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20211112_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criticalpatient',
            old_name='chealthproblem',
            new_name='healthproblem',
        ),
        migrations.RenameField(
            model_name='criticalpatient',
            old_name='cpatient_address',
            new_name='patient_address',
        ),
        migrations.RenameField(
            model_name='criticalpatient',
            old_name='cpatient_firstname',
            new_name='patient_firstname',
        ),
        migrations.RenameField(
            model_name='criticalpatient',
            old_name='cpatient_lastname',
            new_name='patient_lastname',
        ),
        migrations.RenameField(
            model_name='criticalpatient',
            old_name='cpatient_middlename',
            new_name='patient_middlename',
        ),
        migrations.RenameField(
            model_name='criticalpatient',
            old_name='cpatient_mobileno',
            new_name='patient_mobileno',
        ),
        migrations.RenameField(
            model_name='criticalpatient',
            old_name='cprescribedoctorname',
            new_name='prescribedoctorname',
        ),
        migrations.RenameField(
            model_name='criticalpatient',
            old_name='ctime',
            new_name='time',
        ),
    ]
