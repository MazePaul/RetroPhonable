# Generated by Django 4.2.1 on 2023-05-20 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_alter_game_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='cover',
        ),
    ]
