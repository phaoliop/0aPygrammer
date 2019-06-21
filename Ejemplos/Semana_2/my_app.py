import argparse

class Alumno():
    facultad = ""

    def __init__(self, nombres, correo, laptop, programacion):
        self.nombres = nombres
        self.correo = correo
        self.laptop = laptop
        self.programacion = programacion

    def __str__(self):
        return "Alumno: " + self.correo

    def __getNombre(self):
        dato = self.nombres
        return dato.split()[0]

    def getNombre2(self, dato1):
        return self.__getNombre()


'''
    FUNCIONES
'''
def leerCSV(ruta):
    archivo = open(ruta, 'r')
    datos = archivo.read()
    archivo.close()
    return datos

def estructurarArchivo(datos):
    lista_alumnos = []
    for linea in datos.split('\n')[1:]:
        dato = linea.split(",")
        alumno = Alumno(nombres=dato[0],
                        correo=dato[1],
                        laptop=dato[2],
                        programacion=dato[4])
        lista_alumnos.append(alumno)

    return lista_alumnos

# CLI Python
def implement_cli():
    parser = argparse.ArgumentParser(description='Programa para obtener datos.')

    parser.add_argument("-v", "--version", help="Get Datos Archivo", action="store_true")
    parser.add_argument("-f","--archivo", help="Ruta de archivo de entrada")

    args = parser.parse_args()

    if args.version:
        print("Obtener datos Archivo - 2019 v0.1")  # 2019 v0.1 Version inicial

    if args.archivo:
        dato = leerCSV(args.archivo)
        lista_alumnos = estructurarArchivo(dato)

        alumno1 = lista_alumnos[0]
        alumno1.facultad = "Sistemas"

        alumno2 = lista_alumnos[1]
        alumno2.facultad = "Software"

        print(alumno1.nombres, ": "+ alumno1.getNombre2(""), alumno1.facultad)
        print(alumno2.nombres, ": "+ alumno2.getNombre2(""), alumno2.facultad)

        pass

    else:
        print("= " *60)
        if not args.archivo:
            print("INFO: Debe ingresar una ruta del archivo.")

if __name__=='__main__':
	implement_cli()