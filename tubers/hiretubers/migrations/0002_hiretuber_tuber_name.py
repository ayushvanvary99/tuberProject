# Generated by Django 4.0.1 on 2022-01-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiretuber',
            name='tuber_name',
            field=models.CharField(default='hi', max_length=100),
        ),
    ]
