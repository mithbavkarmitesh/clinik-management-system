# Generated by Django 3.2.6 on 2021-09-30 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210930_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='medicineprice',
            field=models.CharField(default='HELLO', max_length=100),
        ),
    ]
