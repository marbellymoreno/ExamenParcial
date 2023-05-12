import os
import time

clear = lambda: os.system("cls")

users = [{"id":"1","nombre":"Nicolas","password":"Nico123","tipo_usuario":"Administrador","estado":"A","edad":19},
        {"id":"2","nombre":"Rolando","password":"Rolando123","tipo_usuario":"Gerente","estado":"A","edad":19},
        {"id":"3","nombre":"Gerardo","password":"Gerardo123","tipo_usuario":"Cajero","estado":"I","edad":19},
        {"id":"4","nombre":"Josue","password":"Josue123","tipo_usuario":"Cajero","estado":"A","edad":19},
        {"id":"5","nombre":"Bryan","password":"Bryan123","tipo_usuario":"Gerente","estado":"A","edad":19}]

areas = [
    {"id":"1","area":"Componentes"},
    {"id":"2","area":"Perifericos"},
    {"id":"3","area":"Enfriamientos"},
]

categorias = [
    {"id":"1","categoria":"Procesadores","id_areas":"1"},
    {"id":"2","categoria":"Motherboards","id_areas":"1"},
    {"id":"3","categoria":"Mouses","id_areas":"2"},
    {"id":"4","categoria":"Teclados","id_areas":"2"},
    {"id":"5","categoria":"Enfriamiento por aire","id_areas":"3"},
    {"id":"6","categoria":"Enfriamiento Liquido","id_areas":"3"},
]

productos = [
    {"id":"1","id_categorias":"1","nombre":"Ryzen 3 3200G","proveedor":"AMD","fecha_caducidad":"N/A","fecha_entrada":"1-5-2023","detalle":"Procesador con arquitectura Zen 3 y graficos integrados Vega 8","precio":90.50,"unidades":4},
    {"id":"2","id_categorias":"1","nombre":"Intel Core i3 12100F","proveedor":"Intel","fecha_caducidad":"N/A","fecha_entrada":"1-5-2023","detalle":"Procesador sin graficos integrados con socket LGA1700","precio":159,"unidades":3},
    {"id":"3","id_categorias":"2","nombre":"Asus TUF gaming","proveedor":"ASUS TUF","fecha_caducidad":"N/A","fecha_entrada":"9-5-2023","detalle":"Motherboard DDR4 90MB19Y0","precio":235,"unidades":3},
    {"id":"4","id_categorias":"2","nombre":"Asus TUF gaming","proveedor":"ASUS TUF","fecha_caducidad":"N/A","fecha_entrada":"9-5-2023","detalle":"Motherboard AURA 90MB1BF0","precio":349,"unidades":3},
    {"id":"5","id_categorias":"3","nombre":"Mouse Logitech G-pro","proveedor":"LOGITECH","fecha_caducidad":"N/A","fecha_entrada":"9-5-2023","detalle":"Mouse inalambrico DPI 910","precio":129,"unidades":5},
    {"id":"6","id_categorias":"3","nombre":"Mouse Loitech G502 X","proveedor":"LOGITECH","fecha_caducidad":"N/A","fecha_entrada":"9-5-2023","detalle":"Mouse USB X lightforc3 hero","precio":84.95,"unidades":6},
    {"id":"7","id_categorias":"4","nombre":"Teclado Redragon Kumara","proveedor":"KUMARA","fecha_caducidad":"N/A","fecha_entrada":"9-5-2023","detalle":"Teclado K552-KR","precio":45,"unidades":9},
    {"id":"8","id_categorias":"4","nombre":"Teclado Logitech pro","proveedor":"LOGITECH","fecha_caducidad":"N/A","fecha_entrada":"9-5-2023","detalle":"Teclado League of legens","precio":129,"unidades":4},
    {"id":"9","id_categorias":"5","nombre":"Noctua NH-D15","proveedor":"Noctuna","fecha_caducidad":"N/A","fecha_entrada":"10-5-2023","detalle":"disipador de calor de CPU de doble torre, 2 ventiladores NF-A15","precio":100,"unidades":9},
    {"id":"10","id_categorias":"5","nombre":"be quiet! Dark Rock pro 4","proveedor":"be quiet!","fecha_caducidad":"N/A","fecha_entrada":"10-5-2023","detalle":"disipador de calor CPU de doble torre, 2 ventiladores Silent Wing 3","precio":90,"unidades":5},
    {"id":"11","id_categorias":"6","nombre":"H100i RGB Platinum SE","proveedor":"Corsair","fecha_caducidad":"N/A","fecha_entrada":"10-5-2023","detalle":"2 ventiladores de 120mm","precio":200,"unidades":4},
    {"id":"12","id_categorias":"6","nombre":"NZXT Kraken X73 RGB","proveedor":"NZXT","fecha_caducidad":"N/A","fecha_entrada":"10-5-2023","detalle":"3 ventiladores de 120mm","precio":200,"unidades":5},
    {"id":"13","id_categorias":"1","nombre":"Intel Core i9 12100K","proveedor":"Intel","fecha_caducidad":"N/A","fecha_entrada":"10-5-2023","detalle":"Procesador sin graficos integrados con socket LGA1700","precio":580,"unidades":8},
    {"id":"14","id_categorias":"1","nombre":"Ryzen 9 5700X","proveedor":"AMD","fecha_caducidad":"N/A","fecha_entrada":"10-5-2023","detalle":"Procesador con arquitectura Zen 4","precio":600,"unidades":4},


]
arrayCant = []
venta = []


