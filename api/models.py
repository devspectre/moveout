from django.db import models
from django.utils import timezone

# Create your models here.
class Moveout(models.Model):
    # id = models.IntegerField()
    date = models.DateField(default=timezone.now)
    address = models.CharField(max_length=255, blank=True)
    room = models.SmallIntegerField(default=1)
    location = models.CharField(max_length=255, blank=True)
    last_occupant = models.CharField(max_length=255, blank=True)
    uid = models.IntegerField()
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return 'Moveout at {} on {}'.format(self.address, str(self.date))