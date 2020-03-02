from .contacto import Contacto
from .cita import Cita

class model:
    def __init__(self):
        self.contactos = []
        self.citas = []

    def buscar_id(self, id_contacto):
        for i in self.contactos:
            if i.id_contacto == id_contacto:
                return True, i
        return False,0
                

    # Contacto methods
    def agregar_contacto(self, id_contacto, nombre, tel, correo, direccion):
        e,c = self.buscar_id(id_contacto)
        if not e:
            c = Contacto(id_contacto, nombre, tel, correo, direccion)
            self.contactos.append(c)
            return True, c
        return False, 0
    
    def leer_contacto (self, id_contacto):
        e, c = self.buscar_id(id_contacto)
        return e, c

    def leer_todos_contactos(self):
        return self.contactos

    def actualizar_contacto (self, id_contacto= '', nombre= '', tel= '', correo= '', direccion= ''):
        e, c = self.buscar_id(id_contacto)
        if e:
            if id_contacto != '':
                 c.id_contacto = id_contacto
            if nombre != '':
                 c.nombre = nombre
            if tel != '':
                 c.tel = tel
            if correo != '':
                 c.correo = correo 
            if direccion != '':
                 c.direccion = direccion
            return True

        return False

    def borra_contacto(self,id_contacto):
        e, c = self.buscar_id(id_contacto)
        if e:
            self.contactos.remove(c)
            return False
        return True

    def leer_contactos_letra (self, letra):
        #lista = [c for c in self.contactos is c.nombre.lower().startswith(letra.lower)]
        return [c for c in self.contactos if c.nombre.lower().startwith(letra.lower())]
        # lista = []
        # for c in self.contactos:
        #     if c.nombre[0].lower==letra.lower()
        #     lista.append(c)
        #return lista
    
    def borrar_contacto_cita (self, id_contacto):
        e, contacto = self.buscar_id(id_contacto)
        if e:
            self.contactos.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for c in lista_temp:
                self.citas.remove(c)
            return True, contacto
        return False, 0

    # Cita methods

    def buscar_idCita (self, id_cita):
        for i in self.citas:
            if i.id_cita == id_cita:
                return True, i
        return False,0

    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        if self.buscar_id(id_contacto)[0]:
            e,c = self.buscar_idCita(id_cita)
            if not e:
                c = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
                self.citas.append(c)
                return True, c
        return False, 0

    def leer_cita (self, id_cita):
        e, c = self.buscar_idCita(id_cita)
        if e:
            return c
        return False

    def actualizar_cita (self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        e, c = self.buscar_idCita(id_cita)
        if e:
            c.id_cita = id_cita
            c.id_contacto = id_contacto
            c.lugar = lugar
            c.fecha = fecha
            c.hora = hora
            c.asunto = asunto
            return True
        return False

    def borra_cita(self,id_cita):
        e, c = self.buscar_idCita(id_cita)
        if e:
            self.citas.remove(c)
            return False
        return True


    def actualizar_cita2 (self, id_cita = None, id_contacto = None, lugar = None, fecha = None, hora = None, asunto = None):
        if id_cita != None:
            e, c = self.buscar_idCita(id_cita)
        if e:
            if id_cita != None:
                c.id_cita = id_cita
            if id_contacto != None:
                c.id_contacto = id_contacto
            if lugar != None:
                c.lugar = lugar
            if fecha != None:
                c.fecha = fecha
            if hora != None:
                c.hora = hora
            if asunto != None:
                c.asunto = asunto
            return True
        return False
    
    def buscar_contacto (self, letra):
        listaContactos = []
        for i in self.contactos:
            if letra == i.nombre[0]:
                listaContactos.append(i.nombre)
        
        return listaContactos
    
    def buscar_citas_fecha (self, fecha):
        listaCitas = []
        for i in self.citas:
            if fecha == i.fecha:
                listaCitas.append(i)
        return listaCitas
    
    def leer_todas_citas(self):
        return self.citas
    