def login():
    clear()
    try:
        print("+===================================+")
        print("|               Login               |")
        print("+===================================+")
        while True:
            nombreUser = input("Ingresa el nombre de usuario: ")
            password = input("Ingresar Contraseña de usuario: ")
            for usuario in users:
                if usuario["nombre"] == nombreUser and usuario["password"] == password:
                    if usuario['estado'] == "A":
                        print(f"Inicio de sesión exitoso.\n Bienvenido {usuario['nombre']}")
                        View1(usuario["tipo_usuario"])
                        return
                    else:
                        print("!!Este usuario esta desactivado,consulta a la gerencia!!")
                        time.sleep(3)
                        login()
                        return
            
            print("Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")
            time.sleep(3)
            login()  
            return      
        
    except ValueError:
       print("erro logico")
        
#Funcion donde se Crean,Leen,Actualizan y Eliminan Usuarios
def CrudUser(accion):
    clear()
    seguir = True
    while seguir == True:
        match accion:
            case "1":
                try: 
                        clear()
                        #Crear un nuevo usuario
                        print("+======================================+")
                        print("|       Creando un usuario Nuevo       |")
                        print("+======================================+")
                        
                        nombre = input("Ingresa el nombre del usuario: ")
                        contra = input("Ingresar contraseña de usuario: ")
                        print("nivel de usuario\n1- Administrador\n2- Gerente\n3- Cajero")
                        continuar = True
                        while continuar == True:
                            k = input("Ingrese el numero de nivel de usuario: ")
                            if k == "1":
                                tipo_usuario = "Administrador"
                                continuar == False
                                break
                            elif k == "2":
                                tipo_usuario = "Gerente"
                                continuar == False
                                break
                            elif k == "3":
                                tipo_usuario = "Cajero"
                                continuar == False
                                break
                            else:
                                print("la opcion ingresada no existe,Vuelve a intentarlo")
                        follow = True
                        while follow == True:
                            try:
                                edad = int(input("Ingrese la Edad del usuario Nuevo: "))
                                follow = False
                            except:
                                print("El valor ingresado no es un numero")
                        
                        users.append({"id":len(users) + 1,"nombre":nombre,"password":contra,"tipo_usuario":tipo_usuario,"estado":"A","edad":edad},)
                        x = users[-1]
                       
                        #Mostrando datos del usuario ingresado#
                        clear()
                        print("+=============+===========+================+===============+========+")
                        print("|                           Usuario Ingresado                       |")
                        print("+=============+===========+================+===============+========+")
                        print("|{:<12} |{:<10} |{:<15} |{:<15}|{:<8}|".format("Nombre","Contraseña","Tipo Usuario","Estado","Edad"))
                        print("+=============+===========+================+===============+========+")
                        print("|{:<12} |{:<10} |{:<15} |{:<15}|{:<8}|".format(x['nombre'],x["password"],x["tipo_usuario"],x["estado"],x['edad']))
                        print("+=============+===========+================+===============+========+")
                        #print("Nombre:",x["nombre"],"\nContraseña:",x["password"],"\nNivel de usuario:",x["tipo_usuario"],"\nEstado:",x["estado"])
                        print("!Usuario Ingresado con exito!, (4s)para redireccionar...")
                        time.sleep(4)
                        ViewAdmin()
                            
                        
                except:
                    print("ocurrio un error")
                
            case "2":
                #Actualizar un nuevo usuario
                print("+===============================================================+========+")
                print("|                           Lista de Usuarios                            |")
                print("+====+=============+===========+================+===============+========+")
                print("|{:<4}|{:<12} |{:<10} |{:<15} |{:<15}|{:<8}|".format("id","Nombre","Contraseña","Tipo Usuario","Estado","Edad"))
                print("+====+=============+===========+================+===============+========+")
                for j in range(len(users)):
                    print ("|{:<4}|{:<12} |{:<10} |{:<15} |{:<15}|{:<8}|".format( users[j]['id'],users[j]['nombre'], users[j]['password'], users[j]['tipo_usuario'],"Activo" if users[j]['estado'] == "A" else "Inactivo",users[j]['edad']))
                print("+====+=============+===========+================+===============+========+")
                usuarioUpd = input("Ingresa el 'id' del usuario para actualizarlo: ")
                x = users[int(usuarioUpd)-1]
                print(f"Nombre actual: {x['nombre']}")
                x['nombre']= input(f"Ingresar nuevo nombre: ")
                print(f"Contraseña actual: {x['password']}")
                x['password']= input(f"Ingresar nueva contraseña: ")
                print(f"Tipo de Usuario actual: {x['tipo_usuario']}")
                x['tipo_usuario']= input(f"Ingresar nuevo tipo de usuario: ").capitalize()
                print(f"Estado actual: {x['estado']}")
                x['estado']= input(f"Ingresar estado de usuario: ")
                print(f"Edad Actual del Usuario: {x['edad']}")
                follow = True
                while follow == True:
                    try:
                        x['edad'] = int(input("Ingrese la Edad del usuario Nuevo: "))
                        follow = False
                    except:
                        print("El valor ingresado no es un numero")
                users[int(usuarioUpd)-1] = x
                #print(users[int(usuarioUpd)-1])
                print("!Usuario Actualizado con exito!, (4s)para redireccionar...")
                time.sleep(4)
                ViewAdmin()  
            case "3":
                #Eliminar un usuario
                print("+========================================================================+")
                print("|                             Lista de Usuarios                          |")
                print("+===============================================================+========+")
                print("|{:<4}|{:<12} |{:<10} |{:<15} |{:<15}|{:<8}|".format("id","Nombre","Contraseña","Tipo Usuario","Estado","Edad"))
                print("+===============================================================+========+")
                for j in range(len(users)):
                    print ("|{:<4}|{:<12} |{:<10} |{:<15} |{:<15}|{:<8}|".format( users[j]['id'],users[j]['nombre'], users[j]['password'], users[j]['tipo_usuario'],"Activo" if users[j]['estado'] == "A" else "Inactivo",users[j]['edad']))
                print("+===============================================================+========+")
                usuarioUpd = input("Ingresa el 'id' del usuario para Eliminarlo: ")
                users.pop(int(usuarioUpd)-1)
                print("!Usuario Eliminado con exito!, (4s)para redireccionar...")
                time.sleep(4)
                ViewAdmin()
                
            case "4":
                print("+========================================================================+")
                print("|                            Lista de Usuarios                           |")
                print("+====+=============+===========+================+===============+========+")
                print("|{:<4}|{:<12} |{:<10} |{:<15} |{:<15}|{:<8}|".format("id","Nombre","Contraseña","Tipo Usuario","Estado","Edad"))
                print("+====+=============+===========+================+===============+========+")
                for j in range(len(users)):
                    print ("|{:<4}|{:<12} |{:<10} |{:<15} |{:<15}|{:<8}|".format( users[j]['id'],users[j]['nombre'], users[j]['password'], users[j]['tipo_usuario'],"Activo" if users[j]['estado'] == "A" else "Inactivo",users[j]['edad']))
                print("+====+=============+===========+================+===============+========+")
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()
            case "5":
                ViewAdmin()
            case _:
                print("La opcion ingresada no existe, Vuelve a intentarlo: ")
