# Generated by Django 4.2 on 2023-05-19 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_game_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='cover',
        ),
    ]
