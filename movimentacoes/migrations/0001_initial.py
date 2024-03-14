# Generated by Django 5.0.2 on 2024-03-13 23:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0009_alter_categorias_tipo_transacao'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('tipo', models.IntegerField(choices=[(1, 'Receita'), (2, 'Despesa')])),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField()),
                ('carteira', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movimentacao_carteira', to='usuarios.carteira', verbose_name='Carteira')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movimentacao_categoria', to='usuarios.categorias', verbose_name='Categoria')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movimentacao_usuario', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Movimentações',
                'verbose_name_plural': 'Movimentações',
                'ordering': ('usuario', 'carteira', 'categoria', 'tipo'),
            },
        ),
    ]
