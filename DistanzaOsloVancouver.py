import math
#raggio terra = 6371
#x1, y1 = radians(59.9), radians(10.8)
#x2, y2 = radians(49.3), radians(-123.1)
x1 = 59.9;
y1 = 10.8;
x2 = 49.3;
y2 = -123.1;
d = (2*(6371))*math.asin(math.sqrt((math.sin((1/2)*(x2-x1)))**2)+(math.cos(x1)*(math.cos(x2)))*((math.sin((1/2)*(y2-y1))**2)));
print ("La distanza è: ", d);
