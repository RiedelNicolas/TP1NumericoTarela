from constant import *

#inversion>0
def valor_actual_neto(interes, inversion_en_pesos=inversion_inicial_en_dolares*45, flujo_de_caja=flujo_de_caja, años=VIDA_UTIL_PROYECTO):
    van = -inversion_en_pesos
    for año in range(1,años+1):
        van += flujo_de_caja/((1+interes)**año)

    return van


def biseccion_van(error_porcentual):
    #VAN(interes=0)>0
    #VAN(interes=1)<0

    interes_menor=0
    interes_mayor=1
    interes_medio=(interes_mayor+interes_menor)/2
    interes_medio_anterior=interes_medio
    cota_de_error=(interes_mayor-interes_menor)/2

    while((100*cota_de_error/interes_medio)>error_porcentual):
        if (valor_actual_neto(interes_menor)*valor_actual_neto(interes_medio)>0):
            interes_menor=interes_medio
        if (valor_actual_neto(interes_menor)*valor_actual_neto(interes_medio)<0):
            interes_mayor=interes_medio
        interes_medio_anterior=interes_medio
        interes_medio=(interes_mayor+interes_menor)/2
        cota_de_error=(interes_mayor-interes_menor)/2

    return interes_medio,interes_medio_anterior




def punto_fijo_van(error_porcentual, interes_inicial):

    interes_actual =  interes_inicial

    interes_siguiente = interes_actual-valor_actual_neto(interes_actual)
    #print("Valor siguiente", interes_siguiente)
    cota_error =  abs (interes_siguiente-interes_actual)
    interes_actual=interes_siguiente
    #print("Error", cota_error)

    while((abs(100*cota_error/interes_siguiente)) > error_porcentual):
        interes_siguiente = interes_actual-valor_actual_neto(interes_actual)
        cota_error =  abs (interes_siguiente-interes_actual)
        interes_actual=interes_siguiente
        #print(cota_error)

    print("Error relativo", abs(100*cota_error/interes_siguiente))

    return interes_siguiente



def pendiente_secante_van(ultimo_interes, anteultimo_interes):
    dividendo = valor_actual_neto(ultimo_interes) - valor_actual_neto (anteultimo_interes)
    divisor = ultimo_interes - anteultimo_interes
    return dividendo/divisor


def secante_van(ultimo_interes, anteultimo_interes, cota_error_porcentual):

    siguiente_interes = ultimo_interes- valor_actual_neto(ultimo_interes)/pendiente_secante_van (ultimo_interes, anteultimo_interes)
    error = abs (siguiente_interes - ultimo_interes)
    anteultimo_interes = ultimo_interes
    ultimo_interes = siguiente_interes

    while(abs(100*error/siguiente_interes) > cota_error_porcentual):
        siguiente_interes = ultimo_interes- valor_actual_neto(ultimo_interes)/pendiente_secante_van (ultimo_interes, anteultimo_interes)
        error = abs (siguiente_interes - ultimo_interes)
        #print(abs(100*error/siguiente_interes))
        anteultimo_interes = ultimo_interes
        ultimo_interes = siguiente_interes

    return siguiente_interes

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
    #https://youtu.be/5kC4_iEXhGc

    #SECANTE

    interes_secante=secante_van(interes_biseccion, interes_biseccion_anterior, 0.1)
    print("Interes secante:", interes_secante)
    print("VAN secante:", valor_actual_neto(interes_secante))


TP1()
