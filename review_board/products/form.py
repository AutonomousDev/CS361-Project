from django import forms


class ProductForm(forms.Form):
    name = forms.CharField()
    brand = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

