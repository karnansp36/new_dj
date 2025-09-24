from django.db import models

# Create your models here.
class UserSignup(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True, default='profiles/default.jpg')
    new_Field =models.DateTimeField(auto_now_add=True, null=True, blank=True)

class MailInbox(models.Model):
    subject = models.CharField(max_length=400)
    message = models.TextField(max_length=4000)
    toAddress = models.TextField()
    fromAddress = models.EmailField()
    createdAt = models.DateTimeField(auto_now_add=True)