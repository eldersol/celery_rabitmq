from django.shortcuts import render
from django.http import HttpRequest
from .forms import Formulario
from .models import Registro
from .tarea import send_emails_users, add


# Create your views here.
class Registrar(HttpRequest):
    def inicio(request):
        form = Formulario()
        return render(request, "registro.html", {"form": form})

    def guardar(request):
        try:
            form = Formulario(request.POST)
            if form.is_valid():
                add.delay(2, 2)
                #send_emails_users.delay(str(request.POST['correo']))
                send_emails_users(str(request.POST['correo']))
                form.save()
            return render(request, "registro.html", {"form": form, "mensaje": "ok"})
        except Exception as e:
            print(e)

    def listar(request):
        form = Registro.objects.all()
        return render(request, "lista.html", {"form": form})
