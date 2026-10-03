# As regras de escrita do PTS

Este arquivo dá as regras de escrita do Português Técnico Simplificado (PTS) e 5 recomendações gerais.
As regras seguem a estrutura do ASD-STE100 (Issue 7) e usam a mesma numeração quando possível.
As regras não são o texto oficial do ASD-STE100. Nós as adaptamos para a gramática do português do Brasil.
As regras marcadas com **[PT]** não existem no ASD-STE100. Elas tratam de problemas próprios do português.

## Conteúdo

- Seção 1: Palavras (regras 1.1 a 1.17)
- Seção 2: Sequências de complementos (regras 2.1 a 2.3)
- Seção 3: Verbos (regras 3.1 a 3.10)
- Seção 4: Frases (regras 4.1 a 4.6)
- Seção 5: Texto de procedimento (regras 5.1 a 5.5)
- Seção 6: Texto descritivo (regras 6.1 a 6.6)
- Seção 7: Avisos de segurança (regras 7.1 a 7.3)
- Seção 8: Pontuação e contagem de palavras (regras 8.1 a 8.7)
- Seção 9: Práticas de redação (regras 9.1 a 9.4)
- Seção 10: Estruturas visuais e diagramas (regras 10.1 a 10.3)
- Seção 11: Protocolo para agentes no Hermes (regras 11.1 a 11.3)
- Recomendações gerais (RG-1 a RG-5)

Nos exemplos, "Não PTS" mostra um texto incorreto. "PTS" mostra um texto correto.

## Seção 1: Palavras

**Regra 1.1**: Você pode usar somente estas palavras: palavras do vocabulário (`vocabulario.md`), nomes técnicos e verbos técnicos.

**Regra 1.2**: Use cada palavra somente com a classe gramatical que o vocabulário dá.
- Não PTS: "O comprimento é o dobro." ("dobro" como substantivo, mas o vocabulário dá "duas vezes")
- PTS: "O comprimento é duas vezes maior."

**Regra 1.3**: Use cada palavra somente com um sentido. Este sentido é frequentemente mais restrito do que o sentido comum.
- Não PTS: "Verificou-se uma falha no sistema." ("verificar" com o sentido de "ocorrer")
- PTS: "Ocorreu uma falha no sistema."

**Regra 1.4**: Use somente as formas verbais permitidas pela regra 3.2. O vocabulário dá as formas irregulares.

**Regra 1.5**: Você pode usar uma palavra de uma categoria de nomes técnicos. Consulte `substituicoes.md` para as 19 categorias.

**Regra 1.6**: Você pode usar uma palavra que não está no vocabulário somente quando ela é um nome técnico ou parte de um nome técnico.
- Permitido: "a base do triângulo" (termo da matemática).
- Não PTS: "na base da unidade". PTS: "na parte inferior da unidade".

**Regra 1.7**: Não transforme um nome técnico em verbo.
- Não PTS: "Graxe as superfícies de aço."
- PTS: "Aplique graxa nas superfícies de aço."

**Regra 1.8**: Use os nomes técnicos da nomenclatura oficial do seu projeto ou da sua empresa.

**Regra 1.9**: Quando você precisar escolher um nome técnico, escolha um nome curto e fácil de entender.

**Regra 1.10**: Não use gíria ou jargão como nome técnico.
- Não PTS: "Faça um sanduíche com as duas arruelas e o espaçador."
- PTS: "Instale o espaçador entre as duas arruelas."

**Regra 1.11**: Use somente um nome técnico para um item. Não troque de nome.
- Não PTS: "Abra o painel. Depois, feche a tampa." (o painel e a tampa são o mesmo item)
- PTS: "Abra o painel. Depois, feche o painel."

**Regra 1.12**: Você pode usar um verbo de uma categoria de verbos técnicos. Use um verbo do vocabulário se ele existir.
- Não PTS: "Se você detectar fios partidos, conserte-os."
- PTS: "Se você encontrar fios partidos, repare os fios."

**Regra 1.13**: Não transforme um verbo técnico em substantivo genérico. O particípio de um verbo técnico é permitido como adjetivo ("o furo alargado").

**Regra 1.14**: Use a ortografia oficial do português do Brasil, conforme o Acordo Ortográfico de 1990 e o VOLP da Academia Brasileira de Letras. Escreva "ideia", e não "idéia". Escreva "para", e não "pra".

