# Generated by Django 4.0.1 on 2022-02-03 19:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team_yt_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pargraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstpara', ckeditor.fields.RichTextField()),
                ('secondpara', ckeditor.fields.RichTextField()),
            ],
        ),
    ]