#Funcion donde se Crean,Leen,Actualizan y Eliminan areas
def CrudArea(accion):
    clear()
    seguir = True
    while seguir == True:
        match accion:
            case "1":
                clear()
                #crear una area
                print("+===================================+")
                print("|          Ingresar una area        |")
                print("+===================================+")
                area = input("Ingrese el nombre de la nueva area: ")
                areas.append({"id":len(areas) + 1,"area":area},)
                x = areas[-1]
                #Mostrando datos del usuario ingresado#
                print("+=======================+")
                print("|     Area Ingresada    |")
                print("+====+==================+")
                print("|{:<4}|{:<18}|".format("id","Nombre"))
                print("|{:<4}|{:<18}|".format(x['id'],x['area']))
                print("+====+==================+")
                print("!Area Registrada con exito!, (4s)para redireccionar...")
                time.sleep(4)
                ViewAdmin()
                
            case "2":
                 #Actualizar una area
                print("+=======================+")
                print("|    Actualizar Area    |")
                print("+====+==================+")
                print("|{:<4}|{:<18}|".format("id","Nombre"))
                for j in range(len(areas)):
                    print("|{:<4}|{:<18}|".format(areas[j]['id'],areas[j]['area']))
                print("+====+==================+")
                areaUpd = input("Ingresa el 'id' del area para actualizarlo: ")
                id =areas[int(areaUpd)-1]
                print(f"Nombre actual del area: {id['area']}")
                id['area']= input(f"Ingresar nombre del area: ")
                areas[int(areaUpd)-1] = id
                #print(areas[int(areaUpd)-1])
                print("Area actualizada con exito...")
                input("Presiona una tecla para continuar")
                ViewAdmin()  
            case "3":
                #  Opcion 4 Mostras las areas#
                print("+=======================+")
                print("|       Lista Area      |")
                print("+====+==================+")
                print("|{:<4}|{:<18}|".format("id","Nombre"))
                for j in range(len(areas)):
                    print("|{:<4}|{:<18}|".format(areas[j]['id'],areas[j]['area']))   
                print("+====+==================+") 
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()
            case "4":
                ViewAdmin()
            case _:
                print()

