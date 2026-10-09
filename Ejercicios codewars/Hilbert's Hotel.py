def hilberts_hotel(rooms, people, buses):

    if people != float("inf") and buses != float("inf"):
        movimiento = people * buses
        return [habitacion + movimiento for habitacion in rooms]

    elif people == float("inf") and buses == float("inf"):
        return [habitacion * (habitacion + 1) // 2 for habitacion in rooms]

    elif people == float("inf"):
        return [habitacion * (buses + 1) for habitacion in rooms]

    elif buses == float("inf"):
        return [habitacion * (people + 1) for habitacion in rooms]