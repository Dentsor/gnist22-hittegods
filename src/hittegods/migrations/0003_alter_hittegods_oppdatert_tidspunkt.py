# Generated by Django 4.0.5 on 2022-06-28 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hittegods', '0002_gjenfunnet_utlevert_hittegods_oppdatert_tidspunkt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hittegods',
            name='oppdatert_tidspunkt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]