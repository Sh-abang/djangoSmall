from django.contrib import admin
from .models import MyUser, Entry, Profile

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Entry)
admin.site.register(Profile)