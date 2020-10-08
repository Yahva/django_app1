from django import forms
 
class PatientForm(forms.Form):
    surname = forms.CharField(label="Фамилия",max_length=20)
    name = forms.CharField(label="Имя",max_length=20)
    patronymic = forms.CharField(label="Отчество",max_length=20)
    age = forms.IntegerField(label="Возраст")
    sex = forms.ChoiceField(label="Пол", choices=((1, "Муж."), (2, "Жен.")))

class DoctorForm(forms.Form):
    surname = forms.CharField(label="Фамилия",max_length=20)
    name = forms.CharField(label="Имя",max_length=20)
    patronymic = forms.CharField(label="Отчество",max_length=20)
    age = forms.IntegerField(label="Возраст")
    sex = forms.ChoiceField(label="Пол", choices=((1, "Муж."), (2, "Жен.")))
    specDoctor = forms.ChoiceField(label="Специализация")
        
class SpecDoctorForm(forms.Form):
    name = forms.CharField(label="Название",max_length=50)

class TicketForm(forms.Form):
      time = forms.TimeField(label="Время приёма")
      docID = forms.ChoiceField(label="Врач")
    
    