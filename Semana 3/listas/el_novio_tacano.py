def producto_mas_barato(catalogo: dict)->str:
    if not catalogo:
        return "No hay productos para escoger"
    flipped = {}
    for key, value in catalogo.items(): 
        if value not in flipped: 
            flipped[value] = [key] 
        else: 
            flipped[value].append(key)
    menor = min(flipped.keys())
    cheap_prod = sorted(flipped[min(flipped.keys())])
    
    return None if menor > 10000 else cheap_prod[0]
        
    
catalogo = {'pantuflas': 20, 'chicle': 20000, 'coca cola': 25000, 'lenceria': 70000}

r = producto_mas_barato(catalogo)
print(r)
