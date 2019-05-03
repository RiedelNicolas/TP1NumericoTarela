#Alumnos:
#Cambiano Agustín, padrón: 102291
#Riedel Nicolás padrón: 102130


import math
import csv


#CONSTANTES

IMPUESTO_GANANCIAS=0.3
PADRON=102291
COSTO_POTENCIA_A_INSTALAR=1200#usd/kWp instalado
COSTO_ELECTRICIDAD_CONSUMIDA=3.2#$/kWh
COSTO_POTENCIA_CONSUMIDA=610#$/kW.mes
COSTOS_OPERACION=10000#$/año
VIDA_UTIL_PROYECTO=20#años
CAMBIO=45#$/usdCOSTO_POTENCIA_A_INSTALAR
POTENCIA_TOTAL_INSTALADA=30#kWp
HORAS_POR_AÑO=8760
MESES_POR_AÑO=12

inversion_inicial_en_dolares=POTENCIA_TOTAL_INSTALADA*COSTO_POTENCIA_A_INSTALAR
factor_de_uso=(0.18*PADRON)/100000
ahorro_energia=POTENCIA_TOTAL_INSTALADA * HORAS_POR_AÑO * factor_de_uso * COSTO_ELECTRICIDAD_CONSUMIDA
ahorro_potencia=POTENCIA_TOTAL_INSTALADA * 0.3 *COSTO_POTENCIA_CONSUMIDA * MESES_POR_AÑO
ahorros=ahorro_energia+ahorro_potencia

flujo_de_caja= (ahorros-COSTOS_OPERACION)*(1-IMPUESTO_GANANCIAS)
flujo_de_caja_sin_impuestos = (ahorros-COSTOS_OPERACION)

#DOMICILIARIA
POT_INSTALADA_DOM = 1
COSTO_ELECTRICIDAD_DOM = 3.025

inversion_domiciliaria = POT_INSTALADA_DOM * COSTO_POTENCIA_A_INSTALAR * CAMBIO
ahorros_domicilarios = POT_INSTALADA_DOM * HORAS_POR_AÑO * factor_de_uso * COSTO_ELECTRICIDAD_DOM
flujo_de_caja_dom = ahorros_domicilarios


#COMIENZO DE LAS OPERACIONES


#inversion>0
def valor_actual_neto(interes, inversion_en_pesos=inversion_inicial_en_dolares*45, flujo_de_caja=flujo_de_caja, años=VIDA_UTIL_PROYECTO):
    van = -inversion_en_pesos
    for año in range(1,años+1):
        van += flujo_de_caja/((1+interes)**año)

    return van


def van_domiciliario(interes):

        van = -inversion_domiciliaria #en pesos
        for año in range(1,VIDA_UTIL_PROYECTO+1):
            van += flujo_de_caja_dom/((1+interes)**año)

        return van


def funcion_alternativa(x):
    return (x**2)/4-math.sin(x)

def biseccion_con_errores(error_porcentual, funcion=valor_actual_neto):
    #VAN(interes=0)>0
    #VAN(interes=1)<0

    errores=[]

    interes_menor=0
    interes_mayor=1
    interes_medio=(interes_mayor+interes_menor)/2
    interes_medio_anterior=interes_medio
    cota_de_error=(interes_mayor-interes_menor)/2
    errores.append(cota_de_error)

    while((100*cota_de_error/interes_medio)>error_porcentual):
        if (funcion(interes_menor)*funcion(interes_medio)>0):
            interes_menor=interes_medio
        if (funcion(interes_menor)*funcion(interes_medio)<0):
            interes_mayor=interes_medio
        interes_medio_anterior=interes_medio
        interes_medio=(interes_mayor+interes_menor)/2
        cota_de_error=(interes_mayor-interes_menor)/2
        errores.append(cota_de_error)

    print("Error biseccion: ", errores[len(errores)-1])

    return interes_medio,interes_medio_anterior,errores

def biseccion(error_porcentual, funcion=valor_actual_neto):

    interes_medio,interes_medio_anterior,errores=biseccion_con_errores(error_porcentual, funcion)
    return interes_medio,interes_medio_anterior


def punto_fijo_con_errores(error_porcentual, interes_inicial, funcion=valor_actual_neto):

    errores=[]
    interes_actual =  interes_inicial

    interes_siguiente = interes_actual-funcion(interes_actual)
    cota_error =  abs (interes_siguiente-interes_actual)
    errores.append(cota_error)
    interes_actual=interes_siguiente

    while((abs(100*cota_error/interes_siguiente)) > error_porcentual):
        interes_siguiente = interes_actual-funcion(interes_actual)
        cota_error =  abs (interes_siguiente-interes_actual)
        errores.append(cota_error)
        interes_actual=interes_siguiente

    return interes_siguiente,errores

