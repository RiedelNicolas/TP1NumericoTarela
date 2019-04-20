from constant import *




#inversion>0
def valor_actual_neto(inversion, interes, años):
    van = inversion
    for x in range(1,años+1) #ver esto
        van+=( fcf(x)/(1+interes)**x) )

    return

def TP1():

    inversion_inicial_en_dolares=POTENCIA_TOTAL_INSTALADA*COSTO_POTENCIA_A_INSTALAR
