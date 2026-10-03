---
name: portugues-tecnico-simplificado
description: Escreve e reescreve textos em Português Técnico Simplificado (PTS), uma linguagem controlada em português do Brasil para documentação técnica clara. Use quando o usuário pedir PTS, português simplificado, linguagem controlada, linguagem simples ou redação técnica clara, e quando o usuário pedir para escrever, reescrever, revisar ou verificar documentação técnica, procedimentos, manuais, instruções, avisos de segurança, mensagens de erro ou relatórios em português.
license: MIT. Adaptação para o português do Brasil da skill simplified-technical-english de 0xpili. Consulte NOTICE.md.
metadata:
  idioma: pt-BR
  inspiracao: ASD-STE100 Issue 7 (2017), adaptado para a gramática do português
  versao: 1.1.0
---

# Português Técnico Simplificado (PTS)

Esta skill faz você escrever em Português Técnico Simplificado (PTS).
O PTS é uma linguagem controlada para documentação técnica em português do Brasil.
O PTS adapta as regras do ASD-STE100 (Simplified Technical English) para a gramática do português.
Um texto em PTS é claro para leitores com pouca leitura técnica e é fácil de traduzir.

Obedeça às regras deste arquivo em todo o texto técnico que você escrever.
As regras deste arquivo são as regras mais importantes.
O conjunto completo de regras está em `references/regras-de-escrita.md`.
O vocabulário recomendado está em `references/vocabulario.md`.

## Escopo

Aplique o PTS a textos técnicos: documentação, procedimentos, manuais, instruções, relatórios, mensagens de erro e respostas sobre assuntos técnicos.

Não aplique o PTS a:

- Textos de marketing ou de marca
- Poemas, histórias ou conversas informais
- Blocos de código, identificadores, comandos, caminhos de arquivo e mensagens de erro citadas
- Citações e nomes oficiais de produtos, peças e documentos.

Se o usuário pedir um estilo diferente, o pedido do usuário prevalece.

## Passo 1: Classifique o texto

Antes de escrever, classifique cada parte do texto:

- **Texto de procedimento** manda o leitor fazer algo. Exemplo: "Remova os quatro parafusos."
- **Texto descritivo** dá uma informação. Exemplo: "A bomba envia combustível para o motor."

Os dois tipos têm limites diferentes. Não misture os dois tipos no mesmo parágrafo.

## Passo 2: Obedeça às regras de verbo

- Use somente estas formas verbais: infinitivo, imperativo, presente do indicativo, pretérito perfeito, futuro do presente simples e particípio como adjetivo.
- Em condições com "se" ou "quando", use o futuro do subjuntivo. Escreva "Se a luz acender, desligue o motor."
- Não use o gerúndio. Escreva "Quando você fizer este procedimento", e não "Fazendo este procedimento". Nunca use "vou estar enviando".
- Não use tempos compostos. Escreva "o operador ajustou a alavanca", e não "o operador tem ajustado a alavanca" ou "havia ajustado".
- Use a voz ativa. Escreva "um relé conecta os circuitos", e não "os circuitos são conectados por um relé".
- Não use a voz passiva com "-se". Escreva "Instale o filtro", e não "Instala-se o filtro".
- Em procedimentos, use o imperativo na forma de "você". Escreva "Remova", "Abra", "Desligue". Não escreva "Remove", "Abre", "Desliga".
- Se não houver um agente, use "você" ou "nós" como sujeito.
- Use somente "poder" (possibilidade) e "dever" (obrigação) como verbos auxiliares. Use "dever" somente para obrigação, nunca para probabilidade.
- Não use o futuro do pretérito. Não escreva "deveria", "poderia", "seria" ou "teria".
- "Estar" + particípio mostra um estado e é permitido. "Os fios estão desconectados." "Ser" + particípio é voz passiva e não é permitido.

## Passo 3: Obedeça às regras de frase

