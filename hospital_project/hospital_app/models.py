from django.db import models

# Create your models here.

class Docter(models.Model):
    name = models.CharField(max_length=56)
    mobile = models.IntegerField()
    special = models.CharField(max_length=56)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=56)
    gender =models.CharField(max_length=200)
    mobile = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    docter = models.ForeignKey(Docter,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.docter.name+"__"+self.patient.name