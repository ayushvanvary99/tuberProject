# Generated by Django 4.0.1 on 2022-02-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoteam', '0002_contactform_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]