- Frases de procedimento: no máximo 20 palavras.
- Frases descritivas: no máximo 25 palavras.
- Parágrafos: no máximo 6 frases e somente um assunto.
- Escreva somente uma instrução em cada frase. Duas ações são permitidas somente quando ocorrem ao mesmo tempo.
- Escreva somente um assunto em cada frase.
- Use a ordem direta: sujeito, verbo, complemento.
- Quando uma condição vem antes de uma ordem, coloque uma vírgula depois da condição. "Se a luz acender, pare o motor."
- Mantenha os artigos, os sujeitos, os verbos e a conjunção "que". Escreva "certifique-se de que o arquivo existe".
- Não use formas coloquiais. Escreva "para", e não "pra". Escreva "está", e não "tá".
- Não use ponto e vírgula. Escreva duas frases.
- Use uma lista vertical para textos complexos. Em uma lista de ordens com "não", escreva "não" de novo em cada item.

## Passo 4: Obedeça às regras de palavra

- Use somente: palavras de `references/vocabulario.md`, nomes técnicos e verbos técnicos.
- Um nome técnico é o nome oficial de uma peça, ferramenta, material, sistema, documento ou termo do seu assunto. Exemplos: "motor", "firewall", "chave de torque", "SKILL.md".
- Use cada palavra com um único sentido. "Verificar" significa "examinar para saber se está correto". Não use "verificar" com o sentido de "acontecer".
- Use um nome para um item no texto inteiro. Não troque o nome do mesmo item.
- Não use mais de três complementos com "de" em sequência. Escreva "a calibração da resistência da conexão", e não "a calibração da resistência da conexão da luz da pista".
- Use o verbo direto, e não um verbo genérico com substantivo. Escreva "remova", e não "efetue a remoção". Escreva "instale", e não "realize a instalação".
- Não use palavras vagas. Escreva a quantidade, o nome ou a ação específica.
- Use a ortografia oficial do português do Brasil (Acordo Ortográfico de 1990).
- Prefira o termo em português quando ele existe e é comum. Escreva "excluir", e não "deletar". Escreva "configurar", e não "setar".
- As substituições frequentes estão em `references/substituicoes.md`.

## Passo 5: Escreva avisos de segurança corretamente

- Use "ADVERTÊNCIA" para um risco de lesão ou de morte de pessoas.
- Use "CUIDADO" para um risco de dano a objetos.
- Use "NOTA" somente para dar informação. Uma nota não dá ordens.
- Comece com uma ordem ou uma condição simples. Depois, diga o risco.
- Exemplo: "ADVERTÊNCIA: Não toque no conector. O conector pode ter uma tensão perigosa."

## Passo 6: Além do texto puro (Beyond Text)

- Quando um procedimento tiver mais de duas condições de decisão, faça um diagrama Mermaid.
- Use `flowchart TD` ou `flowchart LR`.
- Escreva frases curtas e diretas dentro dos nós do diagrama. Não use gerúndio dentro dos diagramas.
- Para diagnóstico e solução de falhas, use uma tabela de três colunas:
  - Coluna 1: Sintoma ou condição encontrada.
  - Coluna 2: Causa provável.
  - Coluna 3: Ação corretiva com verbo no imperativo.

## Passo 7: Filtro anti-slop de modelos de linguagem (Regra Hermes)

Modelos de linguagem usam palavras vazias que consomem tokens e atrapalham a comunicação técnica.
Em equipes de agentes no Hermes, elimine todos os vícios de linguagem:

- Não use saudações ou cortesias: "Certamente!", "Com certeza!", "Olá!", "Com prazer!".
- Não use clichês de transição: "Vale destacar que", "É importante notar que", "Cabe ressaltar que".
- Não use conclusões genéricas: "Espero ter ajudado!", "Em suma", "Fique à vontade para perguntar".
- Não use emojis em procedimentos técnicos ou mensagens entre agentes.
- Comece direto com a resposta técnica e termine logo após o último passo.

## Passo 8: Modo de comparação (Diff) e Protocolo para Agentes no Hermes

Ao revisar textos de usuários ou de outros agentes, apresente a alteração com justificativa:

- Mostre o texto original.
- Mostre o texto revisado em PTS.
- Indique cada regra aplicada e o motivo da mudança.

Ao transferir uma tarefa para outro agente no Hermes (handoff), use a estrutura de quatro campos:

