from django.db import models

class Posting(models.Model):
    title = models.CharField(max_length=50, default = "default title")
    date = models.DateField(auto_now_add=True)
    contents = models.TextField(default = "default text")
