from view.view import View
from model.model import model

class Controller:
    #Constructor
    def __init__ (self ):
        self.model = model()
        self.view = View()

    #Constructor Controllers
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        b, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dir)
        if b:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)
        
    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contactos(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)
    
    def actualizar_contacto(self, id_contacto= '', nombre= '', tel= '', correo= '', direccion= ''):
        e = self.model.actualizar_contacto(id_contacto, nombre, tel, correo, direccion)
        if e:
            self.view.actualizar_contacto(id_contacto, id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)


    def borrar_contacto(self, id_contacto):
        e,c = self.model.borra_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(c)

    def leer_contactos_letra(self, letra):
        c = self.model.buscar_contacto(letra)
        self.view.mostrar_contactos(c)
        

    def insertar_contactos(self):
        self.agregar_contacto(1, 'Christian' , '4641702754', 'cristian@gmail.com', 'Tomasa Esteves')
        self.agregar_contacto(2, 'Pedro' , '4641702234', 'predro@gmail.com', 'Miguel hidalgo')
        self.agregar_contacto(3, 'Pablo' , '4641702234', 'pablo@gmail.com', 'Miguel hidalgo')

    #Cita controllers

    def agregar_citas(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        b, c = self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if not b:
            self.view.crear_cita(c)
        else:
            self.view.cita_ya_existe(id_cita)

    def insertar_citas (self):
        self.agregar_citas(1, 1 , 'Salamanca', '14/08/29', '02:00', 'Comer carnitas')
        self.agregar_citas(2, 2 , 'Salamanca', '14/08/29', '02:00', 'Comer pikxa')
        self.agregar_citas(3, 3 , 'Salamanca', '14/08/29', '02:00', 'Comer kaka')

    def leer_todas_citas(self):
        c = self.model.leer_todas_citas()
        self.view.mostrar_Citas(c)

    def start (self):
        #Display a welcome message
        self.view.start()
        #Insert data in model
        self.insertar_contactos()
        self.insertar_citas()
        #Show all contacts in database
        self.leer_todos_contactos()
        #self.leer_contactos_letra('a')
        self.leer_todas_citas()
    
    def menu (self):
        while (True):
            self.view.menu()
            o = input('Selecciona una puta opcion (1-9): ')
            if o == '1' :
                id_contacto = input ('Ingresa Id Contacto: ')
                nombre = input ('Ingresa telefono: ')
                tel = input ('Ingresa Nombre: ')
                correo = input ('Ingresa correo: ')
                dir = input ('Ingresa dir: ')
                self.agregar_contacto(id_contacto, nombre, tel, correo, dir)
            if o == '2' :
                id_contacto = input ('Ingresa Id Contacto: ')
                self.leer_contacto(id_contacto)
            if o == '3' :
                self.leer_todos_contactos()
            if o == '4' :
                self.actualizar_contacto()
            if o == '5' :
                id_contacto = input ('Ingresa Id Contacto: ')
                self.borrar_contacto(id_contacto)
            if o == '6' :
                letra = input ('Ingresa letra: ')
                self.leer_contactos_letra(letra)
            if o == '7' :
                self.insertar_contactos()
            if o == '8' :
                self.start()
            if o == '9' :
                self.leer_todas_citas()
            if o == '10' :
                id_cita = input ('Ingresa id_cita: ')
                id_contacto = input('Ingresa id_contacto: ')
                lugar = input('Ingresa lugar: ')
                fecha = input('Ingresa fecha: ')
                hora = input('Ingresa hora: ')
                asunto = input('Ingresa asunto: ')
                self.agregar_citas(id_cita, id_contacto, lugar, fecha, hora, asunto)
            if o == '11':
                print('Vaya a chingar a su puta madre\t')
                break
            # if o == '9' :
            #     self.view.opcion_no_valida(o)