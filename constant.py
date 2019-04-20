IMPUESTO_GANANCIAS=0.3
PADRON=102291
COSTO_POTENCIA_A_INSTALAR=1200#usd/kWp instalado
COSTO_ELECTRICIDAD_CONSUMIDA=3.2#$/kWh
COSTO_POTENCIA_CONSUMIDA=610#$/kW.mes
COSTOS_OPERACION=10000#$/año
VIDA_UTIL_PROYECTO=20#años
CAMBIO=45#$/usd
POTENCIA_TOTAL_INSTALADA=30#kWp
HORAS_POR_AÑO=8760
MESES_POR_AÑO=12

inversion_inicial_en_dolares=POTENCIA_TOTAL_INSTALADA*COSTO_POTENCIA_A_INSTALAR
factor_de_uso=(0.18*PADRON)/100000
ahorro_energia=POTENCIA_TOTAL_INSTALADA * HORAS_POR_AÑO * factor_de_uso * COSTO_ELECTRICIDAD_CONSUMIDA
ahorro_potencia=POTENCIA_TOTAL_INSTALADA * 0.3 *COSTO_POTENCIA_CONSUMIDA * MESES_POR_AÑO
ahorros=ahorro_energia+ahorro_potencia

flujo_de_caja= (ahorros-COSTOS_OPERACION)*(1-IMPUESTO_GANANCIAS)
