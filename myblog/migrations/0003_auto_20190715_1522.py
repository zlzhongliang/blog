# Generated by Django 2.2.3 on 2019-07-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_usermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='sex',
            field=models.BooleanField(null=True, verbose_name='性别'),
        ),
    ]
