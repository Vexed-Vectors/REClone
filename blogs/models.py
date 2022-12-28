from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#https://github.com/gayatriagarwal19/rec
