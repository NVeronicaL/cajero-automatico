import json

with open('data/usuarios.json') as f:
    lista_users = json.load(f)

with open('data/tarjetas.json') as f:
    lista_cards = json.load(f)

with open('data/opciones.json') as f:
    lista_opciones = json.load(f)

# for usuario in lista_users['usuarios']:
#     print(usuario)

# for card in lista_cards['tarjetas']:
#     print(card)

respuesta = 'SI'

# fun: obtiene un solo cbu
def obtener_cbu(lista_cards, clave_user):
    cbu_origen = ''
    for card in lista_cards['tarjetas']:
        if card['clave'] == clave_user:
            cbu_origen = card['cbu']
            break
    return cbu_origen

# fun: obtiene todos los cbus
def obtener_cbus(lista_cards):
    lista_cbus = []
    for cbu in lista_cards['tarjetas']:
        lista_cbus.append(cbu)

    print(lista_cbus)
    return lista_cbus
    
#print(obtener_cbus(lista_cards))

# fun: verifica si exite el cbu del usuario.
def existe_cbu(cbu):
    lista_cbus = []
    existe_cbu = False
    for card in lista_cards['tarjetas']:
        lista_cbus.append(card['cbu'])
    #print(lista_cbus)
    for c in lista_cbus: 
        if c == cbu:
            existe_cbu = True
            break
    return existe_cbu

# fun: incrementa el saldo del usuario.
def incrementar_saldo(cbu_detination, saldo):
    for card in lista_cards['tarjetas']:
        #print(card)
        if card['cbu'] == cbu_detination:
            card['saldo'] = str(obtener_saldo(lista_cards, cbu_detination) + saldo)
            print("nuevo saldo del destinacion: ", card['saldo'])
            break

# fun: decrementa el saldo del usuario.
def decrementar_saldo(cbu_origen, saldo):
    for card in lista_cards['tarjetas']:
        #print(card)
        if card['cbu'] == cbu_origen:
            card['saldo'] = str(obtener_saldo(lista_cards, cbu_origen) - saldo)
            print("nuevo saldo del origen: ", card['saldo'])
            break

# fun: obtiene el saldo del usuario
def obtener_saldo(lista_cards, cbu):
    saldo_origen = 0
    for card in lista_cards['tarjetas']:
        if card['cbu'] == cbu:
            saldo_origen = int(card['saldo'])
            break
    return saldo_origen

# fun: verifica si exite la clave del usuario.
def existe_clave(clave_user):
    lista_claves = []
    existe_clave = False
    for card in lista_cards['tarjetas']:
        lista_claves.append(card['clave'])

    for k in lista_claves: 
        if k == clave_user:
            existe_clave = True
            break
    return existe_clave

# fun: Encrripta la clave del usuario.
def encriptar(clave_user):
    clave_encriptada = ' '
    for i in range(len(clave_user)):
        clave_encriptada += '*'
    print(clave_encriptada)
    return clave_encriptada

# fun: mensaje de bienvenida para el usuario.
def mensaje(lista_cards, clave_user):
    for card in lista_cards['tarjetas']:
        if card['clave'] == clave_user:
            print("\n+++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\t\t BIENVENIDO/A\t", card['nombre'], card['apellido'])
            print("+++++++++++++++++++++++++++++++++++++++++++++++++")
            break

while True:
    print("Ingrese la clave")
    clave_user = input()
    if existe_clave(clave_user):
        e = encriptar(clave_user)
        print("Encriptado", e)
        mensaje(lista_cards, clave_user)
        cbu_origen = obtener_cbu(lista_cards, clave_user)
        break
    else:
        print("\n❌ Error 🙁, contraseña no  válida")

while (lista_opciones['opciones'] != [] and respuesta == 'SI' and existe_clave(clave_user)):
    print("respuesta", respuesta)
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
                cbu_origen = obtener_cbu(lista_cards, clave_user)
                # print(cbu_origen)
                print("cbu_origen", cbu_origen)
                if existe_cbu(cbu_detination) and existe_cbu(cbu_origen) :
                    monto = int(input("Ingresa un monto 💲: "))
                    incrementar_saldo(cbu_detination, monto)
                    decrementar_saldo(cbu_origen, monto)
                    print("\n✅ Felicidades la operación de",op['nombre'], "se realizo con Exito!😀")
                    print("\nDesea realaizar otra operación? SI o NO")
                    respuesta = input().upper()
                    break
                else:
                    print("\n❌ Error 🙁, porfavor ingrese  un CBU válido")
        case 1:
            monto = input("Ingresa un monto 💲: ")
            print("\n✅ Felicidades la operación de", op_elegida, "se realizo con Exito!😀")
            print("\nDesea realaizar otra operación? SI o NO")
            respuesta = input().upper()
        case 2:
            while True:
                cbu_detination = input("Ingrese un CBU destino: ")
                if existe_cbu(cbu_detination) :
                    monto = input("Ingresa un monto 💲: ")
                    incrementar_saldo(cbu_detination, monto)
                    decrementar_saldo(cbu_origen, monto)

                    print("\n✅ Felicidades la operación de", op_elegida, "se realizo con Exito!😀")
                    print("\nDesea realaizar otra operación? SI o NO")
                    respuesta = input().upper()
                    break
                else:
                    print("\n❌ Error 🙁, porfavor ingrese  un CBU válido")

                    cbu_detination = input("Ingrese un CBU destino: ")           
        case 3 :
            cbu_origen = obtener_cbu(lista_cards, clave_user)
            print("caso 3: ", cbu_origen)
            saldo_origen = obtener_saldo(lista_cards, cbu_origen)
            print(saldo_origen)
            print("\nDesea realaizar otra operación? SI o NO")
            respuesta = input().upper()
        case 4: 
            print("\nEl CBU es:", obtener_cbu(lista_cards, clave_user))
            print("\nDesea realaizar otra operación? SI o NO")
            respuesta = input().upper()
        case 5:
            print("GRACIAS POR ELEGIRNOS")
            respuesta = 'NO'
        case _:
            print("\n❌ Error 🙁, porfavor ingrese una opcion válida, del Menu de opciones")