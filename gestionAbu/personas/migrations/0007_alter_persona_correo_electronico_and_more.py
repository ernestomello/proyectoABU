# Generated by Django 5.1.2 on 2025-02-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0006_alter_departamento_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='correo_electronico',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
