# Função de controle manual da câmera

def controle(dir,alt,p_servo1,p_servo2):

    servo1 = Servo(p_servo1)
    servo2 = Servo(p_servo2)
    
    val1 = 0

    teste1 = dir
    teste2 = alt

    if teste1 == '1':
        if val1 <= 0.8:
            val1 = val1+0.1
            servo1.value = val1
            sleep(0.5)
            #print(val)
        else:
            servo1.value = val1
    if teste1 == '0':
        if val1 >= -0.8:
            val1 = val1-0.1
            servo1.value = val1
            sleep(0.5)
            #print(val)
        else:
            servo1.value = val1

    if teste2 == '1':
        if val2 <= 0.8:
            val2 = val2+0.1
            servo2.value = val2
            sleep(0.5)
            #print(val)
        else:
            servo2.value = val2
    if teste2 == '0':
        if val2 >= -0.8:
            val2 = val2-0.1
            servo2.value = val2
            sleep(0.5)
            #print(val)
        else:
            servo2.value = val2

