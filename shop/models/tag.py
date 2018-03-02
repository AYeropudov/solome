from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    code = models.SlugField(max_length=100, db_index=True)
