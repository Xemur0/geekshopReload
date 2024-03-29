from django import forms

from mainapp.models import Product
from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderItemsForm(forms.ModelForm):

    price = forms.CharField(label='Цена',required=False)

    class Meta:
        model = OrderItem
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(OrderItemsForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all().select_related()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'