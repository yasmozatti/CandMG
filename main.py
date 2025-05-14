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

# Funcao de atualizacao do grafico
def upd_chart(frame):
    # Obter informacoes de uso da CPU
    cpu_percent = psutil.cpu_percent()
    # Obter informacoes de uso da memoria
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    # Adicionando dados ao grafico
    cpu_line.set_data(List(range(frame)), [cpu_percent]*frame)
    mem_line.set_data(List(range(frame)), [memory_percent]*frame)


plt.show()