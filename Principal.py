from flask import Flask, jsonify, request
from datetime import datetime

Principal = Flask(__name__)

@Principal.route('/')
def home():
    diccionario_inicio = {
        "msg" : "Servidor funcionando correctamente.",
        "status" : 202
    }
    return jsonify(diccionario_inicio)

#--------------------------------------Empezando con USUARIOS--------------------------------------
usuarios = []
#Crear USUARIOS
@Principal.route('/user', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    if len(data) > 6:
        return jsonify({
            "msg" : "User was not created, items must be only 6.",
            "status" : 400
        })
    if len(data) < 6:
        return jsonify({
            "msg" : "User was not created, items are less than 6.",
            "status" : 400
        })
    for i in range(len(usuarios)):
        if (usuarios[i].get("id_user") == data.get("id_user")):
            return jsonify({
                "msg" : "User was not created, id_user already exists.",
                "status" : 400
            })
    
    new_user = {
        "id_user": data.get('id_user'),
        "user_name": request.json['user_name'],
        "user_nickname": request.json['user_nickname'],
        "user_password": request.json['user_password'],
        "user_rol": request.json['user_rol'],
        "available": request.json['available']
    }         
    usuarios.append(new_user)
    return jsonify({
                "msg" : "User created successfully.",
                "status" : 200
    })

#Actualizar USUARIOS
@Principal.route('/user', methods=['PUT'])
def actualizar_usuario():
    data = request.get_json()
    if len(data) > 6:
        return jsonify({
            "msg" : "User was not updated, items must be only 6.",
            "status" : 400
        })
    if len(data) < 6:
        return jsonify({
            "msg" : "User was not updated, items are less than 6.",
            "status" : 400
        })

    user_name = data.get("user_name")
    user_nickname = data.get("user_nickname")
    user_password = data.get("user_password")
    user_rol = data.get("user_rol")
    available = data.get("available")
    for i in range(len(usuarios)):
        if usuarios[i].get("id_user") == data.get("id_user"):
            usuarios[i]["user_name"] = user_name
            usuarios[i]["user_nickname"] = user_nickname
            usuarios[i]["user_password"] = user_password
            usuarios[i]["user_rol"] = user_rol
            usuarios[i]["available"] = available
            return jsonify({
                "msg" : "User was successfully updated.",
                "status" : 200
            })
            
    return jsonify({
                "msg" : "id_user doesn't exist.",
                "status" : 400
    })

#Ver USUARIO
@Principal.route('/user/<string:id>', methods=['GET'])
def ver_usuario(id):

    

    for i in range(len(usuarios)):
        if usuarios[i].get("id_user") == id:
            return jsonify(usuarios[i])
            
    return jsonify({
                "msg" : "id_user doesn't exist.",
                "status" : 400
    })

#Mostrar USUARIOS ----sólo para verificar que todo vaya bien----
@Principal.route('/show_user', methods=['GET'])
def mostrar_usuario():
    return jsonify(usuarios)

#--------------------------------------Empezando con LIBROS--------------------------------------
libros = []
#Crear LIBROS
@Principal.route('/book', methods=['POST'])
def ingresar_libros():
    libros_no_cargados = []
#Ingreso a una lista de diccionarios así:
#lst = [{"a": 1}, {}, {}]
#lst[0]--> {"a": 1}
#lst[0]["a"]--> 1

    data = request.get_json()

    for i in data:
        
        if len(i) > 10:
            libros_no_cargados.append(i)
            continue
        if len(i) < 10:
            libros_no_cargados.append(i)
            continue
        
        new_book = {
            "id_book": i.get("id_book"),
            "book_author": i.get("book_author"),
            "book_title": i.get("book_title"),
            "book_edition": i.get("book_edition"),
            "book_editorial": i.get("book_editorial"),
            "book_year": i.get("book_year"),
            "book_description": i.get("book_description"),
            "book_available_copies": i.get("book_available_copies"),
            "book_unavailable_copies": i.get("book_unavailable_copies"),
            "book_copies": i.get("book_copies")
        }
        for j in libros:

            if new_book.get("id_book") == j.get("id_book"):
                return jsonify({
                    "msg" : "Book(s) was(were) not created successfully. id_book already exists.",
                    "status" : 200
                })
        libros.append(new_book)
    return jsonify({
        "msg" : f"Book(s) was(were) created successfully. Books could not be charged: {libros_no_cargados}",
        "status" : 200
    })

#ACTUALIZAR LIBROS SOLICITANDO TODOS LOS DATOS PERO VERIFICANDO QUE EL ID EXISTE
@Principal.route('/book', methods = ['PUT'])
def actualizar_libro():
    data = request.get_json()
    if len(data) > 10:
        return jsonify({
            "msg" : "Book was not updated, items must be only 10.",
            "status" : 400
        })
    if len(data) < 10:
        return jsonify({
            "msg" : "Book was not updated, items must be 10.",
            "status" : 400
        })

    book_author = data.get("book_author")
    book_title = data.get("book_title")
    book_edition = data.get("book_edition")
    book_editorial = data.get("book_editorial")
    book_year = data.get("book_year")
    book_description = data.get("book_description")
    book_available_copies = data.get("book_available_copies")
    book_unavailable_copies = data.get("book_unavailable_copies")
    book_copies = data.get("book_copies")

    for i in range(len(libros)):
        if libros[i].get("id_book") == data.get("id_book"):
            libros[i]["book_author"] = book_author
            libros[i]["book_title"] = book_title
            libros[i]["book_edition"] = book_edition
            libros[i]["book_editorial"] = book_editorial
            libros[i]["book_year"] = book_year
            libros[i]["book_description"] = book_description
            libros[i]["book_available_copies"] = book_available_copies
            libros[i]["book_unavailable_copies"] = book_unavailable_copies
            libros[i]["book_copies"] = book_copies

            return jsonify({
                "msg" : "Book was successfully updated.",
                "status" : 200
            })
            
    return jsonify({
                "msg" : "id_book doesn't exist.",
                "status" : 400
    })
l = 0
#Eliminar LIBROS con PARAMS ID
@Principal.route('/book/<string:id>', methods=['DELETE'])
def eliminar_libro(id):
    global l
    for i in range(len(libros)):
        if libros[i].get("id_book") == id:
            libros.pop(i)
            l = l + 1
            return jsonify({
                "msg" : "Book was successfully deleted.",
                "status" : 200
            })
            
    return jsonify({
                "msg" : "id_book doesn't exist.",
                "status" : 400
    })

#VER LIBRO USANDO QUERY PARAMS DE AUTHOR Y TITULO -- YA FUNCIONAAAAAAAAAAA --
@Principal.route('/book', methods=['GET'])
def ver_libro():
    author = request.args.get('author')
    titulo = request.args.get('titulo')

    libros_mostrar = []
    for i in libros:
        if (i.get('book_author') == author) or (i.get('book_title') == titulo):
            libros_mostrar.append(i)
            
    if len(libros_mostrar) > 0:
        return jsonify(libros_mostrar)
    return jsonify({
                "msg" : "no matches.",
                "status" : 400
    })

#------------------------------------------PRESTAMOS------------------FALTA QUE HAGA EL CORRELATIVO------------------------

#Incluye un ID que se genera automáticamente como correlativo
#Date, fecha en que se hizo el préstamo
#Returned, falso o verdadero si ya se devolió o no
#Book, crea un objeto libro que se llena con el libro que se prestó
prestados = []
t = 0
#Hacer un PRÉSTAMO
@Principal.route('/borrow', methods=['POST'])
def prestar_libros():
    global t
    data = request.get_json()
    id_user = data.get('id_user')
    id_book = data.get('id_book')
    for i in usuarios:
        if i.get('id_user') == id_user:  
            if i.get('available') == False:
                return jsonify({
                "msg" : "user is not authorized.",
                "status" : 400
                })
            
    for j in libros:
        if j.get('id_book') == id_book:
            if j.get('book_available_copies') < 1:
                return jsonify({
                    "msg" : "There are not available copies.",
                    "status" : 400
                    })
            p = j
            t = t + 1
            p['book_available_copies'] = p.get('book_available_copies') - 1
            p['book_unavailable_copies'] = p.get('book_unavailable_copies') + 1
            
    now = datetime.now()
#INTENTANDO CREAR UN OBJETO PARA EL PRÉSTAMO
    new_prestamo = {
        'id_borrow' : t,
        'borrow_date' : now.date(),
        'returned' : False,
        'borrow_book' : p
    }
    prestados.append(new_prestamo)

    return jsonify({
                "msg" : "Done.",
                "status" : 200
                })

#--------------------------------------------------- DEVOLVER LIBRO ---------------------------------------------------

@Principal.route('/borrow/<int:id>', methods=['PUT'])
def devolver_libro(id):

    for i in range(len(prestados)):
        if prestados[i].get("id_borrow") == id:
            if prestados[i].get("returned") == False: 
                prestados[i]['returned'] = True
                for librito in libros:
                    if prestados[i]['borrow_book']['id_book'] == librito['id_book']:
                        prestados[i]['borrow_book']['book_available_copies'] = prestados[i]['borrow_book'].get('book_available_copies') + 1
                        prestados[i]['borrow_book']['book_unavailable_copies'] = prestados[i]['borrow_book'].get('book_unavailable_copies') - 1
                        librito['book_available_copies'] = librito.get('book_available_copies') + 1
                        librito['book_available_copies'] = librito.get('book_available_copies') - 1
                        
                return jsonify({
                "msg" : "Done.",
                "status" : 200
                })
            return jsonify({
                "msg" : "book was returned already.",
                "status" : 400
            })

    return jsonify({
                "msg" : "id_user doesn't exist.",
                "status" : 400
    })

#---------------------------------------------------Ver PRÉSTAMO-------------------------------------------------------------
@Principal.route('/borrow/<int:id>', methods=['GET'])
def ver_prestamo(id):

    for i in range(len(prestados)):
        if prestados[i].get("id_borrow") == id:
            return jsonify(prestados[i])
            
    return jsonify({
                "msg" : "id_borrow doesn't exist.",
                "status" : 400
    })

#---------------------------------------------------REPORTE---------------------------------------------------
#Podría hacer un reporte que muestre cuántos libros hay ingresados, cuántos eliminados y cuándos prestados
#Cuántos usuarios hay ingresados, cuántos hay disponibles para prestar y cuántos no

#La de usuarios ya hace la cuenta bien

@Principal.route('/reporte/<string:solicitud>', methods=['GET'])
def reportar(solicitud):

    permitidos = []
    no_permitidos = []
    for i in range(len(usuarios)):
        if usuarios[i]['available'] == True:
            permitidos.append(usuarios[i])
        else:
            no_permitidos.append(usuarios[i])

    libros_prestados = []
    libros_devueltos = []
    for j in range(len(prestados)):
        if prestados[j]['returned'] == False:
            libros_prestados.append(prestados[j])
        else:
            libros_devueltos.append(prestados[j])

    if solicitud == "usuarios":
        
        new_sol = {
                "Usuarios ingresados en el sistema": len(usuarios),
                "Usuarios disponibles para prestar": len(permitidos),
                "Usuarios no permitidos para prestar": len(no_permitidos)
        }
        return jsonify(new_sol)

    elif solicitud == "libros":

        new_sol = {
            "Libros ingresados en el sistema": len(libros),
            "Libros que han sido eliminados" : l,
            "Libros en la sección de préstamos": len(prestados),
            "Libros que están prestados": len(libros_prestados),
            "Libros que fueron devueltos": len(libros_devueltos)
        }
        return jsonify(new_sol)
    else:
        return jsonify({
                "msg" : "request doesn't exist",
                "status" : 400
    })

#Mostrar PRÉSTAMOS ----sólo para verificar que todo vaya bien----
@Principal.route('/show_prestamos', methods=['GET'])
def mostrar_prestamos():
    return jsonify(prestados)

#Mostrar LIBROS ----sólo para verificar que todo vaya bien----
@Principal.route('/show_book', methods=['GET'])
def mostrar_libros():
    return jsonify(libros)

if __name__ == '__main__':
    Principal.run(port = 3000, debug=True)