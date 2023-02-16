from django.db import models


class Project(models.Model):
    number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    typology = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    investment = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    map = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

