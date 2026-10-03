#!/usr/bin/env python3
"""test_pts_check.py - Suíte de testes automatizados para o linter PTS."""

import io
import json
import sys
import unittest
from pathlib import Path

# Adiciona o diretório scripts ao path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "scripts"))

import pts_check  # noqa: E402


class TestPtsCheck(unittest.TestCase):

    def _check(self, text, mode="misto", rigor="pragmatico", approved=None):
        report = pts_check.Report()
        pts_check.check_text(text, mode, report, "teste.md", approved=approved, rigor=rigor)
        return report

    def test_frase_limite_palavras_procedimento(self):
        # Frase com 21 palavras em modo procedimento deve acusar erro
        longa = "Instale o suporte de metal na parte frontal da máquina usando os quatro parafusos de aço com cuidado e atenção máxima."
        rep = self._check(longa, mode="procedimento")
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("5.1", regras)

    def test_frase_valida_procedimento(self):
        curta = "Instale o suporte na parte frontal."
        rep = self._check(curta, mode="procedimento")
        self.assertEqual(len(rep.errors), 0)

    def test_ponto_e_virgula(self):
        texto = "Desligue o motor; abra o painel."
        rep = self._check(texto)
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("8.1", regras)

    def test_html_entities_ignora_ponto_e_virgula(self):
        # Entidades HTML como &nbsp; ou &copy; não devem ser tratadas como ponto e vírgula
        texto = "Consulte o manual da máquina &copy; 2026 antes de ligar o motor."
        rep = self._check(texto)
        regras = [r for _, r, _ in rep.errors]
        self.assertNotIn("8.1", regras)

    # --- Regra 1.17: Anti-Slop (Hermes / Karpathy) ---

    def test_slop_abertura_cortesia(self):
        exemplos = [
            "Certamente! Execute o script de instalação.",
            "Com certeza! O serviço está ativo.",
            "Com prazer! Remova o cabo de rede.",
            "Olá! Configure a variável de ambiente.",
            "Bom dia! Reinicie o cluster de servidores.",
            "Claro! O gateway foi configurado.",
            "Perfeito! Os pods estão prontos.",
            "Entendido! Execute a migração do banco.",
            "Aqui está: o resultado da execução.",
        ]
        for ex in exemplos:
            rep = self._check(ex)
            regras = [r for _, r, _ in rep.errors]
            self.assertIn("1.17", regras, f"Falhou para: {ex}")

    def test_slop_transicao_cliche(self):
        exemplos = [
            "Vale destacar que o arquivo está corrompido.",
            "É importante notar que o gateway reiniciou.",
            "Cabe ressaltar que a chave tem vinte caracteres.",
            "É crucial notar que a porta está fechada.",
            "Importante lembrar que a senha expira hoje.",
            "Vale salientar que a memória acabou.",
            "Cumpre destacar que a partição está cheia.",
        ]
        for ex in exemplos:
            rep = self._check(ex)
            regras = [r for _, r, _ in rep.errors]
            self.assertIn("1.17", regras, f"Falhou para: {ex}")

    def test_slop_fechamento_generico(self):
        exemplos = [
            "Espero ter ajudado!",
            "Em suma, a transação terminou.",
            "Em resumo, o serviço está estável.",
            "Fique à vontade para perguntar se precisar.",
            "Qualquer dúvida, estou à disposição.",
            "Fico à disposição.",
            "Espero ter sido útil.",
        ]
        for ex in exemplos:
            rep = self._check(ex)
            regras = [r for _, r, _ in rep.errors]
            self.assertIn("1.17", regras, f"Falhou para: {ex}")

    def test_slop_emoji_proibido(self):
        exemplos = [
            "Execute o procedimento agora. 🚀",
            "Aviso de alta tensão no painel. ⚠️",
            "O teste passou com sucesso. ✅",
            "Dica de configuração da rede. 💡",
        ]
        for ex in exemplos:
            rep = self._check(ex)
            regras = [r for _, r, _ in rep.errors]
            self.assertIn("1.17", regras, f"Falhou para: {ex}")

    def test_slop_em_codigo_ou_aspas_ignorado(self):
        # Exemplos entre aspas ou código não devem gerar erro de slop
        texto = 'Não escreva "Certamente!" ou "Espero ter ajudado!".'
        rep = self._check(texto)
        regras = [r for _, r, _ in rep.errors]
        self.assertNotIn("1.17", regras)

    # --- Regras gramaticais e estruturas complexas (Tolerância Zero) ---

    def test_gerundio_locucao(self):
        texto = "O sistema está processando a imagem."
        rep = self._check(texto)
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("3.5", regras)

    def test_gerundio_isolado_tolerancia_zero(self):
        # Gerúndio em instrução procedural deve ser erro
        texto = "Instale o driver executando o instalador."
        rep = self._check(texto, mode="procedimento")
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("3.5", regras)

    def test_verbo_suporte_tolerancia_zero(self):
        texto = "Efetue a verificação dos cabos de rede."
        rep = self._check(texto, mode="procedimento")
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("3.7", regras)

    def test_passiva_sintetica_com_se(self):
        texto = "Recomenda-se fechar a válvula."
        rep = self._check(texto)
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("3.8", regras)

    def test_passiva_sintetica_generica_tolerancia_zero(self):
        # Qualquer passiva com -se em procedimento deve gerar erro
        texto = "Executa-se o comando de reinicialização."
        rep = self._check(texto, mode="procedimento")
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("3.8", regras)

    def test_futuro_do_preterito_especifico(self):
        texto = "O operador deveria ligar o interruptor."
        rep = self._check(texto)
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("3.9", regras)

    def test_futuro_do_preterito_generico(self):
        texto = "O script executaria o comando automaticamente."
        rep = self._check(texto)
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("3.9", regras)

    def test_tempo_composto(self):
        texto = "O técnico tem verificado o conector."
        rep = self._check(texto)
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("3.4", regras)

    def test_coloquialismo(self):
        texto = "Envie o pacote pra central."
        rep = self._check(texto)
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("4.2", regras)

    def test_palavras_vagas(self):
        texto = "Talvez o sinal esteja oscilando."
        rep = self._check(texto)
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("1.16", regras)

    # --- Rastreamento de linhas e Listas ---

    def test_rastreamento_de_linhas(self):
        texto = "# Título\n\nPrimeiro parágrafo limpo.\n\nSegundo parágrafo com erro; ponto e vírgula."
        rep = self._check(texto)
        locs = [loc for loc, r, _ in rep.errors if r == "8.1"]
        self.assertEqual(len(locs), 1)
        self.assertEqual(locs[0], "teste.md:5")

    def test_lista_multilinha_agrupa_frase(self):
        # Item de lista que quebra em duas linhas deve contar o total de palavras da frase inteira
        texto = """- Esta frase longa de procedimento começa no início do item e continua
  na segunda linha ultrapassando vinte palavras no total para este teste."""
        rep = self._check(texto, mode="procedimento")
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("5.1", regras)

    # --- Formatos e Níveis de Rigor ---

    def test_formato_json(self):
        rep = pts_check.Report()
        rep.error("teste.md:10", "1.17", "emoji detectado")
        d = rep.to_dict()
        self.assertFalse(d["valido"])
        self.assertEqual(d["total_erros"], 1)
        self.assertEqual(d["erros"][0]["regra"], "1.17")

    def test_formato_agente_output(self):
        rep = pts_check.Report()
        rep.error("teste.md:2", "3.5", "gerúndio detectado")
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        try:
            rep.print_agent()
        finally:
            sys.stdout = old_stdout
        out = buffer.getvalue()
        self.assertIn("[ERRO] teste.md:2 (regra 3.5):", out)
        self.assertIn("STATUS: ERRO (1 erros, 0 avisos)", out)

    def test_rigor_estrito_vocabulario(self):
        # No modo estrito, palavras fora do vocabulário são registradas
        approved = {"instale", "o", "motor"}
        texto = "Instale o motor com precisão."
        rep = self._check(texto, rigor="estrito", approved=approved)
        self.assertIn("precisão", rep.unknown)

    # --- Além do texto puro (Mermaid e Tabelas) ---

    def test_blocos_codigo_gerais_ignorados(self):
        # Blocos de código normais (python, bash, etc.) não devem disparar erros de gerúndio ou slop
        texto = """```python
# Certamente! Executando o script
def run():
    print("Olá!")
```

Instale o módulo de rede."""
        rep = self._check(texto)
        self.assertEqual(len(rep.errors), 0)

    def test_mermaid_valido_passa(self):
        texto = """```mermaid
flowchart TD
    A[Início do procedimento] --> B{O pod responde?}
    B -- Sim --> C[Registre o evento no log]
    B -- Não --> D[Reinicie o gateway]
```"""
        rep = self._check(texto)
        self.assertEqual(len(rep.errors), 0)

    def test_mermaid_viola_regra_10_2(self):
        # Gerúndio em nós de Mermaid viola a Regra 10.2
        texto = """```mermaid
flowchart TD
    A[Iniciando o processo] --> B[Finalizando com sucesso]
```"""
        rep = self._check(texto, mode="procedimento")
        regras = [r for _, r, _ in rep.errors]
        self.assertIn("3.5", regras)

    def test_linhas_de_tabela_ignoradas(self):
        texto = """| Coluna 1 | Coluna 2 |
|---|---|
| Iniciando o teste | Executando o script |

Instale o módulo de rede."""
        rep = self._check(texto)
        self.assertEqual(len(rep.errors), 0)

    def test_links_markdown_preservam_texto(self):
        texto = "Consulte a [documentação do sistema](https://exemplo.com) antes de prosseguir."
        rep = self._check(texto)
        self.assertEqual(len(rep.errors), 0)


if __name__ == "__main__":
    unittest.main()
