from django.contrib import admin

# Register your models here.
from .models import Project, Release, Panel, Task, Staff

admin.site.register(Project)
admin.site.register(Release)
admin.site.register(Panel)
admin.site.register(Task)
admin.site.register(Staff)
