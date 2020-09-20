from django.db import models


class MaterialType(models.Model):
    name = models.CharField('material_name', max_length=40)
    abbreviation = models.CharField('Abbreviation', max_length=20, blank=True, null=True, default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    manufacturer = models.CharField('Manufacturer', max_length=30)

    class Meta:
        ordering = ['manufacturer']

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

    class Meta:
        ordering = ['size_x', 'size_y', 'size_z']

    def __str__(self):
        return str(f'{self.size_x}x{self.size_y}')


class MaterialThickness(models.Model):
    thickness = models.FloatField("Thickness", default=0.125)
    SYSTEMS = [
        ("in", "Imperial"),
        ("mm", "CI")
    ]
    measuring_system = models.CharField("Measuring system", choices=SYSTEMS, default='in', max_length=8)

    class Meta:
        verbose_name = "Thickness"
        verbose_name_plural = "Thickness"
        ordering = ['thickness']

    def __str__(self):
        if self.thickness.is_integer():
            return f"{int(self.thickness)}{self.measuring_system}"
        else:
            return f"{self.thickness}{self.measuring_system}"


class MaterialColor(models.Model):
    color = models.CharField("Color", max_length=30)

    def __str__(self):
        return self.color


class Material(models.Model):
    material_type = models.ForeignKey(MaterialType, on_delete=models.SET_NULL, null=True)
    material_size = models.ForeignKey(MaterialSize, on_delete=models.SET_NULL, null=True)
    material_thickness = models.ForeignKey(MaterialThickness, default=1, on_delete=models.SET_NULL, null=True)
    material_shape = models.ForeignKey(MaterialShape, null=True, blank=True, default=1, on_delete=models.SET_NULL)
    color = models.ForeignKey(MaterialColor, default=1, blank=True, on_delete=models.DO_NOTHING)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True, default=None, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{'%.0f' % self.material_size.size_x}x{'%.0f' % self.material_size.size_y}    " \
               f"{str(self.material_type.name)} {self.material_thickness}"

    class Meta:
        verbose_name = 'MATERIAL'
        verbose_name_plural = 'MATERIALS'
        constraints = [
            models.UniqueConstraint(fields=['material_type', 'material_shape', 'material_size'], name='material')
        ]


class PurchaseOrder(models.Model):
    po = models.PositiveIntegerField("PO", auto_created=True, primary_key=True)
    material = models.ManyToManyField(Material, through="MaterialAmount", related_name='pos')
    date_ordered = models.DateField(blank=True, default=None, null=True)
    date_received = models.DateField(blank=True, default=None, null=True)

    class Meta:
        verbose_name = "PO#"
        verbose_name_plural = "PO##"

    def __str__(self):
        return str(self.po)


class MaterialAmount(models.Model):
    po = models.ForeignKey(PurchaseOrder, related_name='material_amounts', on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey(Material, related_name='material_amounts', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()

    class Meta:
        verbose_name = "Material amount"
        verbose_name_plural = "Materials amount"

    def __str__(self):
        return f'PO:{self.po.po} {self.material} {self.amount}pcs'
