from django.db import models

#Creation of Game model
class Game(models.Model):
    console_text = models.CharField(max_length=32)
    title_text = models.CharField(max_length=64)
    category_text = models.CharField(max_length=16)
    nb_player = models.IntegerField(default=1)

    #Hence comprehension of which object (games) it is
    def __str__(self):
        return self.title_text
    def from_console(self):
        return self.console_text
    def is_category(self):
        return self.category_text
    def playable_with(self):
        return self.nb_player