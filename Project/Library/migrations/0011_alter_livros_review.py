# Generated by Django 3.2.6 on 2021-11-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0010_auto_20211128_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='review',
            field=models.IntegerField(help_text='Entre a nota - 0 a 5 (Para não lidos, entre 0)', verbose_name='Review'),
        ),
    ]