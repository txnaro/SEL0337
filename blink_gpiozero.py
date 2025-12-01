from gpiozero import LED
from time import sleep

#inicializa o objeto LED no pino GPIO 18.
#a biblioteca gpiozero abstrai a configuração de direção (IN/OUT).
led = LED(18) 

try:
    #o loop infinito é essencial para que o serviço SystemD permaneça "active".
    while True:
        led.on()           #define nível lógico alto (3.3V)
        print("LED on")    #log
        sleep(1)           #temporização de 1 segundo
        
        led.off()          #define nível lógico baixo (0V)
        print("LED off")
        sleep(1)

#tratamento de exceção para encerrar o script sem erros ao usar Ctrl+C manualmente
except KeyboardInterrupt:
    pass
