# Generated by Django 4.2 on 2024-02-13 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppMantenimientoHogar", "0003_reparacion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contacto",
            name="tipo_consulta",
            field=models.IntegerField(
                choices=[
                    [0, "Consulta"],
                    [1, "Reclamo"],
                    [2, "Sugerencia"],
                    [3, "Venta"],
                    [4, "Felicitaciones"],
                ]
            ),
        ),
    ]