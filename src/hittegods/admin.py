from datetime import datetime
from time import timezone
from typing import Any, List, Sequence, Text, Tuple
from django.contrib import admin
from django.http import HttpRequest

from django.db.models.query import QuerySet

from rangefilter.filters import DateTimeRangeFilter

from hittegods.forms import HittegodsForm

# Register your models here.
from .models import Funnet, Gjenfunnet, Kategori, Mistet, NyligOppdatert, Type, Hittegods, Oppdatering, Utlevert


class KategoriAdmin(admin.ModelAdmin):
    search_fields: Sequence[str] = [
        'kategori_navn',
    ]

class TypeAdmin(admin.ModelAdmin):
    search_fields: Sequence[str] = [
        'type_navn',
    ]

class OppdateringAdmin(admin.ModelAdmin):
    search_fields: Sequence[str] = [
        'hittegods__lopenummer',
        'id',
        'beskrivelse',
    ]

class OppdateringInline(admin.StackedInline):
    model = Oppdatering


class HittegodsAdmin(admin.ModelAdmin):
    inlines = [OppdateringInline]
    form = HittegodsForm
    readonly_fields: Sequence[str] = [
        'lopenummer',
        'registreringstidspunkt',
        'oppdatert_tidspunkt',
    ]
    list_display: Tuple[Text] = (
        'lopenummer',
        'type',
        'kategori',
        'tilleggsinfo',
        'mistet_tidspunkt',
        'mistet_sted',
        'funnet_tidspunkt',
        'funnet_sted',
    )
    search_fields: List[Text] = [
        'lopenummer',
        'kategori__kategori_navn',
        'tilleggsinfo',
        'mistet_sted',
        'funnet_sted',
        'mobilnummer',
        'navn',
        'plassering',
        'gruppe',
        'type__type_navn',
        'oppdatering__beskrivelse',
    ]
    common_list_filter: List[Text] = [
        'type',
        'kategori',
    ]
    list_filter: List[Text] = common_list_filter + [
        ('mistet_tidspunkt', DateTimeRangeFilter),
        ('funnet_tidspunkt', DateTimeRangeFilter),
    ]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Hittegods]:
        return Hittegods.objects.filter(utlevert_tidspunkt=None)


class MistetAdmin(HittegodsAdmin):
    list_display: Tuple[Text] = (
        'lopenummer',
        'type',
        'kategori',
        'tilleggsinfo',
        'mistet_tidspunkt',
        'mistet_sted',
    )
    list_filter: List[Text] = HittegodsAdmin.common_list_filter + [
        ('mistet_tidspunkt', DateTimeRangeFilter),
        'mistet_sted',
    ]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Hittegods]:
        return super().get_queryset(request).exclude(mistet_tidspunkt=None)


class FunnetAdmin(HittegodsAdmin):
    list_display: Tuple[Text] = (
        'lopenummer',
        'type',
        'kategori',
        'tilleggsinfo',
        'funnet_tidspunkt',
        'funnet_sted',
    )
    list_filter: List[Text] = HittegodsAdmin.common_list_filter + [
        ('funnet_tidspunkt', DateTimeRangeFilter),
        'funnet_sted',
    ]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Hittegods]:
        return super().get_queryset(request).exclude(funnet_tidspunkt=None)


class UtlevertAdmin(HittegodsAdmin):
    list_display: Tuple[Text] = (
        'lopenummer',
        'type',
        'kategori',
        'tilleggsinfo',
        'utlevert_av',
        'utlevert_til',
        'utlevert_tidspunkt',
    )
    list_filter: List[Text] = HittegodsAdmin.common_list_filter + [
        ('utlevert_tidspunkt', DateTimeRangeFilter),
        'utlevert_av',
        ('mistet_tidspunkt', DateTimeRangeFilter),
        'mistet_sted',
        ('funnet_tidspunkt', DateTimeRangeFilter),
        'funnet_sted',
    ]
    search_fields: List[Text] = HittegodsAdmin.search_fields + [
        'utlevert_av',
        'utlevert_til',
    ]

    def get_queryset(self, _: HttpRequest) -> QuerySet[Hittegods]:
        return Hittegods.objects.exclude(utlevert_tidspunkt=None)


class GjenfunnetAdmin(HittegodsAdmin):
    list_display: Tuple[Text] = (
        'lopenummer',
        'type',
        'kategori',
        'tilleggsinfo',
        'mistet_tidspunkt',
        'mistet_sted',
        'funnet_tidspunkt',
        'funnet_sted',
    )

    def get_queryset(self, request: HttpRequest) -> QuerySet[Hittegods]:
        return super().get_queryset(request).exclude(mistet_tidspunkt=None).exclude(funnet_tidspunkt=None)


class NyligOppdatertAdmin(HittegodsAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Hittegods]:
        return super().get_queryset(request).order_by('-oppdatert_tidspunkt')


admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Oppdatering, OppdateringAdmin)
admin.site.register(Hittegods, HittegodsAdmin)
admin.site.register(Mistet, MistetAdmin)
admin.site.register(Funnet, FunnetAdmin)
admin.site.register(Utlevert, UtlevertAdmin)
admin.site.register(Gjenfunnet, GjenfunnetAdmin)
admin.site.register(NyligOppdatert, NyligOppdatertAdmin)
