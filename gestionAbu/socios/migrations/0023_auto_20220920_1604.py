# Generated by Django 3.2.15 on 2022-09-20 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
        ('socios', '0022_auto_20220915_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formacion',
            name='id_persona',
        ),
        migrations.RemoveField(
            model_name='formacion',
            name='tipo_formacion',
        ),
        migrations.RemoveField(
            model_name='lugartrabajo',
            name='id_persona',
        ),
        migrations.RemoveField(
            model_name='lugartrabajo',
            name='perfil_cargo',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='departamento',
        ),
        migrations.AlterField(
            model_name='socio',
            name='fecha_baja',
            field=models.DateField(blank=True, default=None, verbose_name='Fecha de Baja'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='fecha_reingreso',
            field=models.DateField(blank=True, default=None, verbose_name='Fecha de Reingreso'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='id_persona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='personas.persona', verbose_name='Nombre'),
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.DeleteModel(
            name='Formacion',
        ),
        migrations.DeleteModel(
            name='LugarTrabajo',
        ),
        migrations.DeleteModel(
            name='PerfilCargo',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.DeleteModel(
            name='TipoFormacion',
        ),
    ]