# Skill de Português Técnico Simplificado (PTS)

Esta skill faz um modelo de linguagem (LLM) escrever em Português Técnico Simplificado (PTS).
O PTS é uma linguagem controlada para documentação técnica em português do Brasil.
A especificação ASD-STE100 inspirou as regras do PTS.
Nós adaptamos essas regras para a gramática e para os problemas comuns do português.
Um texto em PTS é claro, direto e fácil de entender.

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
| `SKILL.md` | As instruções principais para o LLM |
| `references/regras-de-escrita.md` | Todas as regras de escrita com exemplos |
| `references/vocabulario.md` | O vocabulário recomendado com formas e classes |
| `references/substituicoes.md` | Substituições para termos burocráticos e estrangeirismos |
| `examples/antes-depois.md` | Exemplos de textos antes e depois da mudança |
| `scripts/pts_check.py` | Ferramenta de verificação das regras em Python |
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
python scripts/pts_check.py --modo procedimento rascunho.txt
python scripts/pts_check.py --modo descritivo capitulo.md
python scripts/pts_check.py --modo misto documento.md
```

A ferramenta encontra estes erros:

- Frases com muitas palavras (mais de 20 em procedimento ou mais de 25 em texto descritivo)
- Parágrafos com mais de seis frases
- Ponto e vírgula e mesóclises
- Locuções com gerúndio e tempos compostos
- Voz passiva e voz passiva com "-se"
- Futuro do pretérito ("deveria", "poderia") e pretérito imperfeito
- Palavras não recomendadas ou termos coloquiais
- Palavras fora do vocabulário recomendado.

A ferramenta usa somente a biblioteca padrão do Python 3.

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
