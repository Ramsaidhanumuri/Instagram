# Generated by Django 4.1.3 on 2022-11-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='url',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]