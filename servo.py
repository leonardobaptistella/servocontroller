import RPi.GPIO as GPIO
import pigpio #sudo apt-get install python3-pigpio
import time

#Portas para os PWM de cada Servo
servo_H = 17
servo_V = 18


# more info at http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth

pwm = pigpio.pi() #Inicia biblioteca

#Define os Servos com Output
pwm.set_mode(servo_H, pigpio.OUTPUT)
pwm.set_PWM_frequency( servo_H, 50 )
pwm.set_mode(servo_V, pigpio.OUTPUT)
pwm.set_PWM_frequency( servo_V, 50 )


def func(x): #Retorna o valor em segundos da rotacao em graus desejada
    return ((2500-500)/(180-0))*x+500 #Funcao de primeiro grau

# Posiciona os servos em um angulo fixo dado na entrada da função
def Angulo(angulo_H=0,angulo_V=0,slp=1):
       
       if (float(angulo_H)<0 or float(angulo_H)>180) or (float(angulo_V)<0 or float(angulo_V)>180):
           #Desliga os Servos
           pwm.set_PWM_dutycycle(servo_H, 0)
           pwm.set_PWM_frequency(servo_H, 0)
           pwm.set_PWM_dutycycle(servo_V, 0)
           pwm.set_PWM_frequency(servo_V, 0)
           return "ERROR: Angulo fora de faixa [0,180]"
       else:
           pwm.set_servo_pulsewidth( servo_H, func(float(angulo_H))) ;
           pwm.set_servo_pulsewidth( servo_V, func(float(angulo_V))) ;
           time.sleep( slp )

# Incrementa ou decrementa a posição do servo
#def Controle_Manual(dir,servo):  
    #Angulo()#chamar a função angulo dando como parametro um passo       
    #print("teste")

# Varre de 0 a 180
def Varredura(servo): 
    if(servo == "H"): #Servo Horizontal
        for i in range(0,180):
            Angulo(i,90,1)
        for i in range(180,0):
            Angulo(i,90,1)    
    elif(servo == "V"): # Servo Vertical
        for i in range(10,100):
            Angulo(90,i,1)
        for i in range(100,10):
            Angulo(90,i,1)

