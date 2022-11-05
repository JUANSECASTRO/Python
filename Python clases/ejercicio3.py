class Alumno:
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.nota=int(input("Ingrese su nota: "))
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Su nota es: ",self.nota)
 
    def aprobacion(self):
        if self.nota > 3:
            print("aprobo")
        else:
            print("no aprobo")
alumno=Alumno()
alumno.mostrar()
alumno.aprobacion()
