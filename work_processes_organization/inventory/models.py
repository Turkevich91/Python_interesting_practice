from django.db import models


class MaterialType(models.Model):
    name = models.CharField('material_name', max_length=40)
    abbreviation = models.CharField('Abbreviation', max_length=20, blank=True, null=True, default="")

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    manufacturer = models.CharField('Manufacturer', max_length=30)

    def __str__(self):
        return self.manufacturer


class MaterialShape(models.Model):
    name = models.CharField('material_shape', max_length=20)

    def __str__(self):
        return self.name


class MaterialSize(models.Model):
    size_x = models.FloatField("size_x")
    size_y = models.FloatField("size_y", default=None, blank=True, null=True)
    size_z = models.FloatField("size_z", default=None, blank=True, null=True)
    sizes = models.CharField('additional sizes', max_length=100, default=None, blank=True)

    def __str__(self):
        return str(f'{self.size_x}x{self.size_y}')


class Material(models.Model):
    material_type = models.ForeignKey(MaterialType, on_delete=models.DO_NOTHING)
    material_shape = models.ForeignKey(MaterialShape, on_delete=models.DO_NOTHING)
    material_size = models.ForeignKey(MaterialSize, on_delete=models.DO_NOTHING)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(f"{str(self.material_type.name)[:3]}: {self.material_size.size_x}x{self.material_size.size_y}")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['material_type', 'material_shape', 'material_size'], name='material')
        ]
