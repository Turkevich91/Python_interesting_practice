from django.db import models
from django.contrib.auth.models import User, Group
# from django.db.models import Q
# from django.utils import timezone


class Project(models.Model):
    project_number = models.PositiveIntegerField('Project number')
    project_title = models.CharField('Project name', max_length=200, blank=True)
    project_path = models.CharField('File Path', max_length=200, blank=True)
    # todo: restrict choice to User(Group='PM').
    project_manager = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
    purchase_order = models.ForeignKey('inventory.PurchaseOrder', default=None, null=True, blank=True, on_delete=models.SET_NULL)   #thanks for solution https://t.me/pydjango@eva_kuator
    address = models.CharField('Address', max_length=254, null=True, blank=True)
    mail_address = models.CharField("Mail address", max_length=254, null=True, blank=True)

    # limit_choices_to=
    # User.objects.select_related('Group').get(id=25),
    # {'username': User.groups.aggregate('PM')
    #     'username': ['BJohn', 'TGilstrap', 'SOrrell', 'THarwell', 'TMesser', 'MKunz', 'JJohns', 'MJacobson', 'SHadley',
    #                  'CWhitehorne', 'TKuhn', 'GVEspinell', 'CTucker', 'ELizardi', 'CJaunsen', 'LBonilla', 'JMatheus',
    #                  'FMcCormick', 'JHulsey']
    #     User.objects.filter(groups__name='PM') #  works in general but not with limit_choices_to: returns Qset
    #     # User.objects.filter(username='JHulsey') # works also for singular instance
    # },
    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        constraints = [
            models.UniqueConstraint(fields=['project_number'], name='project_number')
        ]

    modified = models.DateTimeField(auto_now=True)

    # project_manager = models.ForeignKey(User, limit_choices_to={'Group'})
    # https://stackoverflow.com/questions/2245895/is-there-a-simple-way-to-get-group-names-of-a-user-in-django
    # User.objects.get(groups__name='PM')
    def __str__(self):
        return str(self.project_number)

    # def was_published_recently(self):
    #     return self.creation_date >= (timezone.now() - datetime.timedelta(days=14))


class Release(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    release_title = models.CharField('Release name', max_length=10)
    release_folder = models.CharField('Folder', max_length=200,
                                      default=r"D:\Users\Public\Downloads\01ProjectEmptyFiles",
                                      blank=True)
    release_material = models.ManyToManyField('inventory.Material',  through="ReleaseMaterial")
    # todo finish above first
    # release_material = models.ForeignKey(Material, blank=None, null=True, on_delete=models.DO_NOTHING)
    # punch_nest = models.CharField('Nest_dict', max_length=1000)
    modified = models.DateTimeField(auto_now=True)

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
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    material = models.ForeignKey('inventory.Material', on_delete=models.CASCADE)
    material_quantity = models.PositiveIntegerField('quantity')

    class Meta:
        verbose_name = 'Release material'

    def __str__(self):
        return f'{self.release} - [{self.material}] - ({self.material_quantity} pcs)'


class Panel(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    panel_title = models.CharField('Panel title', max_length=10)
    panel_quantity = models.PositiveIntegerField('Quantity', blank=True, default=1)
    modified = models.DateTimeField(auto_now=True)



    # todo сообразить куда вставить этот блок, скорее всего надо будет создать дополнительную таблицу где будем логировать
    # кто, когда и на каком этапе сделал панель, в случае нестов программа должна обрабатывать каждую панель отдельно, ведь
    # каждая панель может быть спродуктирована разными людьми с разного материала и в разное время
    """
    punching_operator = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
    punch_datetime = models.DateTimeField(default=None, null=True)
    bending_operator = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
    bend_datetime = models.DateTimeField(default=None, null=True)
    fabricator = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
    fabricated = models.DateTimeField(default=None, null=True)
    """

    def __str__(self):
        return f'{self.release}-{self.panel_title}'

    class Meta:
        verbose_name = 'panel'
        verbose_name_plural = 'panels'
        constraints = [
            models.UniqueConstraint(fields=['release', 'panel_title'], name='unique panels')
        ]


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

