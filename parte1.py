dic_user = {
    'nombre': 'veronica leaño',
    'clave': ' '
}

print("Ingrese la clave:")
clave_user = input()
for i in range(len(clave_user)):
    dic_user['clave'] += '*'

print("\n",dic_user['clave'])

if len(clave_user) == 4:
    print("\n+++++++++++++++++++++++Bienvenido/a", dic_user['nombre'],"+++++++++++++++++++++++\n")
if len(clave_user) > 4:
    print("❌ Error: La longitud de clave ingresada supera los 4 digitos!\n")
if len(clave_user) <  4: 
    print("❌ Error: La longitud de la clave ingresada es inferior a 4 digitos!\n")

