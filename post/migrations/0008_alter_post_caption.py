# Generated by Django 4.1.3 on 2022-11-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_post_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=1000000, verbose_name='Caption'),
        ),
    ]