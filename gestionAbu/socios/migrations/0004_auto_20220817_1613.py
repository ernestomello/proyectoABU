# Generated by Django 3.2.15 on 2022-08-17 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0003_cuota'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='cuota',
            name='fecha_generada',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='PagoCuota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=200)),
                ('id_cuota', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='socios.cuota')),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='socios.metodopago')),
            ],
        ),
    ]
