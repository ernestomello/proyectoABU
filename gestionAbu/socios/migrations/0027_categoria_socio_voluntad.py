# Generated by Django 3.2.15 on 2022-09-22 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0026_alter_cuota_importe'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria_socio',
            name='voluntad',
            field=models.BooleanField(default=True, verbose_name='Aporta a Voluntad'),
            preserve_default=False,
        ),
    ]
