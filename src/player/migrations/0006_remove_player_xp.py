# Generated by Django 4.2 on 2023-05-26 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_player_id_alter_player_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='xp',
        ),
    ]
