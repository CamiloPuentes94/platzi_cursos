"""
Se debe modificar el codico para tener un maximo en la
ejecucuin de la sucesion de fibonacci
"""

import time # Importamos la libreria time para darle una espera a alaejecucion del iterators

class FiboIter():
    
    def __init__(self, max = None):
        self.max = max        
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        self.aux = 0
        return self
    
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return  self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        elif self.aux < self.max:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
        else:
            raise StopIteration # De este modo elevamos a la funcion para parar la iteracion
        
if __name__ == '__main__':
    max = int(input("Ingresa el vamos maximo de iteracion en fibonacci: "))
    fibonacci = FiboIter(max)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)