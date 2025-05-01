x1 = float(input("ingrese el primer valor: "))

x2 = float(input("ingrese el segundo valor: "))

w1 = 0.5 #---> colocamos los valores para el and gate 
w2 = 0.5 

b = 0.1 # inicializamos el bias 

y = x1*w1 + x2*w2 + b 

# programamos un binary step function con el step en 1 

if y >1: y = 1 

else:  y =0 

print(y)
