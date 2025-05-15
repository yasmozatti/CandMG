import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurando o grafico
fig, ax = plt.subplots()
ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
ax.set_title('Uso de CPU e Memória')
ax.set_xlabel('Tempo')
ax.set_ylabel('Uso (%)')
cpu_line, = ax.plot([], [], label = 'CPU', color = '#990000')
mem_line, = ax.plot([], [], label = 'Memória', color = '#0066CC')

# adicionando texto aos valores da CPU e memoria
cpu_text = ax.text(0.77, 0.7, '', transform=ax.transAxes)
mem_text = ax.text(0.77, 0.6, '', transform=ax.transAxes)

# listas para armazenar os dados
cpu_data = []
mem_data = []
tempo = []

# Funcao de atualizacao do grafico
def update_chart(frame):
    # Obter informacoes de uso da CPU
    cpu_percent = psutil.cpu_percent()
    # Obter informacoes de uso da memoria
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    # Adicionando dados ao grafico
    cpu_data.append(cpu_percent)
    mem_data.append(memory_percent)
    tempo.append(frame)

    if len(tempo) > 100:
        tempo.pop(0)
        cpu_data.pop(0)
        mem_data.pop(0)

    cpu_line.set_data(tempo, cpu_data)
    mem_line.set_data(tempo, mem_data)
    # Atualizar os textos com os valores da CPU e memoria
    cpu_text.set_text(f'CPU: {cpu_percent:.1f}%')
    mem_text.set_text(f'Memória: {memory_percent:.1f}%')
    return cpu_line, mem_line, cpu_text, mem_text

# Anime o grafico
animation = FuncAnimation(fig, update_chart, frames =100, interval=1000, blit=True)

#Estilizando as linhas do grafico
for line in [cpu_line, mem_line]:
    line.set_linewidth(2)
    line.set_marker('o')
    line.set_markersize(5)

# Estilizar o fundo do grafico
ax.set_facecolor('#D9D9D9')

plt.show()
