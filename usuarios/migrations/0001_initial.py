# Generated by Django 5.0.2 on 2024-03-25 13:08

import colorfield.fields
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import stdimage.models
import usuarios.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('bancos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('imagem_perfil', stdimage.models.StdImageField(default='usuarios/default.png', force_min_size=False, upload_to=usuarios.models.get_file_path, variations={'medium': {'crop': True, 'height': 300, 'width': 300}})),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuarios',
                'ordering': ('first_name', 'last_name'),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_inicial', usuarios.models.CampoMonetario(decimal_places=2, max_digits=10, verbose_name='Saldo Inicial')),
                ('descricao', models.CharField(max_length=255)),
                ('cor', colorfield.fields.ColorField(default='#CC99FF', image_field=None, max_length=25, samples=None)),
                ('status', models.IntegerField(choices=[(0, 'Inativo'), (1, 'Ativo')], default=1)),
                ('instituicao', models.ForeignKey(blank=True, limit_choices_to={'categoria': 2}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carteira_instituicao', to='bancos.dadosinstitucionais', verbose_name='Instituição Financeira')),
                ('tipo_conta', models.ForeignKey(blank=True, limit_choices_to={'categoria': 1}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bancos.dadosinstitucionais', verbose_name='Tipo da conta')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carteira_usuario', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Carteiras',
                'verbose_name_plural': 'Carteiras',
                'ordering': ('usuario', 'instituicao', 'tipo_conta'),
            },
        ),
        migrations.CreateModel(
            name='CartaoCredito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('limite', usuarios.models.CampoMonetario(decimal_places=2, max_digits=10, verbose_name='Limite')),
                ('dia_fechamento', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')], verbose_name='Dia do Fechamento')),
                ('dia_vencimento', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')], verbose_name='Dia do Vencimento')),
                ('status', models.IntegerField(choices=[(0, 'Inativo'), (1, 'Ativo')], default=1)),
                ('bandeira', models.ForeignKey(blank=True, limit_choices_to={'categoria': 3}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bancos.dadosinstitucionais', verbose_name='Bandeira do cartão')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cartao_usuario', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('carteira', models.ForeignKey(blank=True, limit_choices_to=usuarios.models.CartaoCredito.escolhas_carteira, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.carteira', verbose_name='Bandeira do cartão')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cor', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None)),
                ('tipo_transacao', models.IntegerField(choices=[(1, 'Receita'), (2, 'Despesa')])),
                ('status', models.IntegerField(choices=[(0, 'Inativo'), (1, 'Ativo')], default=1)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Categorias',
                'verbose_name_plural': 'Categorias',
                'ordering': ('usuario', 'nome'),
            },
        ),
    ]
