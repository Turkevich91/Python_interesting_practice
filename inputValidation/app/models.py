from django.db import models

# Create your models here.
from django.utils import timezone
import datetime


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
    # release_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    release_title = models.CharField('Release name', max_length=10)
    release_folder = models.CharField('Folder', max_length=200,
                                      default=r"D:\Users\Public\Downloads\01ProjectEmptyFiles",
                                      blank=True)

    def __str__(self):
        return self.release_title


class Panel(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    panel_title = models.CharField('Panel name', max_length=10)
    panel_quantity = models.IntegerField('Quantity', blank=True, default=1)

    def __str__(self):
        return self.panel_title

    class Meta:
        verbose_name = 'Panel'
        verbose_name_plural = 'Panels'


class Staff(models.Model):
    first_name = models.CharField('first_name', max_length=50)
    last_name = models.CharField('last_name', max_length=50)
    STAFF_TITLES = [
        ('PM', 'Project manager'),
        ('Pr', 'Production'),
        ('MP', 'Machine operator'),
        ('TW', 'Table worker'),
        ('Ud', 'Undefined'),
    ]
    title = models.Choices(STAFF_TITLES)


class Task(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    project_manager = models.ForeignKey(Staff.title('PM'),  on_delete=models.CASCADE)
    loose_items = models.BooleanField(default=False)
    outsource_paint = models.CharField(max_length=10, choices=[('NO', 'NO'), ('YES', 'YES')])
    # parts_drawings = models.IntegerField(max_length=4)
    """This is just counter of quantity of dwg inside the folder.
    we dont need to have this field in fact"""
    zee_hats_angels = models.IntegerField(max_length=7, blank=True)
    flashing = models.IntegerField(max_length=7, blank=True)
    coping = models.IntegerField(max_length=7, blank=True)
    splice_plate = models.IntegerField(max_length=7, blank=True)
    blade_screen = models.IntegerField(max_length=7, blank=True)
    perf = models.IntegerField(max_length=7, blank=True)
    plate_panels = models.IntegerField(max_length=7, blank=True)
    frames = models.IntegerField(max_length=7, blank=True)
    strapping = models.IntegerField(max_length=7, blank=True)
    clips = models.IntegerField(max_length=7, blank=True)
    misc = models.IntegerField(max_length=7, blank=True)
    est_mh = models.IntegerField(max_length=7, blank=True)
    rel_date = models.DateField(max_length=7, blank=True)
