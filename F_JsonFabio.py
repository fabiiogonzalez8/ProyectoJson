import json
import datetime
def leer_json(listacines): 
    with open("cines.json") as f:
        datos=json.load(f)
    return datos

def menu():
    menu = """
    ----------------------------------------|
    1. Listar información.                  |
    2. Contar información.                  |
    3. Buscar o filtrar información         |
    4. Buscar información relacionada.      |
    5. Ejercicio libre.                     |
    6. Ejercicio libre. (2)                 |
    7. Salir                                |
    ----------------------------------------|
    """ 
    print(menu)
    numero=int(input("Elije una de las opciones anteriores: "))
    while numero < 1 or numero > 7:
        print("Debe ser un número de los de la lista")
        numero=int(input("Elije una de las opciones anteriores: "))
    return numero

def listar_informacion(listacines):
    cines=[]
    ubicacion=[]
    telefono=[]
    for cine in listacines.get("cines"):
        cines.append(cine)
    for cine in listacines.get("cines").values():
        ubicacion.append(cine.get("direccion"))
    for cine in listacines.get("cines").values():
        telefono.append(cine.get("telefono"))
    return cines,ubicacion,telefono

def contar_informacion(listacines):
    pelicula=[]
    generos=[]
    for peliculas in listacines.get("peliculas"):
        pelicula.append(peliculas)
    for peliculas in listacines.get("peliculas").values():
        generos.append(peliculas.get("genero"))
    return pelicula,generos

def filtrar_informacion(listacines):
    titulospelis=[]
    director=[]
    anyoestreno=[]
    for peliculas in listacines.get("peliculas").values():
        if peliculas.get("titulo") not in titulospelis:
            titulospelis.append(peliculas.get("titulo"))
    print(','.join(titulospelis))
    peliculateclado=input("Introduce el nombre de la película a consultar: ")
    if peliculateclado not in titulospelis:
        return False,False
    else:
        for peliculas in listacines.get("peliculas").values():
            if peliculas.get("titulo") == peliculateclado:
                director.append(peliculas.get("director"))
                anyoestreno.append(peliculas.get("year"))
    return director,anyoestreno

def buscar_informacion_relacionada(listacines):
    pelisvaloradas=[]
    sinopsis=[]
    valoracion=int(input("Introduce el numero de valoración de la pelicula: "))
    while valoracion < 1 or valoracion > 5:
        print("Debe ser un numero del 1 al 5")
        valoracion=int(input("Introduce el numero de valoración: "))
    for peliculas in listacines.get("peliculas").values():
        if peliculas.get("valoracion") == valoracion:
            pelisvaloradas.append(peliculas.get("titulo"))
            sinopsis.append(peliculas.get("sipnosis"))
    return pelisvaloradas,sinopsis

def mostrar_hora():
    hora=datetime.datetime.now()
    hora_formato=hora.strftime('%H:%M')
    return hora_formato

def ejercicio_libre(listacines):
    generos=[]
    generosplano=[]
    generosunicos=[]
    titulos=[]
    sino=[]
    for peliculas in listacines.get("peliculas").values():
        if peliculas.get("genero") not in generos:
            generos.append(peliculas.get("genero"))
    for lista in generos:
        for elem in lista:
            generosplano.append(elem)
    generosunicos=set(generosplano)
    print(','.join(generosunicos))
    generoteclado=input("Introduce un género de los mostrados anteriormente: ")
    if generoteclado not in generosunicos:
        print("Género no válido, saliendo")
        return False
    else:
        for peliculas in listacines.get("peliculas").values():
            if generoteclado in peliculas.get("genero"):
                titulos.append(peliculas.get("titulo"))
        print(','.join(titulos))
        tituloteclado=input("Introduce el título de la película: ")
        if tituloteclado not in titulos:
            print("Pelicula no válida,saliendo.")
            return False
        else:
            print()
            for peliculas in listacines.get("peliculas").values():
                if tituloteclado == peliculas.get("titulo"):
                    sino.append(peliculas.get("sipnosis"))
            return sino

def ejercicio_libre_sugerido(listacines):
    actores=[]
    actoresplano=[]
    pelisinterviene=[]
    cinemas=[]
    cinesclaves=[]
    for peliculas in listacines.get("peliculas").values():
        if peliculas.get("reparto") not in actores:
            actores.append(peliculas.get("reparto"))
    for elem in actores:
        for actor in elem:
            actoresplano.append(actor)
    print("A continuación se mostrarán una serie de actores, escoja uno: ")
    print(','.join(actoresplano))
    actorteclado=input("Introduce el nombre del actor: ")
    if actorteclado not in actoresplano:
        print("Actor no válido, saliendo")
        return False
    else:
        print()
        for peliculas in listacines.get("peliculas").values():
            if actorteclado in peliculas.get("reparto"):
                pelisinterviene.append(peliculas.get("titulo"))
        print("El actor ha participado en",len(pelisinterviene),"película/s")
        print(','.join(pelisinterviene))
        for peliculas in listacines.get("peliculas").values():
            if actorteclado in peliculas.get("reparto"):
                cinemas.append(peliculas.get("cines"))
                cinesclaves=list(cinemas[0].keys())
        return cinesclaves