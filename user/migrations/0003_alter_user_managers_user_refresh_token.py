# Generated by Django 4.1.3 on 2023-04-11 08:22

from django.db import migrations, models
import user.managers.user_manager


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_token'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.managers.user_manager.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='refresh_token',
            field=models.CharField(max_length=255, null=True),
        ),
    ]