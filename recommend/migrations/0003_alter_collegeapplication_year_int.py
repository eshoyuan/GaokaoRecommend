# Generated by Django 3.2.5 on 2021-07-14 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0002_auto_20210714_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeapplication',
            name='year_int',
            field=models.IntegerField(default=2020),
        ),
    ]