# Generated by Django 3.2.6 on 2021-11-28 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='request',
            name='relevance',
        ),
        migrations.AddField(
            model_name='request',
            name='base_url',
            field=models.CharField(default='https://www.amazon.com.br/gp/bestsellers/books/ref=zg_bs_nav_0', max_length=200, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
