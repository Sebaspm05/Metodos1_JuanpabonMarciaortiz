# -*- coding: utf-8 -*-
"""
Created on Wed May 18 13:15:10 2022

@author: aq02047
"""
import pandas as pd
import matplotlib as plt
def cargar_datos_dataframe(archivo:str)->None:
    dataframe = pd.read_csv(archivo)
    return dataframe



def cargar_datos_2 (archivo:str)->None:
    archivo = open(archivo,"r", encoding= "utf-8")
    encabezados = archivo.readline().strip()
    encabezados = encabezados.split(",")
    linea = archivo.readline().strip()
    linea = linea.split(",")
    lista_dics = []
    while linea != "":
        diccionario = {}
        indice = 0
        for dato in linea:
            diccionario[encabezados[indice]]=dato
            indice+=1
        lista_dics.append(diccionario)
        linea = archivo.readline().split(",")
        
    dataframe = pd.DataFrame(lista_dics)
    archivo.close()
    return dataframe

z= cargar_datos_dataframe("estadisticas.csv")
w = z.value_counts()



def division_por_Exgrupo (datos: list)->None:
    grupo_perteneciente = datos["ExGrupo"].value_counts().iloc[0:6]
    total = grupo_perteneciente.sum()
    grupo_perteneciente = grupo_perteneciente.div(total)
    etiquetas = grupo_perteneciente.index.to_list()
    valores = grupo_perteneciente.to_list()
    gg = grupo_perteneciente.plot(kind = "pie", title = "Diagrama de torta según grupo armado", figsize=(8,40))
    labels = []
    for i in range(0,len(etiquetas)):
        labels.append(etiquetas[i]+","+ str(round(valores[i]*100,1))+"%")
    gg.legend( loc='lower left', labels=labels)
    return grupo_perteneciente



def tendecia_por_rango_anios (datos:list, limite_inferior:str,limite_superior)-> None:
    limite_inferior = int(limite_inferior)
    limite_superior = int(limite_superior)
    valores_dentro = datos[(datos["AnioDesmovilizacion"]>= limite_inferior)&(datos["AnioDesmovilizacion"]<=limite_superior)]
    valores_dentro = valores_dentro["AnioDesmovilizacion"].value_counts().sort_index()
    grafica = valores_dentro.plot(kind="line")
    grafica.set_xlabel("Año desmovilización")
    grafica.set_ylabel("Número de desmovilizados")

    return valores_dentro


    
    
def departamento_desmovilizacion (datos:pd.DataFrame,Tipo_de_desmovilización:str)->None:
    datos_por_tipo = datos[(datos["TipoDeDesmovilizacion"]==Tipo_de_desmovilización)]
    filtrado_por_departamento = datos_por_tipo["DepartamentoDeResidencia"].value_counts()
    mayores = filtrado_por_departamento.head()
    grafica = mayores.plot(kind="barh")
    grafica.invert_yaxis()
    grafica.set_ylabel("Departamento de residencia")
    

def hijos_por_sexo (datos:pd.DataFrame)->None:
    filtrado_tiene_hijos = datos[(datos["NumDeHijos"]>0)]
    Nuevo_dataframe = filtrado_tiene_hijos[["NumDeHijos","Sexo"]]
    Agrupamiento = Nuevo_dataframe.groupby("Sexo")
    grafica = Agrupamiento.boxplot(subplots=False)
    grafica.set_ylabel("Número de hijos")
    grafica.set_xlabel("Sexo")
    
print(hijos_por_sexo(z))

def beneficiados (datos:pd.DataFrame)->None:
    filtrado_beneficiados = datos[(datos["BeneficioTRV"]=="Sí")|
                                  (datos["BeneficioFA"]=="Sí")|
                                  (datos["BeneficioFPT"]=="Sí")|
                                  (datos["BeneficioPDT"]=="Sí")|
                                  (datos["DesembolsoBIE"]=="Sí")]
    ocupacion = filtrado_beneficiados["OcupacionEconomica"].value_counts().sort_index()
    grafica = ocupacion.plot(kind="bar")
    grafica.set_xlabel("Ocupación Económica")
