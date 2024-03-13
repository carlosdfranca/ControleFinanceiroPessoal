# Generated by Django 5.0.2 on 2024-03-13 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_categorias_tipo_transacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='tipo_transacao',
            field=models.IntegerField(choices=[(1, 'Receita'), (2, 'Despesa')], default=1),
        ),
    ]
