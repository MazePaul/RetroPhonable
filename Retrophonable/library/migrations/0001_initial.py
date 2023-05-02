# Generated by Django 4.2 on 2023-05-01 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jeu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('console_text', models.CharField(max_length=32)),
                ('titre_text', models.CharField(max_length=64)),
                ('Categorie_text', models.CharField(max_length=16)),
                ('Nb_joueur', models.IntegerField(default=1)),
                ('etat_jeu', models.IntegerField(default=0)),
            ],
        ),
    ]
