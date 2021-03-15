# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()


message = "Hola, \n\nEl puerto 25 presenta fallas, por favor comuniquese con la persona encargada \n\nPor favor no responda este correo, ya que es solo informativo y enviado automaticamente."

# setup the parameters of the message
password = "xxxxxxxxxxxxxxxx"
msg['From'] = "xxxxxxxxxxxxxxx@gmail.com"
msg['To'] = "xxxxxxxxxxx@gmail.com"
msg['Subject'] = "Alerta! falla en puertos de correo"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

#create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)


# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print "Correo de alerta enviado correctamente a %s:" % (msg['To'])
