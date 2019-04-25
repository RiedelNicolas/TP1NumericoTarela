#!/usr/bin/env python
import math
from constant import *
#from decimal import *
#from matplotlib.pyplot import *

#inversion>0
def valor_actual_neto(interes, inversion_en_pesos=inversion_inicial_en_dolares*45, flujo_de_caja=flujo_de_caja, años=VIDA_UTIL_PROYECTO):
    van = -inversion_en_pesos
    for año in range(1,años+1):
        van += flujo_de_caja/((1+interes)**año)

    return van


def biseccion_van_con_errores(error_porcentual):
    #VAN(interes=0)>0
    #VAN(interes=1)<0

    errores=[]

    interes_menor=0
    interes_mayor=1
    interes_medio=(interes_mayor+interes_menor)/2
    interes_medio_anterior=interes_medio
    cota_de_error=(interes_mayor-interes_menor)/2
    errores.append(cota_de_error)
    #cota_de_error_previa=cota_de_error

    while((100*cota_de_error/interes_medio)>error_porcentual):
        if (valor_actual_neto(interes_menor)*valor_actual_neto(interes_medio)>0):
            interes_menor=interes_medio
        if (valor_actual_neto(interes_menor)*valor_actual_neto(interes_medio)<0):
            interes_mayor=interes_medio
        interes_medio_anterior=interes_medio
        interes_medio=(interes_mayor+interes_menor)/2
        #cota_de_error_previa=cota_de_error
        cota_de_error=(interes_mayor-interes_menor)/2
        errores.append(cota_de_error)

    return interes_medio,interes_medio_anterior,errores

def biseccion_van(error_porcentual):

    interes_medio,interes_medio_anterior,errores=biseccion_van_con_errores(error_porcentual)
    return interes_medio,interes_medio_anterior


def punto_fijo_van_con_errores(error_porcentual, interes_inicial):

    errores=[]
    interes_actual =  interes_inicial

    interes_siguiente = interes_actual-valor_actual_neto(interes_actual)
    cota_error =  abs (interes_siguiente-interes_actual)
    errores.append(cota_error)
    #cota_error_previa=cota_error
    interes_actual=interes_siguiente

    while((abs(100*cota_error/interes_siguiente)) > error_porcentual):
        interes_siguiente = interes_actual-valor_actual_neto(interes_actual)
        #cota_error_previa=cota_error
        cota_error =  abs (interes_siguiente-interes_actual)
        errores.append(cota_error)
        interes_actual=interes_siguiente

    return interes_siguiente,errores

def punto_fijo_van(error_porcentual, interes_inicial):

    interes,errores=punto_fijo_van_con_errores(error_porcentual, interes_inicial)
    return interes



def pendiente_secante_van(ultimo_interes, anteultimo_interes):
    dividendo = valor_actual_neto(ultimo_interes) - valor_actual_neto (anteultimo_interes)
    divisor = ultimo_interes - anteultimo_interes
    return dividendo/divisor


def secante_van_con_errores(ultimo_interes, anteultimo_interes, cota_error_porcentual):

    errores=[]

    siguiente_interes = ultimo_interes- valor_actual_neto(ultimo_interes)/pendiente_secante_van (ultimo_interes, anteultimo_interes)
    error = abs (siguiente_interes - ultimo_interes)
    #error_previo=error
    errores.append(error)
    anteultimo_interes = ultimo_interes
    ultimo_interes = siguiente_interes

    while(abs(100*error/siguiente_interes) > cota_error_porcentual):
        siguiente_interes = ultimo_interes- valor_actual_neto(ultimo_interes)/pendiente_secante_van (ultimo_interes, anteultimo_interes)
        #error_previo=error
        error = abs (siguiente_interes - ultimo_interes)
        errores.append(error)
        anteultimo_interes = ultimo_interes
        ultimo_interes = siguiente_interes

    return siguiente_interes,errores

def secante_van(ultimo_interes, anteultimo_interes, cota_error_porcentual):

    interes,errores=secante_van_con_errores(ultimo_interes, anteultimo_interes, cota_error_porcentual)
    return interes


def convergencia(ultimo_error,error_anterior, anteultimo_error):

    #return round(math.log(ultimo_error/error_anterior)/math.log(error_anterior/anteultimo_error))
    return math.log(ultimo_error/error_anterior)/math.log(error_anterior/anteultimo_error)


def TP1():
    print(inversion_inicial_en_dolares*45)

    #BISECCION

    interes_biseccion, interes_biseccion_anterior=biseccion_van(5)
    print("Interes biseccion anterior:",interes_biseccion_anterior)
    print("Interes biseccion:",interes_biseccion)
    print("VAN biseccion:", valor_actual_neto(interes_biseccion))

    #PUNTO FIJO

    interes_punto_fijo=punto_fijo_van(0.1, interes_biseccion)
    print("Interes punto fijo:", interes_punto_fijo)
    print("VAN punto fijo:", valor_actual_neto(interes_punto_fijo))

    #SECANTE

    interes_secante=secante_van(interes_biseccion, interes_biseccion_anterior, 0.1)
    print("Interes secante:", interes_secante)
    print("VAN secante:", valor_actual_neto(interes_secante))


    #ERRORES BISECCION
    interes_biseccion, interes_biseccion_anterior, errores_biseccion=biseccion_van_con_errores(0.0000001)
    #print(errores_biseccion)

    #ERRORES PUNTO FIJO

    #poner una semilla que converja
    interes_punto_fijo, errores_pto_fijo=punto_fijo_van_con_errores(0.2, interes_biseccion)
    #print(errores_pto_fijo)

    #ERRORES SECANTE
    #interes_biseccion, interes_biseccion_anterior, errores_biseccion=biseccion_van_con_errores(70)
    #interes_secante,errores_secante=secante_van_con_errores(interes_biseccion, interes_biseccion_anterior, 0.0000000000001)
    interes_secante,errores_secante=secante_van_con_errores(0.05, 0.9, 0.0000000000001)
    print(errores_secante)

    p_biseccion=convergencia(errores_biseccion[len(errores_biseccion)-1], errores_biseccion[len(errores_biseccion)-2], errores_biseccion[len(errores_biseccion)-3])
    print("Convergencia biseccion: ", p_biseccion)

    p_pto_fijo=convergencia(errores_pto_fijo[len(errores_pto_fijo)-1], errores_pto_fijo[len(errores_pto_fijo)-2], errores_pto_fijo[len(errores_pto_fijo)-3])
    print("Convergencia punto fijo: ", p_pto_fijo)

    p_secante=convergencia(errores_secante[len(errores_secante)-1], errores_secante[len(errores_secante)-2], errores_secante[len(errores_secante)-3])
    print("Convergencia secante: ", p_secante)


TP1()
