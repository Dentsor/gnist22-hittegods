# Generated by Django 4.0.5 on 2022-06-28 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hittegods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gjenfunnet',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Hittegods - Gjenfunnet',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('hittegods.hittegods',),
        ),
        migrations.CreateModel(
            name='Utlevert',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Hittegods - Utlevert',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('hittegods.hittegods',),
        ),
        migrations.AddField(
            model_name='hittegods',
            name='oppdatert_tidspunkt',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]