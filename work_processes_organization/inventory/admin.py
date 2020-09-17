from django.contrib import admin
from .models import Material, MaterialType, MaterialShape, MaterialSize, Manufacturer, MaterialColor
# Register your models here.

admin.site.register(Material)
admin.site.register(MaterialType)
admin.site.register(MaterialShape)
admin.site.register(MaterialSize)
admin.site.register(Manufacturer)
admin.site.register(MaterialColor)