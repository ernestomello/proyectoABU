# Generated by Django 3.2.15 on 2023-03-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0029_alter_socio_numero_socio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='numero_socio',
            field=models.IntegerField(),
        ),
    ]
