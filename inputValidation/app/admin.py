from django.contrib import admin

# Register your models here.
from .models import Project, Release, Panel

admin.site.register(Project)
admin.site.register(Release)
admin.site.register(Panel)