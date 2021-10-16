import random
import os

class Memoria:
    __tam = 0
    __tam1 = 0
    __tablero = []
    __tablero_oculto = []
    __fichasS = ['|', '°', '+', '!', '"', '#', '$', '%']
    __fichasL = ['|', '°', '+', '!', '"', '#', '$', '%', '&', '/', '(', ';', '~', '?', '*', '¿', '@', '^']
    pJugador = 0
    pMaquina = 0
    
    def __init__(self):
        print('¡Nuevo tablero de Memoria creado! Por favor elige la dificultad deseada')
        self.__tam1 = input('\n1)Principiante\n2)Avanzado\n\n')
        self.__setDificultad(int(self.__tam1))

    def __setDificultad(self, tam):
        self.__dif = tam
        print()

        if self.__dif == 1:
            self.__tam = 4
            self.__facil()
        elif self.__dif == 2:
            self.__tam = 6
            self.__dificil()
        else:
            print('Dificultad no existente, elige una de las opciones\n\n')
            self.__setDificultad(int(input('1)Principiante\n2)Avanzado\n\n')))

    def __facil(self):
        print('Dificultad elegida: "Principiante"\nNúmero de casillas: ', self.__tam)

        self.__tam1 = self.__tam + 1

        for i in range(0, self.__tam1):
            for j in range(0, self.__tam1):
                if i == 0 and j == 0:
                    self.__tablero.append('\\')
                    self.__tablero_oculto.append('\\')
                elif i == 0:
                    self.__tablero.append(j)
                    self.__tablero_oculto.append(j)
                elif i != 0 and j == 0:
                    self.__tablero.append(i)
                    self.__tablero_oculto.append(i)
                else:
                    self.__tablero.append('-')
                    self.__tablero_oculto.append('-')

        for i in range(0, len(self.__tablero)):
            if (i + 1) % self.__tam1 == 0 and i != 0:
                print(self.__tablero[i])
            else:
                print(self.__tablero[i], end=' ')
        
        print()

        for i in self.__fichasS:
            if '-' in self.__tablero_oculto and self.__tablero_oculto.count('-') > 2:
                self.casilla = random.randrange(0, 24)
                self.casilla1 = random.randrange(0, 24)

                while self.casilla == 0 or self.casilla1 == 0 or self.casilla == 1 or self.casilla1 == 1 or self.casilla == 2 or self.casilla1 == 2 or self.casilla == 3 or self.casilla1 == 3 or self.casilla == 4 or self.casilla1 == 4 or self.casilla == 5 or self.casilla1 == 5 or self.casilla == 10 or self.casilla1 == 10 or self.casilla == 15 or self.casilla1 == 15 or self.casilla == 20 or self.casilla1 == 20 or self.casilla1 == self.casilla or self.__tablero_oculto[self.casilla] != '-' or self.__tablero_oculto[self.casilla1] != '-':
                    self.casilla = random.randrange(0, 24)
                    self.casilla1 = random.randrange(0, 24)

                self.__tablero_oculto[self.casilla] = i
                self.__tablero_oculto[self.casilla1] = i
            else:
                self.__tablero_oculto[self.__tablero_oculto.index('-')] = i
        
        self.__tablero_oculto[self.__tablero_oculto.index('-')] = self.__fichasS[len(self.__fichasS) - 1]

    def __dificil(self):
        print('Dificultad elegida: "Avanzado"\nNumero de casillas: ', self.__tam)
        
        self.__tam1 = self.__tam + 1

        for i in range(0, self.__tam1):
            for j in range(0, self.__tam1):
                if i == 0 and j == 0:
                    self.__tablero.append('\\')
                    self.__tablero_oculto.append('\\')
                elif i == 0:
                    self.__tablero.append(j)
                    self.__tablero_oculto.append(j)
                elif i != 0 and j == 0:
                    self.__tablero.append(i)
                    self.__tablero_oculto.append(i)
                else:
                    self.__tablero.append('-')
                    self.__tablero_oculto.append('-')
        
        for i in range(0, len(self.__tablero)):
            if (i + 1) % self.__tam1 == 0 and i != 0:
                print(self.__tablero[i])
            else:
                print(self.__tablero[i], end=' ')

        print()

        for i in self.__fichasL:
            if '-' in self.__tablero_oculto and self.__tablero_oculto.count('-') > 4:
                self.casilla = random.randrange(0, 48)
                self.casilla1 = random.randrange(0, 48)

                while self.casilla == 0 or self.casilla1 == 0 or self.casilla == 1 or self.casilla1 == 1 or self.casilla == 2 or self.casilla1 == 2 or self.casilla == 3 or self.casilla1 == 3 or self.casilla == 4 or self.casilla1 == 4 or self.casilla == 5 or self.casilla1 == 5 or self.casilla == 10 or self.casilla1 == 10 or self.casilla == 15 or self.casilla1 == 15 or self.casilla == 20 or self.casilla1 == 20 or self.casilla1 == self.casilla or self.__tablero_oculto[self.casilla] != '-' or self.__tablero_oculto[self.casilla1] != '-':
                    self.casilla = random.randrange(0, 48)
                    self.casilla1 = random.randrange(0, 48)

                self.__tablero_oculto[self.casilla] = i
                self.__tablero_oculto[self.casilla1] = i
            else:
                self.__tablero_oculto[self.__tablero_oculto.index('-')] = i
        
        self.__tablero_oculto[self.__tablero_oculto.index('-')] = self.__fichasL[len(self.__fichasL) - 2]
        self.__tablero_oculto[self.__tablero_oculto.index('-')] = self.__fichasL[len(self.__fichasL) - 1]


    def tirar(self):
        self.y = int(input('Selecciona la columna en la que quieres realizar tu primera eleccion\n'))
        self.x = int(input('Selecciona la fila en la que quieres realizar tu primera eleccion\n'))

        self.tiro = 0
        
        if self.__tam == 4:
            if self.x == 1 and self.y == 1:
                self.tiro = 6
            elif self.x == 1 and self.y == 2:
                self.tiro = 7
            elif self.x == 1 and self.y == 3:
                self.tiro = 8
            elif self.x == 1 and self.y == 4:
                self.tiro = 9

            elif self.x == 2 and self.y == 1:
                self.tiro = 11
            elif self.x == 2 and self.y == 2:
                self.tiro = 12
            elif self.x == 2 and self.y == 3:
                self.tiro = 13
            elif self.x == 2 and self.y == 4:
                self.tiro = 14

            elif self.x == 3 and self.y == 1:
                self.tiro = 16
            elif self.x == 3 and self.y == 2:
                self.tiro = 17
            elif self.x == 3 and self.y == 3:
                self.tiro = 18
            elif self.x == 3 and self.y == 4:
                self.tiro = 19

            elif self.x == 4 and self.y == 1:
                self.tiro = 21
            elif self.x == 4 and self.y == 2:
                self.tiro = 22
            elif self.x == 4 and self.y == 3:
                self.tiro = 23
            elif self.x == 4 and self.y == 4:
                self.tiro = 24
        else:
            if self.x == 1 and self.y == 1:
                self.tiro = 8
            elif self.x == 1 and self.y == 2:
                self.tiro = 9
            elif self.x == 1 and self.y == 3:
                self.tiro = 10
            elif self.x == 1 and self.y == 4:
                self.tiro = 11
            elif self.x == 1 and self.y == 5:
                self.tiro = 12
            elif self.x == 1 and self.y == 6:
                self.tiro = 13

            if self.x == 2 and self.y == 1:
                self.tiro = 15
            elif self.x == 2 and self.y == 2:
                self.tiro = 16
            elif self.x == 2 and self.y == 3:
                self.tiro = 17
            elif self.x == 2 and self.y == 4:
                self.tiro = 18
            elif self.x == 2 and self.y == 5:
                self.tiro = 19
            elif self.x == 2 and self.y == 6:
                self.tiro = 20

            if self.x == 3 and self.y == 1:
                self.tiro = 22
            elif self.x == 3 and self.y == 2:
                self.tiro = 23
            elif self.x == 3 and self.y == 3:
                self.tiro = 24
            elif self.x == 3 and self.y == 4:
                self.tiro = 25
            elif self.x == 3 and self.y == 5:
                self.tiro = 26
            elif self.x == 3 and self.y == 6:
                self.tiro = 17

            if self.x == 4 and self.y == 1:
                self.tiro = 29
            elif self.x == 4 and self.y == 2:
                self.tiro = 30
            elif self.x == 4 and self.y == 3:
                self.tiro = 31
            elif self.x == 4 and self.y == 4:
                self.tiro = 32
            elif self.x == 4 and self.y == 5:
                self.tiro = 33
            elif self.x == 4 and self.y == 6:
                self.tiro = 34

            if self.x == 5 and self.y == 1:
                self.tiro = 36
            elif self.x == 5 and self.y == 2:
                self.tiro = 37
            elif self.x == 5 and self.y == 3:
                self.tiro = 38
            elif self.x == 5 and self.y == 4:
                self.tiro = 39
            elif self.x == 5 and self.y == 5:
                self.tiro = 40
            elif self.x == 5 and self.y == 6:
                self.tiro = 41

            if self.x == 6 and self.y == 1:
                self.tiro = 43
            elif self.x == 6 and self.y == 2:
                self.tiro = 44
            elif self.x == 6 and self.y == 3:
                self.tiro = 45
            elif self.x == 6 and self.y == 4:
                self.tiro = 46
            elif self.x == 6 and self.y == 5:
                self.tiro = 47
            elif self.x == 6 and self.y == 6:
                self.tiro = 48
    
        self.aux = list.copy(self.__tablero)
        self.elem = self.__tablero_oculto[self.tiro]
        self.aux[self.tiro] = self.elem

        for i in range(0, len(self.aux)):
            if (i + 1) % self.__tam1 == 0 and i != 0:
                print(self.aux[i])
            else:
                print(self.aux[i], end=' ')

        self.y = int(input('Selecciona la columna en la que quieres realizar tu segunda eleccion\n'))
        self.x = int(input('Selecciona la fila en la que quieres realizar tu segunda eleccion\n'))

        self.tiro = 0
        
        if self.__tam == 4:
            if self.x == 1 and self.y == 1:
                self.tiro = 6
            elif self.x == 1 and self.y == 2:
                self.tiro = 7
            elif self.x == 1 and self.y == 3:
                self.tiro = 8
            elif self.x == 1 and self.y == 4:
                self.tiro = 9

            elif self.x == 2 and self.y == 1:
                self.tiro = 11
            elif self.x == 2 and self.y == 2:
                self.tiro = 12
            elif self.x == 2 and self.y == 3:
                self.tiro = 13
            elif self.x == 2 and self.y == 4:
                self.tiro = 14

            elif self.x == 3 and self.y == 1:
                self.tiro = 16
            elif self.x == 3 and self.y == 2:
                self.tiro = 17
            elif self.x == 3 and self.y == 3:
                self.tiro = 18
            elif self.x == 3 and self.y == 4:
                self.tiro = 19

            elif self.x == 4 and self.y == 1:
                self.tiro = 21
            elif self.x == 4 and self.y == 2:
                self.tiro = 22
            elif self.x == 4 and self.y == 3:
                self.tiro = 23
            elif self.x == 4 and self.y == 4:
                self.tiro = 24
        else:
            if self.x == 1 and self.y == 1:
                self.tiro = 8
            elif self.x == 1 and self.y == 2:
                self.tiro = 9
            elif self.x == 1 and self.y == 3:
                self.tiro = 10
            elif self.x == 1 and self.y == 4:
                self.tiro = 11
            elif self.x == 1 and self.y == 5:
                self.tiro = 12
            elif self.x == 1 and self.y == 6:
                self.tiro = 13

            if self.x == 2 and self.y == 1:
                self.tiro = 15
            elif self.x == 2 and self.y == 2:
                self.tiro = 16
            elif self.x == 2 and self.y == 3:
                self.tiro = 17
            elif self.x == 2 and self.y == 4:
                self.tiro = 18
            elif self.x == 2 and self.y == 5:
                self.tiro = 19
            elif self.x == 2 and self.y == 6:
                self.tiro = 20

            if self.x == 3 and self.y == 1:
                self.tiro = 22
            elif self.x == 3 and self.y == 2:
                self.tiro = 23
            elif self.x == 3 and self.y == 3:
                self.tiro = 24
            elif self.x == 3 and self.y == 4:
                self.tiro = 25
            elif self.x == 3 and self.y == 5:
                self.tiro = 26
            elif self.x == 3 and self.y == 6:
                self.tiro = 17

            if self.x == 4 and self.y == 1:
                self.tiro = 29
            elif self.x == 4 and self.y == 2:
                self.tiro = 30
            elif self.x == 4 and self.y == 3:
                self.tiro = 31
            elif self.x == 4 and self.y == 4:
                self.tiro = 32
            elif self.x == 4 and self.y == 5:
                self.tiro = 33
            elif self.x == 4 and self.y == 6:
                self.tiro = 34

            if self.x == 5 and self.y == 1:
                self.tiro = 36
            elif self.x == 5 and self.y == 2:
                self.tiro = 37
            elif self.x == 5 and self.y == 3:
                self.tiro = 38
            elif self.x == 5 and self.y == 4:
                self.tiro = 39
            elif self.x == 5 and self.y == 5:
                self.tiro = 40
            elif self.x == 5 and self.y == 6:
                self.tiro = 41

            if self.x == 6 and self.y == 1:
                self.tiro = 43
            elif self.x == 6 and self.y == 2:
                self.tiro = 44
            elif self.x == 6 and self.y == 3:
                self.tiro = 45
            elif self.x == 6 and self.y == 4:
                self.tiro = 46
            elif self.x == 6 and self.y == 5:
                self.tiro = 47
            elif self.x == 6 and self.y == 6:
                self.tiro = 48

        self.elem1 = self.__tablero_oculto[self.tiro]
        self.aux[self.tiro] = self.elem1

        for i in range(0, len(self.aux)):
            if (i + 1) % self.__tam1 == 0 and i != 0:
                print(self.aux[i])
            else:
                print(self.aux[i], end=' ')
        
        if self.elem == self.elem1:
            print('Acertaste, vuelves a escoger')
            self.__tablero = list.copy(self.aux)
            self.pJugador += 1
            if self.revisarTablero() == True:
                self.tirar()
            else:
                return
        else:
            print('No acertaste, turno de la Máquina')

    def tiroMaquina(self):
        self.tiro = 0
        self.tiro1 = 0

        if self.__tam == 4:
            while self.tiro == 0 or self.tiro == 1 or self.tiro == 2 or self.tiro == 3 or self.tiro == 4 or self.tiro == 5 or self.tiro == 10 or self.tiro == 15 or self.tiro == 20:
                self.tiro = random.randrange(0,24)
            while self.tiro1 == 0 or self.tiro1 == 1 or self.tiro1 == 2 or self.tiro1 == 3 or self.tiro1 == 4 or self.tiro1 == 5 or self.tiro1 == 10 or self.tiro1 == 15 or self.tiro1 == 20:
                self.tiro1 = random.randrange(0,24)
        else:
            while self.tiro == 0 or self.tiro == 1 or self.tiro == 2 or self.tiro == 3 or self.tiro == 4 or self.tiro == 5 or self.tiro == 6 or self.tiro == 7 or self.tiro == 14 or self.tiro == 21 or self.tiro == 28 or self.tiro == 35 or self.tiro == 42:
                self.tiro = random.randrange(0,48)
            while self.tiro1 == 0 or self.tiro1 == 1 or self.tiro1 == 2 or self.tiro1 == 3 or self.tiro1 == 4 or self.tiro1 == 5 or self.tiro1 == 6 or self.tiro1 == 7 or self.tiro1 == 14 or self.tiro1 == 21 or self.tiro1 == 28 or self.tiro1 == 35 or self.tiro1 == 42:
                self.tiro1 = random.randrange(0,48)
        
        print()

        self.aux = list.copy(self.__tablero)

        if self.aux[self.tiro] == '-' and self.aux[self.tiro1] == '-':
            self.elem = self.__tablero_oculto[self.tiro]
            self.elem1 = self.__tablero_oculto[self.tiro1]

            self.aux[self.tiro] = self.elem
            print('Primer tiro de la Maquina')

            for i in range(0, len(self.aux)):
                if (i + 1) % self.__tam1 == 0 and i != 0:
                    print(self.aux[i])
                else:
                    print(self.aux[i], end=' ')
            
            self.aux[self.tiro1] = self.elem1
            print('Segundo tiro de la Maquina')

            for i in range(0, len(self.aux)):
                if (i + 1) % self.__tam1 == 0 and i != 0:
                    print(self.aux[i])
                else:
                    print(self.aux[i], end=' ')
            
            if self.elem == self.elem1:
                print('La Maquina acertó, vuelve a tirar')
                self.pMaquina += 1
                self.__tablero = list.copy(self.aux)
                self.tiroMaquina()
            else:
                print('La Maquina no acertó, es tu turno')
        else:
            print('\nTiro de maquina fallido, reintentando tirar\n\n')
    
    def revisarTablero(self):
        return '-' in self.__tablero
    
    def getPuntosJ(self):
        return self.pJugador
    
    def getPuntosM(self):
        return self.pMaquina

    def getTablero(self):
        return self.__tablero

    def mostrarTablero(self):
        for i in range(0, len(self.__tablero)):
            if (i + 1) % self.__tam1 == 0 and i != 0:
                print(self.__tablero[i])
            else:
                print(self.__tablero[i], end=' ')