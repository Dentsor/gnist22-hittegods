from django.db import models
from django.db.models import TextField, CharField, ForeignKey, DateTimeField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

class Kategori(models.Model):
    id = models.AutoField(primary_key=True)
    kategori_navn = CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.id} - {self.kategori_navn}"

class Utfodring(models.Model):
    id = models.AutoField(primary_key=True)
    navn = CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return f"{self.id} - {self.navn}"

class Hittegods(models.Model):
    lopenummer = models.AutoField(primary_key=True)
    kategori = ForeignKey(Kategori, null=False, on_delete=models.CASCADE)
    tilleggsinfo = TextField(unique=False, null=False, blank=False)
    mistet_tidspunkt = DateTimeField()
    mistet_sted = CharField(max_length=255, null=False, blank=False)
    funnet_tidspunkt = DateTimeField()
    funnet_sted = CharField(max_length=255, null=False, blank=False)
    registreringstidspunkt = DateTimeField(default=timezone.now)
    mobilnummer = PhoneNumberField(region="NO")
    navn = CharField(max_length=255, null=False, blank=False)
    gruppe = CharField(max_length=255, null=False, blank=True)
    plassering = CharField(max_length=255, null=True, blank=True)
    utfodring = ForeignKey(Utfodring, null=False, on_delete=models.CASCADE)
    utlevert_til = CharField(max_length=255, null=False, blank=True)
    utlevert_av = CharField(max_length=255, null=False, blank=True)
    utlevert_tidspunkt = DateTimeField(null=False, blank=True)

    def __str__(self):
        return f"{self.lopenummer} - {self.tilleggsinfo}"

class Oppdatering(models.Model):
    id = models.AutoField(primary_key=True)
    hittegods = ForeignKey(Hittegods, null=False, on_delete=models.CASCADE)
    registreringsTidspunkt = DateTimeField(default=timezone.now)
    beskrivelse = TextField(unique=False, null=False, blank=False)

    def __str__(self):
        return f"{self.id} - {self.hittegods} : {self.beskrivelse}"
