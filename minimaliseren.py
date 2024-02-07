#invoerwaarden
min_x = 0
max_x = 10

def minimaliseren(a,b):
    min_kosten = 10**100000
    beste_x = 0
    beste_y = 0

    for x in range(0,10):
        y = a - b * x

        if y >= 0:
            kosten = round(x + (8/20) * y, 2)

            if kosten < min_kosten:
                min_kosten = kosten
                beste_x = x 
                beste_y = y 
    
    print("Minimale kosten bij x = " + str(beste_x) + " en y = " + str(beste_y) + ". De minimale kosten zijn dan " + str(min_kosten) + ".")

#uitvoerfunctie
minimaliseren(7,2)

