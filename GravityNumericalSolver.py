import math

r = 6371000
v=0
m = 6*math.pow(10, 24) 
t =0
delta_t = 0.05
while r > 6370940:
    v += (6.67*math.pow(10, -11)*m/math.pow(r,2))*delta_t
    r -= v*delta_t
    t += delta_t   
print(v)
print(r)
print(t)