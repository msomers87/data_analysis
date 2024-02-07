
#invoerwaarden
min_x = 0
max_x = 5
min_y = 0
max_y = 5

def maximalisatie():
    max_winst = 0
    beste_x = 0
    beste_y = 0

    for x in range(min_x, max_x):
        y = 7 - x

        if y >= min_y and y <= max_y and x + y <= 7:
            y = 5.5 - 0.5 * x
            
            if y >= min_y and y <= max_y and x + y <= 7 and x + 2 * y <= 11:
                winst = 200 * x + 300 * y

                if winst > max_winst:
                    max_winst = winst
                    beste_x = x
                    beste_y = y

    print("Maximale winst bij x = " + str(beste_x) + " en y = " + str(beste_y) + ". De maximale winst is dan " + str(max_winst) + ".")

#uitvoer functie
maximalisatie()



