#importa a classe LED da biblioteca gpiozero
from gpiozero import LED

#importa sleep
from time import sleep

#este script é executado quando o comando 'systemctl stop' é chamado.
#o objetivo é garantir que o hardware (LED) não fique em um estado inconsistente (aceso) após o fim do serviço.

#instancia o objeto LED no pino GPIO 18.
#é necessário redefinir o pino aqui para que este script possa controlá-lo.
led = LED(18)

#garante que o LED esteja desligado.
#isso finaliza o serviço de forma limpa ("graceful shutdown").
led.off()

# Obs: removemos o 'while True' original, pois um script de 'stop'
#deve executar a ação de limpeza e encerrar o processo imediatamente.
#se houvesse um loop infinito aqui, o comando de parar o serviço travaria.
