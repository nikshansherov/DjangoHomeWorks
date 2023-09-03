from  django import forms


class ClientForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=12)
    address = forms.CharField(max_length=15)


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField()
