import os
class Tienda:
    def __init__(self):
        self.dinero_inicial = 500
        self.pocion=1
        self.superpocion=1
        self.hiperpocion=1
        self.restaurar=1
        self.pokeball=0
        self.superball=0
        self.ultraball=0
        self.masterball=0
    def dinero(self,N):
        if N >0 and N <=10:
            self.dinero_inicial += 200
        elif N >10 and N <=30:
            self.dinero_inicial +=500
        elif N >30 and N <=60:
            self.dinero_inicial +=1000
        elif N >60 and N <=80:
            self.dinero_inicialo +=2000
        elif N >80 and N <=100:
            self.dinero_inicial +=10000
        else:
            print('error')
        return  self.dinero_inicial    
    def tienda(self):
        
        os.system('cls')
        while True:
            print('-----Bienvenido(a) a la tienda Pokémon---- \n ')
            print('1. Objetos curativos ')
            print('2. Tipos de Poké Ball ')
            print('3. salir de la tienda')
            opcion = int(input('Eliga una opcion: '))
            if opcion == 1:
                os.system('cls')
                print('¿Que objeto curativo desea comprar? \n')
                print('1. POCIÓN: +20 puntos de salud - precio Q 300.00')
                print('2. SUPERPOCIÓN: +50 puntos de salud - precio Q 700.00')
                print('3. HIPERPOCIÓN: +200 puntos de salud - precio Q 1,200.00')
                print('4. RESTAURAR TODO: Vida completa - precio Q 3,000.00')
                print('5. Salir')
                opcion = int(input('Seleccione una opción '))
                if opcion == 1:
                    if self.dinero_inicial >= 300:
                        os.system('cls')
                        print('Desea comprar la POCIÓN ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opción. '))
                        if opcion == 1:
                            self.pocion+=1
                            self.dinero_inicial -= 300
                        elif opcion == 2:
                            print('regresando al menú....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 2:
                    if self.dinero_inicial >= 700:
                        os.system('cls')
                        print('Desea comprar la SUPERPOCIÓN ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opción. '))
                        
                        if opcion == 1:
                            self.dinero_inicial -= 700
                            self.superpocion+=1
                        elif opcion == 2:
                            print('regresando al menú....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 3:
                    if self.dinero_inicial >= 1200:
                        os.system('cls')
                        print('Desea comprar la HIPERPOCIÓN ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opción. '))
                        
                        if opcion == 1:
                            self.dinero_inicial -=1200
                            self.hiperpocion+=1
                        elif opcion == 2:
                            print('regresando al menú....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 4:
                    if self.dinero_inicial >= 3000:
                        os.system('cls')
                        print('Desea comprar la RESTAURAR TODO?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opción. '))
                        
                        if opcion == 1:
                            self.dinero_inicial -=3000
                            self.restaurar+=1
                        elif opcion == 2:
                            print('regresando al menú....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 5:
                    print("\n Saliendo...\n")
                    break
                else:
                    continue
            elif opcion == 2:
                os.system('cls')
                print('¿Que tipo de Poké Ball desea comprar? \n')

                print('1. POKÉBALL: proporción de captura: 1 - precio Q 200.00')
                print('2. SUPERBALL: Proporcion de captura: 1.5 - precio Q 600.00')
                print('3. ULTRABALL: proporción de captura: 2 - precio Q 1,200.00')
                print('4. MASTERBALL: proporción de captura: 255 - precio Q 100,000.00')
                print('5. Salir')
                opcion = int(input('Seleccione una opción '))
                if opcion == 1:
                    if self.dinero_inicial >= 200:
                        os.system('cls')
                        print('Desea comprar la POKÉBALL ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opción. '))
                        if opcion == 1:
                            self.pokeball+=1
                            self.dinero_inicial  -=200
                        elif opcion == 2:
                            print('regresando al menú....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 2:
                    if self.dinero_inicial >= 600:
                        os.system('cls')
                        print('Desea comprar la SUPERBALL ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opción. '))
                        if opcion == 1:
                            self.dinero_inicial -=600
                            self.superball+=1
                        elif opcion == 2:
                            print('regresando al menú....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 3:
                    if self.dinero_inicial >= 1200:
                        os.system('cls')
                        print('Desea comprar la ULTRABALL ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opción. '))
                        if opcion == 1:
                            self.ultraball+=1
                            self.dinero_inicial -=1200
                        elif opcion == 2:
                            print('regresando al menú....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 4:
                    if self.dinero_inicial >= 100000:
                        os.system('cls')
                        print('Desea comprar la MASTERBALL ?')
                        print('1. SI \n2. NO ')
                        opcion = int(input('Elija una opción. '))
                        if opcion == 1:
                            self.dinero_inicial -= 100000
                            self.masterball+=1
                        elif opcion == 2:
                            print('regresando al menú....\n')
                            break
                        else:
                            continue
                    else:
                        print('NO DISPONE DE SUFICIENTE DINERO')
                elif opcion == 5:
                    print('\n Saliendo...\n')
                    break
                else:
                    continue
            elif opcion == 3:
                print("\n Saliendo...\n")
                break
            else:
                continue
       