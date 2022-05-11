# Função de posicionamento da câmera p/ ângulo fixo

def angulo(pos, p_servo):

    servo = Servo(p_servo)

    if(pos == '1'): servo.max()
    if(pos == '0'): servo.mid()
    if(pos == '-1'): servo.min()