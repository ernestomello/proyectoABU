# Generated by Django 3.2.15 on 2022-09-07 01:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0014_auto_20220906_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='departamento',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='socios.departamento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acta',
            name='contenido',
            field=ckeditor.fields.RichTextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='socio',
            name='categoria_socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='socios.categoria_socio', verbose_name='Categoria Socio'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='id_persona',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='socios.persona'),
        ),
    ]