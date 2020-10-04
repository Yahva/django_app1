from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

def index(request):
    header = "Calculator" 
    
    if request.method == "POST":
        userform = UserForm(request.POST) #заполняем форму пришедшими данными
        if userform.is_valid():
            a = request.POST.get("a")
            b = request.POST.get("b")     # получение значения поля age
            sum = float(a)+float(b)
            data = {"header": header, "form": userform, "sum": sum}  
        else:
            return HttpResponse("Invalid data")
    else:  
        userform = UserForm()
        data = {"header": header, "form": userform}

    return render(request, "index.html", context=data)
 
def about(request):
    return HttpResponse("<h2>О сайте</h2>")
 
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def products(request, productid):
    output = "<h2>Product № {0}</h2>".format(productid)
    return HttpResponse(output)
 
def users(request, id, name):
    output = "<h2>User</h2><h3>Id: {0}  Name: {1}</h3>".format(id, name)
    return HttpResponse(output)