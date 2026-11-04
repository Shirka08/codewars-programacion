def round_by_2_decimal_places(n):
    from decimal import Decimal, ROUND_HALF_UP                  #Decimal permite trabajar con decimales precisos y Round_Half_Up permite establecer tus propias reglas de redondeo
    
    return n.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)  #Permite ajustar el numero,le indicamos que queremos dos decimales, le indicamos la regla de reondeo 