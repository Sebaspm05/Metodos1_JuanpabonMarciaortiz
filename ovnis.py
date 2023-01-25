# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 22:04:09 2022

@author: Sra Yini
"""
def crear_diccionario (llaves_dicts:list, valores_linea: list)-> dict:
    dicccionario_avistamiento = {}
    
    dicccionario_avistamiento[llaves_dicts[0]]= valores_linea[0]
    dicccionario_avistamiento[llaves_dicts[1]]= valores_linea[1]
    dicccionario_avistamiento[llaves_dicts[2]]= valores_linea[2]
    dicccionario_avistamiento[llaves_dicts[4]]= valores_linea[4]
    if valores_linea[5]=="":
        dicccionario_avistamiento[llaves_dicts[5]]= ""
    else:
        dicccionario_avistamiento[llaves_dicts[5]]= float(valores_linea[5])
        
    dicccionario_avistamiento[llaves_dicts[6]]= valores_linea[6]
    dicccionario_avistamiento[llaves_dicts[7]]= valores_linea[7]
    if valores_linea[8]=="":
        dicccionario_avistamiento[llaves_dicts[8]]= ""
    else:
        dicccionario_avistamiento[llaves_dicts[8]]= float(valores_linea[8])
        
    if valores_linea[9]=="":
         dicccionario_avistamiento[llaves_dicts[9]]= ""
    else:
         dicccionario_avistamiento[llaves_dicts[9]]= float(valores_linea[9])
    return dicccionario_avistamiento
 

def avistamientos (archivo:str)-> dict:
 
    archivo = open(archivo,"r",encoding="utf-8")

    llaves_dicts = archivo.readline().strip()
    llaves_dicts = llaves_dicts.split(",")
    diccionario = {}
    valores = archivo.readline().strip()
    
    while len(valores)>0:
        valores_linea = valores.split(",")
        dicccionario_avistamiento = crear_diccionario(llaves_dicts, valores_linea)
        pais = valores_linea[3]
        
        
        if pais not in diccionario:
            lista_avistamiento = []
            diccionario[pais] = lista_avistamiento
            lista_avistamiento.append(dicccionario_avistamiento)
            
        else: 
            diccionario[pais].append(dicccionario_avistamiento)
        
        valores = archivo.readline().strip() 
    return diccionario


def avistamientos_por_fecha (avistamientos:dict,fecha:str)->list:
    
    #obtener lisca con las llaves del diccionario
    llaves = list(avistamientos.keys())
    indice_llaves = 0
    fechas_coincidencia = []
    indice_lista = 0
    
    fecha_buscar1= fecha.replace(" ", "")
    fecha_buscar2 = fecha_buscar1.replace ("-","")
    fecha_buscar = int(fecha_buscar2)
    
    while indice_llaves < len(llaves) and indice_lista <= len(avistamientos[llaves[indice_llaves]]):
        
        fechas = avistamientos[llaves[indice_llaves]][indice_lista]["datetime"]
        fecha1 = fechas.replace(" ", "")
        fecha2 = fecha1.replace(":", "")
        fecha3 = fecha2.replace ("-","")
        fecha_numero = int(fecha3)
        
        #eliminar los valores que equivalen a las horas,minutos y segundos
        fecha_acomparar = fecha_numero //1000000
     
        if fecha_acomparar == fecha_buscar:
            fechas_coincidencia.append(avistamientos[llaves[indice_llaves]][indice_lista])
        
        indice_lista += 1
        
        if indice_lista == len(avistamientos[llaves[indice_llaves]]):
            indice_llaves += 1
            indice_lista = 0
    
        
    return fechas_coincidencia

def avistamientos_entrefechas(avistamientos:dict,fecha_inicial:str,fecha_final:str)->list:
    paises = list(avistamientos.keys())
    indice_paises = 0
    fechas_medias = []
    indice_lista = 0
    
    fecha_inicial1= fecha_inicial.replace(" ", "")
    fecha_inicial2 = fecha_inicial1.replace ("-","")
    fecha_inicial = int(fecha_inicial2)
    
    fecha_final1= fecha_final.replace(" ", "")
    fecha_final2 = fecha_final1.replace ("-","")
    fecha_final = int(fecha_final2)
    
    while indice_paises < len(paises):
        
        if indice_lista < len(avistamientos[paises[indice_paises]]):
        
            fechas = avistamientos[paises[indice_paises]][indice_lista]["datetime"]
            fecha1 = fechas.replace(" ", "")
            fecha2 = fecha1.replace(":", "")
            fecha3 = fecha2.replace ("-","")
            fecha_numero = int(fecha3)
        
            #eliminar los valores que equivalen a las horas,minutos y segundos
            fecha_acomparar = fecha_numero //1000000
    
        
            if fecha_inicial <= fecha_acomparar <= fecha_final:
                fechas_medias.append(avistamientos[paises[indice_paises]][indice_lista])
    
            indice_lista += 1
        
        elif indice_lista == len(avistamientos[paises[indice_paises]]):
            indice_paises += 1
            indice_lista = 0
    return fechas_medias

def avistamientos_por_ciudad (avistamientos:dict)->dict:
    #Sacar lista con las ciudades:
    paises = list(avistamientos.keys())
    diccionario_ciudades = {}
    lista_por_ciudades = []
    indice_avistamiento = 0
    indice_pais = 0
    
    while indice_pais < len(paises):
    
        if indice_avistamiento < len(avistamientos[paises[indice_pais]]):
            ciudad = avistamientos[paises[indice_pais]][indice_avistamiento]["city"]
        
        
            if ciudad not in diccionario_ciudades:
                new_dict = avistamientos[paises[indice_pais]][indice_avistamiento]
                lista_por_ciudades = []
                lista_por_ciudades.append(new_dict)
                diccionario_ciudades[ciudad] = lista_por_ciudades
            
            else: 
                new_dict = avistamientos[paises[indice_pais]][indice_avistamiento]
                diccionario_ciudades[ciudad].append(new_dict)
     
            indice_avistamiento +=1
            
        elif indice_avistamiento == len(avistamientos[paises[indice_pais]]):
            indice_pais += 1
            indice_avistamiento = 0
            
    return diccionario_ciudades



def avistamientos_por_segundos (avistamientos:dict,duracion:str)-> dict :
   duracion = float(duracion)

   diccionario_avistamientos = {}
   
   for pais in avistamientos:
       for avistamiento in avistamientos[pais]:
           duracion_comparar = avistamiento["duration (seconds)"]
           if duracion_comparar > duracion:
             if pais not in diccionario_avistamientos:
                 diccionario_avistamientos[pais] = []
             diccionario_avistamientos[pais].append(avistamiento)
    
   return diccionario_avistamientos


from math import radians, cos, sin, asin, sqrt
def distancia_entre_dos_puntos(lat1: float, lon1: float, lat2: float, lon2: float)-> float:
 lon1 = radians(lon1)
 lon2 = radians(lon2)
 lat1 = radians(lat1)
 lat2 = radians(lat2)
 dif_lon = lon2 - lon1
 dif_lat = lat2 - lat1
 a = sin(dif_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(dif_lon / 2)**2
 c = 2 * asin(sqrt(a))
 return c*6371
     

def avistamientos_dentro (avistamientos:dict,latitud:str,longitud:str,radio:str)->list:
    latitud = float(latitud)
    longitud = float(longitud)
    radio = float(radio)
    lista_dentro = []
    paises = list(avistamientos.keys())
    indice_pais = 0
    indice_avistamiento = 0
    while indice_pais < len(paises):
        if indice_avistamiento < len(avistamientos[paises[indice_pais]]):
            longitud_avistamiento = avistamientos[paises[indice_pais]][indice_avistamiento]["longitude"]
            latitud_avistamiento = avistamientos[paises[indice_pais]][indice_avistamiento]["latitude"]
            distacia = distancia_entre_dos_puntos(latitud, longitud, latitud_avistamiento, longitud_avistamiento)
            if distacia < radio:
                lista_dentro.append(avistamientos[paises[indice_pais]][indice_avistamiento])
            indice_avistamiento += 1
        elif indice_avistamiento == len(avistamientos[paises[indice_pais]]):
            indice_avistamiento = 0
            indice_pais += 1
            
    return lista_dentro


def suficientes_avistamientos (avistamientos:dict,cantidad:str, mes_y_anio:str)->bool:
    cantidad = int(cantidad)
    mes_y_anio_buscar = mes_y_anio.replace("-", "")
    mes_y_anio_buscar = int(mes_y_anio_buscar)
    contador = 0 
    paises = list(avistamientos.keys())
    indice_pais = 0
    indice_avistamiento = 0
    centinela = False

    while indice_pais < len(paises) and centinela == False:
        if indice_avistamiento < len(avistamientos[paises[indice_pais]]):
            fecha =  avistamientos[paises[indice_pais]][indice_avistamiento]["datetime"]
            fecha1 =  fecha.replace(" ", "")
            fecha2 = fecha1.replace(":", "")
            fecha3 = fecha2.replace ("-","")
            fecha_numero = int(fecha3)
            
            fecha_acomparar = fecha_numero //100000000
            
            if fecha_acomparar == mes_y_anio_buscar:
                contador +=1
            
            if contador == cantidad:
                centinela = True
                
            indice_avistamiento += 1
            
        elif indice_avistamiento == len(avistamientos[paises[indice_pais]]):
            indice_avistamiento = 0
            indice_pais += 1
            
    return centinela 

def mayor_y_menor_duracion (avistamientos:dict, pais:str)->dict:
    
    diccionario = {"corto": None,"largo":None}
    indice_avistamiento = 0
    dicc_mayor = avistamientos[pais][indice_avistamiento]
    dicc_menor = avistamientos[pais][indice_avistamiento]
    duracion_menor = avistamientos[pais][indice_avistamiento]["duration (seconds)"]
    duracion_mayor = avistamientos[pais][indice_avistamiento]["duration (seconds)"]
    
    while indice_avistamiento < len(avistamientos[pais]) and indice_avistamiento +1 < len(avistamientos[pais]):
        if duracion_mayor < avistamientos[pais][indice_avistamiento+1]["duration (seconds)"]:
            duracion_mayor = avistamientos[pais][indice_avistamiento+1]["duration (seconds)"]
            dicc_mayor = avistamientos[pais][indice_avistamiento+1]
    
        if duracion_menor > avistamientos[pais][indice_avistamiento+1]["duration (seconds)"]:
            duracion_menor = avistamientos[pais][indice_avistamiento+1]["duration (seconds)"]
            dicc_menor = avistamientos[pais][indice_avistamiento+1]
        indice_avistamiento += 1
        
    
    diccionario["corto"]= dicc_menor
    diccionario["largo"]= dicc_mayor
    
    return diccionario

def avistamientos_por_forma (avistamientos:dict)->dict:
    paises = list(avistamientos.keys())
    diccionario_formas = {}
    indice_avistamiento = 0
    indice_pais = 0
    
    while indice_pais < len(paises):
        
        if indice_avistamiento < len(avistamientos[paises[indice_pais]]):
            forma = avistamientos[paises[indice_pais]][indice_avistamiento]["shape"]
            if forma not in diccionario_formas:
                contador_formas = 0
                contador_formas += 1
                diccionario_formas[forma]= contador_formas
                
            else: 
                diccionario_formas[forma] += 1
                
            indice_avistamiento +=1
        
        elif indice_avistamiento == len(avistamientos[paises[indice_pais]]):
            indice_pais += 1
            indice_avistamiento = 0

        
    return diccionario_formas

def avistamientos_por_cadena (avistamientos:dict, cadena_buscar:str)-> list:
    paises = list(avistamientos.keys())
    indice_avistamiento = 0
    indice_pais = 0
    coincidencias = []
    
    while indice_pais < len(paises):
        if indice_avistamiento < len(avistamientos[paises[indice_pais]]):
            comentario = avistamientos[paises[indice_pais]][indice_avistamiento]["comments"]
            if cadena_buscar in comentario:
                coincidencias.append(avistamientos[paises[indice_pais]][indice_avistamiento])
            indice_avistamiento +=1
            
        elif indice_avistamiento == len(avistamientos[paises[indice_pais]]):
            indice_avistamiento = 0
            indice_pais +=1
    
    return coincidencias


def avistamiento_mayor_cantidad (avistamientos:dict, duracion:str)->dict:
    diccionario_utilizar = avistamientos_por_segundos(avistamientos, duracion)
    diccionario = {"país":"","avistamientos":0}
    if diccionario_utilizar == {}:
        diccionario = diccionario

    else: 
        paises = list(diccionario_utilizar.keys())
        indice_pais = 0
        mayor = len(diccionario_utilizar[paises[indice_pais]])
        pais = paises[indice_pais]
        diccionario = {"país":None,"avistamientos":None}
        while indice_pais < len(paises) and indice_pais+1 < len(paises) :
            if mayor < len(diccionario_utilizar[paises[indice_pais+1]]):
                mayor = len(diccionario_utilizar[paises[indice_pais+1]])
                pais = paises[indice_pais+1]
            indice_pais +=1
            
        diccionario["país"]= pais
        diccionario["avistamientos"]= mayor
    
    return diccionario 



avistamientoss = {"us":[{"city":"ny","state":2,"datetime":"1949-10-10 20:10:10","duration (seconds)":1000.0,"latitude":29.88,"longitude":-97.94,"shape": "circle","comments":"pe"},
                        {"city":"tx", "datetime":"1949-10-10 20:10:10", "duration (seconds)":200.0,"latitude":50.88,"longitude":-97.94,"shape": "square","comments":"pez"}]
                  ,"uk":[{"city":"ld", "datetime":"1949-10-10 20:10:10", "duration (seconds)":100.0,"latitude":45.88,"longitude":-7.94, "shape": "circle","comments":"oka"},
                         {"city":"durman", "datetime":"1949-10-10 20:10:10", "duration (seconds)":1000.0,"latitude":45.88,"longitude":-7.94, "shape": "circle","comments":"ola"},
                         {"city":"yrk","datetime":"1949-10-10 20:10:10","duration (seconds)":100.0,"latitude":21.88,"longitude":-57.94, "shape": "square","comments":"paz"},
                         {"city":"belf","datetime":"1949-10-10 20:10:10","duration (seconds)":100.0,"latitude":21.88,"longitude":-57.94, "shape": "circle","comments":"opa"}]
                  ,"co":[{"city":"bog","datetime":"1949-10-10 20:10:10", "duration (seconds)":200.0,"latitude":9.88,"longitude":-27.94, "shape": "circle","comments":"ola"}]}







        
        
        

    
    