from django.db import models



class Place(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=90)
    description = models.CharField(max_length=88)
    
    def __str__(self):
        return self.name
