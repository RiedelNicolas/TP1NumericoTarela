from tp1.py import*


def pendiente_secante_van(izquierda, derecha):
    dividendo = valor_actual_neto (derecha)*(derecha - izquierda)
    divisor = valor_actual_neto(derecha) - valor_actual_neto (izquierda)
    return = derecha - dividendo/divisor


def secante_van(izquierda, derecha, cota_error_porcentual):

    error = 100 #inicio en  un valor suficiente para que entre al while
    while( 100*error > cota_error_porcentual ):
        actual = pendiente_secante_van (izquierda, derecha)
        izquierda = derecha
        derecha = actual
        error = abs (actual - derecha)

    return actual
