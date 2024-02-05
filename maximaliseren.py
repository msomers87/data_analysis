
#invoerwaarden
max_kosten = 360
min_x = 0
max_x = 100
min_y = 0
max_y = 75

def maximalisatie(a, b):
    max_winst = 0
    beste_x = 0
    beste_y = 0

    for x in range(min_x, max_x):
        y = (max_kosten - a * x) / b

        if y >= min_y and y <= max_y:
            winst = x + 2 * y

            if winst > max_winst:
                max_winst = winst
                beste_x = x
                beste_y = y

    print("Maximale winst bij x = " + str(beste_x) + " en y = " + str(beste_y) + ". De maximale winst is dan " + str(max_winst) + ".")

#uitvoer functie
maximalisatie(3, 4)



