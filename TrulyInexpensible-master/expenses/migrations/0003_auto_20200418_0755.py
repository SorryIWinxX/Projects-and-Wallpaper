# Generated by Django 3.0.4 on 2020-04-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20200418_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
