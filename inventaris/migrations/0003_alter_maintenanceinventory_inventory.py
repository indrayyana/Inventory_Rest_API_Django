# Generated by Django 4.1.5 on 2023-02-01 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventaris', '0002_alter_maintenanceinventory_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenanceinventory',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relasi_inventory', to='inventaris.inventory'),
        ),
    ]
