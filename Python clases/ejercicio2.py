class Empleado:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
        self.sueldo=int(input("Ingrese el sueldo: "))
        self.descuento=self.sueldo * 0.035
        self.sueldofinal=self.sueldo - self.descuento
 
 
    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Sueldo: ",self.sueldo)
 
 
    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no
    def pagar_impuestos(self):
        if self.sueldo > 3600000:
            print("El empleado paga impuestos de 3,5% por lo tanto su sueldo final es de: ",self.sueldofinal)
        else:
            print("El empleado no paga impuestos",self.sueldo)
 
# bloque principal
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()
