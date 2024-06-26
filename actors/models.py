from django.db import models

# Create your models here.

NATIONALITY_CHOICHES = (
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brasil'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField(blank=True, null=True)
    nationality = models.CharField(choices=NATIONALITY_CHOICHES, max_length=3)

    def __str__(self):
        return self.name
