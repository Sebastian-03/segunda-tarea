#EJERCICIO 2


print("¿Que busca?")
biblioteca={
    'categorias':['terror','drama','suspenso','comedia'],
    'nombres':['el decameron','la odisea','las mil y una noche','la iliada'],
    'autores':['giovani bocaccio','ana frank','homero','dante aligueri'],
    'usuarios':['sebastian','maria','valentina','sergio' ]}
while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) categoria de libros
    2) nombres de libros
    3) autores
    4) Estado del libro""")
    
    opcion = input() # me devuelve un string ''
    if opcion == '1':

       print(biblioteca['categorias'])

    elif opcion == '2':
      print(biblioteca['nombres'])

    elif opcion =='3':
      print(biblioteca['autores'])
                
    elif opcion =='4':
      ibrosSinAsignar=biblioteca["nombresLibros"]
      librosPorAsignar=input("¿Qué libro desea asignar?: ")
      if librosPorAsignar in librosSinAsignar:
        accionLibro=input("Ingrese el estado por asignar: ")
        prestado="prestado"
        disponible="disponible"
        if accionLibro==prestado:
         biblioteca["Libros Prestados"]=librosPorAsignar
         print(biblioteca)
        elif accionLibro==disponible:
          biblioteca["Libros Disponibles"]=librosPorAsignar
          print(biblioteca)
        else:
          print("Comando desconocido")
      else:
       print("Este libro no existe.")

      break




