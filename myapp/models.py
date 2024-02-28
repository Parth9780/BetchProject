from django.db import models

# Create your models here.
class usersignup(models.Model):
    created=models.DateTimeField(auto_now_add = True)
    Firstname = models.CharField(max_length=20)
    Lasttname = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    username = models.EmailField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile = models.BigIntegerField()

class user_notes(models.Model):
    title = models.CharField(max_length=100)
    cate = models.CharField(max_length=50)
    file = models.FileField(upload_to='User_Notes')
    textarea = models.TextField()