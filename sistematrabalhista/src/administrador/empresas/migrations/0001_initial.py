# Generated by Django 3.1.5 on 2022-04-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='foto/empresa', verbose_name='Foto')),
                ('logo', models.ImageField(upload_to='logo/empresa', verbose_name='Logo')),
                ('razao_social', models.CharField(max_length=45, verbose_name='Razão social')),
                ('cnpj', models.CharField(max_length=18, unique=True, verbose_name='CNPJ')),
                ('nome_contato', models.CharField(max_length=45, verbose_name='Nome do contato')),
                ('telefone', models.CharField(max_length=14, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=45, unique=True, verbose_name='E-mail')),
                ('senha_hash', models.CharField(max_length=64, verbose_name='Hash senha')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('numero', models.CharField(max_length=5, verbose_name='Número')),
                ('acessibilidade', models.CharField(blank=True, max_length=6, verbose_name='Acessibilidade')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'db_table': 'empresa',
                'ordering': ['razao_social'],
            },
        ),
    ]
