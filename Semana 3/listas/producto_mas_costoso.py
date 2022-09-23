def producto_mas_costoso(carrito_compras: dict)->str:
    if not carrito_compras:
        return "No hay productos en el carrito"
    flipped = {}
    for key, value in carrito_compras.items(): 
        if value not in flipped: 
            flipped[value] = [key] 
        else: 
            flipped[value].append(key)
    cheap_prod = sorted(flipped[max(flipped.keys())])
    
    return cheap_prod[0]


catalogo = {'pantuflas': 20, 'chicle': 20000, 'coca cola': 25000, 'lenceria': 70000}

r = producto_mas_costoso(catalogo)
print(r)
