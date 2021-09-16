
import json
import pywhatkit
import requests

lista_de_numeros = ['+5544998465693', '+5511...']
 
msg = "Olá, essa é uma msg enviada pelo PyWhatKit!!!"
 
for numero in lista_de_numeros:
    pywhatkit.sendwhatmsg(numero, msg, 16,24)