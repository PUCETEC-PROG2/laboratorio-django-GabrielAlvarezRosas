from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name=models.CharField(max_length=100, null=False)
    type=models.CharField(max_length=40, null=False)
    weight=models.IntegerField(null=False)
    height=models.IntegerField(null=False)

    def __str__(self):
        return self.name
    ##Trainer
    #name, age y level
class Trainer(models.Model):
    name=models.CharField(max_length=100, null=False)
    lastname=models.CharField(max_length=100, null=False)
    birthdate=models.DateField(null=False)
    level=models.CharField(max_length=70, null=False)

    def __str__(self):
        return self.name
    