from django.db import models


class College(models.Model):
    name = models.CharField(max_length=2048)
    established_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name