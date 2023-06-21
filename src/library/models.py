from django.db import models

#Creation of Game model
class Game(models.Model):
    console_text = models.CharField(max_length=32)
    title_text = models.CharField(max_length=64)
    category_text = models.CharField(max_length=16)
    multiplayer = models.BooleanField(default=0)
    #upload_to='images/' permet d'upload les images dans la valeur de MEDIA ROOT définie dans settings.py
    cover = models.ImageField(upload_to='images', default='images/placeholder.jpeg')

    #Hence comprehension of which object (games) it is
    def __str__(self):
        return self.title_text
    def from_console(self):
        return self.console_text
    def is_category(self):
        return self.category_text
    def playable_with(self):
        return self.nb_player
    def is_multiplayer(self):
        return self.multiplayer
    def cover_game(self):
        return self.cover