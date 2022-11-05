class Valores:
    def __init__(self):
        self.numero1=int(input("digite un primer numero: "))
        self.numero2=int(input("digite un segundo numero: "))
    def mostrar(self):
        print("Numero 1: ",self.numero1)
        print("Numero 2: ",self.numero2)

    def suma(self):
        self.suma=self.numero1 + self.numero2
        print("La suma de los dos numeros es: ",self.suma)

    def resta(self):
        self.resta=self.numero1 - self.numero2
        print("La resta de los dos numeros es: ",self.resta)

    def multiplicacion(self):
        self.multiplicacion=self.numero1 * self.numero2
        print("La multiplicacion de los dos numeros es: ",self.multiplicacion)

    def divicion(self):
        self.divicion=self.numero1 / self.numero2
        print("La divicion de los dos numeros es: ",self.divicion)

valor=Valores()
valor.mostrar()
valor.suma()
valor.resta()
valor.multiplicacion()
valor.divicion()