**Regra 1.15** **[PT]**: Prefira o termo em português quando ele existe e é comum na área. Mantenha o termo estrangeiro quando ele é o nome técnico oficial.
- Não PTS: "Delete o arquivo e dê um restart no servidor."
- PTS: "Exclua o arquivo e reinicie o servidor."
- Permitido: "Configure o firewall." ("firewall" é o nome técnico comum)

**Regra 1.16** **[PT]**: Não use palavras de significado vago ou de excesso formal. Consulte `substituicoes.md`.
- Não PTS: "Procede-se à efetivação do aludido procedimento."
- PTS: "Faça este procedimento."

**Regra 1.17** **[PT]** **[Hermes]**: Não use preenchimento vazio, saudações de cortesia, clichês de transição ou emojis em texto técnico.
- Não use aberturas de cortesia como "Certamente!", "Com certeza!" ou "Olá!". Escreva a informação técnica diretamente.
- Não use clichês de transição como "Vale destacar que", "É importante notar que" ou "Cabe ressaltar que". Remova a locução e declare o fato.
- Não use conclusões genéricas como "Espero ter ajudado!" ou "Em suma". Termine o texto logo após a última instrução técnica.
- Não use emojis em procedimentos técnicos ou mensagens entre agentes.
- Não PTS: "Certamente! Vale destacar que o cluster foi criado. Espero ter ajudado!"
- PTS: "O cluster está pronto para uso."

## Seção 2: Sequências de complementos

O inglês junta substantivos em grupos ("runway light connection"). O português liga substantivos com "de", "do", "da", "dos" e "das". Sequências longas de "de" deixam o texto confuso.

**Regra 2.1**: Não use mais de três complementos com "de" em sequência. Divida a frase ou use um nome mais curto.
- Não PTS: "a calibração da resistência da conexão da luz da pista"
- PTS: "a calibração da resistência na conexão das luzes da pista"
- PTS: "Calibre a resistência. A resistência está na conexão das luzes da pista."

**Regra 2.2**: Quando um nome técnico tiver mais de quatro palavras, escreva o nome completo uma vez. Depois, use um nome mais curto ou uma sigla.
- Exemplo: "Unidade de Controle Eletrônico do Motor (UCE)". Depois: "a UCE".

**Regra 2.3**: Use um artigo ("o", "a", "um", "uma") ou um pronome demonstrativo ("este", "esta") antes de um substantivo.
- Não PTS: "Gire eixo."
- PTS: "Gire o eixo."
- Exceção: não use artigo antes de um nome com identificador. Escreva "disjuntor 36L7".

## Seção 3: Verbos

**Regra 3.1**: Use somente as formas verbais regulares ou as formas irregulares que o vocabulário dá.

**Regra 3.2**: Use um verbo somente nestas formas:
- infinitivo ("remover")
- imperativo, na forma de "você" ou "vocês" ("remova", "removam")
- presente do indicativo ("remove")
- pretérito perfeito ("removeu")
- futuro do presente simples ("removerá")
- particípio como adjetivo ("o painel removido")
- futuro do subjuntivo, somente depois de "se" ou "quando" ("se você remover")
- presente do subjuntivo, somente depois de "que" em ordens ("certifique-se de que a válvula esteja fechada").

As outras formas não são permitidas: gerúndio, pretérito imperfeito, pretérito mais-que-perfeito, futuro do pretérito, tempos compostos e mesóclise.

**Regra 3.3**: Use o particípio somente como adjetivo, antes ou depois de um substantivo, ou depois de "estar" e "ficar". Isto mostra um estado e não é voz passiva.
- Permitido: "Os fios estão desconectados."
- Permitido: "Instale o painel removido."

**Regra 3.4**: Não use verbos auxiliares para fazer estruturas verbais complexas.
- Não PTS: "O operador tem ajustado a alavanca." PTS: "O operador ajustou a alavanca."
- Não PTS: "O operador havia ajustado a alavanca." PTS: "O operador ajustou a alavanca."
- Não PTS: "O volume pode ser ajustado." PTS: "Você pode ajustar o volume."
- Não PTS: "A temperatura deve ser ajustada." PTS: "Ajuste a temperatura."

