from django.db import models

# Create your models here.
class Generated_adress(models.Model):
    address = models.CharField(max_length=42)
    user_id = models.CharField(max_length=50)
    value = models.IntegerField(blank=True, default=None)
    def __str__(self):
        return self.address