# from model.contacto import Contacto
# from model.cita import Cita
# from model.model import model
# from view.view import View
from controller.controller import Controller

# c = Contacto (1, 'Christian' , '4641702754', 'cristian@gmail.com', 'Tomasa Esteves')
# c2 = Contacto (1, 'Pedro' , '4641702234', 'predro@gmail.com', 'Miguel hidalgo')

# print(c.id_contacto)
# print(c.nombre)
# print(c.tel)
# print(c.correo)
# print(c.direccion)


# ci = Cita(1, 'Christian', 'el tocumbo', '17/02/20', '20:00', 'Amor')

# print(ci.id_cita)
# print(ci.id_contacto)
# print(ci.lugar)
# print(ci.fecha)
# print(ci.hora)
# print(ci.asunto)

# ListaContactos = []

# ListaContactos.append(c)
# ListaContactos.append(c2)

# name = input('Dame un nombre: ')

# for i in ListaContactos:
#     if name == i.nombre:
#         print('si esta')
#         break
#     else:
#         print('no esta')

# m = model()
# m.agregar_contacto(1, 'Christian' , '4641702754', 'cristian@gmail.com', 'Tomasa Esteves')
# m.agregar_contacto(2, 'Pedro' , '4641702234', 'predro@gmail.com', 'Miguel hidalgo')
# m.agregar_contacto(3, 'Pablo' , '4641702234', 'pablo@gmail.com', 'Miguel hidalgo')

# s = m.leer_contacto(2)
# print(s.nombre)

# s = m.actualizar_contacto(2, 'Peppa' , '464170212312', 'pepa@gmail.com', 'Miguel')
# s = m.leer_contacto(2)
# print(s.nombre)


# m.agregar_cita(1, 1, 'Salamanca', '10 de agosto', '15:00', 'Comer tacos')
# m.agregar_cita(2, 2, 'Salamanca', '10 de agosto', '15:00', 'Comer tortas')
# m.agregar_cita(3, 1, 'Salamanca', '10 de agosto', '15:00', 'Comer kaka')
# s2 = m.leer_cita(1)
# print(s2.lugar)

# m.actualizar_cita2(id_cita=1,id_contacto=1,lugar='irapuato')
# s3 = m.leer_cita(1)
# print(s3.lugar)

# s = m.leer_todos_contactos()
# for c in s:
#     print(c.nombre)

# # s = m.buscar_citas_fecha('10 de agosto')
# # for c in s:
# #     print(c.asunto)

# # m.borrar_contacto_cita(1)
# s = m.leer_todas_citas()
# for c in s:
#     print(c.asunto)

# # print('*******')
# # m.borrar_contacto_cita(1)

# s = m.leer_todas_citas()
# for c in s:
#     print(c.asunto)

# v = View()
# s = m.leer_todos_contactos()
# v.mostrar_contactos(s)
# c = m.leer_contacto(1)
# v.mostrar_contacto(c)

# f, c = m.borrar_contacto_cita(1)
# if f:
#     v.borrar_contacto(c)
# else:
#     v.contacto_no_existe(1)

# s = m.leer_todos_contactos()
# v.mostrar_contactos(s)

cont = Controller()
cont.menu()