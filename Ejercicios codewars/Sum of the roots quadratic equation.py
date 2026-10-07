def roots(a, b, c):
    import math
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return None
    if discriminante > 0:
        x1 = ((-b + math.sqrt(discriminante)) / (2*a))
        x2 = ((-b - math.sqrt(discriminante)) / (2*a))
        return round(x1 + x2, 2)
    if discriminante == 0:   
        raiz= -b / (2*a)
        return round (raiz + raiz,2)