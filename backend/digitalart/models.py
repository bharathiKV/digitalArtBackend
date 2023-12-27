from django.db import models

class Calendar(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    total_cost=models.CharField(max_length=100)
    prize=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Images/')
    details=models.TextField(max_length=100000, blank=True)
    order=models.PositiveSmallIntegerField(default=0)
    calendars=models.BooleanField(default=False)
    art_print=models.BooleanField(default=False)
    enabled=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering=['order']