from F_JsonFabio import * 
import time

listacines=leer_json("cines.json")

numero=menu()
while numero != 7:
    #Ejercicio 1
    if numero == 1:
        cines,ubicacion,telefonos=listar_informacion(listacines)
        print("Se encuentran los siguientes cines: ")
        time.sleep(1)
        for cine,ubicacion,telefono in zip(cines,ubicacion,telefonos):
            print("\nCine:",cine,"\nUbicación:",ubicacion,"\nTeléfono:",telefono)

    #Ejercicio 2
    if numero == 2:
        pelis,generos=contar_informacion(listacines)
        print("La cantidad de peliculas almacenadas es: ",len(pelis))
        time.sleep(1)
        for peli,genero in zip(pelis,generos):
           print("\nTítulo:",peli,"\nGénero/s:",','.join(genero))

    #Ejercicio 3
    if numero == 3:
        director,anyoestreno=filtrar_informacion(listacines)
        if director == False and anyoestreno == False:
            print("Película no encontrada")
        else:
           print("\nDirector:",director[0][0],"\nAño de estreno:",anyoestreno[0])
    #Ejercicio4
    if numero == 4:
        titulopeli,resumen=buscar_informacion_relacionada(listacines)
        print("La cantidad de peliculas con esta valoracion es:",len(titulopeli))
        time.sleep(1)
        for peli,sinopsis in zip(titulopeli,resumen):
           print("\nTítulo:",peli,"\nSinopsis:",sinopsis)
    #Ejercicio 5        
    if numero == 5:
        sino=ejercicio_libre(listacines)
        if sino == False:
            print()
        else:
            print("Sinopsis:",sino[0])
    #Ejercicio 6 sugerencia
    if numero == 6:
        cinesclaves=ejercicio_libre_sugerido(listacines)
        if cinesclaves == False:
            print()
        else:
            print("Puedes ver esta película en los siguientes cines:")
            print(','.join(cinesclaves))
    numero=menu()
if numero == 7:
    print("Saliendo.")