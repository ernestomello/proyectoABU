# Generated by Django 3.2.15 on 2022-09-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0019_movimientocaja'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimientocaja',
            name='motivo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
