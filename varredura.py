# Função de varredura de ambiente com a câmera

def varredura(t, theta_i, theta_f, p_servo):
    servo = Servo(p_servo)
    val_i = -1+(theta_i/9)*0.1
    val_f =  1-(theta_f/9)*0.1
    servo.value = val
    sleep(t/20)
    val = val + 0.1
    if val > val_f:
        val = val_i