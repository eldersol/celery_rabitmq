from celery import Celery
from django.shortcuts import render
from django.http import HttpRequest
from .forms import Formulario
from .models import Registro

# Create your views here.
class Registrar(HttpRequest):
    def inicio(request):
        form = Formulario()
        return render(request, "registro.html", {"form": form})

    def guardar(request):
        try:
            form = Formulario(request.POST)
            if form.is_valid():
                tasks = []
                app = Celery(
                    'postman',
                    broker='amqp://user:bitnami@rabbitmq',
                )

                tasks.append(app.send_task('addTask', (str(request.POST['correo']), str(request.POST['usuario']))))

                form.save()

            return render(request, "registro.html", {"form": form, "mensaje": "ok"})
        except Exception as e:
            print(e)

    def listar(request):
        form = Registro.objects.all()
        return render(request, "lista.html", {"form": form})
