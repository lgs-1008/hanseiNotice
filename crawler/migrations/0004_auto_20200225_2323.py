# Generated by Django 2.2.7 on 2020-02-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0003_auto_20200225_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateField(),
        ),
    ]
