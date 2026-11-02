def comp(a, b):
    if a is None or b is None:          #Cuandp las listas a y b estan vacias
        return False                    #Hay que debolver False

    cuadrados = []                      #Lista para almacenar los cuadrados de la lista a

    for numero in a:                    #Por cada numero de la lista
        cuadrados.append(numero ** 2)   #Se añade a l alista cuadrado y se eleva al cuadrado

    cuadrados.sort()                    #Se ordenan los cuadrados
    b.sort()                            #Se ordena la lista b

    return cuadrados == b               #Se comparan las listas y se devuelve True si son iguales y False si no lo son










        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        test.assert_equals(comp(a1, a2), True)
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        test.assert_equals(comp(a1, a2), False)
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
        test.assert_equals(comp(a1, a2), False)