from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Languangedetails(models.Model):
    languange_name = models.CharField(max_length=255)
    is_language = models.BooleanField(default=True)

    def __str__(self):
        return self.languange_name
class Note(models.Model):
    title=models.CharField(max_length=1000,null=False)
    description=models.TextField(null=False)
    languange_name=models.ForeignKey(Languangedetails,on_delete=models.CASCADE, verbose_name="Programming Language")
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
