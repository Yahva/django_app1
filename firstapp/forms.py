from django import forms
 
class UserForm(forms.Form):
    a = forms.DecimalField(label="Операнд 1", initial=0)
    b = forms.DecimalField(label="Операнд 2", initial=0)