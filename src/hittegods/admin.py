from typing import List, Sequence, Text, Tuple
from django.contrib import admin
from django.http import HttpRequest

from django.db.models.query import QuerySet

from rangefilter.filters import DateTimeRangeFilter

from hittegods.forms import HittegodsForm

# Register your models here.
from .models import Funnet, Kategori, Mistet, Type, Hittegods, Oppdatering


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
        'gruppe',
        'type__type_navn',
    ]
    common_list_filter: List[Text] = [
        'type',
        'kategori',
    ]
    list_filter: List[Text] = common_list_filter + [
        ('mistet_tidspunkt', DateTimeRangeFilter),
        ('funnet_tidspunkt', DateTimeRangeFilter),
    ]

    def get_form(self, request, *args, **kwargs):
        form = super().get_form(request, *args, **kwargs)
        # form.base_fields['navn'].initial = "JMS"
        # form.base_fields['utlevert_av'].initial = "Kari"
        return form

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


admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Oppdatering, OppdateringAdmin)
admin.site.register(Hittegods, HittegodsAdmin)
admin.site.register(Mistet, MistetAdmin)
admin.site.register(Funnet, FunnetAdmin)
