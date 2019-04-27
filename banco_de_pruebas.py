from tp1 import*

def imprimir_interes_fijo(error_porcentual, interes):

    print(error_porcentual,"% de error semilla", interes, "resultado: " )
    resultado=punto_fijo(error_porcentual,interes)
    print(resultado)
    print()
    return resultado

def probar_convergencia_punto_fijo():
    print("pruebas de convergencia punto fijo: ")
    """imprimir_interes_fijo(0.1,0)
    imprimir_interes_fijo(0.1,0.1)
    imprimir_interes_fijo(0.1,0.2)
    imprimir_interes_fijo(0.1,0.3)
    imprimir_interes_fijo(0.1,0.4)
    imprimir_interes_fijo(0.1,0.5)
    imprimir_interes_fijo(0.1,0.05678)
    imprimir_interes_fijo(0.1,0.06)
    imprimir_interes_fijo(0.1,0.0621)
    imprimir_interes_fijo(0.1,0.0621869)
    imprimir_interes_fijo(0.1,0.06218692500459636)
    imprimir_interes_fijo(0.1,0.067899)
    """

    #tope = 10**6
    tope=int(0.07*(10**7))
    inicio=int(0.06*(10**7))

    for i in range(inicio,(tope),1):
        resultado=imprimir_interes_fijo(0.1,i/ (10000000) )
        if abs(resultado)<0.1:
            print("Empezo a converger en: ", resultado)
            break



def imprimir_interes_secante(error_porcentual,semilla):

    #ultimo_interes,anteultimo_interes=biseccion_van(5)

    tope=int(1*(10**4))
    #inicio=int(0.06*(10**7))
    inicio=int(0.00*(10**4))

    for i in range(inicio, tope):

        if i/10000==semilla:
            continue

        resultado=secante(semilla, i/10000, error_porcentual)
        print(error_porcentual,"% de error ultima semilla", semilla, "anteultima semilla", i/10000, "resultado: " )
        print(resultado)
        print()


    #resultado=secante(semilla, ultimo_interes, error_porcentual)
    return resultado


def probar_convergencia_secante():
    print("pruebas de convergencia secante: ")
    #tope = 10**6
    tope=int(1*(10**4))
    #inicio=int(0.06*(10**7))
    inicio=int(0*(10**4))

    for i in range(inicio,tope):
        resultado=imprimir_interes_secante(0.00000001,i/10000)
        #if abs(resultado)<0.1:
            #print("Empezo a converger en: ", resultado)
            #break




#probar_convergencia_punto_fijo()
probar_convergencia_secante()
