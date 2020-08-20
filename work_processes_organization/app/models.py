from django.db import models
from django.utils import timezone


class Project(models.Model):
    project_title = models.CharField('Project name', max_length=200)
    project_number = models.IntegerField('Project number')
    project_path = models.CharField('Folder', max_length=200)

    # creation_date = models.DateTimeField('Creation date')

    def __str__(self):
        return self.project_title

    # def was_published_recently(self):
    #     return self.creation_date >= (timezone.now() - datetime.timedelta(days=14))


class Release(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    release_title = models.CharField('Release name', max_length=10)
    release_folder = models.CharField('Folder', max_length=200,
                                      default=r"D:\Users\Public\Downloads\01ProjectEmptyFiles",
                                      blank=True)

    class Meta:
        verbose_name = 'release'
        verbose_name_plural = 'releases'
        constraints = [
            models.UniqueConstraint(fields=['release_title', 'project'], name='unique pro releases'),
            # models.CheckConstraint(check=())
        ]

    def __str__(self):
        return str(f'{self.project.project_number} - {self.release_title}')


class Panel(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    panel_title = models.CharField('Panel name', max_length=10)
    panel_quantity = models.PositiveIntegerField('Quantity', blank=True, default=1)

    def __str__(self):
        return self.panel_title

    class Meta:
        verbose_name = 'panel'
        verbose_name_plural = 'panels'
        constraints = [
            models.UniqueConstraint(fields=['release', 'panel_title'], name='unique panels')
        ]


class Staff(models.Model):
    first_name = models.CharField('first_name', max_length=50)
    last_name = models.CharField('last_name', max_length=50)
    email = models.EmailField(blank=True)
    STAFF_TITLES = [
        ('PM', 'Project manager'),
        ('Pr', 'Production'),
        ('MP', 'Machine operator'),
        ('TW', 'Table worker'),
        ('Ud', 'Undefined'),
    ]
    title = models.CharField(max_length=20, choices=STAFF_TITLES)

    def __str__(self):
        return self.first_name[0] + '. ' + self.last_name


class Task(models.Model):
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    project_manager = models.ForeignKey(Staff, on_delete=models.CASCADE, limit_choices_to={'title': 'PM'})
    loose_items = models.BooleanField(default=False)
    outsource_paint = models.BooleanField(default=False)
    # parts_drawings = models.IntegerField(max_length=4)
    """This is just counter of quantity of dwg inside the folder.
    we dont need to have this field in fact"""
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
    requested_ship_date = models.DateField(blank=True)
    shipped_date = models.DateField(blank=True)
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

    def __str__(self):
        return str(self.release.project.project_number) + ' - ' + str(self.release.release_title)

    # @staticmethod
    # def get_heads():
    #     pass
