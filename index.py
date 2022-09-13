
# --------------------------
# Login
# --------------------------


print('Bienvenido a su cajero automático, complete el registro para continuar:')
nombreUsuarioRegistro = input('Ingrese nombre de usuario para registro :')
claveUsuarioRegistro = int(input('Ingrese clave numérica de usuario para registro :'))
lista = []
nombreUsuario = input('Ingrese nombre de usuario :')
claveUsuario = int(input('Ingrese clave de usuario :'))
while nombreUsuario != nombreUsuarioRegistro or claveUsuario != claveUsuarioRegistro:
    print('Las credenciales no coinciden !')
    nombreUsuario = input('Ingrese nombre de usuario :')
    claveUsuario = input('Ingrese clave de usuario :')

usuariosRegistrados = {
    nombreUsuario: claveUsuario,

}
# --------------------------
# Fin Login
# --------------------------

def registro():
    lista.append(usuariosRegistrados)
    print('Registrado !')
    print(lista)
registro()


saldo = 100000
saldoActual = ''
lista = []
nombre = 'Nombre de usuario'
clave = 'Clave'


def extraccion():
    print('Saldo actual :' + str(saldo))
    importeExtraccion = int(input('Cuanto dinero desea extraer ? '))
    saldoEnCuenta = saldo-importeExtraccion
    print('Procesando extraccion...')
    print('Extraído :' + str(importeExtraccion))
    saldoActual = saldoEnCuenta
    return print(('Saldo restante ' + str(saldoActual)))

# ---------------------------------------


def transferencia():
    listaContactos = [{
        'Nombre': 'Martin',
        'Apelido': 'Garcia',
        'Dni': 32456982,
        'CBU': 463103230093
    },
        {
        'Nombre': 'Juan',
        'Apellido': 'Morales',
        'Dni': 324893538,
        'CBU': 580238702501
    }]
    for item in listaContactos:
        print('Contacto : ' + str(item))
        
    lista=listaContactos[0]
    listando=list(lista.keys())
    dato=lista.get(listando[3])
    lista2=listaContactos[1]
    listando2=list(lista2.keys())
    dato2=lista2.get(listando2[3])
    contador = 2
    numeroTransferencia = int(
        (input('Ingrese el número de CBU de destino : ')))
    if numeroTransferencia == dato or numeroTransferencia==dato2:
        importeAEnviar = int(input('Cuanto dinero desea enviar : '))
        print('Enviado ' + str(importeAEnviar))
        saldoEnCuenta = saldo-importeAEnviar
        print('Saldo en cuenta : '+str(saldoEnCuenta))
    elif numeroTransferencia != dato or numeroTransferencia != dato2:
        while numeroTransferencia != dato or numeroTransferencia != dato2:
            print('Numero de CBU incorrecto, tiene ' +
                  str(contador)+' posibilidades mas')
            contador -= 1
            numeroTransferencia = int(
                (input('Ingrese el número de CBU de destino : ')))
            if contador == 0:
                print('Numero de CBU incorrecto')
                break


def consultaSaldo():
    print()


# ------------------------------------
def crearCuenta():
    registroUsuario = input('Ingrese nombre de usuario: ')
    registroClave = input('Ingrese clave de 4 digitos: ')
    longitudClave = len(registroClave)
    if longitudClave == 4:
        usuario = {
            nombre: registroUsuario,
            clave: registroClave,
            'CBU':745290826194,
        }
        lista.append(usuario)
        print('Registrado : ' + str(lista))

    elif longitudClave != 4:
        while longitudClave != 4:
            registroClave = (input('Ingrese clave de 4 digitos: '))
            longitudClave = len(registroClave)
            if longitudClave == 4:
                usuario = {
                    nombre: registroUsuario,
                    clave: registroClave
                }
                lista.append(usuario)
                print(lista)

# ------------------------------------

def consultaCbu():
    print('CBU : ' + str(745290826194))


def menuOperaciones():
    opciones = int(input(
        'Que operaciones desea realizar: \n 1: Extracción. \n 2: Transferencia. \n 3: Consulta de saldo. \n 4: Crear cuenta. \n 5: Consulta de CBU. \n 6: Salir.\n '))
    while opciones != 6:
        if opciones == 1:
            extraccion()
            opciones = int(input(
                'Que operaciones desea realizar: \n 1: Extracción. \n 2: Transferencia. \n 3: Consulta de saldo. \n 4: Crear cuenta. \n 5: Consulta de CBU. \n 6: Salir. \n '))
        elif opciones == 2:
            transferencia()
            opciones = int(input(
                'Que operaciones desea realizar: \n 1: Extracción. \n 2: Transferencia. \n 3: Consulta de saldo. \n 4: Crear cuenta. \n 5: Consulta de CBU. \n 6: Salir. \n '))
        elif opciones == 3:
            print('viendo')
            opciones = int(input(
                'Que operaciones desea realizar: \n 1: Extracción. \n 2: Transferencia. \n 3: Consulta de saldo. \n 4: Crear cuenta. \n 5: Consulta de CBU. \n 6: Salir. \n '))
        elif opciones == 4:
            crearCuenta()
            opciones = int(input(
                'Que operaciones desea realizar: \n 1: Extracción. \n 2: Transferencia. \n 3: Consulta de saldo. \n 4: Crear cuenta. \n 5: Consulta de CBU. \n 6: Salir. \n '))
        elif opciones == 5:
            consultaCbu()
            opciones = int(input(
                'Que operaciones desea realizar: \n 1: Extracción. \n 2: Transferencia. \n 3: Consulta de saldo. \n 4: Crear cuenta. \n 5: Consulta de CBU. \n 6: Salir. \n '))


menuOperaciones()
print('Fin del programa')
