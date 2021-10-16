class Buscaminas:
    __tam = 0
    __tam1 = 0
    __tablero = []
    
    def __init__(self):
        print('¡Nuevo tablero de Buscaminas creado! Por favor elige la dificultad deseada')
        self.__tam1 = input('\n1)Principiante\n2)Avanzado\n\n')
        self.__setDificultad(int(self.__tam1))

    def __setDificultad(self, tam):
        self.__dif = tam
        print()

        if self.__dif == 1:
            self.__tam = 9
            self.__facil()
        elif self.__dif == 2:
            self.__tam = 16
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
        
        self.mostrarTableroAv()

    def getTablero(self):
        return self.__tablero

    def mostrarTablero(self):
        for i in range(0, len(self.__tablero)):
            if (i + 1) % self.__tam1 == 0 and i != 0:
                print(self.__tablero[i])
            else:
                print(self.__tablero[i], end=' ')

    def mostrarTableroAv(self):
        for i in range(0, len(self.__tablero)):
            if (i + 1) % self.__tam1 == 0 and i != 0:
                print(self.__tablero[i])
            elif (i + 1) % self.__tam1 == 1 and i < 160 or i == 0 or ((i + 1) % self.__tam1 > 10 and i > 16):
                print(self.__tablero[i], end='   ')
            else:
                print(self.__tablero[i], end='  ')