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
