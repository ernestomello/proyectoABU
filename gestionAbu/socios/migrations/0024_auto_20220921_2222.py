# Generated by Django 3.2.15 on 2022-09-22 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0023_auto_20220920_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actadescriptor',
            name='acta',
        ),
        migrations.RemoveField(
            model_name='actadescriptor',
            name='descriptor',
        ),
        migrations.RemoveField(
            model_name='actasocio',
            name='id_acta',
        ),
        migrations.RemoveField(
            model_name='actasocio',
            name='id_socio',
        ),
        migrations.RemoveField(
            model_name='movimientocaja',
            name='user',
        ),
        migrations.RemoveField(
            model_name='pagocuota',
            name='id_cuota',
        ),
        migrations.RemoveField(
            model_name='pagocuota',
            name='metodo_pago',
        ),
        migrations.AddField(
            model_name='socio',
            name='importe_cuota_jubilado',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='socio',
            name='estado',
            field=models.CharField(choices=[('A', 'ALTA'), ('B', 'BAJA')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='socio',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Baja'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='fecha_reingreso',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Reingreso'),
        ),
        migrations.DeleteModel(
            name='Acta',
        ),
        migrations.DeleteModel(
            name='ActaDescriptor',
        ),
        migrations.DeleteModel(
            name='ActaSocio',
        ),
        migrations.DeleteModel(
            name='Descriptor',
        ),
        migrations.DeleteModel(
            name='MovimientoCaja',
        ),
        migrations.DeleteModel(
            name='PagoCuota',
        ),
    ]
