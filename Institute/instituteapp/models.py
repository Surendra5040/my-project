from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    query=models.TextField(max_length=200)

class Feedback(models.Model):
    name=models.CharField(max_length=30)
    Date=models.DateTimeField(auto_now_add=True)
    feedback=models.TextField(max_length=100)


