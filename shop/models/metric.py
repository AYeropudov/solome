import datetime
from django.db import models

# HASH url + ip + session


class Metric(models.Model):
    hash_counter = models.CharField(max_length=250)
    hash_url = models.CharField(max_length=250)
    created_at = models.DateTimeField('date created', auto_now_add=True)


class MetricTotals(models.Model):
    id = models.CharField(max_length=250, primary_key=True)
    counter = models.IntegerField(blank=False, default=0)
