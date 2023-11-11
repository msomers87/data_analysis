#Lineair regression model for bouncy balls.
#In this code there will be searched for a model (y = ax + b) 
#to predict the height of a bouncy ball based on the width of the ball.
#Other variables like force, speed or height at start are not included in this model. 


#Input variables:
    #Width is width of bouncy ball. 
    #Datapoints are points (width, height) found in a test with a sample of bouncy balls.
width = 6
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

#Input for lineair regression model:
    #Decimal_places will determine the number of decimal places for slope (a) and intercept (b) in the model. 
    #The ranges will determine the range of possible as en bs in the model.
decimal_places = 3
minimal_range_a = -1000
maximal_range_a = 1000
minimal_range_b = -2000
maximal_range_b = 2000

#Function for lineair formula, a = slope, b = intercept.
def get_y(a,b,x):
    y = a*x + b
    return y

#Function for calculating error for single point (x,y).
def calculate_error(a,b,point):
    x_point = point[0]
    y_point = point[1]
    y_value = get_y(a,b,x_point)
    return abs(y_value - y_point)

#Function for calculating total of errors with set of points(x,y).
def calculate_all_error(a, b, points):
    errors = 0
    for point in points:
        errors += calculate_error(a, b, point)
    return errors

#Generate multiple possible as en bs for model.  
possible_as = [slope / pow(10, decimal_places) for slope in range(minimal_range_a, maximal_range_a)]
possible_bs = [intercept / pow(10, decimal_places) for intercept in range(minimal_range_b, maximal_range_b)]

#Retrieve best a en b for model with the smallest error.
smallest_error = float("inf")
best_a = 0
best_b = 0

for a in possible_as:
    for b in possible_bs:
        current_error = calculate_all_error(a,b,datapoints)
        if current_error < smallest_error:
            best_a = a
            best_b = b
            smallest_error = current_error

#best values for model
print("The best slope for this model is " + str(best_a) + ".")
print("The best intercept for this model is " + str(best_b) + ".")
print("This means the lineair formula in this model is: height = " + str(best_a) + " * width + " + str(best_b) + ".")
print("This model has the smallest error with the datapoints from the sample: " + str(round(smallest_error,4)) + ".")

#model predicts height of bounce of a bouncy ball by certain width 
height = get_y(best_a,best_b, width)
print("The model predicts a bouncy ball with a width of " + str(width) + " cm bounces " + str(height) + " m high.")


