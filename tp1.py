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
    #raiz_actual=medio
    cota_de_error=(interes_mayor-interes_menor)/2

    while((100*cota_de_error/interes_medio)>error_porcentual):
        if (valor_actual_neto(interes_menor)*valor_actual_neto(interes_medio)>0):
            interes_menor=interes_medio
        if (valor_actual_neto(interes_menor)*valor_actual_neto(interes_medio)<0):
            interes_mayor=interes_medio
        interes_medio=(interes_mayor+interes_menor)/2
        cota_de_error=(interes_mayor-interes_menor)/2

    return interes_medio




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


def TP1():
    print(inversion_inicial_en_dolares*45)
    interes_biseccion=biseccion_van(5)
    print("Interes biseccion:",interes_biseccion)
    print("VAN biseccion:", valor_actual_neto(interes_biseccion))

    interes_punto_fijo=punto_fijo_van(0.1, interes_biseccion)
    print("Interes punto fijo:", interes_punto_fijo)
    print("VAN punto fijo:", valor_actual_neto(interes_punto_fijo))
    #https://youtu.be/5kC4_iEXhGc
TP1()
