from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models import Q


# from django.utils import timezone


class Project(models.Model):
    project_number = models.PositiveIntegerField('Project number')
    project_title = models.CharField('Project title', max_length=200, blank=True)
    project_path = models.CharField('File Path', max_length=200, blank=True)
    project_manager = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_NULL,
                                        limit_choices_to=Q(groups=2))  # id(2) == group_name("PM")
    purchase_order = models.ForeignKey('inventory.PurchaseOrder', default=None, null=True, blank=True,
                                       on_delete=models.SET_NULL)  # thanks https://t.me/pydjango@eva_kuator
    address = models.CharField('Address', max_length=254, null=True, blank=True)
    mail_address = models.CharField("Mail address", max_length=254, null=True, blank=True)

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        constraints = [
            models.UniqueConstraint(fields=['project_number'], name='project_number')
        ]

    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.project_number)

    # def was_published_recently(self):
    #     return self.creation_date >= (timezone.now() - datetime.timedelta(days=14))


class Release(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    release_title = models.CharField('Release name', max_length=10)
    release_folder = models.CharField('Folder', max_length=200,
                                      default=r"PD",
                                      blank=True)
    # production specific information
    material_type = models.ForeignKey('inventory.MaterialType', on_delete=models.CASCADE)
    material_thickness = models.ForeignKey('inventory.MaterialThickness', on_delete=models.CASCADE)
    material_color = models.ForeignKey('inventory.MaterialColor', on_delete=models.CASCADE, blank=True, null=True)
    grain_direction = models.BooleanField("GD")
    provided_material = models.ManyToManyField('inventory.Material', through="ReleaseMaterial",
                                               blank=True)

    # data-time fields
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'release'
        verbose_name_plural = 'releases'
        constraints = [
            models.UniqueConstraint(fields=['release_title', 'project'], name='unique pro releases'),
            # models.CheckConstraint(check=())
        ]

    def __str__(self):
        return str(f'{self.project.project_number} - {self.release_title}')


class ReleaseMaterial(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)  # не вырубать! нужно даже если все вот это.
    material = models.ForeignKey('inventory.Material', on_delete=models.CASCADE)
    material_quantity = models.PositiveIntegerField('quantity')

    class Meta:
        verbose_name = 'Expected material usage'

    def __str__(self):
        return f'{self.release} - [{self.material}] - ({self.material_quantity} pcs)'


class Panel(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    panel_title = models.CharField('Panel title', max_length=10)
    panel_quantity = models.PositiveIntegerField('Quantity', blank=True, default=1)
    modified = models.DateTimeField(auto_now=True)
    size_x = models.FloatField('X')
    size_y = models.FloatField('Y')

    # # report fields
    punching_operator = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name="punching_operator")
    punching_operator_helper = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_NULL,
                                                 related_name="punch_operator_helper")
    bending_operator = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name="bending_operator")
    fabricator = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="fabricator")
    punch_datetime = models.DateTimeField(default=None, null=True, blank=True)
    bend_datetime = models.DateTimeField(default=None, null=True, blank=True)
    fabricated = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.release}-{self.panel_title}'

    class Meta:
        verbose_name = 'panel'
        verbose_name_plural = 'panels'
        constraints = [
            models.UniqueConstraint(fields=['release', 'panel_title'], name='unique panels')
        ]


class Nest(models.Model):
    name = models.CharField("name", max_length=56, unique=True)
    release = models.ForeignKey(Release, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Nest'
        verbose_name_plural = 'Nests'


class Layout(models.Model):
    name = models.CharField("name", max_length=16)
    quantity = models.PositiveIntegerField('Quantity', default=1)
    produced = models.PositiveIntegerField('Produced', default=0)
    nest = models.ForeignKey(Nest, on_delete=models.CASCADE)
    panels = models.ManyToManyField(Panel, through="LayoutPanel")

    def __str__(self):
        return f'{self.nest}-{self.name}'

    class Meta:
        verbose_name = 'layout'
        verbose_name_plural = 'layouts'
        constraints = [
            models.UniqueConstraint(fields=['name', 'nest'], name='unique layout')
        ]


class LayoutPanel(models.Model):
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.layout.nest.name}-{self.layout.name}-{self.panel.panel_title} ({self.quantity})'

    class Meta:
        verbose_name = "Layout's panel"


class Task(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    loose_items = models.BooleanField(default=False)
    outsource_paint = models.BooleanField(default=False)
    zee_hats_angels = models.IntegerField(blank=True, null=True)
    flashing = models.IntegerField(blank=True, null=True)
    coping = models.IntegerField(blank=True, null=True)
    splice_plate = models.IntegerField(blank=True, null=True)
    blade_screen = models.IntegerField(blank=True, null=True)
    perf = models.IntegerField(blank=True, null=True)
    plate_panels = models.IntegerField(blank=True, null=True)
    frames = models.IntegerField(blank=True, null=True)
    strapping = models.IntegerField(blank=True, null=True)
    clips = models.IntegerField(blank=True, null=True)
    misc = models.IntegerField(blank=True, null=True)
    est_mh = models.IntegerField(blank=True, null=True)  # Established Man hours
    rel_date = models.DateField(auto_now_add=True)
    requested_ship_date = models.DateField(blank=True, default=None, null=True)
    shipped_date = models.DateField(blank=True, default=None, null=True)
    STATUSES = [
        ('In progress', 'In progress'),
        ('Delayed', 'Delayed'),
        ('Producing', 'Producing'),
        ('Ready for Pick Up', 'Ready for Pick Up'),
        ('Partial Pick Up', 'Partial Pick Up'),
        ('Shipped', 'Shipped')
    ]
    status = models.CharField(max_length=20, choices=STATUSES, default='In progress')
    shipped_to_location = models.CharField(max_length=100, blank=True)
    remarks = models.CharField(max_length=200, blank=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['release'], name='task_uniques')
        ]

    def __str__(self):
        return str(self.release.project.project_number) + ' - ' + str(self.release.release_title)
