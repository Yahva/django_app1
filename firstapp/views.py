from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
from .models import Patient

# получение данных из бд
def index(request):
    patients = Patient.objects.all()
    userForm = UserForm()
    data = {"patients": patients, "form": userForm}
    return render(request, "index.html", context=data)
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        newPatient = Patient()
        newPatient.surname = request.POST.get("surname")
        newPatient.name = request.POST.get("name")
        newPatient.patronymic = request.POST.get("patronymic")
        newPatient.age = request.POST.get("age")
        newPatient.save()
    return HttpResponseRedirect("/")

# изменение данных в бд
def edit(request, id):
    try:
        editPatient = Patient.objects.get(id=id)
 
        if request.method == "POST":
            editPatient.surname = request.POST.get("surname")
            editPatient.name = request.POST.get("name")
            editPatient.patronymic = request.POST.get("patronymic")
            editPatient.age = request.POST.get("age")
            editPatient.save()
            return HttpResponseRedirect("/")
        else:
            userForm = UserForm(initial=
                                {
                                    'surname': editPatient.surname, 
                                    'name': editPatient.name,
                                    'patronymic': editPatient.patronymic,
                                    'age': editPatient.age
                                })
            data = { "form": userForm}
            return render(request, "edit.html", context=data)
    except Patient.DoesNotExist:
        return HttpResponseNotFound("<h2>Пациент не найден!</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        patient = Patient.objects.get(id=id)
        patient.delete()
        return HttpResponseRedirect("/")
    except Patient.DoesNotExist:
        return HttpResponseNotFound("<h2>Пациент не найден!</h2>")