def punto_fijo(error_porcentual, interes_inicial, funcion=valor_actual_neto):

    interes,errores=punto_fijo_con_errores(error_porcentual, interes_inicial, funcion)
    return interes



def pendiente_secante(ultimo_interes, anteultimo_interes, funcion=valor_actual_neto):
    dividendo = funcion(ultimo_interes) - funcion (anteultimo_interes)
    divisor = ultimo_interes - anteultimo_interes
    return dividendo/divisor


def secante_con_errores(ultimo_interes, anteultimo_interes, cota_error_porcentual, funcion=valor_actual_neto):

    errores=[]

    siguiente_interes = ultimo_interes- funcion(ultimo_interes)/pendiente_secante (ultimo_interes, anteultimo_interes, funcion)
    error = abs (siguiente_interes - ultimo_interes)
    errores.append(error)
    anteultimo_interes = ultimo_interes
    ultimo_interes = siguiente_interes

    while(abs(100*error/siguiente_interes) > cota_error_porcentual):
        siguiente_interes = ultimo_interes- funcion(ultimo_interes)/pendiente_secante (ultimo_interes, anteultimo_interes, funcion)
        error = abs (siguiente_interes - ultimo_interes)
        errores.append(error)
        anteultimo_interes = ultimo_interes
        ultimo_interes = siguiente_interes

    print("Error secante: ", errores[len(errores)-1])

    return siguiente_interes,errores

def secante(ultimo_interes, anteultimo_interes, cota_error_porcentual, funcion=valor_actual_neto):
    interes,errores=secante_con_errores(ultimo_interes, anteultimo_interes, cota_error_porcentual, funcion)
    return interes


def imprimir_interes_fijo(error_porcentual, interes):
    print(error_porcentual,"% de error semilla", interes, "resultado: " )
    resultado=punto_fijo(error_porcentual,interes)
    print(resultado)
    print()
    return resultado

def probar_convergencia_punto_fijo():
    print("pruebas de convergencia punto fijo: ")
    tope=int(0.07*(10**7))
    inicio=int(0.06*(10**7))

    for i in range(inicio,(tope),1):
        resultado=imprimir_interes_fijo(0.1,i/ (10000000) )
        if abs(resultado)<0.1:
            print("Empezo a converger en: ", resultado)
            break


def imprimir_interes_secante(error_porcentual,semilla):
    tope=int(1*(10**4))
    inicio=int(0.00*(10**4))

    for i in range(inicio, tope):
        if i/10000==semilla:
            continue
        resultado=secante(semilla, i/10000, error_porcentual)
        print(error_porcentual,"% de error ultima semilla", semilla, "anteultima semilla", i/10000, "resultado: " )
        print(resultado)
        print()

    return resultado

def probar_convergencia_secante():
    print("pruebas de convergencia secante: ")
    tope=int(1*(10**4))
    #inicio=int(0*(10**4))
    #inicio=int(0.276*(10**4))
    inicio=int(0.7*(10**4))
    for i in range(inicio,tope):
        resultado=imprimir_interes_secante(0.00001,i/10000)

def analizar_convergencias():
    probar_convergencia_punto_fijo()
    probar_convergencia_secante()


def convergencia(ultimo_error,error_anterior, anteultimo_error):
    p=math.log(ultimo_error/error_anterior)/math.log(error_anterior/anteultimo_error)
    landa= ultimo_error/(error_anterior**p)

    return p,landa


def exportar_errores(nombre_archivo,errores):
    with open(nombre_archivo+".csv", "w") as archivo_errores:
        writer=csv.writer(archivo_errores)
        listas_errores=map(lambda x:[x, math.log(x)], errores)
        for error in listas_errores:
            writer.writerow(error)




def operar_con_biseccion():
    interes_biseccion, interes_biseccion_anterior=biseccion(5)
    print("Interes biseccion anterior:",interes_biseccion_anterior)
    print("Interes biseccion:",interes_biseccion)
    print("VAN biseccion:", valor_actual_neto(interes_biseccion))

    #ERRORES BISECCION
    interes_biseccion, interes_biseccion_anterior, errores_biseccion=biseccion_con_errores(0.0000001)
    exportar_errores("errores_biseccion",errores_biseccion)

    p_biseccion, landa_van_biseccion=convergencia(errores_biseccion[len(errores_biseccion)-1], errores_biseccion[len(errores_biseccion)-2], errores_biseccion[len(errores_biseccion)-3])
    print("Convergencia biseccion: ", p_biseccion, " con landa van: ", landa_van_biseccion)

    return interes_biseccion, interes_biseccion_anterior


