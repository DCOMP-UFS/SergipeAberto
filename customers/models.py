from django.db import models

class MunicipalPortal(models.Model):
    name = models.CharField("Portal Name", max_length=255)
    link = models.TextField(blank=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self): 
        return self.name

