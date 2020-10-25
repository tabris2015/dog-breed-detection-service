from django.db import models


# Create your models here.
class Detection(models.Model):
    PERRO = 1
    GATO = 2
    ANIMAL = (
        (PERRO, 'Perro'),
        (GATO, 'Gato')
    )

    date = models.DateTimeField('detection date')
    animal = models.PositiveSmallIntegerField(choices=ANIMAL)
    breed = models.CharField(max_length=32,null=True, blank=True)

    def __str__(self):
        return f'{self.animal} {self.breed}'
