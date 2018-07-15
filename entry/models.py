from django.db import models

class NightlyStat(models.Model):
    alcohol = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.alcohol)
