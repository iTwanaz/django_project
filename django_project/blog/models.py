from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#this class model is a corresponding mysql table in the database----to view the sql code :use: python manage.py sqlmigrate <app_name> <migration no.>
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)        #references to the User class in auth.models

    def __str__(self):
        return self.title