import random

class Tictactoe:
    __tam = 0
    __tam1 = 0
    __tablero = []
    __ficha = 'X'
    __ficha1 = 'O'
    
    def __init__(self):
        print('¡Nuevo tablero de Tic Tac Toe creado! Por favor elige la dificultad deseada')
        self.__tam1 = input('\n1)Principiante\n2)Avanzado\n\n')
        self.__setDificultad(int(self.__tam1))

    def __setDificultad(self, tam):
        self.__dif = tam
        print()

        if self.__dif == 1:
            self.__tam = 3
            self.__facil()
        elif self.__dif == 2:
            self.__tam = 5
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
                elif i == 0:
                    self.__tablero.append(j)
                elif i != 0 and j == 0:
                    self.__tablero.append(i)
                else:
                    self.__tablero.append('-')
        
        self.mostrarTablero()
            
    def __dificil(self):
        print('Dificultad elegida: "Avanzado"\nNumero de casillas: ', self.__tam)
        
        self.__tam1 = self.__tam + 1

        for i in range(0, self.__tam1):
            for j in range(0, self.__tam1):
                if i == 0 and j == 0:
                    self.__tablero.append('\\')
                elif i == 0:
                    self.__tablero.append(j)
                elif i != 0 and j == 0:
                    self.__tablero.append(i)
                else:
                    self.__tablero.append('-')
        
        self.mostrarTablero()
    
    def tirar(self, x, y):
        self.x = int(y)
        self.y= int(x)

        self.tiro = 0
        
        if self.__tam == 3:
            if self.x == 1 and self.y == 1:
                self.tiro = 5
            elif self.x == 1 and self.y == 2:
                self.tiro = 6
            elif self.x == 1 and self.y == 3:
                self.tiro = 7
            elif self.x == 2 and self.y == 1:
                self.tiro = 9
            elif self.x == 2 and self.y == 2:
                self.tiro = 10
            elif self.x == 2 and self.y == 3:
                self.tiro = 11
            elif self.x == 3 and self.y == 1:
                self.tiro = 13
            elif self.x == 3 and self.y == 2:
                self.tiro = 14
            elif self.x == 3 and self.y == 3:
                self.tiro = 15
        else:
            if self.x == 1 and self.y == 1:
                self.tiro = 7
            elif self.x == 1 and self.y == 2:
                self.tiro = 8
            elif self.x == 1 and self.y == 3:
                self.tiro = 9
            elif self.x == 1 and self.y == 4:
                self.tiro = 10
            elif self.x == 1 and self.y == 5:
                self.tiro = 11

            if self.x == 2 and self.y == 1:
                self.tiro = 13
            elif self.x == 2 and self.y == 2:
                self.tiro = 14
            elif self.x == 2 and self.y == 3:
                self.tiro = 15
            elif self.x == 2 and self.y == 4:
                self.tiro = 16
            elif self.x == 2 and self.y == 5:
                self.tiro = 17

            if self.x == 3 and self.y == 1:
                self.tiro = 19
            elif self.x == 3 and self.y == 2:
                self.tiro = 20
            elif self.x == 3 and self.y == 3:
                self.tiro = 21
            elif self.x == 3 and self.y == 4:
                self.tiro = 22
            elif self.x == 3 and self.y == 5:
                self.tiro = 23

            if self.x == 4 and self.y == 1:
                self.tiro = 25
            elif self.x == 4 and self.y == 2:
                self.tiro = 26
            elif self.x == 4 and self.y == 3:
                self.tiro = 27
            elif self.x == 4 and self.y == 4:
                self.tiro = 28
            elif self.x == 4 and self.y == 5:
                self.tiro = 29

            if self.x == 5 and self.y == 1:
                self.tiro = 31
            elif self.x == 5 and self.y == 2:
                self.tiro = 32
            elif self.x == 5 and self.y == 3:
                self.tiro = 33
            elif self.x == 5 and self.y == 4:
                self.tiro = 34
            elif self.x == 5 and self.y == 5:
                self.tiro = 35

        print()

        if self.__tablero[self.tiro] == '-':
            self.__tablero[self.tiro] = self.__ficha1

            print('\nTiro del jugador realizado:\n\n')

            self.mostrarTablero()

        else:
            print('No se puede realizar el tiro, vuelve a intentar\n\n')
            x, y = self.recibirCasilla()
            self.tirar(x, y)
        
    def tiroMaquina(self):
        self.tiro = 0

        if self.__tam == 3:
            while self.tiro == 0 or self.tiro == 1 or self.tiro == 2 or self.tiro == 3 or self.tiro == 4 or self.tiro == 8 or self.tiro == 12:
                self.tiro = random.randrange(0,15)
        else:
            while self.tiro == 0 or self.tiro == 1 or self.tiro == 2 or self.tiro == 3 or self.tiro == 4 or self.tiro == 5 or self.tiro == 6 or self.tiro == 12 or self.tiro == 18 or self.tiro == 24 or self.tiro == 30:
                self.tiro = random.randrange(0,35)
        
        print()

        if self.__tablero[self.tiro] == '-':
            self.__tablero[self.tiro] = self.__ficha

            print('\nTiro de máquina realizado:\n\n')

            self.mostrarTablero()
        else:
            print('\nTiro de maquina fallido, reintentando tirar\n\n')
            self.tiroMaquina()
    
    def revisarTablero(self):
        print()
        if self.__tam == 3:
            if self.__tablero[5] == self.__ficha1 and self.__tablero[6] == self.__ficha1 and self.__tablero[7] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[9] == self.__ficha1 and self.__tablero[10] == self.__ficha1 and self.__tablero[11] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[13] == self.__ficha1 and self.__tablero[14] == self.__ficha1 and self.__tablero[15] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[5] == self.__ficha1 and self.__tablero[9] == self.__ficha1 and self.__tablero[13] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[6] == self.__ficha1 and self.__tablero[10] == self.__ficha1 and self.__tablero[14] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[7] == self.__ficha1 and self.__tablero[11] == self.__ficha1 and self.__tablero[15] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[5] == self.__ficha1 and self.__tablero[10] == self.__ficha1 and self.__tablero[15] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[7] == self.__ficha1 and self.__tablero[10] == self.__ficha1 and self.__tablero[13] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            
            elif self.__tablero[5] == self.__ficha and self.__tablero[6] == self.__ficha and self.__tablero[7] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[9] == self.__ficha and self.__tablero[10] == self.__ficha and self.__tablero[11] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[13] == self.__ficha and self.__tablero[14] == self.__ficha and self.__tablero[15] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[5] == self.__ficha and self.__tablero[9] == self.__ficha and self.__tablero[13] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[6] == self.__ficha and self.__tablero[10] == self.__ficha and self.__tablero[14] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[7] == self.__ficha and self.__tablero[11] == self.__ficha and self.__tablero[15] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[5] == self.__ficha and self.__tablero[10] == self.__ficha and self.__tablero[15] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[7] == self.__ficha and self.__tablero[10] == self.__ficha and self.__tablero[13] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[5] != '-' and self.__tablero[6] != '-' and self.__tablero[7] != '-' and self.__tablero[9] != '-' and self.__tablero[10] != '-' and self.__tablero[11] != '-' and self.__tablero[13] != '-' and self.__tablero[14] != '-' and self.__tablero[15] != '-':
                print('Fin del juego, nadie gana :(')
                return False
            else:
                print('Juego en Marcha')
                return True
        
        else:
            if self.__tablero[7] == self.__ficha1 and self.__tablero[8] == self.__ficha1 and self.__tablero[9] == self.__ficha1 and self.__tablero[10] == self.__ficha1 and self.__tablero[11] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[13] == self.__ficha1 and self.__tablero[14] == self.__ficha1 and self.__tablero[15] == self.__ficha1 and self.__tablero[16] == self.__ficha1 and self.__tablero[17] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[19] == self.__ficha1 and self.__tablero[20] == self.__ficha1 and self.__tablero[21] == self.__ficha1 and self.__tablero[22] == self.__ficha1 and self.__tablero[23] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[25] == self.__ficha1 and self.__tablero[26] == self.__ficha1 and self.__tablero[27] == self.__ficha1 and self.__tablero[28] == self.__ficha1 and self.__tablero[29] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[31] == self.__ficha1 and self.__tablero[32] == self.__ficha1 and self.__tablero[33] == self.__ficha1 and self.__tablero[34] == self.__ficha1 and self.__tablero[35] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[7] == self.__ficha1 and self.__tablero[13] == self.__ficha1 and self.__tablero[19] == self.__ficha1 and self.__tablero[25] == self.__ficha1 and self.__tablero[31] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[8] == self.__ficha1 and self.__tablero[14] == self.__ficha1 and self.__tablero[20] == self.__ficha1 and self.__tablero[26] == self.__ficha1 and self.__tablero[32] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[9] == self.__ficha1 and self.__tablero[15] == self.__ficha1 and self.__tablero[21] == self.__ficha1 and self.__tablero[27] == self.__ficha1 and self.__tablero[33] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[10] == self.__ficha1 and self.__tablero[16] == self.__ficha1 and self.__tablero[22] == self.__ficha1 and self.__tablero[28] == self.__ficha1 and self.__tablero[34] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[11] == self.__ficha1 and self.__tablero[17] == self.__ficha1 and self.__tablero[23] == self.__ficha1 and self.__tablero[29] == self.__ficha1 and self.__tablero[35] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[7] == self.__ficha1 and self.__tablero[14] == self.__ficha1 and self.__tablero[21] == self.__ficha1 and self.__tablero[28] == self.__ficha1 and self.__tablero[35] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            elif self.__tablero[11] == self.__ficha1 and self.__tablero[16] == self.__ficha1 and self.__tablero[21] == self.__ficha1 and self.__tablero[26] == self.__ficha1 and self.__tablero[31] == self.__ficha1:
                print('Fin del juego, gana el Jugador')
                return False
            
            elif self.__tablero[7] == self.__ficha and self.__tablero[8] == self.__ficha and self.__tablero[9] == self.__ficha and self.__tablero[10] == self.__ficha and self.__tablero[11] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[13] == self.__ficha and self.__tablero[14] == self.__ficha and self.__tablero[15] == self.__ficha and self.__tablero[16] == self.__ficha and self.__tablero[17] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[19] == self.__ficha and self.__tablero[20] == self.__ficha and self.__tablero[21] == self.__ficha and self.__tablero[22] == self.__ficha and self.__tablero[23] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[25] == self.__ficha and self.__tablero[26] == self.__ficha and self.__tablero[27] == self.__ficha and self.__tablero[28] == self.__ficha and self.__tablero[29] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[31] == self.__ficha and self.__tablero[32] == self.__ficha and self.__tablero[33] == self.__ficha and self.__tablero[34] == self.__ficha and self.__tablero[35] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[7] == self.__ficha and self.__tablero[13] == self.__ficha and self.__tablero[19] == self.__ficha and self.__tablero[25] == self.__ficha and self.__tablero[31] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[8] == self.__ficha and self.__tablero[14] == self.__ficha and self.__tablero[20] == self.__ficha and self.__tablero[26] == self.__ficha and self.__tablero[32] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[9] == self.__ficha and self.__tablero[15] == self.__ficha and self.__tablero[21] == self.__ficha and self.__tablero[27] == self.__ficha and self.__tablero[33] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[10] == self.__ficha and self.__tablero[16] == self.__ficha and self.__tablero[22] == self.__ficha and self.__tablero[28] == self.__ficha and self.__tablero[34] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[11] == self.__ficha and self.__tablero[17] == self.__ficha and self.__tablero[23] == self.__ficha and self.__tablero[29] == self.__ficha and self.__tablero[35] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[7] == self.__ficha and self.__tablero[14] == self.__ficha and self.__tablero[21] == self.__ficha and self.__tablero[28] == self.__ficha and self.__tablero[35] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[11] == self.__ficha and self.__tablero[16] == self.__ficha and self.__tablero[21] == self.__ficha and self.__tablero[26] == self.__ficha and self.__tablero[31] == self.__ficha:
                print('Fin del juego, gana la Máquina')
                return False
            elif self.__tablero[7] != '-' and self.__tablero[8] != '-' and self.__tablero[9] != '-' and self.__tablero[10] != '-' and self.__tablero[11] != '-' and self.__tablero[13] != '-' and self.__tablero[14] != '-' and self.__tablero[15] != '-' and self.__tablero[16] != '-' and self.__tablero[17] != '-' and self.__tablero[19] != '-' and self.__tablero[20] != '-' and self.__tablero[21] != '-' and self.__tablero[22] != '-' and self.__tablero[23] != '-' and self.__tablero[25] != '-' and self.__tablero[26] != '-' and self.__tablero[27] != '-' and self.__tablero[28] != '-' and self.__tablero[29] != '-' and self.__tablero[31] != '-' and self.__tablero[32] != '-' and self.__tablero[33] != '-' and self.__tablero[34] != '-' and self.__tablero[35] != '-':
                print('Fin del juego, nadie gana :(')
                return False
            else:
                print('Juego en Marcha')
                return True
    
    def getTablero(self):
        return self.__tablero
    
    def mostrarTablero(self):
        for i in range(0, len(self.__tablero)):
            if (i + 1) % self.__tam1 == 0 and i != 0:
                print(self.__tablero[i])
            else:
                print(self.__tablero[i], end=' ')

    def recibirCasilla(self):
        x = input('Ingresa la columna en la que deseas realizar tu tiro: ')
        y = input('Ingresa la fila en la que deseas realizar tu tiro: ')

        return x, y