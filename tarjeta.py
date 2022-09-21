class Tarjeta():


    def __init__(self, id_tarjeta, nombre, apellido, dni, cbu, saldo, clave):
        self.id_tarjeta = id_tarjeta
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cbu = cbu
        self.saldo = saldo
        self.clave = clave

    def create_tarjeta(id_tarjeta, nombre, apellido, dni, cbu, saldo, clave):
        """
            fun: crea una instancia de objeto, con los atributos : 
            id_tarjeta, nombre, apellido, dni, cbu, saldo, clave
        """
        new_tarjeta = Tarjeta(id_tarjeta, nombre, apellido, dni, cbu, saldo, clave)
        return new_tarjeta


    def existe_clave(lista_objects_cards, clave_user):
        """
            verifica si exite la clave del usuario.
        """
        existe_clave = False
        for card in lista_objects_cards:
            if card.clave == clave_user:
                existe_clave = True
                break
        return existe_clave


    def encriptar(clave_user):
        """
            fun: Encrripta la clave del usuario.
        """
        clave_encriptada = ' '
        for i in range(len(clave_user)):
            clave_encriptada += '*'
        print(clave_encriptada)
        return clave_encriptada


    def mensaje(lista_objects_cards, clave_user):
        """
            fun: mensaje de bienvenida para el usuario.
        """
        for card in lista_objects_cards:
            if card.clave == clave_user:
                print("\n+++++++++++++++++++++++++++++++++++++++++++++++++")
                print("\t\t BIENVENIDO/A\t", card.nombre, card.apellido)
                print("+++++++++++++++++++++++++++++++++++++++++++++++++")
                break


    def obtener_cbu(lista_objects_cards, clave_user):
        """
            fun: obtiene un solo cbu
        """
        cbu_origen = ''
        for card in lista_objects_cards:
            if card.clave == clave_user:
                cbu_origen = card.cbu
                break
        return cbu_origen



    def existe_cbu(lista_objects_cards, cbu):
        """
            fun: verifica si exite el cbu del usuario.
        """
        existe_cbu = False
        for card in lista_objects_cards:
            if card.cbu == cbu:
                existe_cbu = True
                break
        return existe_cbu



    def obtener_saldo(lista_objects_cards, cbu):
        """
            fun: obtiene el saldo del usuario
        """
        saldo_origen = 0
        for card in lista_objects_cards:
            if card.cbu == cbu:
                saldo_origen = card.saldo
                break
        return saldo_origen



    def incrementar_saldo(self, lista_objects_cards, cbu_detination, saldo):
        """
            fun: incrementa el saldo del usuario.
        """
        for card in lista_objects_cards:
            if card.cbu == cbu_detination:
                card.saldo = self.obtener_saldo(lista_objects_cards, cbu_detination) + saldo
                print("nuevo saldo del destinacion: ", card.saldo)
                break


    def decrementar_saldo(self, lista_objects_cards, cbu_origen, saldo):
        """
            fun: decrementa el saldo del usuario.
        """
        for card in lista_objects_cards:
            if card.cbu == cbu_origen:
                card.saldo = self.obtener_saldo(lista_objects_cards, cbu_origen) - saldo
                print("nuevo saldo del origen: ", card.saldo)
                break


    def autodeposito(self, lista_objects_cards, cbu_origen, saldo):
        """
            fun: autodeposito
        """
        for card in lista_objects_cards:
            if card.cbu == cbu_origen:
                card.saldo = self.obtener_saldo(lista_objects_cards, cbu_origen) + saldo
                print("Nuevo saldo en cuenta:💲", card.saldo)
                break   
        