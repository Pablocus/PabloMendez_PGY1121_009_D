import numpy as np
import os
import time

precio_platinum = 120000
precio_gold = 80000
precio_silver = 50000

cont_platinum = 0
cont_gold = 0
cont_silver = 0

escenario = np.zeros((10,10), int)
lista_ruts = []

def mostrar_escenario():
    os.system('cls')
    for x in range(10):
        print(f"FILA {x+1}: ", end=" ")
        for y in range(10):
            print(escenario[x][y], end=" ")
        print()
    print("COLUMNA: 1 2 3 4 5 6 7 8 9 10")

def mostrar_menu():
    os.system('cls')
    print("""Menu de opciones:
    1. Comprar entradas
    2. Ubicaciones disponibles
    3. Listado de asistentes
    4. Ganacias totales
    5. Salir""")
    opc = validar_opcion()
    return opc

def validar_opcion():
    while True:
        try:
            opc = int(input("¿Que desea hacer?: "))
            if opc :
                return opc
            else:
                print("ERROR! DEBE SER UN NUMERO ENTRE 1 Y 5")
        except:
            print("ERROR! DEBE SER UN NUMERO ENTERO")

def validar_rut():
    while True:
        try:
            rut = int(input("Indique su rut, sin punto verificador ni coma: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! DEBE SER UN RUT ENTRE 1000000 Y 99999999")
        except:
            print("ERROR! DEBE SER NUMEROS ENTEROS")

def salir():
    print("""    Gracias por usar la aplicación
    Creada por Pablo Mendez el 6 de Julio de 2023""")

def comprar_entrada():
    os.system('cls')
    if 0 not in escenario:
        print("NO HAY ASIENTOS DISPONIBLES!")
        return mostrar_menu()
    rut = validar_rut()
    cant = validar_cant_ent()
    for cant in range(cant):
        mostrar_escenario()
        mostrar_precios()
        while True:
            fila = validar_fila()
            columna = validar_columna()
            if escenario[fila-1][columna-1] == 0:
                escenario[fila-1][columna-1] = 1
            else:
                print("ERROR! ASIENTO OCUPADO")
                return
    lista_ruts.append(rut)
    print("REGISTRO EXITOSO")     
    

def validar_cant_ent():
    while True:
        try:
            cant = int(input("¿Cuantas entradas desea comprar? (min 1, max 3): "))
            if cant in(1,2,3):
                return cant
            else:
                print("ERROR! DEBE SER ENTRE 1 A 3 ENTRADAS")
        except:
            print("ERROR! DEBE SER UN NUMERO ENTERO")

def validar_fila():
    while True:
        try:
            fila = int(input("Eliga la fila que desea ocupar: "))
            if fila <= 10 and fila >= 1:
                return fila
            else:
                print("ERROR! DEBE SER UN NUMERO ENTRE 1 Y 10")
        except:
            print("ERROR! DEBE SER UN NUMERO ENTERO")

def validar_columna():
    while True:
        try:
            columna = int(input("Eliga la columna que desea ocupar: "))
            if columna <= 10 and columna >= 1:
                return columna
            else:
                print("ERROR! DEBE SER UN NUMERO ENTRE 1 Y 10")
        except:
            print("ERROR! DEBE SER UN NUMERO ENTERO")

def mostrar_precios():
    print(f"""
    Precios:
    - Fila 1 a 2 'Platinum': ${precio_platinum}
    - Fila 3 a 5 'Gold': ${precio_gold}
    - Fila 6 a 10 'Silver': ${precio_silver}""")

def mostrar_ganancias():
    total_platinum = precio_platinum * cont_platinum
    total_gold = precio_gold * cont_gold
    total_silver = precio_silver * cont_silver
    total_cont = cont_platinum + cont_gold + cont_silver
    total_ganacias = total_platinum + total_gold + total_silver
    print(f"""
    TIPO DE ENTRADA                       CANTIDAD         TOTAL
    Entrada Platinum: ${precio_platinum}             {cont_platinum}                {total_platinum}
    Entrada Gold:     ${precio_gold}              {cont_gold}                {total_gold}
    Entrada Silver:   ${precio_silver}              {cont_silver}                {total_silver}
    TOTAL:                                {total_cont}                {total_ganacias}""")
    time.sleep(20)
    return mostrar_menu()  



