import Funciones_examen as fn
import time
import os

os.system('cls')
print("Bienveidos a Cretivos.cl, esta aplicación esta hecha para comprar entradas para el concierto de Michael Jam")
time.sleep(5)

opc = fn.mostrar_menu()

if opc == 1:
    fn.comprar_entrada()
elif opc == 2:
    fn.mostrar_escenario()
elif opc == 3:
    print(fn.lista_ruts)
elif opc == 4:
    fn.mostrar_ganancias()
else:
    fn.salir()