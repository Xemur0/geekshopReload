from django import forms
from mainapp.models import ProductCategory, Product
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'image')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'


class UserAdminProfileForm(UserProfileForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'is_active')

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control'
            elif field_name == 'is_active':
                field.widget.attrs['class'] = 'form'
            else:
                field.widget.attrs['class'] = 'form-control py-4'


class CategoryAdminRegisterForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите имя категории'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class CategoryAdminProfileForm(forms.ModelForm):

    discount = forms.IntegerField(widget=forms.NumberInput(), label='скидка', required=False, min_value=0, max_value=90,
                                  initial=0)


    class Meta:
        model = ProductCategory
        fields = ('name', 'description', 'is_active', 'discount')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите имя категории'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание'
        for field_name, field in self.fields.items():
            if field_name == 'is_active':
                field.widget.attrs['class'] = 'form'
            else:
                field.widget.attrs['class'] = 'form-control py-4'


class ProductAdminRegisterForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    category = forms.ModelChoiceField(widget=forms.Select(), queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category', 'is_active')

    def __init__(self, *args, **kwargs):
        super(ProductAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['select'] = ProductCategory.objects.all()
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'custom-file-input'
            elif field_name == 'category':
                field.widget.attrs['class'] = 'custom-select'
            elif field_name == 'is_active':
                field.widget.attrs['class'] = 'form-check-inline'
            else:
                field.widget.attrs['class'] = 'form-control py-4'


class ProductAdminUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    category = forms.ModelChoiceField(widget=forms.Select(), queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category', 'is_active')

    def __init__(self, *args, **kwargs):
        super(ProductAdminUpdateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'custom-file-input'
            elif field_name == 'category':
                field.widget.attrs['class'] = 'custom-select'
            elif field_name == 'is_active':
                field.widget.attrs['class'] = 'form-check-inline'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
