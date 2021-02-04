import datetime
import math
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 400)
canvas1.pack()

entry1 = tk.Entry (root) 
entry2 = tk.Entry (root) 
entry3 = tk.Entry (root) 
canvas1.create_window(100, 140, window=entry1)
canvas1.create_window(250, 140, window=entry2)
canvas1.create_window(400, 140, window=entry3)

label1 = tk.Label(root, text = "Starting distance \n Might crash if too big")
canvas1.create_window(100, 110, window = label1)
label2 = tk.Label(root, text = "Mass 1")
canvas1.create_window(250, 110, window = label2)
label3 = tk.Label(root, text = "Mass 2")
canvas1.create_window(400, 110, window = label3)

def getResults():
    r = int(entry1.get())
    m1 = int(entry2.get())
    m2 = int(entry3.get())
    
    v = 0
    v2 = 0
    x1 = 0
    x2 =0
    t =0
    
    delta_t = 0.03
    while r > 0:
        v += (6.67*math.pow(10, -11)*m1/math.pow(r,2))*delta_t
        v2 += (6.67*math.pow(10, -11)*m2/math.pow(r,2))*delta_t
        x1 += v*delta_t
        x2 += v2*delta_t
        r -= v*delta_t + v2*delta_t
        t += delta_t   
    
    labelt = tk.Label(root, text = "t = " + str(t) + " s")
    canvas1.create_window(250, 230, window=labelt) 
    
button1 = tk.Button(text='Get time of collision', command = getResults)
canvas1.create_window(250, 180, window=button1)    
      
root.mainloop()        