# Generated by Django 3.2.17 on 2023-02-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csiblog', '0024_auto_20230224_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
