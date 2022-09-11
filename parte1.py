dic_user = {
    'user': 'veronica leaño',
    'clave': ' '
}

print("Ingrese la clave: ")
clave_user = int(input())
for i in range(len(clave_user)):
    dic_user['clave'] += '*'

print(dic_user)
