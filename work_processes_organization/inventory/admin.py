from django.contrib import admin
from .models import MaterialType, MaterialShape, MaterialSize, Manufacturer
# Register your models here.

# admin.site.register(Material)
admin.site.register(MaterialType)
admin.site.register(MaterialShape)
admin.site.register(MaterialSize)
admin.site.register(Manufacturer)