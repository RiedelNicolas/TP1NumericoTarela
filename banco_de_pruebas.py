from tp1 import*

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
