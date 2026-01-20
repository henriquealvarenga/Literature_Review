# Forest Plot Educativo para Revisão Sistemática
# Objetivo: Ilustrar a interpretação de um forest plot

library(ggplot2)
library(dplyr)

# Dados fictícios para o forest plot
dados <- data.frame(
  estudo = c(
    "Silva et al., 2018",
    "Santos et al., 2019",
    "Oliveira et al., 2020",
    "Costa et al., 2021",
    "Pereira et al., 2022",
    "Efeito Combinado"
  ),
  efeito = c(0.75, 0.82, 0.68, 0.71, 0.85, 0.76),
  ic_inferior = c(0.55, 0.65, 0.52, 0.58, 0.70, 0.68),
  ic_superior = c(0.95, 0.99, 0.84, 0.84, 1.00, 0.84),
  peso = c(15, 25, 20, 18, 22, 100),
  tipo = c(rep("estudo", 5), "combinado")
)

# Ordenar estudos (combinado por último)
dados$estudo <- factor(dados$estudo, levels = rev(dados$estudo))

# Separar dados
dados_estudos <- dados %>% filter(tipo == "estudo")
dados_combinado <- dados %>% filter(tipo == "combinado")

# Criar o forest plot
forest <- ggplot(dados, aes(x = efeito, y = estudo)) +
  # Linha de nulidade (sem efeito)
  geom_vline(
    xintercept = 1,
    linetype = "dashed",
    color = "gray50",
    linewidth = 0.5
  ) +

  # Intervalos de confiança - usando geom_linerange + geom_errorbar
  geom_linerange(
    aes(xmin = ic_inferior, xmax = ic_superior, color = tipo),
    linewidth = 0.8
  ) +

  # Pontos dos efeitos (quadrados para estudos)
  geom_point(
    data = dados_estudos,
    aes(size = peso),
    shape = 15,
    color = "#2166AC"
  ) +

  # Losango para efeito combinado
  geom_point(data = dados_combinado, shape = 18, size = 6, color = "#B2182B") +

  # Escalas
  scale_size_continuous(range = c(3, 8), guide = "none") +
  scale_color_manual(
    values = c("estudo" = "#2166AC", "combinado" = "#B2182B"),
    guide = "none"
  ) +
  scale_x_continuous(
    breaks = seq(0.4, 1.2, 0.2),
    limits = c(0.35, 1.25)
  ) +

  # Anotações - posição ajustada e dentro dos limites
  annotate(
    "text",
    x = 0.90,
    y = 0.4,
    label = "← Favorece intervenção",
    size = 3.2,
    color = "#2166AC",
    hjust = 0.5
  ) +
  annotate(
    "text",
    x = 1.1,
    y = 0.4,
    label = "Favorece controle →",
    size = 3.2,
    color = "#B2182B",
    hjust = 0.5
  ) +

  # Tema e rótulos
  labs(
    title = "Forest Plot: Interpretação Visual",
    subtitle = "Razão de Risco (RR) com Intervalos de Confiança de 95%",
    x = "Razão de Risco (RR)",
    y = NULL,
    caption = "Linha tracejada = sem efeito (RR = 1) | Tamanho do quadrado = peso do estudo"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", size = 14, hjust = 0),
    plot.subtitle = element_text(color = "gray40", size = 11),
    plot.caption = element_text(color = "gray50", size = 9, hjust = 0),
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank(),
    plot.margin = margin(20, 30, 20, 20)
  ) +
  coord_cartesian(ylim = c(0, 6.5), clip = "off")

# Salvar o gráfico
ggsave(
  "forest_plot_v2.png",
  forest,
  width = 10,
  height = 7,
  dpi = 300,
  bg = "white"
)

cat("Forest plot corrigido salvo como 'forest_plot_v2.png'\n")
