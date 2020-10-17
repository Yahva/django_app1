from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Patient
from .models import Doctor
from .models import SpecDoctor
from .models import Ticket
from .forms import PatientForm
from .forms import DoctorForm
from .forms import SpecDoctorForm
from .forms import TicketForm


# Главная страница
def homePage(request):
    data = {"step":0,}
    return render(request, "recordPatient.html", context=data)

# шаг1 - Выбор специальности врача
def recordStep1(request):
    specDoctors = SpecDoctor.objects.all()
    data = {"step":1, "specDoctors": specDoctors}
    return render(request, "recordPatient.html", context=data)
 
#  шаг2 - Выбор  врача
def recordStep2(request, specDocID):
        try:
           specDoctor = SpecDoctor.objects.get(id=specDocID)
           doctors = Doctor.objects.filter(specDoctor=specDocID)

           data = {"step":2, "specDoctor": specDoctor.name, "doctors": doctors}
           return render(request, "recordPatient.html", context=data)
        except Doctor.DoesNotExist:
            return HttpResponseNotFound("<h2>Специальность врача не выбрана!</h2>")

#  шаг3 Выбор талона
def recordStep3(request, specDocID, docID):
    try:
        specDoctor = SpecDoctor.objects.get(id=specDocID)
        doctor = Doctor.objects.get(id=docID)
        tickets = Ticket.objects.filter(docID=docID).order_by('time')

        data = {"step":3, "specDoctor": specDoctor.name, "doctor": doctor, "tickets": tickets}
        return render(request, "recordPatient.html", context=data)
    except Doctor.DoesNotExist:
       return HttpResponseNotFound("<h2>Доктор не выбран!</h2>")

#  шаг4 Личные данные пациента
def recordStep4(request, specDocID, docID, ticketID):
    specDoctor = SpecDoctor.objects.get(id=specDocID)
    doctor = Doctor.objects.get(id=docID)
    ticket = Ticket.objects.get(id = ticketID)

    if request.method == "POST":
        newPatient = Patient()
        newPatient.surname = request.POST.get("surname")
        newPatient.name = request.POST.get("name")
        newPatient.patronymic = request.POST.get("patronymic")
        newPatient.age = request.POST.get("age")
        newPatient.sex = request.POST.get("sex")
        newPatient.save()

        ticket.patID = newPatient.id
        ticket.isBusy = True
        ticket.save()

        data = {"step":5, "specDoctor": specDoctor.name, "doctor": doctor, "ticket": ticket, "patient":newPatient}
    else:
        patientForm = PatientForm()
        data = {"step":4, "form": patientForm, "specDoctor": specDoctor.name, "doctor": doctor, "ticket": ticket}

    return render(request, "recordPatient.html", context=data)


#---------------------------------------------------------------------------------------------------------#
def createDoctor(request):
    if request.method == "POST":
        newDoctor = Doctor()
        newDoctor.surname = request.POST.get("surname")
        newDoctor.name = request.POST.get("name")
        newDoctor.patronymic = request.POST.get("patronymic")
        newDoctor.age = request.POST.get("age")
        newDoctor.sex = request.POST.get("sex")
        newDoctor.specDoctor = request.POST.get("specDoctor")
        newDoctor.save()

    doctors = Doctor.objects.all()
    specDoctors = SpecDoctor.objects.all()

    itemsSpecDoctor = list()
    for specDoctor in specDoctors:
        itemsSpecDoctor.append([specDoctor.id,specDoctor.name])

    doctorForm = DoctorForm()
    doctorForm.fields["specDoctor"].choices = itemsSpecDoctor

    data = {"form": doctorForm, "doctors": doctors, "specDoctors": specDoctors}
    return render(request, "createDoctor.html", context=data)

# удаление данных из бд
def deleteDoctor(request, docID):
    doctor = Doctor.objects.get(id=docID)
    doctor.delete()
    return HttpResponseRedirect("/createDoctor")


#---------------------------------------------------------------------------------------------------------#
def createSpecDoctor(request):
    if request.method == "POST":
        newSpecDoctor = SpecDoctor()
        newSpecDoctor.name = request.POST.get("name")
        newSpecDoctor.save()

    specDoctors = SpecDoctor.objects.all()
    data = {"form": SpecDoctorForm(), "specDoctors": specDoctors }
    return render(request, "createSpecDoctor.html", context=data)

# удаление данных из бд
def delSpecDoctor(request, specDocID):
    specDoctor = SpecDoctor.objects.get(id=specDocID)
    specDoctor.delete()
    return HttpResponseRedirect("/createSpecDoctor")

#---------------------------------------------------------------------------------------------------------#
def createTicket(request):
    if request.method == "POST":
        newTicket = Ticket()
        newTicket.time = request.POST.get("time")
        newTicket.docID = request.POST.get("docID")
        newTicket.patID = -1
        newTicket.isBusy = False
        newTicket.save()

    doctors = Doctor.objects.all()
    tickets = Ticket.objects.all().order_by('time')
    ticketForm = TicketForm()

    itemsDoctor = list()
    for doctor in doctors:
        itemsDoctor.append([doctor.id, doctor.surname+" "+doctor.name+" "+doctor.patronymic ])
    ticketForm.fields["docID"].choices = itemsDoctor

    specDoctors = SpecDoctor.objects.all()

    data = {"form": ticketForm, "tickets": tickets, "doctors": doctors, "specDoctors":specDoctors }
    return render(request, "createTicket.html", context=data)

# удаление данных из бд
def delTicket(request, ticketID):
    delTicket = Ticket.objects.get(id=ticketID)
    patient = Patient.objects.filter(id=delTicket.patID)

    delTicket.delete()
    patient.delete()
    return HttpResponseRedirect("/createTicket")

# Кабинет врача---------------------------------------
def doctorAccount(request, docID):
    try:
        doctor = Doctor.objects.get(id=docID)
        tickets = Ticket.objects.filter(docID=docID)
        idPats = list()
        for ticket in tickets:
           idPats.append(ticket.patID)
        patients = Patient.objects.filter(id__in=idPats)

        specDoctors = SpecDoctor.objects.all()
        itemsSpecDoctor = list()
        for specDoctor in specDoctors:
            itemsSpecDoctor.append([specDoctor.id,specDoctor.name])

        doctorForm = DoctorForm()
        doctorForm.fields["surname"].initial = doctor.surname
        doctorForm.fields["name"].initial = doctor.name
        doctorForm.fields["patronymic"].initial = doctor.patronymic
        doctorForm.fields["age"].initial = doctor.age
       # doctorForm.fields["sex"].initial = doctor.sex
        doctorForm.fields["specDoctor"].initial = doctor.specDoctor
        doctorForm.fields["specDoctor"].choices = itemsSpecDoctor

        data = {"form":doctorForm, "doctor": doctor, "patients":patients, "tickets":tickets}
        return render(request, "doctorAccount.html", context=data)
    except Doctor.DoesNotExist:
       return HttpResponseNotFound("<h2>Доктор не выбран!</h2>")

# удаление данных из бд
def takePatient(request, docID, patID):
   try:
       patient = Patient.objects.get(id=patID)
       patient.delete()

       ticket = Ticket.objects.get(patID=patID)
       ticket.patID = -1
       ticket.isBusy = False
       ticket.save()
       return HttpResponseRedirect("/doctorAccount/"+str(docID)+"/")
   except Doctor.DoesNotExist:
       return HttpResponseNotFound("<h2>Пациент не найден!</h2>")