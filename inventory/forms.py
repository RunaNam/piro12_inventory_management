from django import forms
from .models import Item, Client


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'photo', 'desc', 'price', 'amount',)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'tel', 'address',)



