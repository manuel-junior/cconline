# Generated by Django 2.1.1 on 2018-09-21 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0002_auto_20180921_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]