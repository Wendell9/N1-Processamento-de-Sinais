import matplotlib.pyplot as plt
import numpy as np
import re
from sympy import symbols, sympify

def plot_sinal_discreto(x, title='Ex 1)Sinal Discreto x[n]', xlabel='Índice n', ylabel='Amplitude'):
    """
    Plota um sinal discreto usando stem plot.
    
    Parâmetros:
    x (list ou np.array): Sinal discreto a ser plotado
    title (str): Título do gráfico (opcional)
    xlabel (str): Rótulo do eixo x (opcional)
    ylabel (str): Rótulo do eixo y (opcional)
    """
    n = np.arange(len(x))  # Cria os índices discretos
    
    plt.figure(figsize=(10, 5))
    markerline, stemlines, baseline = plt.stem(
        n, 
        x, 
        linefmt='blue',  # Cor das hastes
        markerfmt='bo',   # Formato dos marcadores (círculos azuis)
        basefmt=' '       # Remove a linha de base
    )
    
    # Customização
    plt.setp(stemlines, linewidth=1.5)
    plt.setp(markerline, markersize=5)
    
    # Labels e título
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    
    # Eixos e grade
    plt.xticks(n)
    plt.grid(linestyle='--', alpha=0.5)
    plt.axhline(0, color='black', linewidth=0.5)
    
    plt.tight_layout()
    plt.show()
    
    # Exemplo 1: Sinal padrão

def plot_transformacoes_discretas(x):
    """
    Aplica e plota três transformações em um sinal discreto x[n]:
    1. x[n-2] (deslocamento para direita em 2 unidades)
    2. x[-n]  (reflexão temporal)
    3. x[2n]  (compressão por 2)
    
    Parâmetros:
    x (list ou np.array): Sinal discreto de entrada
    """
    x = np.array(x)
    n = np.arange(len(x))
    
    # Calcula as transformações
    x_deslocado = np.roll(x, 2)  # Deslocamento
    x_deslocado[:2] = 0          # Preenche com zeros
    
    x_reflexao = x[::-1]         # Reflexão
    
    x_compressao = x[::2]        # Compressão
    
    # Configuração do gráfico
    plt.figure(figsize=(15, 8))
    
    # Subplot 1: Sinal original
    plt.subplot(2, 2, 1)
    plt.stem(n, x, linefmt='blue', markerfmt='bo', basefmt=' ')
    plt.title('Sinal Original $x[n]$')
    plt.xlabel('n')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(n)
    
    # Subplot 2: x[n-2]
    plt.subplot(2, 2, 2)
    plt.stem(n, x_deslocado, linefmt='green', markerfmt='go', basefmt=' ')
    plt.title('Deslocamento $x[n-2]$')
    plt.xlabel('n')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(n)
    
    # Subplot 3: x[-n]
    plt.subplot(2, 2, 3)
    plt.stem(n, x_reflexao, linefmt='red', markerfmt='ro', basefmt=' ')
    plt.title('Reflexão Temporal $x[-n]$')
    plt.xlabel('n')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(n)
    
    # Subplot 4: x[2n]
    n_compressao = np.arange(len(x_compressao))
    plt.subplot(2, 2, 4)
    plt.stem(n_compressao, x_compressao, linefmt='purple', markerfmt='mo', basefmt=' ')
    plt.title('Compressão $x[2n]$')
    plt.xlabel('n')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(n_compressao)
    
    plt.tight_layout()
    plt.show()

def analisar_sistema(equacao):
     # Padrão regex para encontrar termos como x[n], x[n-2], y[n+3], etc.
    padrao = r'(x|y)\[n([+-]\d+)?\]'
    termos = re.findall(padrao, equacao)
    
    # Verifica memória
    memoria = "estático (sem memória)"
    for termo in termos:
        if termo[1]:  # Se tem algo como +2 ou -3 (não é apenas n)
            memoria = "dinâmico (com memória)"
            break
    
    # Verifica causalidade
    causal = "causal"
    for termo in termos:
        if '+' in termo[1]:  # Se tem n+algum_numero (avanço no tempo)
            causal = "não causal"
            break
    
    # VERIFICA INVARIÂNCIA NO TEMPO (PARTE CORRIGIDA)
    invariante = True
    # Verifica se há índices não lineares (ex: x[3n], x[n/2], x[n^2])
    if re.search(r'(x|y)\[[^\]]*[*/^]\s*n|n\s*[*/^]', equacao):  # Ex: 3n, n/2, n^2
        invariante = False
    # Verifica se há índices com escalares não unitários (ex: x[2n], x[-3n])
    if re.search(r'(x|y)\[[+-]?\d+n', equacao):  # Ex: x[3n], x[-2n]
        invariante = False
    
    invariancia = "invariante no tempo" if invariante else "variante no tempo"
    
    return memoria, causal, invariancia

# Exemplo de uso:
equacao_usuario = input("Digite a equação do sistema (ex: y[n] = x[n] - x[n-2]): ")
memoria, causalidade,invariancia = analisar_sistema(equacao_usuario)
print(f"Tipo de sistema: {memoria}")
print(f"Causalidade: {causalidade}")
print(f"Invariância no tempo: {invariancia}")