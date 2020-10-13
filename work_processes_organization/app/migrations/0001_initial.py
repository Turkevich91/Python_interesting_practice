# Generated by Django 3.1.1 on 2020-09-17 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200, verbose_name='Project name')),
                ('project_number', models.IntegerField(verbose_name='Project number')),
                ('project_path', models.CharField(max_length=200, verbose_name='Folder')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('project_manager', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_title', models.CharField(max_length=10, verbose_name='Release name')),
                ('release_folder', models.CharField(blank=True, default='D:\\Users\\Public\\Downloads\\01ProjectEmptyFiles', max_length=200, verbose_name='Folder')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
            ],
            options={
                'verbose_name': 'release',
                'verbose_name_plural': 'releases',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loose_items', models.BooleanField(default=False)),
                ('outsource_paint', models.BooleanField(default=False)),
                ('zee_hats_angels', models.IntegerField(blank=True, null=True)),
                ('flashing', models.IntegerField(blank=True, null=True)),
                ('coping', models.IntegerField(blank=True, null=True)),
                ('splice_plate', models.IntegerField(blank=True, null=True)),
                ('blade_screen', models.IntegerField(blank=True, null=True)),
                ('perf', models.IntegerField(blank=True, null=True)),
                ('plate_panels', models.IntegerField(blank=True, null=True)),
                ('frames', models.IntegerField(blank=True, null=True)),
                ('strapping', models.IntegerField(blank=True, null=True)),
                ('clips', models.IntegerField(blank=True, null=True)),
                ('misc', models.IntegerField(blank=True, null=True)),
                ('est_mh', models.IntegerField(blank=True, null=True)),
                ('rel_date', models.DateField(auto_now_add=True)),
                ('requested_ship_date', models.DateField(blank=True)),
                ('shipped_date', models.DateField(blank=True)),
                ('status', models.CharField(choices=[('In progress', 'In progress'), ('Delayed', 'Delayed'), ('Producing', 'Producing'), ('Ready for Pick Up', 'Ready for Pick Up'), ('Partial Pick Up', 'Partial Pick Up'), ('Shipped', 'Shipped')], default='In progress', max_length=20)),
                ('shipped_to_location', models.CharField(blank=True, max_length=100)),
                ('remarks', models.CharField(blank=True, max_length=200)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.release')),
            ],
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_title', models.CharField(max_length=10, verbose_name='Panel name')),
                ('panel_quantity', models.PositiveIntegerField(blank=True, default=1, verbose_name='Quantity')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.release')),
            ],
            options={
                'verbose_name': 'panel',
                'verbose_name_plural': 'panels',
            },
        ),
        migrations.AddConstraint(
            model_name='release',
            constraint=models.UniqueConstraint(fields=('release_title', 'project'), name='unique pro release_view'),
        ),
        migrations.AddConstraint(
            model_name='panel',
            constraint=models.UniqueConstraint(fields=('release', 'panel_title'), name='unique panel_info'),
        ),
    ]
