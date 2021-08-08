lugares=[1,1,0,0,1] #1 es TRUE 0 es FALSE
dato= [1,1,0,1,0] #Datos ingresando

for i in range(len(lugares)):
   if lugares[i] == dato[i]:
       print(True)
   else:
       print(False)