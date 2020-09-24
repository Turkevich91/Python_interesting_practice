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

    class Meta:
        verbose_name = 'MATERIAL'
        verbose_name_plural = 'MATERIALS'
        ordering = ['material_type', 'material_size', 'material_thickness', 'color', ]
        constraints = [
            models.UniqueConstraint(fields=['material_type', 'material_shape', 'material_size'], name='material')
        ]

    def __str__(self):
        return f"{str(self.material_type.name)} { '%.0f' % self.material_size.size_x}x" \
               f"{'%.0f' % self.material_size.size_y} {self.material_thickness}"


class PurchaseOrder(models.Model):
    po = models.PositiveIntegerField("PO", auto_created=True, primary_key=True)
    material = models.ManyToManyField(Material, through="Pallet")
    date_ordered = models.DateField(blank=True, default=None, null=True)
    date_received = models.DateField(blank=True, default=None, null=True)

    class Meta:
        verbose_name = "PO#"
        verbose_name_plural = "PO##"

    def __str__(self):
        return str(self.po)


class PalletPlace(models.Model):
    place_name = models.CharField("Pallet place", max_length=30)
    place_descriptions = models.CharField("Place descriptions", max_length=100, blank=True)

    def __str__(self):
        if self.place_descriptions:
            return f"{self.place_name} ({self.place_descriptions})"
        else:
            return self.place_name


class Pallet(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, null=True)
    material = models.ForeignKey(Material, related_name="pallet", on_delete=models.CASCADE, null=True)
    material_amount = models.IntegerField()
    pallet_place = models.ForeignKey(PalletPlace, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Pallet"
        verbose_name_plural = "Pallets"

    def __str__(self):
        return f'PO:{self.purchase_order} {self.material} {self.material_amount}pcs'
