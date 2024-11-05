# Proyecto de Detección de ADN Mutante

Este proyecto es una API REST para analizar secuencias de ADN y detectar mutantes. La aplicación permite a los usuarios enviar secuencias de ADN y obtener resultados sobre si la secuencia corresponde a un mutante o a un humano, además de proporcionar estadísticas sobre el número de secuencias analizadas.

## Requisitos

- Python 3.10 o superior
- Flask
- SQLAlchemy

## Pasos para ejecutar el programa


### Paso 1
Instala las dependencias requeridas ejecutando el siguiente comando en la terminal: pip install -r requirements.txt
### Paso 2
Inicia el programa ejecutando el archivo principal con el siguiente comando: python app.py
### Paso 3
Abrir postman y abrir el archivo que se encuentra en la carpeta collection
### Paso 4
En Postman, selecciona el request POST para enviar una secuencia de ADN y verifica si es mutante. Ingresa una secuencia de dna en el cuerpo de la solicitud y envíala.
### Paso 5
Para obtener estadísticas, selecciona el request GET en Postman para ver el número de mutantes y no mutantes registrados en la base de datos.


Postman se ejecutara en esta URL: http://127.0.0.1:5000/

## Como esta dockreizado y hosteado con render solo hace falta abrir postman y poner las siguientes url:
### Para realizar POST  
https://parcialds-wsbn.onrender.com/mutant
### Para realizar GET  
https://parcialds-wsbn.onrender.com/stats
