from constant import *

#inversion>0
def valor_actual_neto(inversion_en_pesos, flujo_de_caja, interes, años):
    van = -inversion_en_pesos
    for año in range(1,años+1):
        van += flujo_de_caja/((1+interes)**año)

    return van

#https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/bisection/
def biseccion_van(error_porcentual):
    #VAN(interes=0)>0
    #VAN(interes=1)<0

    valor_menor=0
    valor_mayor=1
    medio=(valor_mayor+valor_menor)/2
    raiz_actual=medio
    cota_de_error=(valor_mayor-valor_menor)/2

    while((100*cota_de_error/raiz_actual)>error_porcentual)
        if condition:
            pass



def TP1():

    print(valor_actual_neto(inversion_inicial_en_dolares*45, flujo_de_caja, 1, VIDA_UTIL_PROYECTO))

TP1()
