# Generated by Django 3.2.15 on 2022-09-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_persona_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfilcargo',
            options={'verbose_name': 'Perfil del Cargo', 'verbose_name_plural': 'Perfiles del Cargo'},
        ),
        migrations.AlterField(
            model_name='formacion',
            name='fecha_revalida',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Revalida'),
        ),
        migrations.AlterField(
            model_name='lugartrabajo',
            name='fecha_egreso',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Egreso'),
        ),
        migrations.AlterField(
            model_name='lugartrabajo',
            name='perfil_cargo',
            field=models.ManyToManyField(to='personas.PerfilCargo', verbose_name='Perfiles del Cargo'),
        ),
    ]