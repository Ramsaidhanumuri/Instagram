# Generated by Django 4.1.3 on 2022-11-05 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='psot',
            new_name='post',
        ),
    ]
