from mailjet_rest import Client
from celery import Celery

app = Celery(
    'postman',
    broker='pyamqp://user:bitnami@rabbitmq',
    backend='rpc://user:bitnami@rabbitmq',
)

@app.task(name='addTask')
def add(mail, usuario):
	api_key = '85a3c2eb23558d84a4f125d5a24fd281'
	api_secret = '860eefad125b9911973e2b5fb902c987'
	mailjet = Client(auth=(api_key, api_secret), version='v3.1')
	data = {
		'Messages': [
			{
				"From": {
					"Email": "eldertojins@gmail.com",
					"Name": "PruebaCeleryRabbit"
				},
				"To": [
					{
						"Email": mail,
						"Name": "Prueba email Celery & Rabbit"
					}
				],
				"Subject": "Probando Celery & Rabbit",
				"TextPart": "My first Mailjet email",
				"HTMLPart": "<h3>Dear "+ usuario + ", welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />Correo de prueba :)",
				"CustomID": "AppGettingStartedTest"
			}
		]
	}
	result = mailjet.send.create(data=data)
	print(result.status_code)
	print(result.json())
	return None