def CrudCategorias(acccion):
    seguir = True
    while seguir == True:
        match acccion:
            case "1":
                #Crear categoria nueva
                categoria = input("Ingrese el nombre de la nueva categoria: ")
                 #relacion de area con categorias por medio del id_area
                j = 1
                for area in areas:
                    print(f"{j}-{area['area']}")
                    j += 1
                id_area = input("Ingrese el area a la que pertenece: ")
                categorias.append({"id":len(categorias) + 1,"categoria":categoria,"id_areas":id_area},)
                data = categorias[-1]
                 #Mostrando datos del usuario ingresado# <+++++++ areglar estilo con .format()*************
                for j in areas:
                    if data["id_areas"] == j["id"]:
                         print("Id:",data['id'],"Categoria:",data['categoria'],"area",j['area'])
                print("!Categoria Registrada con exito!")
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()
            case "2":
                #Actualizar categoria 
                #  {"id":"1","categoria":"Procesadores","id_areas":"1"},
                print("-------------------------------------------")
                print("\tLista de Categorias")
                print("-------------------------------------------")
                print ("{:<4} {:<25} {:<15}".format( "Id","categorias","areas"))
                for j in range(len(categorias)):
                    for i in areas:
                        if categorias[j]["id_areas"] == i["id"]:
                            print ("{:<4} {:<25} {:<15} ".format( categorias[j]['id'],categorias[j]['categoria'],i['area']))
                catUpd = input("Ingresa el 'id' de la categoria para actualizarlo: ")
                id = categorias[int(catUpd)-1]
                print(f"Nombre actual de la categoria: {id['categoria']}")
                id['categoria']= input(f"Ingresar nombre de la categoria: ")
                #relacion de area con categorias por medio del id_area
                j = 1
                for area in areas:
                    print(f"{j}-{area['area']}")
                    j += 1
                id_area = input("Ingrese el area a la que pertenece: ")
                id['id_areas']= id_area
                categorias[int(catUpd)-1] = id
                print("Area actualizada con exito...")
                input("Presiona una tecla para continuar")
                ViewAdmin()       
            case "3":
                #Mostrar categorias
                
                print ("{:<8} {:<25} {:<15} ".format( "Id","Categoria","Area"))
                for j in range(len(categorias)):
                    for area in areas:
                        if categorias[j]['id_areas'] == area['id']:
                            print("{:<8} {:<25} {:<15}".format( categorias[j]['id'],categorias[j]['categoria'],area['area']))
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()
            case "4":
                print("Cerrando Session...")
                ViewAdmin()
            case _:
                print("La opcion no esta registra,Vuelvelo a intentar")

