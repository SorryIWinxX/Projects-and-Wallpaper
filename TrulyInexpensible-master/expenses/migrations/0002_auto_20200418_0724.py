# Generated by Django 3.0.4 on 2020-04-18 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='spent_on',
            new_name='date',
        ),
    ]