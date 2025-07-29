import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo = "caminho_do_arquivo.csv"
dados = pd.read_csv(caminho_arquivo)
dados.columns = dados.columns.str.strip()
print("Colunas disponíveis após strip():")
print(dados.columns.tolist())

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

ax1.plot(dados['Tempo (s)'], dados['Aceleração X'], label='Aceleração X', color='crimson')
ax1.plot(dados['Tempo (s)'], dados['Aceleração Y'], label='Aceleração Y', color='darkblue')
ax1.plot(dados['Tempo (s)'], dados['Aceleração Z'], label='Aceleração Z', color='green')
ax1.set_title('Aceleração ao Longo do Tempo')
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Aceleração (g)')
ax1.legend()
ax1.grid(True)

ax2.plot(dados['Tempo (s)'], dados['Giroscópio X'], label='Giroscópio X', color='crimson')
ax2.plot(dados['Tempo (s)'], dados['Giroscópio Y'], label='Giroscópio Y', color='darkblue')
ax2.plot(dados['Tempo (s)'], dados['Giroscópio Z'], label='Giroscópio Z', color='green')
ax2.set_title('Velocidade Angular ao Longo do Tempo')
ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel('Velocidade Angular (°/s)')
ax2.legend()
ax2.grid(True)
plt.tight_layout()
plt.show()