def CrudProductos(accion):
    seguir = True
    while seguir == True:
        match accion:
            case "1":
                #Crear producto nuevo
                 #relacion de categoria con producto 
                j = 1
                for cat in categorias:
                    print(f"{j}-{cat['categoria']}")
                    j += 1
                id_cat = input("Ingrese el numero de la categoria : ")
                nombreProduct = input("Ingrese el nombre del producto: ")
                proveedor = input("Ingrese el nombre del proveedor: ")
                fecha_caducidad = "N/A"
                fecha_entrada = input("Ingrese la fecha de entrada *1-1-2020*: ")
                detalle = input("Ingrese el detalle del producto: ")
                #Validar que sea numeros decimales#
                follow = True
                while  follow == True:
                    try:
                        precio = float(input("Ingrese el precio del producto: "))
                        follow = False
                        break
                    except:
                        print("El dato ingresado con tiene letra,Vuelve a intentarlo")
                follow_unid = True
                while follow_unid == True:
                    try:
                        unidades = int(input("Ingrese las unidades de productos: "))
                        follow_unid = False
                        break
                    except:
                        print("El dato ingresado con tiene letra,Vuelve a intentarlo")
                productos.append({"id":len(productos) + 1,"id_categorias":id_cat,"nombre":nombreProduct,"proveedor":proveedor,"fecha_caducida":fecha_caducidad,"fecha_entrada":fecha_entrada,"detalle":detalle,"precio":precio,"unidades":unidades},)
                data = productos[-1]
                 #Mostrando datos del producto ingresado#
                print("+=========+==========================+================+================+================+================+===============+")
                print("|                                                  Producto Ingresado                                                    |")
                print("+=========+==========================+================+================+================+================+===============+")
                print ("|{:<8} |{:<25}|{:<25} |{:<15} |{:<15} |{:<15} |{:<10} |{:<10}|".format( "Id","Categoria","Nombre","Proveedor","F.Caducida","F.Entrada","Precio","Unidades"))
                for j in categorias:
                    if data["id_categorias"] == j["id"]:
                          print("|{:<8} |{:<25}|{:<25} |{:<15} |{:<15} |{:<15} |{:<10} |{:<10}|".format( productos[j]['id'],cat["categoria"],productos[j]['nombre'],productos[j]['proveedor'],productos[j]['fecha_caducidad'],productos[j]['fecha_entrada'],productos[j]['precio'],productos[j]['unidades']))
                print("+=========+==========================+================+================+================+================+===============+")
                print("!Categoria Registrada con exito!")
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()
            case "2":
                #Actualizar Productos 
                print("+=========+==========================+================+================+================+================+===============+")
                print("|                                                 Lista de Productos                                                     |")
                print("+=========+==========================+================+================+================+================+===============+")
                print ("|{:<8} |{:<25}|{:<25} |{:<15} |{:<15} |{:<15} |{:<10} |{:<10}|".format( "N®","Categoria","Nombre","Proveedor","F.Caducida","F.Entrada","Precio","Unidades"))
                for j in range(len(productos)):
                    for i in categorias:
                        if productos[j]["id_categorias"] == i["id"]:
                            print("|{:<8} |{:<25} |{:<15} |{:<15} |{:<15} |{:<15} |{:<15}|".format(productos[j]['id'],productos[j]['nombre'],productos[j]['proveedor'],productos[j]['fecha_caducidad'],productos[j]['fecha_entrada'],"$"+str(productos[j]['precio']),productos[j]['unidades']))
                    print("+=========+==========================+================+================+================+================+===============+")       
                productUpd = input("Ingresa el 'id' del producto para actualizarlo: ")
                #buscamos en productos[] por medio del id menos 1 para encontrar el dato exacto con su posicion y lo guardamos en una varible id
                id = productos[int(productUpd)-1]
                #relacion de area con categorias por medio del id_area
                j = 1
                for cat in categorias:
                    print(f"{j}-{cat['categoria']}")
                    j += 1
                id['id_categorias']= input(f"Ingrese a que categoria pertenece: ")
                
                print(f"Nombre actual del producto: {id['nombre']}")
                id['nombre']= input(f"Ingrese el nombre del producto: ")
                print(f"Nombre actual del Proveedor: {id['proveedor']}")
                id['proveedor']= input(f"Ingrese el nombre del Proveedor: ")                
                print(f"Fecha de caducidad del producto: {id['fecha_caducidad']}")
                id['fecha_caducidad']= input(f"Ingrese la fecha de caducidad de su producto: ")
                print(f"Fecha de entrada del producto: {id['fecha_entrada']}")
                id['fecha_entrada']= input(f"Ingrese la fecha de entrada de su producto: ")
                print(f"Detalle Actual del producto: {id['detalle']}")
                id['detalle']= input(f"Ingrese el detalle del producto: ")
                print(f"precio actual del producto: {id['precio']}")
                id['precio']= input(f"Ingrese el precio del producto: ")
                print(f"Unidades actuales del producto: {id['unidades']}")
                id['unidades']= input(f"Ingrese las unidades del producto: ")
                productos[int(productUpd)-1] = id
                print("producto actualizado con exito...")
                input("Presiona una tecla para continuar")
                ViewAdmin()       
            case "3":
                #Mostrar productos
                print("+=========+=========================+==========================+================+================+================+===========+==========+")
                print("|                                                          Lista de Productos                                                            |")
                print("+=========+=========================+==========================+================+================+================+===========+==========+")
                print ("|{:<8} |{:<25}|{:<25} |{:<15} |{:<15} |{:<15} |{:<10} |{:<10}|".format( "N®","Categoria","Nombre","Proveedor","F.Caducida","F.Entrada","Precio","Unidades"))
                for j in range(len(productos)):
                    for cat in categorias:
                        if productos[j]['id_categorias'] == cat['id']:
                            print("|{:<8} |{:<25}|{:<25} |{:<15} |{:<15} |{:<15} |{:<10} |{:<10}|".format( productos[j]['id'],cat["categoria"],productos[j]['nombre'],productos[j]['proveedor'],productos[j]['fecha_caducidad'],productos[j]['fecha_entrada'],productos[j]['precio'],productos[j]['unidades']))
                    print("+=========+=========================+==========================+================+================+================+===========+==========+")
                input("Presiona cualquier tecla para regresar al menu: ")
                ViewAdmin()
            case "4":
                print("Cerrando Session...")
                ViewAdmin()
            case _:
                print("La opcion no esta registra,Vuelvelo a intentar")

