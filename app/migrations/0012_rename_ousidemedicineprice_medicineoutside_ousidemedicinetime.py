# Generated by Django 3.2.6 on 2021-10-02 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_medicineoutside'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicineoutside',
            old_name='ousidemedicineprice',
            new_name='ousidemedicinetime',
        ),
    ]
