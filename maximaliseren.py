
#invoerwaarden
min_x = 0
max_x = 16
min_y = 0
max_y = 16

def maximalisatie():
    max_mensen = 0
    beste_x = 0
    beste_y = 0

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):

            if y >= min_y and y <= max_y and 2*x + y <= 16 and 8*x + 5*y <= 80 and 1000*x + 2000*y <= 14000:
                mensen = 50 * x + 25 * y

                if mensen > max_mensen:
                    max_mensen = mensen
                    beste_x = x
                    beste_y = y

    print("Max aantal mensen gebaat bij x = " + str(beste_x) + " en y = " + str(beste_y) + ". Het aantal is dan " + str(max_mensen) + ".")

#uitvoer functie
maximalisatie()



