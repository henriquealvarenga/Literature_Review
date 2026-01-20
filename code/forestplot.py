# Forest Plot Educativo para Revisão Sistemática
# Objetivo: Ilustrar a interpretação de um forest plot

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Configurar fonte e estilo
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

# Dados fictícios para o forest plot
estudos = [
    "Silva et al., 2018",
    "Santos et al., 2019", 
    "Oliveira et al., 2020",
    "Costa et al., 2021",
    "Pereira et al., 2022"
]

# Efeitos (Razão de Risco) e intervalos de confiança
efeitos = [0.75, 0.82, 0.68, 0.71, 0.85]
ic_inf = [0.55, 0.65, 0.52, 0.58, 0.70]
ic_sup = [0.95, 0.99, 0.84, 0.84, 1.00]
pesos = [15, 25, 20, 18, 22]

# Efeito combinado (meta-análise)
efeito_comb = 0.76
ic_comb_inf = 0.68
ic_comb_sup = 0.84

# Criar figura com mais espaço na parte inferior
fig, ax = plt.subplots(figsize=(12, 8))

# Posições Y para os estudos
y_pos = np.arange(len(estudos), 0, -1)
y_comb = -0.5  # Posição do efeito combinado

# Linha de nulidade (RR = 1, sem efeito)
ax.axvline(x=1, color='gray', linestyle='--', linewidth=1, zorder=1)

# Plotar estudos individuais
for i, (estudo, ef, inf, sup, peso) in enumerate(zip(estudos, efeitos, ic_inf, ic_sup, pesos)):
    y = y_pos[i]
    
    # Linha do intervalo de confiança
    ax.hlines(y=y, xmin=inf, xmax=sup, color='#2166AC', linewidth=2, zorder=2)
    
    # Quadrado proporcional ao peso
    tamanho = peso * 8  # Escalar o tamanho
    ax.scatter(ef, y, s=tamanho, marker='s', color='#2166AC', zorder=3, 
               edgecolors='white', linewidth=0.5)

# Plotar efeito combinado (losango)
ax.hlines(y=y_comb, xmin=ic_comb_inf, xmax=ic_comb_sup, color='#B2182B', linewidth=2.5, zorder=2)
ax.scatter(efeito_comb, y_comb, s=300, marker='D', color='#B2182B', zorder=3,
           edgecolors='white', linewidth=1)

# Linha separadora antes do efeito combinado
ax.axhline(y=0.25, color='gray', linestyle='-', linewidth=0.5, xmin=0.05, xmax=0.95)

# Adicionar nomes dos estudos e valores
for i, (estudo, ef, inf, sup, peso) in enumerate(zip(estudos, efeitos, ic_inf, ic_sup, pesos)):
    y = y_pos[i]
    ax.text(0.35, y, estudo, ha='right', va='center', fontsize=10)
    ax.text(1.35, y, f'{ef:.2f} [{inf:.2f}, {sup:.2f}]', ha='left', va='center', fontsize=9, 
            family='monospace')
    ax.text(1.75, y, f'{peso}%', ha='center', va='center', fontsize=9)

# Efeito combinado - texto
ax.text(0.35, y_comb, 'Efeito Combinado', ha='right', va='center', fontsize=10, fontweight='bold')
ax.text(1.35, y_comb, f'{efeito_comb:.2f} [{ic_comb_inf:.2f}, {ic_comb_sup:.2f}]', 
        ha='left', va='center', fontsize=9, family='monospace', fontweight='bold')
ax.text(1.75, y_comb, '100%', ha='center', va='center', fontsize=9, fontweight='bold')

# Cabeçalhos
ax.text(0.35, len(estudos) + 1, 'Estudo', ha='right', va='center', fontsize=10, fontweight='bold')
ax.text(1.35, len(estudos) + 1, 'RR [IC 95%]', ha='left', va='center', fontsize=10, fontweight='bold')
ax.text(1.75, len(estudos) + 1, 'Peso', ha='center', va='center', fontsize=10, fontweight='bold')

# ========================================
# SETAS E ANOTAÇÕES SIMÉTRICAS (distância igual de RR=1)
# ========================================
distancia = 0.30  # Distância simétrica do eixo RR=1
y_setas = -1.5
y_texto = -2.0

# Seta esquerda (Favorece intervenção) - começa em 1-0.05 e vai até 1-distância-0.20
ax.annotate('', xy=(1 - distancia - 0.20, y_setas), xytext=(1 - 0.05, y_setas),
            arrowprops=dict(arrowstyle='->', color='#2166AC', lw=1.5))

# Seta direita (Favorece controle) - começa em 1+0.05 e vai até 1+distância+0.20
ax.annotate('', xy=(1 + distancia + 0.20, y_setas), xytext=(1 + 0.05, y_setas),
            arrowprops=dict(arrowstyle='->', color='#B2182B', lw=1.5))

# Texto esquerda
ax.annotate('Favorece\nintervenção', xy=(1 - distancia, y_texto), ha='center', va='top', 
            fontsize=9, color='#2166AC', fontweight='bold')

# Texto direita
ax.annotate('Favorece\ncontrole', xy=(1 + distancia, y_texto), ha='center', va='top', 
            fontsize=9, color='#B2182B', fontweight='bold')

# Configurar eixos
ax.set_xlim(0.3, 1.85)
ax.set_ylim(-3.2, len(estudos) + 1.5)
ax.set_xlabel('Razão de Risco (RR)', fontsize=11, labelpad=10)

# Remover eixo Y
ax.set_yticks([])
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Título
ax.set_title('Forest Plot: Interpretação Visual de uma Meta-análise\n', 
             fontsize=13, fontweight='bold', loc='left')

# ========================================
# LEGENDA - posicionada abaixo, sem sobreposição
# ========================================
legenda_texto = ('■ Quadrado: estimativa pontual (tamanho ∝ peso)   │   '
                 '── Linha: intervalo de confiança de 95%   │   '
                 '◆ Losango: efeito combinado   │   '
                 '┆ Tracejado: linha de nulidade (RR = 1)')

ax.text(0.5, -0.1, legenda_texto, transform=ax.transAxes, fontsize=8, 
        color='gray', va='top', ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f9f9f9', edgecolor='#e0e0e0'))

plt.tight_layout()
plt.subplots_adjust(bottom=0.12)

plt.savefig('forest_plot_v3.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
#plt.savefig('forest_plot_v3.pdf', bbox_inches='tight', facecolor='white', edgecolor='none')
print("Forest plot salvo como 'forest_plot_v3.png' e 'forest_plot_v3.pdf'")