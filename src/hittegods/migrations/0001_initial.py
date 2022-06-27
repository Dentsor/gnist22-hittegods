# Generated by Django 4.0.5 on 2022-06-27 20:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hittegods',
            fields=[
                ('lopenummer', models.AutoField(primary_key=True, serialize=False)),
                ('tilleggsinfo', models.TextField(blank=True)),
                ('mistet_tidspunkt', models.DateTimeField(blank=True, null=True)),
                ('mistet_sted', models.CharField(blank=True, max_length=255)),
                ('funnet_tidspunkt', models.DateTimeField(blank=True, null=True)),
                ('funnet_sted', models.CharField(blank=True, max_length=255)),
                ('registreringstidspunkt', models.DateTimeField(default=django.utils.timezone.now)),
                ('mobilnummer', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='NO')),
                ('navn', models.CharField(max_length=255)),
                ('gruppe', models.CharField(blank=True, max_length=255)),
                ('plassering', models.CharField(blank=True, max_length=255)),
                ('utlevert_til', models.CharField(blank=True, max_length=255)),
                ('utlevert_av', models.CharField(blank=True, max_length=255)),
                ('utlevert_tidspunkt', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Hittegods',
            },
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('kategori_navn', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Kategorier',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_navn', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Typer',
            },
        ),
        migrations.CreateModel(
            name='Oppdatering',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('registreringstidspunkt', models.DateTimeField(default=django.utils.timezone.now)),
                ('beskrivelse', models.TextField()),
                ('hittegods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hittegods.hittegods')),
            ],
            options={
                'verbose_name_plural': 'Oppdateringer',
            },
        ),
        migrations.AddField(
            model_name='hittegods',
            name='kategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hittegods.kategori'),
        ),
        migrations.AddField(
            model_name='hittegods',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hittegods.type'),
        ),
        migrations.CreateModel(
            name='Funnet',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Hittegods - Funnet',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('hittegods.hittegods',),
        ),
        migrations.CreateModel(
            name='Mistet',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Hittegods - Mistet',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('hittegods.hittegods',),
        ),
    ]