def operar_con_punto_fijo(interes_biseccion):
    interes_punto_fijo=punto_fijo(0.1, interes_biseccion)
    print("Interes punto fijo:", interes_punto_fijo)
    print("VAN punto fijo:", valor_actual_neto(interes_punto_fijo))

    #ERRORES PUNTO FIJO
    interes_punto_fijo, errores_pto_fijo=punto_fijo_con_errores(0.00000001, 1.75, funcion_alternativa)
    exportar_errores("errores_punto_fijo",errores_pto_fijo)

    p_pto_fijo, landa_pto_fijo_biseccion=convergencia(errores_pto_fijo[len(errores_pto_fijo)-1], errores_pto_fijo[len(errores_pto_fijo)-2], errores_pto_fijo[len(errores_pto_fijo)-3])
    print("Convergencia punto fijo: ", p_pto_fijo, " con landa van: ", landa_pto_fijo_biseccion)



def operar_con_secante(interes_biseccion, interes_biseccion_anterior):
    interes_secante=secante(interes_biseccion, interes_biseccion_anterior, 0.1)
    print("Interes secante:", interes_secante)
    print("VAN secante:", valor_actual_neto(interes_secante))

    #ERRORES SECANTE
    interes_secante,errores_secante=secante_con_errores(0.00001,1, 0.00000001)
    exportar_errores("errores_secante",errores_secante)

    p_secante, landa_secante_biseccion=convergencia(errores_secante[len(errores_secante)-1], errores_secante[len(errores_secante)-2], errores_secante[len(errores_secante)-3])
    print("Convergencia secante: ", p_secante, " con landa van: ", landa_secante_biseccion)




def van_inversion_reducida(interes):
    return valor_actual_neto(interes, inversion_inicial_en_dolares*45*0.7)


def van_impuesto_nulo(interes):
    return valor_actual_neto(interes, flujo_de_caja= flujo_de_caja_sin_impuestos)

def van_precio_electricidad_duplicado(interes):
    return valor_actual_neto(interes,flujo_de_caja=(ahorro_energia*2+ahorro_potencia-COSTOS_OPERACION)*(1-IMPUESTO_GANANCIAS))

def van_factor_de_uso_aumentado(interes):
    return valor_actual_neto(interes,flujo_de_caja=(ahorro_energia*(0.2/0.18)+ahorro_potencia-COSTOS_OPERACION)*(1-IMPUESTO_GANANCIAS))

def  van_cinco_anos_sin_impuestos(interes):
    inversion_en_pesos=inversion_inicial_en_dolares*45
    años=VIDA_UTIL_PROYECTO

    van = -inversion_en_pesos
    for año in range(1,años+1):
        if ( año<=5 ) :
            van += flujo_de_caja_sin_impuestos/((1+interes)**año)
        else :
            van += flujo_de_caja/((1+interes)**año)
    return van


def secante_van_modificado(van_modificado):
    ultimo_interes,anteultimo_interes=biseccion(5,van_modificado)
    return secante(ultimo_interes,anteultimo_interes,0.1,van_modificado)


def operar_con_valores_modificados():

    print("Interes con inversion reducida: ", secante_van_modificado(van_inversion_reducida))
    print("Interes con impuesto nulo: ", secante_van_modificado(van_impuesto_nulo))
    print("Interes con precio electricidad duplicado: ", secante_van_modificado(van_precio_electricidad_duplicado))
    print("Interes con factor de uso aumentado: ", secante_van_modificado(van_factor_de_uso_aumentado))
    print("Interes con primeros 5 años sin impuestos", secante_van_modificado(van_cinco_anos_sin_impuestos))
    print("Con precios duplicados ahorro de energia:", ahorro_energia*2)
    print("Con factor de uso aumentado: ", ahorro_energia*(0.2/0.18) )
    print("FCF sin impuestos: ", flujo_de_caja_sin_impuestos)
    print("FCF regular", flujo_de_caja)

    #residencial (punto ocho)
    #utilizo el interes significativo de la secante
    print("Interes VAN domiciliario: ", secante_van_modificado(van_domiciliario))


def TP1():

    print("Alumnos:")
    print("Cambiano Agustín, padrón: 102291")
    print("Riedel Nicolás padrón: 102130")
    print()

    interes_biseccion,interes_biseccion_anterior=operar_con_biseccion()
    operar_con_punto_fijo(interes_biseccion)
    operar_con_secante(interes_biseccion, interes_biseccion_anterior)

    operar_con_valores_modificados()


TP1()
