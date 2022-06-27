from weakref import proxy
from django.db import models
from django.db.models import TextField, CharField, ForeignKey, DateTimeField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Kategori(models.Model):
    id = models.AutoField(primary_key=True)
    kategori_navn = CharField(
        max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return self.kategori_navn

    class Meta:
        verbose_name_plural = "Kategorier"


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type_navn = CharField(max_length=128, null=False, blank=False, unique=True)

    def __str__(self):
        return self.type_navn

    class Meta:
        verbose_name_plural = "Typer"


class Hittegods(models.Model):
    lopenummer = models.AutoField(primary_key=True)
    kategori = ForeignKey(Kategori, null=False, on_delete=models.CASCADE)
    tilleggsinfo = TextField(unique=False, null=False, blank=True)
    mistet_tidspunkt = DateTimeField(null=True, blank=True)
    mistet_sted = CharField(max_length=255, null=False, blank=True)
    funnet_tidspunkt = DateTimeField(null=True, blank=True)
    funnet_sted = CharField(max_length=255, null=False, blank=True)
    registreringstidspunkt = DateTimeField(default=timezone.now, null=False, blank=False)
    mobilnummer = PhoneNumberField(region="NO")
    navn = CharField(max_length=255, null=False, blank=False)
    gruppe = CharField(max_length=255, null=False, blank=True)
    plassering = CharField(max_length=255, null=False, blank=True)
    type = ForeignKey(Type, null=False, on_delete=models.CASCADE)
    utlevert_til = CharField(max_length=255, null=False, blank=True)
    utlevert_av = CharField(max_length=255, null=False, blank=True)
    utlevert_tidspunkt = DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.lopenummer} : {self.tilleggsinfo[:64]}{'...' if len(self.tilleggsinfo) > 64 else ''}"

    class Meta:
        verbose_name_plural = "Hittegods"


class Mistet(Hittegods):
    class Meta:
        proxy = True
        verbose_name_plural = "Hittegods - Mistet"


class Funnet(Hittegods):
    class Meta:
        proxy = True
        verbose_name_plural = "Hittegods - Funnet"


class Oppdatering(models.Model):
    id = models.AutoField(primary_key=True)
    hittegods = ForeignKey(Hittegods, null=False, on_delete=models.CASCADE)
    registreringstidspunkt = DateTimeField(default=timezone.now, null=False)
    beskrivelse = TextField(unique=False, null=False, blank=False)

    def __str__(self):
        return f"{self.hittegods.lopenummer}.{self.id}: {self.beskrivelse[:32]}"

    class Meta:
        verbose_name_plural = "Oppdateringer"
