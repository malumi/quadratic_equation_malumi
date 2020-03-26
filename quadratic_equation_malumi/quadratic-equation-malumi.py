import math


def quad_eqtion(a, b, c):
    d = b ** 2 - 4 * a * c  # ruutv6rrandi diskriminant

    if d < 0:  # diskriminant ei saa olla negatiivne
        return "Lahendid puuduvad"
    elif d == 0:  # kui diskriminant v6rdub nulliga, siis on x1 ja x2 v6rdsed
        x = (-b + math.sqrt(d)) / 2 * a
        return f"Antud v6rrandil on x1 ning x2 v6rdsed ning vastus on {x}"
    else:  # x1 ja x2 arvutus, kui diskriminant on positiivne
        x1 = (-b + math.sqrt(d)) / 2 * a
        x2 = (-b - math.sqrt(d)) / 2 * a
        return f"Antud ruutv6rrandi x1 on {x1} ja x2 on {x2}"
