from django import forms
from .models import Stocks

class StockForm(forms.ModelForm):
    class Meta:
        model=Stocks
        fields=['name','description','price']

# class BusinessForm(forms.ModelForm):
#     class meta:
#         models=Businesses
#         fields=['name','location','description']

# class PromotionForm(forms.ModelForm):
#     class Meta:
#         model=Promotions
#         fields=['title','description','start_date','end_date']
