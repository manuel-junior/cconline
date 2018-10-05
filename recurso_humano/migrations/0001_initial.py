# Generated by Django 2.1.1 on 2018-10-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoHumano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.CharField(max_length=2, verbose_name='Activo')),
                ('nif', models.PositiveIntegerField(null=True, verbose_name='NIF')),
                ('co', models.CharField(max_length=20, verbose_name='CO')),
                ('id_funcionario', models.IntegerField(default=0, verbose_name='Nº')),
                ('nome_completo', models.CharField(max_length=60, verbose_name='Nome completo')),
                ('nome', models.CharField(max_length=60, null=True, verbose_name='Nome')),
                ('obs', models.CharField(max_length=50, verbose_name='OBS')),
            ],
        ),
    ]
