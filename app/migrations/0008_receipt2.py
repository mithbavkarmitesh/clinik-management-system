# Generated by Django 3.2.6 on 2021-09-30 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210928_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='receipt2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('medicinename', models.CharField(max_length=70)),
                ('medicinetiming', models.CharField(max_length=100)),
                ('medicineprice', models.CharField(max_length=100)),
            ],
        ),
    ]
