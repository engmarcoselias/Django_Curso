# Generated by Django 4.1.7 on 2023-03-29 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_rename_phon_members_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]