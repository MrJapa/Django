from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    pass

class NewRestaurantForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = NewRestaurant
        fields = ['name', 'address', 'description', 'opening_time', 'closing_time', 'delivery_fee', 'minimum_order', 'FoodType']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_image(self.cleaned_data['image'])
        if commit:
            instance.save()
        return instance
    
class NewCategoryForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = NewCategory
        fields = ['name']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_image(self.cleaned_data['image'])
        if commit:
            instance.save()
        return instance