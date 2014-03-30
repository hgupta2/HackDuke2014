from django.contrib import admin

from blog.models import youtube
from blog.models import courses

# Register your models here.
admin.site.register(youtube)
admin.site.register(courses)

