#Equipo
#Jairo Elias Martinez Morales
#Emmanuel Juan Trujillo Muñoz

def main():
    n =int(input("1: Correr Programa  2: Salir:  "))
    while n != 2:
       print("Ingresa tus datos: ")
       x= input()
       print("Ingresa la potencia deseada: ")
       y = int(input())
       if 7 < 0:
           print("no valido")
       if y == 0:
        print("E")
         
       if y == 1:
        print("Cadena: " +x)
       
       if y == 2:
        print("Cadena: "+ x +" "+ x)
        
       if y == 3:
        print("Cadena: "+ x + " " + x + " " + x)
        
       if y > 3:
        print ("Potencia no aceptada")
       n =int(input("1: Continuar  2: Salir: "))
    
main()