**Regra 3.5** **[PT]**: Não use o gerúndio. Use o gerúndio somente em um nome técnico ou em um título.
- Não PTS: "Fazendo este procedimento, você evita danos."
- PTS: "Quando você faz este procedimento, você evita danos."
- Não PTS: "O sistema está processando os dados." PTS: "O sistema processa os dados."
- Não PTS: "Vamos estar enviando o relatório." PTS: "Nós enviaremos o relatório."

**Regra 3.6**: Use a voz ativa em textos de procedimento. Use a voz ativa o máximo possível em textos descritivos.
- Coloque o agente como sujeito: "Um relé de comutação conecta os circuitos."
- Use o imperativo: "Continue o teste."
- Se não houver agente, use "você" (o leitor) ou "nós" (o autor).
- Não PTS: "Os circuitos são conectados por um relé." PTS: "Um relé conecta os circuitos."

**Regra 3.7**: Use um verbo para mostrar uma ação. Não use um verbo genérico com um substantivo.
- Não PTS: "O ohmímetro fornece uma indicação de 450 ohms." PTS: "O ohmímetro mostra 450 ohms."
- Não PTS: "Efetue a remoção da tampa." PTS: "Remova a tampa."
- Não PTS: "Realize a verificação do nível." PTS: "Verifique o nível."

**Regra 3.8** **[PT]**: Não use a voz passiva com "-se" (passiva sintética) nem o "-se" de sujeito indeterminado em procedimentos. Use o imperativo.
- Não PTS: "Instala-se o filtro." PTS: "Instale o filtro."
- Não PTS: "Recomenda-se desligar a energia." PTS: "Desligue a energia."
- Não PTS: "Deve-se verificar a pressão." PTS: "Verifique a pressão."
- Permitido: verbos que são pronominais por natureza, como "certifique-se" e "afaste-se".

**Regra 3.9** **[PT]**: Use somente "poder" e "dever" como verbos auxiliares de modo.
- "Poder" mostra possibilidade ou capacidade: "O conector pode ter tensão."
- "Dever" mostra obrigação: "O operador deve usar luvas."
- Não use "dever" para probabilidade. Não use "talvez".
  - Não PTS: "O fusível deve estar queimado." Não PTS: "Talvez o fusível esteja queimado."
  - PTS: "Examine o fusível. Se o fusível estiver queimado, substitua o fusível."
- Não use "ter que" ou "ter de". Escreva "deve".
- Não use o futuro do pretérito: "deveria", "poderia", "seria", "teria", "gostaria".

**Regra 3.10** **[PT]**: Em procedimentos, use o imperativo na forma de "você" (terceira pessoa). Não use a forma de "tu". Não misture as duas formas.
- Não PTS: "Abre a tampa e remove o filtro." (forma de "tu")
- PTS: "Abra a tampa. Remova o filtro."

## Seção 4: Frases

**Regra 4.1**: Escreva frases curtas e claras. Dê informações específicas. Escreva um assunto em cada frase.
- Não PTS: "Vazamentos não permitidos."
- PTS: "Certifique-se de que não há vazamentos."

**Regra 4.2**: Mantenha todas as palavras necessárias. Não use formas coloquiais.
- Mantenha o sujeito quando ele não está claro: "Se os calços estiverem instalados, remova os calços." Não: "Se instalados, remova-os."
- Mantenha o verbo, os artigos e a conjunção "que".
- Escreva "para", e não "pra". Escreva "você", e não "cê" ou "vc".

**Regra 4.3**: Use uma lista vertical para textos complexos. Coloque dois-pontos no fim da primeira linha. Em uma lista de ordens com "não", escreva "não" de novo em cada item.

**Regra 4.4**: Use palavras de ligação para conectar frases com assuntos relacionados. Exemplos: "e", "mas", "depois", "então", "assim", "como resultado".

**Regra 4.5** **[PT]**: Use a ordem direta: sujeito, verbo, complemento. Não coloque o sujeito depois do verbo sem necessidade.
- Não PTS: "Ao sistema chegam os dados do sensor."
- PTS: "Os dados do sensor chegam ao sistema."

**Regra 4.6** **[PT]**: Coloque os pronomes oblíquos de forma simples. Não use mesóclise. Se um pronome deixar a frase confusa, repita o substantivo.
- Não PTS: "Instalá-lo-emos depois."
- PTS: "Nós instalaremos o módulo depois."

