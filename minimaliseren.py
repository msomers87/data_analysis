

#invoerwaarden
min_x = 0
max_x = 20
min_y = 0
max_y = 20

def minimalisatie():
    min_pillen = 10**100
    beste_x = 0
    beste_y = 0

    for x in range(min_x, max_x):
      for y in range(min_y, max_y):
      
        if y >= min_y and y <= max_y and 2*x + 3*y >= 18 and x + 3*y >= 12 and 2*x + y >= 8:
            pillen = x + y
            
            if pillen < min_pillen:
                min_pillen = pillen
                beste_x = x
                beste_y = y

    print("Minimaal aantal pillen bij x = " + str(beste_x) + " en y = " + str(beste_y) + ". Het aantal pillen is dan " + str(min_pillen) + ".")

#uitvoer functie
minimalisatie()
