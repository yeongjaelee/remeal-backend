# Generated by Django 4.1.3 on 2023-05-10 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userimage',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
