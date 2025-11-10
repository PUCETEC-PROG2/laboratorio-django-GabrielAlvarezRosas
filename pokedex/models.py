from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name=models.CharField(max_length=100, null=False)
    POKEMON_TYPES = {
        ('Agua', 'Agua'),
        ('Fuego', 'Fuego'), 
        ('Tierra', 'Tierra'),
        ('Electrico', 'Electrico'),
        ('Planta', 'Planta'),
        ('Lucha', 'Lucha'),
       
    }
    type=models.CharField(max_length=40, choices=POKEMON_TYPES, null=False)
    weight=models.IntegerField(null=False)
    height=models.IntegerField(null=False)
    trainer = models.ForeignKey('Trainer', on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to='pokemon_pictures/', null=True, blank=True)

    def __str__(self):
        return self.name
    #Trainer
    #name, age y level
class Trainer(models.Model):
    name=models.CharField(max_length=100, null=False)
    lastname=models.CharField(max_length=100, null=False)
    birthdate=models.DateField(null=False)
    level=models.CharField(max_length=70, null=False)
    picture = models.ImageField(upload_to='trainer_pictures/', null=True, blank=True)

    def __str__(self):
        return self.name
    