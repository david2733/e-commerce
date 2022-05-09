from django.db import models

# Create your models here.




class User(models.Model):
    first_name = models.CharField("El nombre de la persona", max_length=30)
    last_name = models.CharField("El apellido de la persona", max_length=30)
    cars = models.ManyToManyField("Car", verbose_name="los carros del usuario")


STATUS_CHOICES = (
    ('R', "Reviewed"),
    ('N', "Not Reviewed"),
    ('E', "Error"),
    ('A', "Accepted")
)

class Website(models.Model):
    name = models.CharField( max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)#on_delete=[models.CASCADE, models.SET_NULL, models.SET_DEFAULT]



class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)
