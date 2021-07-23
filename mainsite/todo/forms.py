from django import forms


class CategoryForm(forms.Form):
    content=forms.CharField(max_length=200)
    
