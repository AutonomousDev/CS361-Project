from django import forms


class ProductForm(forms.Form):
    name = forms.CharField()
    brand = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    product_image = forms.ImageField()


class ReviewForm(forms.Form):
    title = forms.CharField()
    comment = forms.Textarea()