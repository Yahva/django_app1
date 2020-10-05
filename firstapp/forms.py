from django import forms
 
class UserForm(forms.Form):
    surname = forms.CharField(label="Фамилия",max_length=20)
    name = forms.CharField(label="Имя",max_length=20)
    patronymic = forms.CharField(label="Отчество",max_length=20)
    age = forms.IntegerField(label="Возраст")