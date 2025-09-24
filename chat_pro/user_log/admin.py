from django.contrib import admin
from .models import UserSignup, MailInbox
# Register your models here.

admin.site.register(UserSignup)
admin.site.register(MailInbox)
