# Generated by Django 4.2.1 on 2023-05-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_remove_game_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cover',
            field=models.ImageField(default='images/placeholder.jpeg', upload_to='images'),
        ),
    ]
