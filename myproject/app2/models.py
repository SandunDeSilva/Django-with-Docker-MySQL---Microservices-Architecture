from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    cost = models.DecimalField(max_length=10, decimal_places=2)
    created_at = models.DateTimeField(auto_add_now=True)

    def __str__(self):
        return self.title