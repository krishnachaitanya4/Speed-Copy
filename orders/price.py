def get_price_printing(pages,sides,colour,copies):
    if sides == 1 and colour == 0:
        return (pages*1.25)*copies
    elif sides == 2 and colour == 0:
        papers = (pages+1)//2
        return (papers*1.5)*copies
    elif sides == 1 and colour == 1:
        return (pages*10)*copies
    raise ValueError("Irrelevant arguments!!!")

def get_price_3d_printing():
    pass

def get_price_record_printing(pages,copies):
    if pages <= 60:
        return 275.00
    else:
        return 275+((pages-60)*2)

def get_price_spiral_binding(pages,sides,colour,copies):
    p = get_price_printing(pages,sides,colour,copies)
    if pages <= 50:
        return 25 + p
    elif pages <= 100:
        return 35 + p
    elif pages <= 150:
        return 45 + p
    return 55 + p