def ticket(data):
    print("+============================================================+")
    print("|                      Ticket de Venta                       |")
    print("+========+=========================+=========================+")
    print ("|{:<8}|{:^25}|{:^25}|".format("Cantidad","Nombre","Precio"))
    print("+========+=========================+=========================+")
    total = 0
    for j in range(len(venta)):
        # print(venta[j])
        precio = int(data[j]) * float(venta[j]['precio'])
        total = total + precio
        print("|{:<8}|{:<25}|{:<25}|".format(data[j],venta[j]['nombre'],precio))
    print("+========+=========================+=========================+")
    print(f"|          Total                   |     ${total}              |")
    print("+========+=========================+=========================+")
    print("          **Gracias Por su Compra Pase Buen Dia**             ")
    print("+============================================================+")
    input("Presiona cualquier tecla para continuar!!")
    arrayCant[:] = []
    venta [:] = []
    return False
def SaleOfProduct():
    clear()
    print("+=======================+")
    print("|       Lista Area      |")
    print("+====+==================+")
    print("|{:<4}|{:<18}|".format("id","Areas"))
    for j in range(len(areas)):
        print("|{:<4}|{:<18}|".format(areas[j]['id'],areas[j]['area'])) 
    print("+====+==================+")
    
    selectArea = input("Selecione una area: ")
    #mostrando categorias de esa area#
    clear()
    print("+===================================+")
    print("|        Lista de categorias        |")
    print("+=========+=========================+")
    print ("|{:<8} |{:<25}| ".format( "Id","Categoria"))
    for j in range(len(categorias)):
                if categorias[j]['id_areas'] == selectArea:
                    print("|{:<8} |{:<25}|  ".format( categorias[j]['id'],categorias[j]['categoria']))
    print("+=========+=========================+")
    selectCat = input("Selecione una categoria: ")
    #mostrando productos de esa categoria#
    venta_follow = True
    while venta_follow == True:
        clear()
        print("+=========+==========================+================+================+================+================+===============+")
        print("|                                                 Lista de Productos                                                     |")
        print("+=========+==========================+================+================+================+================+===============+")
        print ("|{:<8} |{:<25} |{:<15} |{:<15} |{:<15} |{:<15} |{:<15}|".format( "Id","Nombre","Proveedor","F.Caducida","F.Entrada","Precio","Unidades"))
        found_products = False
        for j in range(len(productos)):
            if productos[j]['id_categorias'] == selectCat:
                if productos[j]['unidades'] > 0:
                    print("|{:<8} |{:<25} |{:<15} |{:<15} |{:<15} |{:<15} |{:<15}|".format(productos[j]['id'],productos[j]['nombre'],productos[j]['proveedor'],productos[j]['fecha_caducidad'],productos[j]['fecha_entrada'],"$"+str(productos[j]['precio']),productos[j]['unidades']))
                found_products = True
        print("+=========+==========================+================+================+================+================+===============+")
        if not found_products:
            print("===============================================")
            print("No hay producto para mostrar en esta categoria")
            print("==============================================")
            input("Presiona una tecla para volverlo a intentar")
            SaleOfProduct()
                
    # venta_follow = True
    # while venta_follow == True:
        try:
            selectProduct = input("Ingrese el 'id' del producto para agregarlo a la compra:")
            cantidad = input("Ingrese la cantidad de productos: ")#validar este campo para solo int
            for j in range(len(productos)):
                if productos[j]['id'] == selectProduct:
                    if productos[j]['unidades'] >= int(cantidad):
                        #actualizando en tiempo real el inventario simulando en tiempo real#
                        id = productos[int(selectProduct)-1]
                        #print(id)
                        id['unidades'] = id['unidades'] - int(cantidad)
                        
                        arrayCant.append(cantidad)
                        productos[int(selectProduct)-1] = id
                        venta.append(productos[j])
                        print("¿Quieres continuar agregando productos?\n1-SI\n2-NO")
                        seguir = input("Esperando opcion: ").upper()
                        if seguir == "SI" or seguir == "1":
                            SaleOfProduct()
                        else: 
                            ticket(arrayCant)
                            venta_follow = False
                            ViewCashier()
                    else:
                        print("'No se cuenta con esa cantidad de productos,Vuelva a intentarlo'")
                        time.sleep(2)
        except ValueError:
            print("ocurrio un erro logico")
