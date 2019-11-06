from django.db import models

# Create your models here.
class Lead(models.Model): # using Model from models
  # define the fields we want
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100, unique=True) #capital True
  message = models.CharField(max_length=500, blank=True) #blank makes message optional
  created_at = models.DateTimeField(auto_now_add=True) # add date automatically