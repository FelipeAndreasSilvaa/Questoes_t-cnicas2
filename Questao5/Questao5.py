class Lampada:
    def __init__(self):
        self.estado = 'desligada'
        self.quente = False

    def ligar(self):
        self.estado = 'ligada'
        self.quente = True  # Quando a lâmpada é ligada, ela fica quente

    def desligar(self):
        self.estado = 'desligada'
        self.quente = False  # Quando a lâmpada é desligada, ela esfria

class Interruptor:
    def __init__(self, lampada):
        self.lampada = lampada

    def ligar(self):
        self.lampada.ligar()

    def desligar(self):
        self.lampada.desligar()

# Criação das lâmpadas
lampada1 = Lampada()
lampada2 = Lampada()
lampada3 = Lampada()

# Criação dos interruptores
interruptorA = Interruptor(lampada1)
interruptorB = Interruptor(lampada2)
interruptorC = Interruptor(lampada3)

# Lógica de descoberta
def descobrir_lampadas():
    # Passo 1: Ligar o interruptor A
    interruptorA.ligar()
    
    # Esperar para simular que a lâmpada esquenta (aqui, apenas um placeholder)
    
    # Passo 2: Desligar o interruptor A e ligar o interruptor B
    interruptorA.desligar()
    interruptorB.ligar()
    
    # Passo 3: Verificar o estado das lâmpadas
    estados = {
        'Lampada 1': lampada1.estado,
        'Lampada 2': lampada2.estado,
        'Lampada 3': lampada3.estado,
    }
    
    quente = {
        'Lampada 1': lampada1.quente,
        'Lampada 2': lampada2.quente,
        'Lampada 3': lampada3.quente,
    }
    
    return estados, quente

# Chama a função e imprime os resultados
estados, quentes = descobrir_lampadas()
print("Estado das lâmpadas:", estados)
print("Quentes:", quentes)

# Identificação das lâmpadas
for i in range(1, 4):
    if quentes[f'Lâmpada {i}']:
        print(f'Lâmpada {i} é controlada pelo Interruptor A.')
    elif estados[f'Lâmpada {i}'] == 'ligada':
        print(f'Lâmpada {i} é controlada pelo Interruptor B.')
    else:
        print(f'Lâmpada {i} é controlada pelo Interruptor C.')
