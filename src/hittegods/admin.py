from django.contrib import admin

# Register your models here.
from .models import Kategori, Utfodring, Hittegods, Oppdatering

admin.site.register(Kategori)
admin.site.register(Utfodring)
admin.site.register(Hittegods)
admin.site.register(Oppdatering)
