from django.db import models

# Create your models here.
class Details(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    email = models.TextField()
    password = models.TextField()
    
    def __str__(self):
        return self.email
    