## Seção 5: Texto de procedimento

**Regra 5.1**: Escreva frases curtas. Use no máximo 20 palavras em cada frase. Este limite também vale para advertências e cuidados.

**Regra 5.2**: Escreva somente uma instrução em cada frase. Duas ou mais ações na mesma frase são permitidas somente quando ocorrem ao mesmo tempo.
- Permitido: "Segure o painel na posição e instale o fixador."

**Regra 5.3**: Escreva cada instrução no imperativo.
- PTS: "Coloque a chave na posição LIGADO."

**Regra 5.4**: Quando uma condição ou uma descrição vem antes de uma ordem, coloque uma vírgula entre as duas.
- PTS: "Quando a luz acender, coloque a chave na posição NORMAL."

**Regra 5.5**: Escreva uma nota somente para dar informação. Uma nota não dá uma instrução nem uma exigência. Se a informação evita dano ou lesão, escreva um cuidado ou uma advertência. Uma nota tem no máximo 25 palavras.

## Seção 6: Texto descritivo

**Regra 6.1**: Dê a informação aos poucos. Escreva um assunto em cada frase.

**Regra 6.2**: Use palavras-chave e palavras de ligação para mostrar a estrutura do texto. Use a mesma palavra-chave na frase seguinte.

**Regra 6.3**: Escreva frases curtas. Use no máximo 25 palavras em cada frase.

**Regra 6.4**: Use parágrafos para agrupar informações relacionadas. Comece cada parágrafo com uma frase de assunto. As outras frases dão mais dados sobre o assunto.

**Regra 6.5**: Escreva somente um assunto em cada parágrafo.

**Regra 6.6**: Escreva no máximo seis frases em cada parágrafo.

## Seção 7: Avisos de segurança

Uma advertência mostra um risco de lesão ou de morte de pessoas. Um cuidado mostra um risco de dano a objetos.

**Regra 7.1**: Use uma palavra aplicável, por exemplo "ADVERTÊNCIA" ou "CUIDADO", para mostrar o nível de risco. Faça uma análise de risco para escolher a palavra correta. Se o seu projeto obedece a uma norma de sinalização (por exemplo, ABNT ou ANSI Z535), use as palavras da norma.

**Regra 7.2**: Comece um aviso de segurança com uma ordem ou uma condição clara e simples.
- PTS: "NÃO ENGULA O SOLVENTE."
- PTS: "QUANDO VOCÊ USAR A TINTA EM SPRAY, APONTE O SPRAY PARA LONGE DO SEU ROSTO."

**Regra 7.3**: Explique o risco ou o resultado possível.
- PTS: "OS SOLVENTES SÃO VENENOSOS E PODEM CAUSAR LESÃO OU MORTE."

## Seção 8: Pontuação e contagem de palavras

**Regra 8.1**: Você pode usar todos os sinais de pontuação do português, menos o ponto e vírgula. Escreva duas frases.

**Regra 8.2**: Use hífen conforme a ortografia oficial. Exemplos: "anel de vedação", "porta-fusível", "micro-ondas", "quarenta e sete".

**Regra 8.3**: Você pode usar parênteses para: referências ("consulte a Figura 1"), números de itens ("as mangueiras (2) e (12)"), siglas ("Tela de Cristal Líquido (LCD)") e explicações curtas.

**Regra 8.4**: Em uma lista vertical, os dois-pontos têm o mesmo efeito de um ponto final na contagem de palavras. Cada item da lista conta como uma nova frase.

**Regra 8.5**: Um texto entre parênteses conta como uma palavra na sua frase. O mesmo texto também conta separadamente como uma frase.

**Regra 8.6**: Cada um destes itens conta como uma palavra: número com unidade, sigla, identificador, texto entre aspas e texto de placa ou título.

**Regra 8.7**: Uma palavra composta com hífen conta como uma palavra. As contrações da gramática ("do", "na", "pelo", "ao") contam como uma palavra.

## Seção 9: Práticas de redação

