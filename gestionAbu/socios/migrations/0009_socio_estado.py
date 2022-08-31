# Generated by Django 3.2.15 on 2022-08-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0008_auto_20220829_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='estado',
            field=models.CharField(choices=[('A', 'ALTA'), ('B', 'BAJA'), ('R', 'REAFILIADO')], default='A', max_length=1),
        ),
    ]