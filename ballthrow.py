import math
h=float(input("Enter the initial height: "))
v_0=float(input("Enter the initial speed: "))
a_degrees=float(input("Enter the angle: "))
a_degrees=math.radians(a_degrees)
g=9.81
x=(v_0*math.sin(a_degrees))**2+2*g*h
t=(v_0*math.sin(a_degrees)+math.sqrt(x))/g
print(f"The flight time is {t}s")
d=float(v_0*math.cos(a_degrees)*t)
print(f"The throw distance is: {d}m")

#max angle for max distance: a_degrees=45 when h=0, but not when you have h. Then the angle has to be smaller