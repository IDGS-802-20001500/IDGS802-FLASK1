
per = 0
tickets = 0
costo = 12
tarjeta = ""
total = 0

def boletos(per, tickets):

    if per == 1 and tickets > 7:
        return "Solo se pueden comprar 7 boletos por persona" 
    elif per == 1 and tickets <= 7:
        return True
    elif per > 1 and tickets == per * 7:
        return True
    else:
        return "El número de boletos no coincide con el número de personas"


def ventaTicket(tarjeta, tickets, per):

    total = costo * tickets * per

    if tickets > 5:
        total = total - (total * 0.15)
    elif tickets > 2 and tickets <= 5:
        total = total -(total * 0.10)
    elif tickets <= 2:
       return total
    
    if tarjeta == "Si":
        total = total - (total * 0.10)
    else:
        return total
    
    return total

