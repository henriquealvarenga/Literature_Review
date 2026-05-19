# Literature Review — Revisões de Literatura em Saúde

Site Quarto com material didático sobre tipos de revisão de literatura em saúde (narrativa, integrativa, escopo, sistemática, meta-análise), ferramentas (PICO, OSF) e atividades práticas. Material da disciplina ministrada na UFSJ / AFYA.

Publicado em: **https://henriquealvarenga.com/Literature_Review/**

================================================================================

## ⚠️ ATENÇÃO — VOCÊ **NÃO** PRECISA RODAR `quarto render` ANTES DO `git push`

**LEIA ISTO COM ATENÇÃO. NO FUTURO VOCÊ VAI ESQUECER.**

Este repositório é publicado **via GitHub Actions**, NÃO via "Deploy from a branch".
O workflow [`.github/workflows/publish.yml`](.github/workflows/publish.yml) cuida de
toda a renderização **no servidor do GitHub**, automaticamente, a cada `git push`
para `main`.

### Por que aqui não precisa de `quarto render` local?

Porque este projeto **NÃO tem chunks de código executável**. Verifique:

- Não há nenhum chunk ```` ```{r} ```` ou ```` ```{python} ```` em nenhum `.qmd`.
- Os únicos chunks especiais são ```` ```{mermaid} ```` (diagramas, renderizados pelo
  próprio Quarto) e ```` ```{=html} ```` (HTML cru, passado direto).
- Os scripts em [`code/`](code/) (`forestplot.r`, `forestplot.py`) **NÃO são
  executados durante o render** — são scripts standalone que foram rodados uma vez
  para gerar as imagens estáticas em [`images/`](images/).
- Não há chamadas a APIs/internet durante o render.

Como o conteúdo do site é 100% determinístico a partir dos `.qmd`/`.css`/`.scss`,
o CI consegue renderizar do zero em ~30 segundos no Ubuntu, sem precisar instalar
R, Python, nem versionar `_freeze/`.

### Quando precisaria de `quarto render` local?

**Outro tipo de projeto** (Estratégia A com `_freeze/` versionado): quando há chunks
`{r}` ou `{python}` no `.qmd`. Nesse caso, o CI **reusa** o `_freeze/` versionado
em vez de instalar R/Python, e você precisa rodar `quarto render` localmente antes
do push para atualizar o `_freeze/`. **Este repositório NÃO é esse caso.**

### Seu fluxo de publicação aqui é simplesmente:

```bash
# 1) Edita os .qmd como quiser
# 2) (Opcional) preview local: quarto preview
# 3) Publica:
git add -A
git commit -m "sua mensagem"
git push
```

O GitHub Actions renderiza e publica sozinho. Acompanhe a aba **Actions** do repo
para ver o build.

================================================================================

## Estrutura do projeto

```
.
├── _quarto.yml              # config do site (type: website, output-dir: docs)
├── _metadata.yml            # metadados globais
├── index.qmd                # landing page
├── 00-sinopse.qmd
├── 01-introducao.qmd        # visão geral dos tipos de revisão
├── 01.1-historia.qmd
├── 02-revisao-narrativa.qmd
├── 03-revisao-integrativa.qmd
├── 04-revisao-escopo.qmd
├── 05-revisao-sistematica.qmd
├── 06-metanalise.qmd
├── 07-acronimos-pico.qmd
├── 08-registro-osf.qmd
├── 09-pratica-{0,1,2}.qmd   # atividades práticas
├── About.qmd
│
├── custom.scss              # tema (variáveis Bootstrap)
├── styles.css               # estilos gerais
├── landing.css              # estilos da landing page
│
├── images/                  # imagens estáticas (logo, forest plot, etc.)
├── code/                    # scripts standalone (forestplot.r/py) — NÃO rodam no render
├── references/              # references.bib, CSL styles, PDFs de referência
│
├── .github/workflows/
│   └── publish.yml          # CI: roda quarto render e publica no GitHub Pages
│
└── docs/                    # GERADO pelo CI — NÃO versionado, NÃO editar à mão
```

## Configuração do GitHub Pages

Em **Settings → Pages**, a *Source* deve estar como **GitHub Actions** (não como
"Deploy from a branch"). Se ainda estiver no modo antigo, basta mudar — o workflow
já está configurado.

## Estratégia de build adotada

**Workflow simples** (sem R/Python no CI, sem `_freeze/`):

- Sem chunks executáveis → CI só precisa do Quarto.
- Render do zero a cada push (~30s).
- Output `docs/` é **gerado pelo CI** e publicado, mas nunca versionado.
- `_freeze/` não existe e não é necessário.
