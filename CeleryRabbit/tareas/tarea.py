from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_emails_users():
	asunto = 'Mensaje de prueba'
	mensaje = 'Mensaje de prueba CELERY, RABBITMQ'
	send_mail(asunto, mensaje, 'elderusac2022@gmail.com', ['eldertojins@gmail.com'], fail_silently=False)
	return "enviando..."