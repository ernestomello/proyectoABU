# Generated by Django 3.2.15 on 2022-08-12 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
                ('importe_cuota', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=45)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido_paterno', models.CharField(max_length=45)),
                ('apellido_materno', models.CharField(max_length=45)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id_socio', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de Ingreso')),
                ('fecha_baja', models.DateField(verbose_name='Fecha de Baja')),
                ('fecha_reingreso', models.DateField(verbose_name='Fecha de Reingreso')),
                ('frecuencia_pago', models.CharField(choices=[('ME', 'MENSUAL'), ('SE', 'SEMESTRAL'), ('AN', 'ANUAL')], default='ME', max_length=2)),
                ('categoria_socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socios.categoria_socio', verbose_name='Categoria Socio')),
                ('id_persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='socios.persona')),
            ],
        ),
    ]