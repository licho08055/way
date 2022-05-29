from django.db import models

class Bone(models.Model):
    title = models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.title
    
    
class Active(models.Model):
    bone = models.ForeignKey(Bone, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=4000,decimal_places=9)
    
    def __str__(self):
        return f'{self.name} {self.price}'
    