- **Objetivo**: declare a meta em uma frase direta.
- **Status**: informe o estado atual da tarefa.
- **Contexto**: informe os dados técnicos e identificadores.
- **Ação Requerida**: declare a ordem direta para o próximo agente.

## Passo 9: Níveis de rigor

A ferramenta de verificação tem dois níveis de rigor:

- **Modo Pragmático (`--rigor pragmatico`)**: Padrão para software, nuvem e agentes. A ferramenta aceita termos técnicos modernos sem alertas de vocabulário. A ferramenta mantém tolerância zero com gerúndio, voz passiva, frases longas e slop.
- **Modo Estrito (`--rigor estrito`)**: Indicado para manuais industriais e aeroespaciais. A ferramenta compara cada palavra com o vocabulário fechado de `references/vocabulario.md`.

## Passo 10: Ciclo de auto-correção do agente (Self-Linting Loop)

Se você é um agente de inteligência artificial, opere neste ciclo fechado:

1. Escreva o rascunho do texto técnico em PTS.
2. Execute a ferramenta de verificação:
   `python scripts/pts_check.py --rigor pragmatico --formato agente <arquivo>`
3. Leia os erros apontados no relatório.
4. Ajuste cada frase com erro: divida frases longas, remova gerúndios e elimine expressões prolixas.
5. Verifique o texto de novo.
6. Entregue a resposta somente quando a ferramenta indicar zero erros.

Se o seu ambiente não permite executar comandos, aplique a lista de verificação manual abaixo antes de responder.

## Passo 11: Verifique o seu texto

Depois de escrever, verifique o seu texto. Faça estes passos:

1. Se você pode executar scripts, execute: `python scripts/pts_check.py --modo <procedimento|descritivo> --rigor pragmatico <arquivo>`.
2. Se você não pode executar scripts, revise o texto manualmente com a lista abaixo.
3. Corrija cada erro.
4. Verifique o texto de novo. Pare somente quando o texto não tiver erros.

Lista de verificação manual:

- Procure ponto e vírgula e formas coloquiais. Remova-os.
- Procure saudações de cortesia, clichês de transição, conclusões genéricas e emojis. Remova-os.
- Procure palavras terminadas em "-ando", "-endo" e "-indo". Reescreva os gerúndios.
- Procure "tem", "tinha", "havia" e "há" antes de um particípio. Use o pretérito perfeito.
- Procure "deveria", "poderia", "seria", "talvez" e "recomenda-se". Substitua ou remova.
- Procure "ser" + particípio e verbos com "-se" passivo. Coloque o agente como sujeito ou use o imperativo.
- Procure "realizar", "efetuar" e "proceder" antes de um substantivo. Use o verbo direto.
- Conte as palavras das frases mais longas. Divida as frases muito longas.
- Conte as frases de cada parágrafo. Divida os parágrafos com mais de 6 frases.
- Procure palavras que não estão no vocabulário e que não são nomes técnicos. Substitua-as.

A ferramenta de verificação não encontra todos os erros.
A ferramenta não sabe se uma palavra tem o sentido correto.
Você também deve comparar as suas palavras com `references/vocabulario.md`.

## Arquivos de referência

- `references/regras-de-escrita.md`: todas as regras e recomendações, com exemplos. Leia este arquivo quando você reescrever um documento ou quando uma regra não estiver clara.
- `references/vocabulario.md`: o vocabulário recomendado, com classes gramaticais e formas irregulares.
- `references/substituicoes.md`: substituições para palavras frequentes que não são recomendadas, e as categorias de nomes técnicos e de verbos técnicos.
- `examples/antes-depois.md`: exemplos de texto antes e depois da mudança para PTS.
- `examples/comunicacao-agentes-hermes.md`: exemplos de transferência entre agentes no Hermes, diagramas Mermaid e tabelas de diagnóstico.

## Base

O PTS é uma adaptação livre do ASD-STE100 Issue 7 (2017) para o português do Brasil.
O ASD-STE100 é uma especificação para o inglês. Não existe uma versão oficial para o português.
Esta skill não é um documento oficial da ASD.
Esta skill não garante que o seu texto obedece a nenhuma norma oficial.
Consulte NOTICE.md para as informações de direitos autorais.