#menu de vista admin
def ViewAdmin():
    clear()
    seguir = True
    print("¿Que accion quieres realizar?: ")
    print("""
    1- Consultar Usuarios
    2- Consultar Areas
    3- Consultar Categorias
    4- Consultar Productos
    5- Cerrar session
    """)
    
    while seguir == True:
        
        consulta = input("Ingresa una accion: ")
        match consulta:
            case "1":
                print("""
        ¿Que desea hacer?
    1- Crear un Usuario        
    2- Actualizar un Usuario
    3- Eliminar un Usuario
    4- Mostrar Usuarios
    5- Volver atras...
                """)
                accion = input("Ingresar accion a realizar: ")
                try:
                    if accion.isdigit() == True:
                        CrudUser(accion)
                    else:
                        print("La opcion ingresada no esta agregada, Vuelva a intentarlo")
                        time.sleep(2)
                        ViewAdmin()    
                except:
                    print("La opcion ingresada no esta agregada, Vuelva a intentarlo")
                    time.sleep(2)
                    ViewAdmin()
            case "2":
                print("""
        ¿Que desea hacer?
    1- Crear una area        
    2- Actualizar area
    3- Mostrar areas
    4- Volver atras...
                """)
                accion = input("Ingresar opcion a realizar: ")
                try:
                    if accion.isdigit() == True:
                        CrudArea(accion)
                    else:
                        print("La opcion ingresada no esta agregada, Vuelva a intentarlo")
                        time.sleep(2)
                        ViewAdmin()    
                except:
                    print("La opcion ingresada no esta agregada, Vuelva a intentarlo")
                    time.sleep(2)
                    ViewAdmin()
            case "3":
                print("""
        ¿Que desea hacer?
    1- Crear una categoria        
    2- Actualizar una categoria
    3- Mostrar categorias
    4- Volver atras...
                """)
                accion = input("Ingresar opcion a realizar: ")
                try:
                    if accion.isdigit() == True:
                        CrudCategorias(accion)
                    else:
                        print("La opcion ingresada no esta agregada, Vuelva a intentarlo")
                        time.sleep(2)
                        ViewAdmin()    
                except:
                    print("La opcion ingresada no esta agregada, Vuelva a intentarlo")
                    time.sleep(2)
                    ViewAdmin()
            case "4":
                print("""
        ¿Que desea hacer?
    1- Crear un producto        
    2- Actualizar un producto
    3- Mostrar productos
    4- Volver atras...
                """)
                accion = input("Ingresar opcion a realizar: ")
                try:
                    if accion.isdigit() == True:
                        CrudProductos(accion)
                    else:
                        print("La opcion ingresada no esta agregada, Vuelva a intentarlo")
                        time.sleep(2)
                        ViewAdmin()    
                except:
                    print("La opcion ingresada no esta agregada, Vuelva a intentarlo")
                    time.sleep(2)
                    ViewAdmin()
            case "5":
                print("Cerrando Session... en (3s)")
                time.sleep(3)
                login()
            case _:
                print("La opcion ingresada no existe, Vuelve a intentarlo")
                
