# Generated by Django 3.1.1 on 2020-09-23 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20200921_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_amount', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Pallet',
                'verbose_name_plural': 'Pallets',
            },
        ),
        migrations.CreateModel(
            name='PalletPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=30, verbose_name='Pallet place')),
                ('place_descriptions', models.CharField(blank=True, max_length=100, verbose_name='Place descriptions')),
            ],
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['material_type', 'material_size', 'material_thickness', 'color'], 'verbose_name': 'MATERIAL', 'verbose_name_plural': 'MATERIALS'},
        ),
        migrations.DeleteModel(
            name='MaterialAmount',
        ),
        migrations.AddField(
            model_name='pallet',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.material'),
        ),
        migrations.AddField(
            model_name='pallet',
            name='pallet_place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.palletplace'),
        ),
        migrations.AddField(
            model_name='pallet',
            name='purchase_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.purchaseorder'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='material',
            field=models.ManyToManyField(related_name='pos', through='inventory.Pallet', to='inventory.Material'),
        ),
    ]
