# Generated by Django 3.1.4 on 2021-01-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210127_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mail',
            field=models.EmailField(max_length=254),
        ),
    ]