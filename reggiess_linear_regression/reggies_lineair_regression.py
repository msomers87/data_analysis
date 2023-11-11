#Input variables, width is width of bouncy ball. Data_points are points found in a test with a sample of bouncy balls
width = 6
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

#function for lineair formula, a = slope, b = intercept
def get_y(a,b,x):
    y = a*x + b
    return y

#function to calculate error for single point (x,y)
def calculate_error(a,b,point):
    x_point = point[0]
    y_point = point[1]
    y_value = get_y(a,b,x_point)
    return abs(y_value - y_point)

#function to calculate total of errors with set of points(x,y)
def calculate_all_error(a, b, points):
    errors = 0
    for point in points:
        errors += calculate_error(a, b, point)
    return errors

#generate multiple possible as en bs for model
possible_as = [slope / 10.0 for slope in range(-100, 101)]
possible_bs = [intercept / 10.0 for intercept in range(-200, 201)]

#find best a en b for model with the smallest error
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
print("This model has the smallest error with the data points from the sample, namely: " + str(smallest_error) + ".")

#model predicts height of bounce of a bouncy ball by width 
height = get_y(best_a,best_b, width)
print("The model predicts a bouncy ball with a width of " + str(width) + " bounces " + str(height) + " high.")


