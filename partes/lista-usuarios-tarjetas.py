# Lista de usuarios con cuenta en el banco
lista_usuarios = [
    {
        'nombre': 'VERONICA',
        'apellido': 'LEAÑO',
        'dni': '37245591'
    },
    {
        'nombre': 'BiANCA MADELEN',
        'apellido': 'ALARCON',
        'dni': '68782412'
    },
    {
        'nombre': 'GiULIANA ISABEL',
        'apellido': 'COSTA',
        'dni': '91872507'
    },
    {
        'nombre': 'MARCOS ALEJANDRO',
        'apellido': 'RIOS',        
        'dni': '91872507'
    },
    {
        'nombre': 'FACUNDO MARTIN',
        'apellido': 'GARCIA',
        'dni': '35813799'
    },
    {
        'nombre': 'AGUSTIN',
        'apellido': 'PONCE',
        'dni': '31510392'
    }
]

# Lista de tarjetas asociadas a usuarios
lista_tarjetas = [
        {
        'nombre': 'VERONICA',
        'apellido': 'LEAÑO',
        'dni': '37245591',
        'cbu': '1234567891011121314151',
        'saldo':  '10000',
        'clave': '3781'
    },
    {
        'nombre': 'BiANCA MADELEN',
        'apellido': 'ALARCON',
        'dni': '68782412',
        'cbu': '2345678910111213141516',
        'saldo': '200',
        'clave': '0135'
    },
    {
        'nombre': 'GiULIANA ISABEL',
        'apellido': 'COSTA',
        'dni': '91872507',
        'cbu': '3456789101112131415161',
        'saldo': ' ',
        'clave': '4321'
    },
    {
        'nombre': 'MARCOS ALEJANDRO',
        'apellido': 'RIOS',        
        'dni': '91872507',
        'cbu': '4567891011121314151617',
        'saldo': '500',
        'clave': '3781'
    },
    {
        'nombre': 'FACUNDO MARTIN',
        'apellido': 'GARCIA',
        'dni': '35813799',
        'cbu': '5678910111213141516171',
        'saldo': '1000',
        'clave': '6834'
    },
    {
        'nombre': 'AGUSTIN',
        'apellido': 'PONCE',
        'dni': '31510392',
        'cbu': '6789101112131415161718',
        'saldo': ' ',
        'clave': '4780'
    }
]

for usuario in lista_usuarios:
    print(usuario)
        

for tarjeta in lista_tarjetas:
    print(tarjeta)