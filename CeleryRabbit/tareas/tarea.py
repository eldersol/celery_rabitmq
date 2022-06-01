from django.core.mail import send_mail
from celery import shared_task


@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def send_emails_users(mail=None):
	asunto = 'Mensaje de prueba'
	mensaje = 'Mensaje de prueba CELERY, RABBITMQ'
	send_mail(asunto, mensaje, 'elderusac2022@gmail.com', [mail], fail_silently=False)
	return "enviando..."
