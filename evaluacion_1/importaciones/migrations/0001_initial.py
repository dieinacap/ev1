# Generated by Django 4.2.6 on 2023-10-16 09:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Importacion",
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
                ("cantidad_unidades", models.PositiveIntegerField()),
                (
                    "costo_unitario_usd",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("nombre_articulo", models.CharField(max_length=100)),
                ("codigo_articulo", models.CharField(max_length=50)),
                ("nombre_proveedor", models.CharField(max_length=100)),
                (
                    "costo_envio_usd",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
    ]
