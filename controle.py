# Função de controle manual da câmera

def controle(dir,p_servo):

    servo = Servo(p_servo)
    val = 0

    i = 0
    j = 0
    teste = dir

    if teste == '1':
        if val <= 0.8:
            for i in range(1):
                val = val+0.1
                servo.value = val
                sleep(0.5)
                #print(val)
        else:
            servo.value = val
    if teste == '0':
        if val >= -0.8:
            for i in range(1):
                val = val-0.1
                servo.value = val
                sleep(0.5)
                #print(val)
        else:
            servo.value = val

