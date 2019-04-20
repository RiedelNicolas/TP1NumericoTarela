from constant import *




#inversion>0
def valor_actual_neto(inversion, flujo_de_caja, interes, años):

    

    return

def TP1():

    inversion_inicial_en_dolares=POTENCIA_TOTAL_INSTALADA*COSTO_POTENCIA_A_INSTALAR
    factor_de_uso=(0.18*PADRON)/100000
    ahorro_energia=POTENCIA_TOTAL_INSTALADA * HORAS_POR_AÑO * factor_de_uso * COSTO_ELECTRICIDAD_CONSUMIDA
    ahorro_potencia=POTENCIA_TOTAL_INSTALADA * 0.3 *COSTO_POTENCIA_CONSUMIDA * MESES_POR_AÑO
    ahorros=ahorro_energia+ahorro_potencia

    flujo_de_caja= (ahorros-COSTOS_OPERACION)*(1-IMPUESTO_GANANCIAS)
