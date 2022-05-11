#from gpiozero import Servo
from time import sleep

# Import das funções
import varredura
import angulo
import controle

error = 0 

# String de operção - teste
#in_str = "v;20;90;180"  # String de entrada

# Parser da string de operação
par =  in_str.split(";")

porta_servo = 12

# Escolha do modo de operação
if(par[0] == "V"):    
    varredura(par[1],par[2],par[3],porta_servo)
elif(par[0] == "C"):     
    controle(par[1],porta_servo)
elif(par[0] == "A"):  
    angulo(par[1],porta_servo)
else:
    print("Error - Invalid input")
           