**Regra 9.1**: Quando uma substituição palavra por palavra não for suficiente, use uma construção diferente. Certifique-se de que a nova frase mantém o sentido correto. O objetivo principal é este: o leitor deve entender cada frase imediatamente.
- Não PTS: "O nível do óleo deve ser visível durante o teste."
- PTS: "Certifique-se de que você pode ver o nível do óleo durante o teste."

**Regra 9.2**: Use cada palavra corretamente. Consulte o sentido restrito antes de usar uma palavra.
- "Verificar" significa somente "examinar para saber se está correto". Escreva "ocorreu uma falha", e não "verificou-se uma falha".
- "Eventualmente" significa "às vezes" em português. Não use com o sentido de "no fim". Escreva "no fim" ou "depois".
- "Através de" significa "de um lado para o outro". Escreva "por meio de" ou "com", e não "através do sistema".

**Regra 9.3**: Não use expressões idiomáticas ou locuções vagas. Use o verbo direto.
- Não PTS: "dar uma olhada no cabo". PTS: "examine o cabo".
- Não PTS: "colocar em funcionamento". PTS: "ligar".
- Não PTS: "levar em consideração". PTS: "considerar".

**Regra 9.4**: Use um estilo consistente. Em procedimentos, use as mesmas palavras para o mesmo tipo de passo e o mesmo nome para o mesmo item. Em textos descritivos, mudanças de construção são permitidas para deixar o texto fácil de ler.

## Seção 10: Estruturas visuais e além do texto puro

**Regra 10.1**: Quando um procedimento ou diagnóstico tiver mais de duas condições de decisão, faça um diagrama Mermaid.
- Use `flowchart TD` ou `flowchart LR`.
- Diagramas facilitam o entendimento de fluxos complexos por humanos e agentes.

**Regra 10.2**: Aplique as regras de escrita do PTS dentro dos nós dos diagramas.
- Escreva frases curtas na ordem direta.
- Não use gerúndio nem voz passiva nos nós dos diagramas.

**Regra 10.3**: Em diagnósticos e solução de falhas, use uma tabela estruturada de três colunas:
- Coluna 1: Sintoma ou condição encontrada.
- Coluna 2: Causa provável da falha.
- Coluna 3: Ação corretiva com verbos no imperativo.

## Seção 11: Protocolo para agentes no Hermes

**Regra 11.1**: Ao transferir tarefas entre agentes no Hermes (handoff), use a estrutura de quatro campos:
- **Objetivo**: declare a meta em uma frase direta.
- **Status**: informe o estado atual da tarefa.
- **Contexto ou Dados**: liste valores e identificadores técnicos.
- **Ação Requerida**: declare a ordem direta no imperativo para o próximo agente.

**Regra 11.2**: Ao revisar textos, apresente a comparação em modo Diff com justificativa:
- Mostre o texto original.
- Mostre o texto revisado em PTS.
- Indique cada regra aplicada e a justificativa da alteração.

**Regra 11.3**: Execute o ciclo de auto-correção do agente (Self-Linting Loop):
1. Escreva o rascunho do texto técnico.
2. Execute a ferramenta de verificação com a linha de comando do projeto.
3. Corrija cada erro apontado no relatório.
4. Verifique o texto de novo.
5. Entregue a resposta somente quando a ferramenta indicar zero erros.

## Recomendações gerais

**RG-1**: Mantenha a conjunção "que" depois de verbos como "certificar-se de" e "mostrar". Escreva "Certifique-se de que a válvula está aberta."

**RG-2**: A preposição "com" pode deixar uma frase confusa. Leia a frase de novo e deixe o sentido explícito.
- Confuso: "Vede a abertura com a ferramenta especificada."
- Claro: "Use a ferramenta especificada para vedar a abertura."

**RG-3**: Se um pronome puder se referir a mais de um substantivo, substitua o pronome pelo substantivo.
- Confuso: "...eles podem ficar danificados." Claro: "...os pinos podem ficar danificados."
- Confuso: "Remova a tampa do painel e limpe-a." Claro: "Remova a tampa do painel. Limpe a tampa."

**RG-4**: Se "isto" ou "isso" puder se referir a mais de uma coisa, repita o contexto completo.
- Claro: "Se a tampa estiver travada, a sonda pode sofrer dano."

**RG-5** **[PT]**: Use "você" como forma de tratamento em todo o texto. Não misture "você", "o usuário" e "o senhor" no mesmo documento.
