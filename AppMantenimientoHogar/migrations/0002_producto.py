# Generated by Django 4.2 on 2024-02-12 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppMantenimientoHogar", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "marca",
                    models.IntegerField(
                        choices=[
                            [0, "Samsung"],
                            [1, "Apple"],
                            [2, "Huawei"],
                            [3, "Xiaomi"],
                        ]
                    ),
                ),
                (
                    "op_venta",
                    models.IntegerField(
                        choices=[
                            [0, "Tablet"],
                            [1, "Smartphone"],
                            [2, "SmartTv"],
                            [3, "SmartWatch"],
                        ]
                    ),
                ),
                (
                    "op_minorista_mayorista",
                    models.IntegerField(choices=[[0, "Minorista"], [1, "Mayorista"]]),
                ),
                ("descripcion", models.TextField()),
            ],
        ),
    ]
