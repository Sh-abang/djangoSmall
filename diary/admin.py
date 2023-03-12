from django.contrib import admin
from .models import MyUser, Entry

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Entry)