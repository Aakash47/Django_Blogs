# Generated by Django 3.1.4 on 2021-01-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210125_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='This Field should be unique', max_length=200, unique=True),
        ),
    ]
