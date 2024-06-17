import csv
lista=[]
def menu(): # funcion menu
    print ("1.- Agregar plan\n2.- Listar planes\n3.- Eliminar plan por ID\n4.- Generar bbdd\n5.- Cargar bbdd\n6.- Estadísticas\n0.-Salir")
def printear_Lista(lis): #op2 funcion printear lista
    for i in lis:
            print(f"id: {i['id']}, nombre: {i['nombre']}, porcentaje: {i['porcentaje']}, categoria: {i['categoria']} ")
def generar_base_de_datos():#op4 generar base de datos
    with open ("planes.csv","w",newline="")as planes:
        fields=['id','nombre','porcentaje','categoria']
        escribir_csv=csv.DictWriter(planes,fieldnames=fields)
        escribir_csv.writeheader()
        escribir_csv.writerows(lista)
        print("se genero la base de datos con exito")
def cargar_base_de_datos(): #op5 cargar base de datos
    lista.clear()
    with open ("planes.csv","r",newline="")as planes:
        lector_csv=csv.DictReader(planes)
        for i in lector_csv:
            id2=int(i['id'])
            nom=i['nombre']
            por=int(i['porcentaje'])
            cat=i['categoria']
            diccionario_IMPORTADO={'id': id2,'nombre': nom,'porcentaje': por,'categoria': cat}
            lista.append(diccionario_IMPORTADO)
        print("se cargo la base de datos con exito")
def promediar_porcentaje():
    acum_porcentaje=0
    for i in lista:
        acum_porcentaje=acum_porcentaje+i['porcentaje']
    cantidad_de_planes=len(lista)
    promedio=acum_porcentaje/cantidad_de_planes
    print(f"El promedio del porcentaje de efectividad de los planes es de: {promedio}")
def mayor_porcentaje():
    mayor_porcentaje=0
    for i in lista:
        if i['porcentaje']>mayor_porcentaje:
            mayor_porcentaje=i['porcentaje']
    print(f"El promedio del porcentaje de efectividad de los planes es de: {mayor_porcentaje}")
def estadisticas():#op6
    print("-----Estadisticas-----\n")
    promediar_porcentaje()
    mayor_porcentaje()
def porcentaje():
    if porcentaje_efectividad>=0 and porcentaje_efectividad<=25:
        cat="Chiste"
    elif porcentaje_efectividad>=26 and porcentaje_efectividad<=50:
        cat="Anecdota"
    elif porcentaje_efectividad>=51 and porcentaje_efectividad<=75:
        cat="Peligro"
    elif porcentaje_efectividad>=76 and porcentaje_efectividad<=99:
        cat="Atencion"
    elif porcentaje_efectividad==100:
        cat="Esclavitud"
    return cat
def espacio():
    print("\n"*2)
while True:
    try:
        espacio()
        menu()
        op=int(input("Ingrese opcion\n"))
        if op==1: #1.- Agregar plan
            print("Agregar plan\n")
            id=int(input("ingrese id del plan\n"))
            nombre=input("ingrese el nombre\n")
            porcentaje_efectividad=int(input("ingrese porcentaje de efectividad del plan"))
            while porcentaje_efectividad<0 or porcentaje_efectividad>100:
                print("error, ingrese un porcentaje valido (0-100)")
                porcentaje_efectividad=int(input("ingrese porcentaje de efectividad del plan"))
            categoria=porcentaje() 
            diccionario_planes={'id' : id,'nombre': nombre,'porcentaje' : porcentaje_efectividad,'categoria' : categoria}
            lista.append(diccionario_planes)
        elif op==2:#2.- Listar planes
            printear_Lista(lista)
        elif op==3:#3.- Eliminar plan por ID
            encontrado=False
            buscar=int(input("Ingrese el id del plan que desea eliminar\n"))
            for i in lista:
                if i['id']==buscar:
                    print("Jugador encontrado!")
                    print(f"id: {i['id']}, nombre: {i['nombre']}, porcentaje: {i['porcentaje']}, categoria: {i['categoria']} ")
                    encontrado=True
                    respuesta=input("Esta seguro que desea borrar al jugador?\n")
                    if respuesta=="si" or respuesta=="s" or respuesta=="i":
                        lista.remove(i)
                    else:
                        print("no se elimino nada\n")
            if encontrado==False:
                print("No se encontro el plan")
        elif op==4:#4.- Generar bbdd(base de datos/csv)
            generar_base_de_datos()
        elif op==5:#5.- Cargar bbdd
            cargar_base_de_datos()
        elif op==6:#6.- Estadísticas(base de datos/csv)
            estadisticas()
        elif op==0:#salir
            print("Adios!!!")
            break
        else:
            print("ingrese opcion valida\n")
    except:
        print("ocurrio un error, ingreso una letra en el menu, intentelo denuevo")