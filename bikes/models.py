from django.db import models

# data returned from api endpoint:
# {
    #     "empty_slots": 5,
    #     "extra": {
    #       "address": "Alcalde Dávalos 124",
    #       "altitude": 0,
    #       "ebikes": 0,
    #       "has_ebikes": true,
    #       "last_updated": 1676478183,
    #       "normal_bikes": 2,
    #       "payment": [
    #         "key",
    #         "transitcard",
    #         "creditcard",
    #         "phone"
    #       ],
    #       "payment-terminal": true,
    #       "post_code": "1111",
    #       "renting": 1,
    #       "returning": 1,
    #       "slots": 7,
    #       "uid": "237"
    #     },
    #     "free_bikes": 2,
    #     "id": "e1593acef03a0fd770595370586bc358",
    #     "latitude": -33.428334,
    #     "longitude": -70.627312,
    #     "name": "P31 - Estación Canal 13",
    #     "timestamp": "2023-02-15T16:24:34.841000Z"
    #   }


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

    