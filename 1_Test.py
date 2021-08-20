a,b,c,d = 10,20,30,40
print("Separate variable values:",a,b,c,d)
#t = (a,b,c,d)
#t = [a,b,c,d]
t = {a,b,c,d}
print("Variable value after packing:",t)
print("Packed variable type:",type(t))
x,y,z,p = t
print("variable values after unpacking:",x,y,z,p)