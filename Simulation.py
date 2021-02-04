import math

v1 = int(input("V_v:"))
a  = int(input("a:"))

t =0
t2 = 0
x =0

def calculate(v , a):
    global t
    global t2
    global x
    
    t = v/a
    x = v1*t - (a/2) * t**2
    t2 = math.sqrt(x * 2 / a )
calculate(v1, a)
    
print("v1:" + str(v1), "a: " + str(a),"t:" + str(t),"x: " + str(x), "t2: "+ str(t2))