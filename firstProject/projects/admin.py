from django.contrib import admin

# Register your models here.
from projects.models import Track, Album

admin.site. register(Track)
admin.site. register(Album)