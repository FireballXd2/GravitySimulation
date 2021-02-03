
import math

r = 10
v= 0
m = 6*math.pow(10, 4) 
v2 = 0
m2 = 6*math.pow(10, 2)
t =0

delta_t = 0.005
while r > 0:
    v += (6.67*math.pow(10, -11)*m/math.pow(r,2))*delta_t
    v2 += (6.67*math.pow(10, -11)*m2/math.pow(r,2))*delta_t
    r -= v*delta_t + v2*delta_t
    t += delta_t   
    
print("v1: " + str(v))
print("v2: " + str(v2))
print("t: " + str(t))