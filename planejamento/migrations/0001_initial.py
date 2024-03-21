# Generated by Django 5.0.2 on 2024-03-21 11:50

import planejamento.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                    "valor",
                    planejamento.models.CampoMonetario(
                        decimal_places=2, max_digits=10, verbose_name="Valor Planejado"
                    ),
                ),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categoria",
                "ordering": ("salario", "categoria"),
            },
        ),
        migrations.CreateModel(
            name="Salario",
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
                    "salario",
                    planejamento.models.CampoMonetario(
                        decimal_places=2, max_digits=10, verbose_name="Salário"
                    ),
                ),
                (
                    "economia",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=5,
                        verbose_name="Porcentagem da Economia",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Inativo"), (1, "Ativo")], default=1
                    ),
                ),
            ],
            options={
                "verbose_name": "Salario",
                "verbose_name_plural": "Salario",
                "ordering": ("usuario",),
            },
        ),
    ]
