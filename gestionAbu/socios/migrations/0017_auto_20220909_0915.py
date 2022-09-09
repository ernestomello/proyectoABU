# Generated by Django 3.2.15 on 2022-09-09 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0016_alter_persona_departamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoFromacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='persona',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='socios.departamento'),
        ),
        migrations.CreateModel(
            name='LugarTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_ingreso', models.DateField()),
                ('fecha_egreso', models.DateField()),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='socios.persona')),
                ('perfil_cargo', models.ManyToManyField(to='socios.PerfilCargo')),
            ],
        ),
        migrations.CreateModel(
            name='Formacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_titulo', models.DateField(verbose_name='Fecha del Titulo')),
                ('institucion', models.CharField(max_length=100)),
                ('duracion', models.CharField(max_length=50)),
                ('plan', models.CharField(max_length=100)),
                ('fecha_revalida', models.DateField()),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='socios.persona')),
                ('tipo_formacion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='socios.tipofromacion')),
            ],
        ),
    ]
