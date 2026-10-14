def zombie_shootout(zombies, distance, ammo):
    shot = 0

    while zombies > 0:
        if distance <= 0:
            return "You shot {} zombies before being eaten: overwhelmed.".format(shot)
        zombies -= 1
        ammo -= 1
        shot += 1
        distance -= 0.5

        if zombies == 0:
            return "You shot all {} zombies.".format(shot)
        elif distance <= 0:
            return "You shot {} zombies before being eaten: overwhelmed.".format(shot)
        elif ammo == 0:
            return "You shot {} zombies before being eaten: ran out of ammo.".format(shot)