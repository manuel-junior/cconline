# Generated by Django 2.1.1 on 2018-09-21 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automovel', '0006_auto_20180921_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automovel',
            name='seguro',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Seguro'),
        ),
    ]