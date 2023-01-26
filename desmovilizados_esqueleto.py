import pandas as pd

#Requerimiento 0 - Cargar datos
def cargar_datos(ruta_archivo:str)->pd.DataFrame:
    return pd.read_csv(ruta_archivo)

def cargar_coordenadas(nombre_archivo:str)->dict:   
    deptos = {}
    archivo = open(nombre_archivo, encoding="utf8")
    archivo.readline()
    linea = archivo.readline()
    while len(linea) > 0:
        linea = linea.strip()
        datos = linea.split(";")
        deptos[datos[0]] = (int(datos[1]),int(datos[2]))
        linea = archivo.readline()
    return deptos

def crear_matriz(datos:pd.DataFrame)-> tuple:
    #Creación de los diccionarios con los grupos y departamentos para la matriz
    datos = datos[datos["ExGrupo"]!="SIN DATO"]
    datos = datos[datos["ExGrupo"]!="SIN DATO MINDEFENSA"]
    grupos =sorted(datos["ExGrupo"].unique())
    grupos_dict = dict(list(enumerate(grupos)))
    deptos = sorted(datos["DepartamentoDeResidencia"].unique())
    dept_dict = dict(list(enumerate(deptos)))
    #TODO - Crear la matriz
