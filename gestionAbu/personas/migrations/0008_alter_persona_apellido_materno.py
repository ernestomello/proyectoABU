# Generated by Django 5.1.2 on 2025-02-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0007_alter_persona_correo_electronico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Segundo Apellido'),
        ),
    ]
