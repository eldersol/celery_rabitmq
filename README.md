## Utilización de Celery y Rabbit 


### Celery y Rabbit
Celery es utilizado para la carga de trabajo dividiendolo en cola de tareas específicas que requieren mucho tiempo, en este caso se ha utilizado para el registro de un usuario y el envio de un correo electronico al usuario agregado.

Rabbit habilita la comunicación como un servicio de mensajeria.

### Versiones
    python = 3.6
    Django = 3.2.5
    psycopg2 = 2.9.3
    celery = 5.2.7
    rabbitmq = 3.7
    nginx = 1.20
    postgres = 11.5

### Funcionamiento

1. Ingresar a localhost:8000
2. Crear nuevo registro con el boton Nuevo
3. ingresar nombre de usuario 
4. ingresar contraseña
5. ingresar correo electronico al que se le enviara el correo
6. Guardar 

* El registro ejecutara la tarea asignada como envio de correo y se habra guardado en base de datos.

### Ejecucion:

    Clonar 
        git clone https://github.com/eldersol/celery_rabitmq.git
        cd celery_rabitmq

    Docker

        sudo docker-compose up --build