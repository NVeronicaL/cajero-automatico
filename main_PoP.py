import json
from tarjeta import Tarjeta

with open('data/usuarios.json') as f:
    lista_users = json.load(f)

with open('data/tarjetas.json') as f:
    lista_cards = json.load(f)

with open('data/opciones.json') as f:
    lista_opciones = json.load(f)

# for usuario in lista_users['usuarios']:
#     print(type(usuario))
# print(type(lista_users['usuarios']))

for card in lista_cards['tarjetas']:
    print(card)

respuesta = 'SI'

"""
    Creacion de tarjetas con los datos del archivo tarjetas.json
"""

lista_objects_cards = []
for tarjeta in lista_cards['tarjetas']:
    new_tarjeta = Tarjeta.create_tarjeta(tarjeta['id_tarjeta'] , tarjeta['nombre'], tarjeta['apellido'],
                                        tarjeta['dni'], tarjeta['cbu'], tarjeta['saldo'], tarjeta['clave'])
    lista_objects_cards.append(new_tarjeta)
# print( 'objetos: ', lista_objects_cards)


while True:
    print("Ingrese la clave")
    clave_user = input()
    if Tarjeta.existe_clave(lista_objects_cards, clave_user):
        e = Tarjeta.encriptar(clave_user)
        print("Encriptado", e)
        Tarjeta.mensaje(lista_objects_cards, clave_user)
        cbu_origen = Tarjeta.obtener_cbu(lista_objects_cards, clave_user)
        break
    else:
        print("\n❌ Error 🙁, contraseña no  válida")

while (lista_opciones['opciones'] != [] and respuesta == 'SI' and Tarjeta.existe_clave(lista_objects_cards, clave_user)):
    #print("respuesta", respuesta)
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t\t MENU DE OPCIONES")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")

    for op in lista_opciones['opciones']:
        print("|------>", op['opcion'], "-", op['nombre'])

    op_elegida = int(input("\nIngresa una opcion: "))

    for op in lista_opciones['opciones']:
        if op['opcion'] == op_elegida:
            print("\n********************* " + op['nombre'] + " *********************")
            break

    match op_elegida: 
        case 0:
            while True:
                cbu_detination = input("Ingrese un CBU destino: ")
                cbu_origen = Tarjeta.obtener_cbu(lista_objects_cards, clave_user)
                # print(cbu_origen)
                #print("cbu_origen", cbu_origen)
                existe_cbu_destination = Tarjeta.existe_cbu(lista_objects_cards, cbu_detination)
                existe_cbu_origen = Tarjeta.existe_cbu(lista_objects_cards, cbu_origen)

                if existe_cbu_destination and existe_cbu_origen and cbu_detination != cbu_origen:
                    monto = input("Ingresa un monto 💲: ")
                    if monto.isnumeric():
                        Tarjeta.incrementar_saldo(Tarjeta.lista_objects_cards, cbu_detination, int(monto))
                        Tarjeta.decrementar_saldo(Tarjeta.lista_objects_cards, cbu_origen, int(monto))
                        print("\n✅ Felicidades la operación de",op['nombre'], "a terceros se realizo con Exito!😀")
                        print("\nDesea realizar otra operación? SI o NO")
                        respuesta = input().upper()
                        break
                    else:
                        print("Por favor ingrese solo numeros")
                        print("\nDesea realizar otra operación? SI o NO")
                        respuesta = input().upper()
                        break
                elif existe_cbu_destination and existe_cbu_origen and  cbu_detination == cbu_origen:
                    monto = input("Ingresa un monto 💲: ")
                    if monto.isnumeric():
                        Tarjeta.autodeposito(Tarjeta, lista_objects_cards, cbu_origen, int(monto))
                        print("\n✅ Felicidades la operación de",op['nombre'], "a su cuenta se realizo con Exito!😀")
                        print("\nDesea realizar otra operación? SI o NO")
                        respuesta = input().upper()
                        break 
                    else:
                        print("Por favor ingrese solo numeros")
                        print("\nDesea realizar otra operación? SI o NO")
                        respuesta = input().upper()
                        break
                    
                else:
                    print("\n❌ Error 🙁, porfavor ingrese  un CBU válido")
        case 1:
            monto = int(input("Ingresa un monto 💲: "))
            saldo_origen = int(Tarjeta.obtener_saldo(lista_objects_cards, cbu_origen))
            cbu_origen = Tarjeta.obtener_cbu(lista_objects_cards, clave_user)
            if monto <= saldo_origen:
                Tarjeta.decrementar_saldo(Tarjeta, lista_objects_cards, cbu_origen, int(monto))
                print("\n✅ Felicidades la operación de", op['nombre'], "se realizo con Exito!😀")
                print("\nDesea realizar otra operación? SI o NO")
                respuesta = input().upper()
            else:
                print("Usted no posee saldo suficiente para realizar la operación")
                print("\nDesea realizar otra operación? SI o NO")
                respuesta = input().upper()
        case 2:
            while True:
                cbu_detination = input("Ingrese un CBU destino: ")
                if Tarjeta.existe_cbu(lista_objects_cards, cbu_detination) :
                    monto = input("Ingresa un monto 💲: ")
                    Tarjeta.incrementar_saldo(Tarjeta, lista_objects_cards, cbu_detination, int(monto))
                    Tarjeta.decrementar_saldo(Tarjeta, lista_objects_cards, cbu_origen, int(monto))

                    print("\n✅ Felicidades la operación de", op_elegida, "se realizo con Exito!😀")
                    print("\nDesea realaizar otra operación? SI o NO")
                    respuesta = input().upper()
                    break
                else:
                    print("\n❌ Error 🙁, porfavor ingrese  un CBU válido")

                    cbu_detination = input("Ingrese un CBU destino: ")           
        case 3 :
            cbu_origen = Tarjeta.obtener_cbu(lista_objects_cards, clave_user)
            print("caso 3: ", cbu_origen)
            saldo_origen = Tarjeta.obtener_saldo(lista_objects_cards, cbu_origen)
            print(saldo_origen)
            print("\nDesea realaizar otra operación? SI o NO")
            respuesta = input().upper()
        case 4: 
            print("\nEl CBU es:", Tarjeta.obtener_cbu(lista_objects_cards, clave_user))
            print("\nDesea realaizar otra operación? SI o NO")
            respuesta = input().upper()
        case 5:
            print("GRACIAS POR ELEGIRNOS")
            respuesta = 'NO'
        case _:
            print("\n❌ Error 🙁, porfavor ingrese una opcion válida, del Menu de opciones")