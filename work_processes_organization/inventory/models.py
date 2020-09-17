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


class MaterialThickness(models.Model):
    thickness = models.FloatField("Thickness", default=0.125)
    SYSTEMS = [
        ("in", "Imperial"),
        ("mm", "CI")
    ]
    measuring_system = models.CharField("Measuring system", choices=SYSTEMS, default='in', max_length=8)

    def __str__(self):
        if self.thickness.is_integer():
            return f"{int(self.thickness)}{self.measuring_system}"
        else:
            return f"{self.thickness}{self.measuring_system}"

    class Meta:
        verbose_name = "Thickness"
        verbose_name_plural = "Thickness"


class MaterialColor(models.Model):
    color = models.CharField("Color", max_length=30)

    def __str__(self):
        return self.color


class Material(models.Model):
    material_type = models.ForeignKey(MaterialType, on_delete=models.DO_NOTHING)
    material_size = models.ForeignKey(MaterialSize, on_delete=models.DO_NOTHING)
    material_thickness = models.ForeignKey(MaterialThickness, default=1, on_delete=models.DO_NOTHING)
    material_shape = models.ForeignKey(MaterialShape, null=True, blank=True, default=1, on_delete=models.DO_NOTHING)
    color = models.ForeignKey(MaterialColor, default=1, blank=True, on_delete=models.DO_NOTHING)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{'%.0f' % self.material_size.size_x}x{'%.0f' % self.material_size.size_y}    " \
               f"{str(self.material_type.name)} {self.material_thickness}"

    class Meta:
        verbose_name = 'MATERIAL'
        verbose_name_plural = 'MATERIALS'
        constraints = [
            models.UniqueConstraint(fields=['material_type', 'material_shape', 'material_size'], name='material')
        ]

