from django.db import models

class Component(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Vehicle(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    model = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)

class Repair(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    issue_description = models.TextField()
    components = models.ManyToManyField(Component, blank=True)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def total_cost(self):
        return self.labor_cost + sum([comp.price for comp in self.components.all()])
