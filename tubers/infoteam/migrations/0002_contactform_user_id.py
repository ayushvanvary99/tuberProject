# Generated by Django 4.0.1 on 2022-02-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoteam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='user_id',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
