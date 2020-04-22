#SISTEMA RUDIMENTARIO DE AUTENTICACION

import platform
import os
import getpass
import re

def limpiar():

    if platform.system() == 'Windows':
        os.system ('cls')
    else:
        os.system ('clear')

userlist = {}

def menu():
    print ("Menú Principal\n⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺\n")
    print ("1) Crear nuevo usuario y contraseña")
    print ("2) Autentificar")
    print ("3) Salir\n")

def crearusuario():
    print ("Creando nuevo usuario: \n⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺")
    usuario = input("Usuario: ")
    password = getpass.getpass("Contraseña: ")
    userlist[usuario] = password
    limpiar()

def validacion():
    print ("Autentificando\n⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺")
    vuser = input("Usuario: ")
    vpass = getpass.getpass("Contraseña: ")

    rep = 0
    for key, value in userlist.items():
        if key == vuser:
            if value == vpass:
                print("\nAutentificacion exitosa!!!....")
            else:
                print("\nContraseña invalida, intente nuevamente...")
        else:
            rep += 1
            if rep == len(userlist):
                print("\nUsuario invalido!!! ")
    input("\nPresione enter para continuar. ")
    limpiar()

if __name__ == "__main__":

    while True:
        limpiar()
        menu()

        try:
            opc = int(input("Ingrese opcion: "))
        except:
            opc = 4

        if opc <= 3 and opc > 0:
            if opc == 1:
                limpiar()
                crearusuario()

            elif opc == 2 and len(userlist) != 0:
                limpiar()
                validacion()

            elif opc == 3:
                break
            
            else:
                input("\nNo existen usuarios. Presione enter para continuar")
                limpiar()