
from django import forms

from hittegods.models import Hittegods


class HittegodsForm(forms.ModelForm):
    class Meta:
        model = Hittegods
        fields = (
            'type',
            'kategori',
            'tilleggsinfo',
            'navn',
            'mobilnummer',
            'gruppe',
            'plassering',
            'mistet_tidspunkt',
            'mistet_sted',
            'funnet_tidspunkt',
            'funnet_sted',
            'utlevert_til',
            'utlevert_av',
            'utlevert_tidspunkt'
        )
