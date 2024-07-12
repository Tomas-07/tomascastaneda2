import random
opc=-1
tabla=[]
a=10
trabajadores={"Juan Perez", "Maria Garcia", " Carlos Lopez", "Ana Martines", "Pedro Rodriguez", "Laura Hernandez", " Miguel Sanchez", "Isabel Gomez", "francisco Diaz"," Elena Fernandez"}
encabezado=["nombre empleado", "sueldo base",  "sueldo liquido"]

def asignar_sueldos():
   
    for nombre in trabajadores:
        plata=random.randint(300000, 2500000)
        print(F"el sueldo del trabajador {nombre} es {plata}")
        tabla.append(nombre)
        tabla.append(plata)
        
   
    

        
    
    
    
def clasificar_sueldos():
    for plata in tabla:
        for nombre in tabla:
            if plata < 800000:
                print(f"los sueldos menores a 800000 son {plata}")
                print(nombre)
                
                if plata>800000 and plata<2000001:
                    print(f"los sueldos entre 800 mil y 2 millones son {plata}")
                    print(nombre)
                    
                if plata>2000000:
                    print(f"los sueldos mayores a 2 millones son {plata}")
                    print(nombre)
            
            


def ver_estadisticas():
    for i in tabla:
       pass
        
        
        
        
def reporte_de_sueldo():
    print(encabezado)

    for nombre in trabajadores:
        for i in tabla:
           
            sueldo_base=i
            sueldo_liquido= sueldo_base
            print(encabezado)
            print(nombre, sueldo_base, sueldo_liquido)


while opc!=5:
    print("1.- asignar sueldos")
    print("2.- clasificar sueldos")
    print("3.- ver estadisticas")
    print("4.- reporte de sueldos")
    print("5.- salir")
    try:
        opc = int(input("ingrese la opcion que desea hacer > "))
    except ValueError:
        print("solo se permiten numeros, intentelo denuevo")
    else:
        match opc:
            case 1:
                asignar_sueldos() 
                
            case 2:
                pass
            
            case 3:
                pass
                
                
            case 4:
                reporte_de_sueldo()
            
            
            case 5:
                print("saliendo del programa.......")
                print("desarrollado por Tomas Castaneda")
                print("rut: 21.894.100-1")