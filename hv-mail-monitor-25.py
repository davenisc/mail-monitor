#!/usr/bin/python3

import os
import time
import datetime
import csv
import commands
import requests
import smtplib
from colorama import Fore
#from decouple import config

def check_port(hostname):
    test_port = os.system("nmap -p 25 " + hostname + " > log_port.txt")
    filter_state = os.system("grep open log_port.txt > state_port.txt")
    state_result = os.system("awk '{print $2}' state_port.txt > state.txt")
    state = commands.getoutput("cat state.txt")

    if state == "open":
        print(Fore.WHITE+"---------->")
        check_port = "[OK]"
        print(Fore.WHITE+"Puerto "+Fore.GREEN+"25 " +Fore.WHITE+"esta abierto")
    else:
        print(Fore.WHITE+"---------->")
        check_port = "[Error]"
        print(Fore.WHITE+"Puerto "+Fore.RED+"25 " +Fore.WHITE+"esta cerrado o filtrado")

        # ------------------ envio de alerta por Telegram ----------------------
        requests.post('https://api.telegram.org/botXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/sendMessage',
                    data={'chat_id': '-XXXXXXXXXXXX', 'text': 'Atencion! puerto de correo 25 cerrado o filtrado!'})

        # ------------------ envio de alerta por correo ------------------------
        send_mail_alert = os.system("python mail-25.py")



    return check_port


#def sonido_alerta():
    #os.system("play -q ent_communicator1.mp3")

# Lee los datos del archivo y los guarda en una variable.
archivo_servidores = open('servidores.csv')
servidores_reader = csv.reader(archivo_servidores)
datos_servidores = list(servidores_reader)


contador = 0

while True:
    for i in range(len(datos_servidores)):
        servidorTexto = datos_servidores[i][0]
        servidorIP = datos_servidores[i][1]
        resultado = check_port(datos_servidores[i][1])

        if resultado == "[Error]":
            print("{0:30} {1:17} {2:7}".format(
                Fore.WHITE + servidorTexto, servidorIP, Fore.RED + resultado))
            print(Fore.WHITE + "")
            #sonido_alerta()
        else:
            print("{0:30} {1:17} {2:7}".format(
                Fore.WHITE + servidorTexto, servidorIP, Fore.GREEN + resultado))
            print(Fore.WHITE + "")

    contador += 1
    print(Fore.YELLOW)
    print('{0} {1:%H:%M:%S} {2}'.format(contador, datetime.datetime.now(),
                                    "________________________________________"))

    # Pausa de 10 minutos.
    time.sleep(60)


    # https://github.com/eternnoir/pyTelegramBotAPI
