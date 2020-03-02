class View:
    def agregar_contacto(self, contacto):
        print('*****Datos del Contacto *****')
        print('Nombre', contacto.nombre)
        print('Telefono', contacto.tel)
        print('Correo', contacto.correo)
        print('Direccion', contacto.direccion)
        print('****************************')
        
    def mostrar_contactos(self, contactos):
        print('*****Contactos definidos*****')
        for c in contactos:
            print(c.nombre,c.tel,c.correo,c.direccion)
        print('*****************************')
    
    def crear_contacto(self, contacto):
        print('*****Se agrego a la base de datos*****')
        print(contacto.nombre)
        print('**************************************')
    
    def borrar_contacto(self, contacto):
        print('*****Se quito de la base de datos*****')
        print(contacto.nombre)
        print('**************************************')
    

    def actualizar_contacto(self, contacto_o, contacto_n):
        print('*****Se modifico en la base de datos*****')
        print(contacto_o.nombre)
        print('**************************************')
    
    def contacto_ya_existe(self, contacto):
        print(contacto.id_contacto,'YA EXISTE EN LA BASE DE DATOS')
    
    def contacto_no_existe(self, id_contacto):
        print(id_contacto,'NO EXISTE EN LA BASE DE DATOS')
    
    def start(self):
        print('Esto es un ejemplo de una vista simple')
    
    def end(self):
        print('Hasta la vista puto')

    def mostrar_cita(self, cita):
        print('*****Datos de la cita*****')
        print('id_cita', cita.id_cita)
        print('id_contacto', cita.id_contacto)
        print('lugar', cita.lugar)
        print('fecha', cita.fecha)
        print('hora', cita.hora)
        print('asunto', cita.asunto)
        print('****************************')
    
    def mostrar_Citas(self, Citas):
        print('*****Citas definidas*********')
        for c in Citas:
            print(c.id_cita,c.id_contacto,c.lugar,c.fecha,c.hora,c.asunto)
        print('*****************************')
    
    def crear_cita(self, cita):
        print('*****Se agrego a la base de datos*****')
        print(cita.nombre)
        print('**************************************')
    
    def borrar_cita(self, cita):
        print('*****Se quito de la base de datos*****')
        print(cita.nombre)
        print('**************************************')
    
    def modificar_cita(self, cita_o, cita_n):
        print('*****Se modifico en la base de datos*****')
        print(cita_o.nombre)
        print('**************************************')
    
    def cita_ya_existe(self, cita):
        print(cita,'YA EXISTE EN LA BASE DE DATOS')
    
    def cita_no_existe(self, id_cita):
        print(id_cita,'NO EXISTE EN LA BASE DE DATOS')

    def menu (self):
        print('1- agregar_contacto')
        print('2- leer_contacto')
        print('3- leer_todos_contactos')
        print('4- actualizar_contacto')
        print('5- borrar_contacto')
        print('6- leer_contactos_letra')
        print('7- insertar_contactos')
        print('8- start')
        print('9- Leer todas las citas')
        print('10- Agregar citas')
        print('11- Terminar')
    
    # def opcion_no_valida():
    #     if 
