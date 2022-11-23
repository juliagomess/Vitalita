# Generated by Django 3.1.5 on 2022-04-02 22:03

import curriculos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('associado_id', models.IntegerField(verbose_name='ID do associado')),
                ('instituicao_ensino', models.CharField(blank=True, max_length=255, verbose_name='Instituições de ensino')),
                ('curso_extra', models.CharField(blank=True, max_length=255, verbose_name='Cursos extras')),
                ('empresa_trabalhada', models.CharField(blank=True, max_length=255, verbose_name='Empresas trabalhadas')),
                ('cargo_ocupado', models.CharField(blank=True, max_length=255, verbose_name='Cargos ocupados')),
                ('laudo_medico', models.FileField(blank=True, upload_to=curriculos.models.uploadfolder, verbose_name='Laudo médico')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Curriculo',
                'verbose_name_plural': 'Curriculo',
                'db_table': 'curriculo',
                'ordering': ['associado_id'],
            },
        ),
    ]
