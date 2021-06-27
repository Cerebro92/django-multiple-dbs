from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=2048)
    age = models.IntegerField()
    gender = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
