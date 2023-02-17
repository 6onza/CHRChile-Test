from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=200)
    gbfs_href = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Station(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    free_bikes = models.IntegerField()
    empty_slots = models.IntegerField()
    timestamp = models.DateTimeField()
    address = models.CharField(max_length=200, default='')
    altitude = models.FloatField(default=0)
    ebikes = models.IntegerField(default=0)
    has_ebikes = models.BooleanField(default=False)
    last_updated = models.CharField(max_length=200, default='')
    payment = models.CharField(max_length=200, default='')
    payment_terminal = models.BooleanField(default=False)
    renting = models.IntegerField(default=0)
    returning = models.IntegerField(default=0)
    slots = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_company_name(self):
        return self.company.name

    