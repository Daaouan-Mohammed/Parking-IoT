from django.db import models

class Car(models.Model):
    clientName = models.CharField(max_length = 255)
    matricule = models.CharField(max_length = 255)


class Abonnement(models.Model):
    start_date = models.DateTimeField("start date") 
    end_date = models.DateTimeField("end date")
    car = models.ForeignKey(Car, on_delete=models.CASCADE)