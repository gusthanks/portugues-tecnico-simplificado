# Skill de Português Técnico Simplificado (PTS)

Esta skill faz um modelo de linguagem (LLM) escrever em Português Técnico Simplificado (PTS).
O PTS é uma linguagem controlada para documentação técnica em português do Brasil.
A especificação ASD-STE100 inspirou as regras do PTS.
Nós adaptamos essas regras para a gramática e para os problemas comuns do português.
Um texto em PTS é claro, direto e fácil de entender.
Esta skill é ideal para documentação de software e para equipes de agentes no Hermes.

A própria documentação desta skill obedece às regras do PTS. Este README está em PTS.

## Exemplo

Texto antes da mudança:

> Previamente ao início da instalação, deve-se assegurar que todos os
> componentes tenham sido minuciosamente inspecionados quanto a danos, e
> as peças defeituosas deverão ser substituídas de imediato; a não
> observância poderá acarretar o mau funcionamento do sistema.

Texto depois da mudança:

> Antes de começar a instalação, examine todos os componentes.
> Se você encontrar uma peça com defeito, substitua a peça imediatamente.
> Uma peça com defeito pode causar uma falha do sistema.

## Conteúdo deste repositório

| Arquivo | Função |
|---|---|
| `SKILL.md` | As instruções principais para o modelo de linguagem |
| `references/regras-de-escrita.md` | Todas as regras de escrita com exemplos |
| `references/vocabulario.md` | O vocabulário recomendado com formas e classes |
| `references/substituicoes.md` | Substituições para termos burocráticos e termos de IA |
| `examples/antes-depois.md` | Exemplos de textos antes e depois da mudança |
| `examples/comunicacao-agentes-hermes.md` | Exemplos de handoff entre agentes, diffs e diagramas |
| `scripts/pts_check.py` | Ferramenta de verificação das regras em Python |
| `tests/test_pts_check.py` | Suíte de testes automatizados da ferramenta |
| `.github/workflows/pts-lint.yml` | Validação contínua com GitHub Actions |
| `NOTICE.md` | Informações de direitos autorais e referências |

## Como instalar a skill

### No Claude Code / Claude Desktop

1. Clone este repositório na sua pasta de skills:

```bash
git clone https://github.com/gusthanks/portugues-tecnico-simplificado.git ~/.claude/skills/portugues-tecnico-simplificado
```

2. Peça ao Claude para escrever ou revisar documentação técnica em PTS.
3. O Claude encontra a skill e obedece às regras.

Você também pode chamar a skill diretamente: `/portugues-tecnico-simplificado`.

### No Hermes / Equipes de Agentes

1. Adicione este repositório ou o arquivo `SKILL.md` às ferramentas do seu agente no Hermes.
2. Agentes de documentação e revisão usam o ciclo de auto-correção com `--formato agente`.
3. Agentes comunicam tarefas com o cabeçalho estruturado de handoff, sem saudações ou palavras vazias.

### No Antigravity / Gemini

Clone o repositório na pasta de skills do seu ambiente:

```bash
git clone https://github.com/gusthanks/portugues-tecnico-simplificado.git ~/.gemini/config/skills/portugues-tecnico-simplificado
```

### Em outros modelos de linguagem

1. Abra `SKILL.md`. Copie o texto para o prompt de sistema do modelo.
2. Adicione o conteúdo de `references/substituicoes.md`.
3. Para resultados melhores, adicione também o conteúdo de `references/regras-de-escrita.md`.
4. Peça ao modelo para escrever texto técnico.

## Como verificar um texto

Execute a ferramenta de verificação em um arquivo ou na entrada padrão:

```bash
# Modo padrão (software e agentes, rigor pragmático)
python scripts/pts_check.py rascunho.md

# Formato compacto para consumo por agentes no Hermes
python scripts/pts_check.py --formato agente rascunho.md

# Saída estruturada em JSON
python scripts/pts_check.py --formato json rascunho.md

# Modo estrito com vocabulário fechado (aeroespacial e manufatura)
python scripts/pts_check.py --rigor estrito manual.md
```

A ferramenta encontra estas violações:

- Frases longas (mais de 20 palavras em procedimento ou mais de 25 em texto descritivo)
- Parágrafos com mais de seis frases
- Ponto e vírgula e mesóclises
- Locuções com gerúndio e tempos compostos
- Voz passiva e voz passiva com "-se"
- Futuro do pretérito ("deveria", "poderia") e pretérito imperfeito
- Vícios de IA (saudações de cortesia, clichês de transição, conclusões genéricas e emojis)
- Palavras não recomendadas ou termos coloquiais
- Palavras fora do vocabulário recomendado (no modo estrito).

A ferramenta usa somente a biblioteca padrão do Python 3.

## Validação Contínua (CI)

O repositório inclui automação com GitHub Actions (`.github/workflows/pts-lint.yml`).
O fluxo executa a suíte de testes unitários e valida todos os arquivos Markdown a cada push e pull request.

Para rodar os testes localmente:

```bash
python -m unittest discover tests
```

## Limites da skill

A ferramenta não encontra todos os erros.
A ferramenta não sabe se uma palavra tem o sentido correto no contexto.
Uma pessoa deve revisar documentos críticos.
Esta skill não é um documento oficial da ASD.
Esta skill não garante conformidade com nenhuma norma governamental ou aeroespacial.

## Origem e licença

Esta skill é uma adaptação para o português do Brasil da skill `simplified-technical-english` de 0xpili.
As regras de base vêm dos princípios do ASD-STE100 Issue 7 (2017).
Nós criamos o vocabulário em `references/vocabulario.md` especialmente para o português.
O texto desta skill e seus scripts têm a licença MIT. Consulte `LICENSE` e `NOTICE.md`.