def ViewManager():
    print("¿Que accion quieres realizar?: ")
    print("""
    1- Consultar Areas
    2- Consultar Categorias
    3- Consultar Productos
    4- Cerrar session
    """)
    
    follow = True
    while follow:
        consulta = input("Ingresa una la accion que quieras realizar: ")
        match consulta:
            case "1":
                i = 1
                print("+=======================+")
                print("|       Lista Area      |")
                print("+====+==================+")
                print("|{:<4}|{:<18}|".format("N®","Nombre"))
                for j in range(len(areas)):
                    print("|{:<4}|{:<18}|".format(i,areas[j]['area'])) 
                    i += 1            
                print("+====+==================+") 
                input("Presiona cualquier tecla para continuar...")
                ViewManager()
                follow = False
            case "2":
                i = 1
                print("=======================================================")
                print("\tConsulta de Categorias")
                print("=======================================================")
                print ("{:<3} {:<25} {:<15}".format( "Id","Categorias","Areas"))
                print("--------------------------------------------------------")
                for cat in categorias:
                    for j in areas:
                        if j['id'] == cat['id_areas']:
                            print ("{:<3} {:<25} {:<15}".format( i, cat['categoria'],j['area']))       
                    i += 1
                print("--------------------------------------------------------")
                input("Presiona cualquier tecla para continuar...")
                ViewManager()
                follow = False
            case "3":
                i = 1
                print("==================================")
                print("\tConsulta de productos")
                print("==================================")
                print ("{:<3} {:<25} {:<15} {:<12} {:<12} {:<8} {:<8} ".format( "Id","producto","proveedor","F.caducidad","F.entrada","Precio","Unidades"))
                print("--------------------------------------------------------------------------")
                for prod in productos: 
                    print ("{:<3} {:<25} {:<15} {:<12} {:<12} {:<8} {:<8}  ".format( i, prod['nombre'],prod['proveedor'],prod['fecha_caducidad'],prod['fecha_entrada'],prod['precio'],prod['unidades'],))       
                    i += 1
                print("--------------------------------------------------------------------------")
                input("Presiona cualquier tecla para continuar...")
                ViewManager()
                follow = False
            case "4":
                print("Cerrando Session...")
                login()
            case _:
                print("La opcion Ingresada no existe vuelva a intentarlo")
def ViewCashier():
    clear()
    continuar = True
    while continuar == True:
       try:
            print("Quiere Iniciar una venta\n1-SI\n2-NO")
            opcion = input("Ingrese su respuesta: ").upper()
            if opcion == "1" or opcion == "SI":
                SaleOfProduct()
            else:
                login()
            print("no quieres hacer una venta")
       except:
           print("Erroro Logico")
            


#Funcion de vista 1
def View1(tipo_user):
    match tipo_user:
        case "Administrador":
            ViewAdmin()
        case "Gerente":
            ViewManager()
        case "Cajero":
            ViewCashier()
        case _:
            print("La opcion ingresada no existe, Vuelve a intentarlo")


login()