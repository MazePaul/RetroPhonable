# Generated by Django 4.2 on 2023-05-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_game_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cover',
            field=models.ImageField(default='media/jeu/placeholder.jpeg', upload_to='media/images/'),
        ),
    ]
