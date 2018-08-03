from django.db import models

class NightlyStat(models.Model):

    INTENSITY = (
        ('0', 'None'),
        ('1', 'Mild'),
        ('2', 'Moderate'),
        ('3', 'Heavy'),
        ('4', 'Intense'),
    )

    MOOD = (
        ('upset', 'Upset'),
        ('irrit', 'Irritated'),
        ('sombe', 'Somber'),
        ('distr', 'Distracted'),
        ('nuetr', 'Nuetral'),
        ('happy', 'Happy'),
        ('posit', 'Positive'),
        ('joyfu', 'Joyful'),
        ('elate', 'Elated'),
        ('bliss', 'Blissful'),
        ('maxim','Top of the World'),
    )

    date = models.DateField(auto_now_add=True)
    alcohol = models.CharField(max_length=1, choices=INTENSITY)
    bedtime = models.CharField(max_length=50)
    chores = models.TextField()
    drugs = models.CharField(max_length=1, choices=INTENSITY)
    exercise = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    guitar = models.CharField(max_length=1, choices=INTENSITY)
    school = models.CharField(max_length=200)
    work = models.CharField(max_length=50)
    mood_wake = models.CharField(max_length=5, choices=MOOD)
    mood_sleep = models.CharField(max_length=5, choices=MOOD)
    notes = models.TextField()

    def __str__(self):
        return "{}".format(self.objects.all())
