# Generated by Django 3.2.15 on 2022-09-20 20:50

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socios', '0028_auto_20220920_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('asunto', models.CharField(default='', max_length=50)),
                ('contenido', ckeditor.fields.RichTextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Descriptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palabra_clave', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Descriptores',
            },
        ),
        migrations.CreateModel(
            name='ActaSocio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_acta', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='actas.acta')),
                ('id_socio', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='socios.socio')),
            ],
            options={
                'verbose_name_plural': 'Socios en Acta',
            },
        ),
        migrations.CreateModel(
            name='ActaDescriptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acta', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='actas.acta')),
                ('descriptor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='actas.descriptor')),
            ],
            options={
                'verbose_name_plural': 'Descriptores en Acta',
            },
        ),
    ]
