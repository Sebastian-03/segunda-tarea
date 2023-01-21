#EJERCICIO 1
print("Bienvenido al menú interactivo")
while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) pregunta 1
    2) pregunta 2
    3) pregunta 3
    4) Salir""")
    
    opcion = input() # me devuelve un string ''
    if opcion == '1':
       
        n=int(input("Numero de asteriscos por lado: "))
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                 print('* ',end='')
            print()
        

    elif opcion == '2':
        lista=[1,2,3,4,5,6,7,8,9,10]
        for nombre in lista:
            if nombre%2==0:
                print(nombre, "es multiplo de 2")
            else: print(nombre, "no es multiplo de 2")

    elif opcion =='3':
        nombres=["maria","pedro","sebastian"]
        edad=[20,15,17]
        lista=[[nombres,edad]]
        for lista in lista:
            print(lista)

                
    elif opcion =='4':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
