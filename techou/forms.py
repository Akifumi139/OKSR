from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['purchase_date', 'medicine_name', 'pharmacy_name']
        labels = {'purchase_date': '購入日',
                  'medicine_name': '薬の名前',
                  'pharmacy_name': '薬局名',}
