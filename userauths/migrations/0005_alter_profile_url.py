# Generated by Django 4.1.3 on 2022-11-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0004_alter_profile_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='url',
            field=models.URLField(blank=True, max_length=10, null=True),
        ),
    ]
