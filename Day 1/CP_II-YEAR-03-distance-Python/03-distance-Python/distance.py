# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.

import math
distance =0
def fun_distance(x1, y1, x2, y2):
	distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
	c = math.trunc(distance)
	# your code goes here
	return c