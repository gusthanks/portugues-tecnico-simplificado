#!/usr/bin/env python3
"""pts_check.py - ferramenta de verificação do Português Técnico Simplificado (PTS).

Esta ferramenta encontra violações das regras de escrita do PTS em texto ou Markdown.
Ela usa somente a biblioteca padrão do Python 3.

Uso:
    python pts_check.py [--modo procedimento|descritivo|misto]
                        [--rigor pragmatico|estrito]
                        [--formato texto|json|agente]
                        [--vocabulario CAMINHO]
                        [--sem-vocabulario]
                        ARQUIVO...

    type rascunho.txt | python pts_check.py --modo procedimento --formato agente

A ferramenta ignora blocos de código, código em linha, URLs, citações e cabeçalho YAML.
Código de saída 0 = sem erros. Código de saída 1 = um ou mais erros.

Adaptado de ste_check.py (simplified-technical-english, de 0xpili, licença MIT).
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

# ------------------------------------------------------------------ constantes

LIMITES = {"procedimento": 20, "descritivo": 25, "misto": 25}

SENT_SPLIT = re.compile(r"(?<=[.!?:])\s+")
WORDISH = re.compile(r"[\w'&/’-]+")
PALAVRA = re.compile(r"[^\W\d_]+(?:-[^\W\d_]+)*")

# Regra 3.5: gerúndio. Palavras que terminam como gerúndio mas não são gerúndio.
NAO_GERUNDIO = {
    "quando", "comando", "brando", "bando", "contrabando", "memorando",
    "nefando", "venerando", "ando", "mando", "demando", "desmando", "abrando",
    "adendo", "dividendo", "minuendo", "subtraendo", "remendo", "estupendo",
    "tremendo", "horrendo", "reverendo", "crescendo", "lindo", "vindo",
    "infindo", "redondo", "hediondo", "entendo", "defendo", "prendo",
    "acendo", "estendo", "pretendo", "suspendo", "dependo", "aprendo",
    "compreendo", "rendo", "ofendo", "fernando", "orlando", "armando",
    "rolando", "rondo",
}
GERUNDIO = re.compile(r"^[^\W\d_]{2,}(?:ando|endo|indo|ondo)$", re.IGNORECASE)

AUX_GERUNDIO = re.compile(
    r"\b(?:estar|está|estão|estou|estamos|estava|estavam|esteve|estará|estarão|"
    r"esteja|estejam|estiver|estiverem|ficar|fica|ficam|ficou|vai|vão|vou|vamos|"
    r"irá|irão|iremos|continua|continuam|continuar|continue|segue|seguem|"
    r"anda|andam|vem|vêm)\s+(?:[^\W\d_]+\s+)?([^\W\d_]+(?:ando|endo|indo|ondo))\b",
    re.IGNORECASE,
)

# Regra 3.4: particípios irregulares mais comuns.
PART_IRREG = (
    r"feit[oa]s?|dit[oa]s?|post[oa]s?|vist[oa]s?|escrit[oa]s?|abert[oa]s?|"
    r"cobert[oa]s?|aceit[oa]s?|entregues?|ganh[oa]s?|gast[oa]s?|pag[oa]s?|"
    r"impress[oa]s?|eleit[oa]s?|pres[oa]s?|solt[oa]s?|mort[oa]s?|aces[oa]s?|"
    r"suspens[oa]s?|extint[oa]s?|express[oa]s?|compost[oa]s?|dispost[oa]s?|"
    r"expost[oa]s?|repost[oa]s?|descrit[oa]s?|frit[oa]s?|sido"
)
PART = rf"(?:[^\W\d_]+(?:ad|id|íd)[oa]s?|{PART_IRREG})"
PART_SING = r"(?:[^\W\d_]+(?:ado|ido|ído)|feito|dito|posto|visto|escrito|aberto|coberto|aceito|entregue|ganho|gasto|pago|impresso|eleito|preso|solto|morto|aceso|suspenso|extinto|expresso|composto|disposto|exposto|reposto|descrito|sido)"

# Substantivos e adjetivos que parecem particípios.
NAO_PARTICIPIO = {
    "cuidado", "cuidados", "sentido", "sentidos", "lado", "lados", "estado",
    "estados", "resultado", "resultados", "dado", "dados", "teclado",
    "teclados", "cadeado", "mercado", "recado", "legado", "soldado", "ruído",
    "ruídos", "ouvido", "partido", "tecido", "fluido", "fluidos", "pedido",
    "pedidos", "significado", "significados", "marido", "vestido", "prado",
    "pecado", "bocado", "senado", "condado", "reinado", "atestado",
    "certificado", "certificados", "comunicado", "mandado", "ido",
}

TER_HAVER = (
    r"(?:tem|têm|tenho|temos|tinha|tinham|tínhamos|tive|teve|tiveram|tivemos|"
    r"terá|terão|teria|teriam|tenha|tenham|tiver|tiverem|tivesse|tivessem|ter|"
    r"tendo|há|hei|havia|haviam|houve|haverá|haveria|haja|hajam|houver|"
    r"houvesse|haver|havendo)"
)
TEMPO_COMPOSTO = re.compile(
    rf"\b{TER_HAVER}\s+(?:não\s+|já\s+|sempre\s+)?({PART_SING})\b", re.IGNORECASE
)

SER = (
    r"(?:é|são|foi|foram|era|eram|será|serão|seria|seriam|seja|sejam|for|forem|"
    r"fosse|fossem|ser|sendo|sido)"
)
PASSIVA_POR = re.compile(
    rf"\b{SER}\s+(?:[^\W\d_]+\s+)?({PART})\s+(?:por|pelo|pela|pelos|pelas)\b",
    re.IGNORECASE,
)
PASSIVA_COMPLEXA = re.compile(
    r"\b(?:deve|devem|deverá|deverão|deveria|deveriam|pode|podem|poderá|poderão|"
    r"poderia|poderiam|precisa|precisam|tem\s+que|têm\s+que|tem\s+de|têm\s+de|"
    r"vai|vão|irá|irão)\s+(?:não\s+)?ser\s+(" + PART + r")\b",
    re.IGNORECASE,
)
PASSIVA_SIMPLES = re.compile(rf"\b{SER}\s+({PART})\b", re.IGNORECASE)

# Regra 3.8: "-se" passivo ou indeterminado.
SE_ERRO = {
    "recomenda", "recomendam", "sugere", "sugerem", "aconselha", "aconselham",
    "deve", "devem", "pode", "podem", "solicita", "solicitam", "pede", "pedem",
    "sabe", "verifica", "verificam", "observa", "observam", "nota", "utiliza",
    "utilizam", "usa", "usam", "faz", "fazem", "tem", "considera", "consideram",
    "espera", "esperam", "precisa", "precisam", "necessita", "necessitam",
    "exige", "exigem", "permite", "permitem", "proíbe", "proíbem", "instala",
    "instalam", "procede", "efetua", "efetuam", "realiza", "realizam",
}
SE_OK = {
    "certifique", "certifiquem", "assegure", "assegurem", "lembre", "lembrem",
    "afaste", "afastem", "mantenha", "mantenham", "dirija", "dirijam",
    "abstenha", "abstenham", "aproxime", "aproximem", "posicione",
    "posicionem", "cadastre", "cadastrem", "inscreva", "inscrevam", "conecte",
    "conectem", "desconecte", "desconectem", "proteja", "protejam", "sente",
    "sentem", "levante", "levantem", "deite", "deitem", "identifique",
    "identifiquem", "acomode", "acomodem", "prepare", "preparem",
}
SE_ENCLITICO = re.compile(r"\b([^\W\d_]+)-se\b", re.IGNORECASE)
SE_PROCLITICO = re.compile(
    r"\b(?:não|que|já|onde|como|também|nunca)\s+se\s+"
    r"(?:recomenda|sugere|aconselha|deve|devem|pode|podem|solicita|pede|"
    r"exige|permite|precisa)\b",
    re.IGNORECASE,
)

# Regra 3.9: futuro do pretérito e pretérito imperfeito.
CONDICIONAL = {
    w + s
    for w in (
        "deveria", "poderia", "seria", "teria", "haveria", "faria", "iria",
        "estaria", "precisaria", "gostaria", "conviria", "recomendaria",
        "diria", "traria", "viria", "daria", "ficaria", "causaria",
        "funcionaria", "aconteceria", "ocorreria", "permitiria", "mostraria",
        "existiria", "afetaria", "resultaria",
    )
    for s in ("", "m")
} | {"deveríamos", "poderíamos", "seríamos", "teríamos", "faríamos", "iríamos"}
CONDICIONAL_GENERICO = re.compile(r"^[^\W\d_]{2,}(?:aria|eria|iria)(?:m)?$|^[^\W\d_]+ríamos$")
NAO_CONDICIONAL = {
    "bateria", "baterias", "galeria", "engenharia", "padaria", "secretaria",
    "portaria", "maquinaria", "carpintaria", "serralheria", "tesouraria",
    "livraria", "joalheria", "cervejaria", "sorveteria", "lavanderia",
    "pizzaria", "loteria", "artilharia", "cavalaria", "infantaria", "ferraria",
    "olaria", "drogaria", "papelaria", "relojoaria", "marcenaria", "funilaria",
    "alvenaria", "tinturaria", "varia", "variam", "avaria", "avarias",
    "contraria", "contrariam", "maria", "ferragem", "hamburgueria",
    "camaria", "chaveiraria", "ourivesaria", "mercearia", "gritaria",
    "concessionaria", "auditoria", "consultoria",
}
IMPERFEITO = {
    "era", "eram", "éramos", "estava", "estavam", "estávamos", "tinha",
    "tinham", "tínhamos", "havia", "haviam", "fazia", "faziam", "podia",
    "podiam", "devia", "deviam", "ia", "iam", "vinha", "vinham", "existia",
    "existiam", "funcionava", "funcionavam", "ficava", "ficavam", "precisava",
    "precisavam", "queria", "queriam", "sabia", "sabiam", "dizia", "diziam",
}
IMPERFEITO_GENERICO = re.compile(r"^[^\W\d_]{2,}(?:avam|ávamos)$")

# Palavras e expressões proibidas ou não recomendadas.
VAGAS = {
    "talvez": "escreva o fato ou a condição",
    "possivelmente": "escreva o fato ou a condição",
    "provavelmente": "escreva o fato ou a condição",
    "eventualmente": "use \"às vezes\" ou \"no fim\"",
    "convém": "use o imperativo",
    "outrossim": "use \"também\"",
    "ademais": "use \"também\"",
    "supracitado": "repita o nome do item",
    "supracitada": "repita o nome do item",
    "aludido": "repita o nome do item",
    "aludida": "repita o nome do item",
    "mediante": "use \"com\" ou \"por meio de\"",
    "utilizar": "use \"usar\"",
    "possuir": "use \"ter\"",
}
TER_QUE = re.compile(r"\b(?:ter|tem|têm|temos|tenho|teve|terá|tenha|tenham)\s+(?:que|de)\s+[^\W\d_]+(?:ar|er|ir|or)\b", re.IGNORECASE)
COLOQUIAL = {
    "pra", "pras", "pro", "pros", "tá", "tô", "cê", "né", "vc", "vcs", "tb",
    "tbm", "pq", "blz", "q", "td", "tds", "msm", "ñ",
}
MESOCLISE = re.compile(
    r"\b[^\W\d_]+-(?:me|te|se|lhe|lhes|nos|vos|o|a|os|as|lo|la|los|las)-"
    r"(?:ei|ás|á|emos|eis|ão|ia|ias|íamos|íeis|iam)\b",
    re.IGNORECASE,
)
VERBO_SUPORTE = re.compile(
    r"\b(?:realiz|efetu|execut|proced|promov|providenci|fa[zç]|fiz|fe[zi])[^\W\d_]*\s+"
    r"(?:a|o|as|os|à|ao|às|aos|uma|um)\s+([^\W\d_]+(?:ção|ções|mento|mentos|agem|agens|são|sões))\b",
    re.IGNORECASE,
)
NAO_SUPORTE = {
    "procedimento", "procedimentos", "documento", "documentos", "equipamento",
    "equipamentos", "versão", "sessão", "conexão",
}
CADEIA_DE = re.compile(
    r"(?:\b(?:de|do|da|dos|das)\s+[^\W\d_]+\s+){3}(?:de|do|da|dos|das)\s+[^\W\d_]+",
    re.IGNORECASE,
)

# Regra 1.17: Filtro anti-slop e economia de tokens de IA (Hermes / Karpathy)
SLOP_ABERTURA = re.compile(
    r"^(?:"
    r"certamente|"
    r"com\s+certeza|"
    r"com\s+prazer|"
    r"com\s+todo\s+o\s+prazer|"
    r"olá|"
    r"oi|"
    r"saudações|"
    r"como\s+uma?\s+(?:ia|modelo\s+de\s+linguagem|assistente)|"
    r"claro\s+que\s+sim|"
    r"sem\s+dúvida"
    r")(?:\s*[,!.]|\s*$)",
    re.IGNORECASE,
)

SLOP_TRANSICAO = re.compile(
    r"\b(?:"
    r"vale\s+(?:destacar|ressaltar|lembrar|notar|pontuar|mencionar|frisar)|"
    r"é\s+(?:importante|crucial|fundamental|essencial|relevante|válido|vital)\s+(?:notar|destacar|ressaltar|lembrar|frisar|mencionar|pontuar|ter\s+em\s+mente)|"
    r"cabe\s+(?:destacar|ressaltar|lembrar|notar|mencionar|pontuar)|"
    r"importante\s+(?:notar|destacar|ressaltar|lembrar|frisar|mencionar)|"
    r"convém\s+(?:notar|lembrar|destacar|ressaltar)"
    r")\s+que\b",
    re.IGNORECASE,
)

SLOP_FECHAMENTO = re.compile(
    r"\b(?:"
    r"em\s+suma|"
    r"espero\s+(?:ter\s+ajudado|que\s+(?:isso\s+)?ajude)|"
    r"(?:fique|sinta-se)\s+à\s+vontade\s+para|"
    r"estou\s+à\s+disposição|"
    r"(?:se|caso)\s+(?:você\s+)?(?:tiver|tenha)\s+(?:alguma\s+)?dúvida|"
    r"qualquer\s+dúvida[,\s]|"
    r"restou\s+alguma\s+dúvida"
    r")\b",
    re.IGNORECASE,
)

# ------------------------------------------------------------------ auxiliares


def contem_emoji(texto):
    """Detecta emojis em texto técnico."""
    for ch in texto:
        cp = ord(ch)
        if 0x1F300 <= cp <= 0x1FAFF or 0x2600 <= cp <= 0x27BF or 0xFE00 <= cp <= 0xFE0F:
            return True
        if unicodedata.category(ch) in ("So", "Sk") and cp > 0x2000:
            return True
    return False


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def tem_acento(s):
    return s != sem_acento(s)


def parece_participio(w):
    lw = w.lower()
    if lw in NAO_PARTICIPIO:
        return False
    # "válido", "rápido", "líquido": acento antes de "-ido" indica adjetivo.
    base = re.sub(r"(?:ído|ída|ídos|ídas)$", "", lw)
    if tem_acento(base):
        return False
    return True


def strip_markdown(text):
    """Remove as partes do texto que as regras do PTS não controlam."""
    text = text.replace("\r\n", "\n")
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)  # YAML
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)  # blocos de código
    text = re.sub(r"`[^`\n]+`", " CODE ", text)  # código em linha
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links
    text = re.sub(r"https?://\S+", " URL ", text)  # URLs
    text = re.sub(r"^>.*$", " ", text, flags=re.MULTILINE)  # citações
    # texto entre aspas conta como uma palavra e não é controlado (regra 8.6)
    text = re.sub(r"\"[^\"\n]*\"|“[^”\n]*”|«[^»\n]*»", " QUOTED ", text)
    return text


def clean_markdown_lines(raw_text):
    """Substitui blocos não controlados por linhas vazias mantendo os números de linha exatos."""
    raw_text = raw_text.replace("\r\n", "\n")
    lines = raw_text.split("\n")
    cleaned = []
    in_yaml = False
    in_code = False

    for idx, line in enumerate(lines):
        stripped = line.strip()
        # Cabeçalho YAML
        if idx == 0 and stripped == "---":
            in_yaml = True
            cleaned.append("")
            continue
        if in_yaml:
            if stripped == "---":
                in_yaml = False
            cleaned.append("")
            continue

        # Blocos de código
        if stripped.startswith("```"):
            in_code = not in_code
            cleaned.append("")
            continue
        if in_code:
            cleaned.append("")
            continue

        # Citações (regra: ignora citações)
        if stripped.startswith(">"):
            cleaned.append("")
            continue

        # Linha de texto comum
        l = line
        l = re.sub(r"`[^`\n]+`", " CODE ", l)
        l = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", l)
        l = re.sub(r"https?://\S+", " URL ", l)
        l = re.sub(r"^>\s?", " ", l)
        l = re.sub(r"\"[^\"\n]*\"|“[^”\n]*”|«[^»\n]*»", " QUOTED ", l)
        cleaned.append(l)

    return cleaned


def count_words(sentence):
    """Conta palavras com as convenções da seção 8."""
    s = re.sub(r"\([^)]*\)", " PAREN ", sentence)  # regra 8.5
    s = re.sub(r"\*\*|\*|__|_|#+", " ", s)  # marcas de Markdown
    return len(WORDISH.findall(s))  # palavra com hífen = 1 (regra 8.7)


def iter_sentences(block):
    for part in SENT_SPLIT.split(block):
        part = part.strip()
        if part and (WORDISH.search(part) or contem_emoji(part)):
            yield part


# ------------------------------------------------------------------ vocabulário


def _plurais(w):
    if w.endswith("ão"):
        return {w[:-2] + "ões", w[:-2] + "ães", w + "s"}
    if w[-1] in "aeiouáéíóúâêôã":
        return {w + "s"}
    if w.endswith("m"):
        return {w[:-1] + "ns"}
    if w.endswith(("r", "z")):
        return {w + "es"}
    if w.endswith("n"):
        return {w + "s", w + "es"}
    if w.endswith("s"):
        return {w, sem_acento(w[-2:]).join([w[:-2], ""]) + "es"}
    if w.endswith("al") or w.endswith("ul"):
        return {w[:-1] + "is"}
    if w.endswith("el"):
        return {w[:-2] + "éis", w[:-2] + "eis"}
    if w.endswith("ol"):
        return {w[:-2] + "óis"}
    if w.endswith("il"):
        return {w[:-1] + "s", w[:-2] + "eis"}
    if w.endswith("x"):
        return {w}
    return {w + "s"}


def _flexionar(w, cls):
    out = {w} | _plurais(w)
    if cls in ("adj", "num", "pron"):
        fems = []
        if w.endswith("o"):
            fems.append(w[:-1] + "a")
        elif w.endswith("or"):
            fems.append(w + "a")
        elif w.endswith("ês"):
            fems.append(w[:-2] + "esa")
        elif w.endswith("ão"):
            fems.append(w[:-2] + "ã")
        for f in fems:
            out |= {f} | _plurais(f)
        if cls == "adj":
            base = fems[0] if fems else w
            out.add(sem_acento(base) + "mente")
    return out


def _conjugar(inf):
    """Gera as formas permitidas (regra 3.2) de um verbo regular."""
    out = {inf}
    if inf.endswith(("por", "pôr")) or len(inf) < 3:
        return out
    s, t = inf[:-2], inf[-2:]
    if t == "ar":
        se = s
        if s.endswith("c"):
            se = s[:-1] + "qu"
        elif s.endswith("g"):
            se = s + "u"
        elif s.endswith("ç"):
            se = s[:-1] + "c"
        out |= {s + x for x in ("o", "a", "am", "amos", "ou", "aram", "ará", "arão",
                                "aremos", "arei", "ar", "arem", "armos",
                                "ado", "ada", "ados", "adas")}
        out |= {se + x for x in ("ei", "e", "em", "emos")}
    elif t == "er":
        sa = s
        if s.endswith("c"):
            sa = s[:-1] + "ç"
        elif s.endswith("g"):
            sa = s[:-1] + "j"
        out |= {s + x for x in ("e", "em", "emos", "i", "eu", "eram", "erá", "erão",
                                "eremos", "erei", "er", "erem", "ermos",
                                "ido", "ida", "idos", "idas")}
        out |= {sa + x for x in ("o", "a", "am", "amos")}
    elif t == "ir":
        if s.endswith("u") and not s.endswith(("gu", "qu")):
            out |= {s + x for x in ("o", "i", "em", "ímos", "í", "iu", "íram", "irá",
                                    "irão", "iremos", "irei", "a", "am", "amos",
                                    "ir", "írem", "irmos", "ído", "ída", "ídos", "ídas")}
            return out
        sa = s
        if s.endswith(("gu", "qu")):
            sa = s[:-1]
        elif s.endswith("g"):
            sa = s[:-1] + "j"
        elif s.endswith("c"):
            sa = s[:-1] + "ç"
        out |= {s + x for x in ("e", "em", "imos", "i", "iu", "iram", "irá", "irão",
                                "iremos", "irei", "ir", "irem", "irmos",
                                "ido", "ida", "idos", "idas")}
        out |= {sa + x for x in ("o", "a", "am", "amos")}
    return out


def load_word_list(path):
    """Lê vocabulario.md e devolve o conjunto de formas permitidas."""
    approved = set()
    line_re = re.compile(r"^([^\W\d_a-zà-ÿ][^a-zà-ÿ\[\]()]*?)\s+\(([a-z, ]+)\)(?:\s+\[(.*?)\])?\s*$")
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = line_re.match(line.strip())
        if not m:
            continue
        head, classes, forms = m.groups()
        head = head.strip().lower()
        words = head.split()
        for w in words:
            approved.add(w)
        cls_list = [c.strip() for c in classes.split(",")]
        if forms:
            for f in forms.split(","):
                for w in f.strip().lower().split():
                    approved.add(w)
                    approved |= _plurais(w) if not w.endswith("s") else {w}
        for cls in cls_list:
            for w in words:
                if cls == "v":
                    approved |= _conjugar(w)
                elif cls in ("s", "adj", "num", "pron"):
                    approved |= _flexionar(w, cls)
    return approved


CLITICOS = {"o", "a", "os", "as", "lo", "la", "los", "las", "no", "na", "nos",
            "nas", "me", "te", "se", "lhe", "lhes", "vos"}
INF_ACENTO = {"á": "ar", "ê": "er", "í": "ir", "ô": "or"}


def palavra_aprovada(lw, approved):
    if lw in approved or len(lw) <= 1:
        return True
    partes = [p for p in lw.split("-") if p]
    if len(partes) > 1 and partes[-1] in CLITICOS:
        base = partes[0]
        if partes[-1] in ("lo", "la", "los", "las"):
            if base[-1] in INF_ACENTO:
                base = base[:-1] + INF_ACENTO[base[-1]]
            elif base.endswith("i"):
                base = base + "r"
        return base in approved
    return all(p in approved for p in partes)


# ------------------------------------------------------------------ verificações


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.unknown = {}

    def error(self, loc, rule, msg):
        self.errors.append((loc, rule, msg))

    def warn(self, loc, rule, msg):
        self.warnings.append((loc, rule, msg))

    def to_dict(self):
        return {
            "valido": len(self.errors) == 0,
            "total_erros": len(self.errors),
            "total_avisos": len(self.warnings),
            "erros": [
                {"local": loc, "regra": rule, "tipo": "erro", "mensagem": msg}
                for loc, rule, msg in self.errors
            ],
            "avisos": [
                {"local": loc, "regra": rule, "tipo": "aviso", "mensagem": msg}
                for loc, rule, msg in self.warnings
            ],
            "palavras_desconhecidas": sorted(self.unknown, key=self.unknown.get, reverse=True) if self.unknown else [],
        }

    def print_text(self, rigor="pragmatico"):
        for loc, rule, msg in self.errors:
            print(f"ERRO    {loc} [regra {rule}] {msg}")
        for loc, rule, msg in self.warnings:
            print(f"AVISO   {loc} [regra {rule}] {msg}")
        if self.unknown and rigor == "estrito":
            words = sorted(self.unknown, key=self.unknown.get, reverse=True)
            print(f"\nCONFERIR {len(words)} palavras não estão no vocabulário.")
            print("         Cada uma deve ser um nome técnico ou um verbo técnico:")
            for chunk in [words[i:i + 10] for i in range(0, len(words), 10)]:
                print("         " + ", ".join(chunk))

        print(f"\nResultado: {len(self.errors)} erros, {len(self.warnings)} avisos.")
        if not self.errors:
            print("O texto obedece às regras estruturais do PTS que esta ferramenta pode verificar.")
            print("Esta ferramenta não sabe se cada palavra tem o sentido correto.")

    def print_agent(self, rigor="pragmatico"):
        for loc, rule, msg in self.errors:
            print(f"[ERRO] {loc} (regra {rule}): {msg}")
        for loc, rule, msg in self.warnings:
            print(f"[AVISO] {loc} (regra {rule}): {msg}")
        if self.unknown and rigor == "estrito":
            words = sorted(self.unknown, key=self.unknown.get, reverse=True)
            amostra = ", ".join(words[:15])
            print(f"[INFO] {len(words)} palavras fora do vocabulário: {amostra}")
        if not self.errors and not self.warnings:
            print("STATUS: OK (0 erros, 0 avisos)")
        elif not self.errors:
            print(f"STATUS: OK_COM_AVISOS (0 erros, {len(self.warnings)} avisos)")
        else:
            print(f"STATUS: ERRO ({len(self.errors)} erros, {len(self.warnings)} avisos)")

    def print_json(self):
        print(json.dumps(self.to_dict(), ensure_ascii=False, indent=2))


def check_sentence(sent, mode, report, loc):
    limit = LIMITES[mode]
    n = count_words(sent)
    head = sent if len(sent) <= 60 else sent[:57] + "..."

    # Limites de palavras
    if n > 25:
        report.error(loc, "5.1/6.3", f"frase com {n} palavras (máx. {limit}): \"{head}\"")
    elif n > 20:
        if mode == "procedimento":
            report.error(loc, "5.1", f"frase com {n} palavras (máx. 20): \"{head}\"")
        elif mode == "misto":
            report.warn(loc, "5.1", f"frase com {n} palavras (máx. 20 em procedimento): \"{head}\"")

    # Ponto e vírgula
    if ";" in sent:
        report.error(loc, "8.1", f"ponto e vírgula: \"{head}\". Escreva duas frases.")

    # Regra 1.17: Filtro anti-slop e economia de tokens (Hermes / Karpathy)
    if contem_emoji(sent):
        report.error(loc, "1.17", f"emoji detectado: \"{head}\". Não use emojis em procedimentos ou comunicação técnica.")

    m_abertura = SLOP_ABERTURA.search(sent.strip())
    if m_abertura:
        report.error(loc, "1.17", f"abertura de cortesia \"{m_abertura.group(0).strip()}\": seja direto, remova a saudação.")

    m_trans = SLOP_TRANSICAO.search(sent)
    if m_trans:
        report.error(loc, "1.17", f"clichê de transição \"{m_trans.group(0)}\": remova o meta-comentário e escreva o fato diretamente.")

    m_fech = SLOP_FECHAMENTO.search(sent)
    if m_fech:
        report.error(loc, "1.17", f"fechamento prolixo \"{m_fech.group(0)}\": remova a frase vazia.")

    # Estruturas verbais complexas
    m = TEMPO_COMPOSTO.search(sent)
    if m and parece_participio(m.group(1)):
        report.error(loc, "3.4", f"tempo composto \"{m.group(0)}\": use o pretérito perfeito.")

    m = PASSIVA_COMPLEXA.search(sent)
    if m and parece_participio(m.group(1)):
        report.error(loc, "3.4", f"passiva complexa \"{m.group(0)}\": use o imperativo ou a voz ativa.")
    else:
        m = PASSIVA_POR.search(sent)
        if m and parece_participio(m.group(1)):
            report.error(loc, "3.6", f"voz passiva \"{m.group(0)}\": coloque o agente como sujeito.")
        else:
            m = PASSIVA_SIMPLES.search(sent)
            if m and parece_participio(m.group(1)):
                fn = report.error if mode == "procedimento" else report.warn
                fn(loc, "3.6", f"\"ser\" + particípio \"{m.group(0)}\": use a voz ativa. Para um estado, use \"estar\".")

    m = AUX_GERUNDIO.search(sent)
    if m and m.group(1).lower() not in NAO_GERUNDIO:
        report.error(loc, "3.5", f"locução com gerúndio \"{m.group(0)}\": use um tempo simples.")

    for m in SE_ENCLITICO.finditer(sent):
        verbo = m.group(1).lower()
        if verbo in SE_ERRO:
            report.error(loc, "3.8", f"\"{m.group(0)}\": não use \"-se\" passivo. Use o imperativo.")
        elif verbo not in SE_OK:
            fn = report.warn if mode != "descritivo" else None
            if fn:
                fn(loc, "3.8", f"\"{m.group(0)}\": confirme que não é voz passiva com \"-se\".")
    m = SE_PROCLITICO.search(sent)
    if m:
        report.error(loc, "3.8", f"\"{m.group(0)}\": não use \"se\" indeterminado. Use o imperativo.")

    m = TER_QUE.search(sent)
    if m:
        report.error(loc, "3.9", f"\"{m.group(0)}\": use \"deve\" + infinitivo.")

    m = MESOCLISE.search(sent)
    if m:
        report.error(loc, "4.6", f"mesóclise \"{m.group(0)}\": reescreva com o substantivo.")

    m = VERBO_SUPORTE.search(sent)
    if m and m.group(1).lower() not in NAO_SUPORTE:
        report.warn(loc, "3.7", f"verbo genérico + substantivo \"{m.group(0)}\": use o verbo direto.")

    m = CADEIA_DE.search(sent)
    if m:
        report.warn(loc, "2.1", f"mais de três complementos com \"de\": \"{m.group(0)}\".")

    for word in PALAVRA.findall(sent):
        if word.isupper() and len(word) > 1:
            continue  # sigla, placa ou aviso em maiúsculas
        lw = word.lower()
        if lw in COLOQUIAL:
            report.error(loc, "4.2", f"forma coloquial \"{word}\": escreva a palavra completa.")
        elif lw in CONDICIONAL:
            report.error(loc, "3.9", f"futuro do pretérito \"{word}\": use o presente, \"deve\" ou \"pode\".")
        elif lw in IMPERFEITO:
            report.error(loc, "3.2", f"pretérito imperfeito \"{word}\": use o presente ou o pretérito perfeito.")
        elif lw in VAGAS:
            report.error(loc, "1.16", f"\"{word}\" não é recomendado: {VAGAS[lw]}.")
        elif CONDICIONAL_GENERICO.match(lw) and lw not in NAO_CONDICIONAL:
            report.warn(loc, "3.9", f"\"{word}\": confirme que não é futuro do pretérito.")
        elif IMPERFEITO_GENERICO.match(lw):
            report.warn(loc, "3.2", f"\"{word}\": confirme que não é pretérito imperfeito.")
        elif GERUNDIO.match(lw) and lw not in NAO_GERUNDIO:
            report.warn(loc, "3.5", f"\"{word}\": o gerúndio é permitido somente em um nome técnico.")


def check_vocab(text, report, approved):
    for word in PALAVRA.findall(text):
        if word.isupper() or any(c.isupper() for c in word[1:]):
            continue  # sigla, identificador ou texto de placa
        lw = word.lower()
        if palavra_aprovada(lw, approved):
            continue
        report.unknown[lw] = report.unknown.get(lw, 0) + 1


def check_paragraph(par, mode, report, loc, approved):
    sents = list(iter_sentences(par))
    if len(sents) > 6:
        report.error(loc, "6.6", f"parágrafo com {len(sents)} frases (máx. 6).")
    for s in sents:
        check_sentence(s, mode, report, loc)
    if approved:
        check_vocab(par, report, approved)


def check_text(raw_text, mode, report, name, approved, rigor="pragmatico"):
    cleaned_lines = clean_markdown_lines(raw_text)
    bullet = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+(.*)")

    i = 0
    n_lines = len(cleaned_lines)
    while i < n_lines:
        line = cleaned_lines[i]
        stripped = line.strip()

        # Linha vazia, cabeçalho markdown (#) ou tabela (|) conta como título
        if not stripped or stripped.startswith("#") or stripped.startswith("|"):
            i += 1
            continue

        # Item de lista vertical (regra 8.4)
        m_bullet = bullet.match(line)
        if m_bullet:
            item_text = m_bullet.group(1).strip()
            loc = f"{name}:{i + 1}"
            for s in iter_sentences(item_text):
                check_sentence(s, mode, report, loc)
            if approved and rigor == "estrito":
                check_vocab(item_text, report, approved)
            i += 1
            continue

        # Parágrafo contínuo
        par_start = i + 1
        par_parts = []
        while i < n_lines:
            curr = cleaned_lines[i]
            curr_strip = curr.strip()
            if not curr_strip or curr_strip.startswith("#") or curr_strip.startswith("|") or bullet.match(curr):
                break
            par_parts.append(curr.strip())
            i += 1

        par_text = " ".join(par_parts)
        if par_text and WORDISH.search(par_text):
            loc = f"{name}:{par_start}"
            check_paragraph(par_text, mode, report, loc, approved if rigor == "estrito" else None)


# ------------------------------------------------------------------ principal


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Verifica um texto com as regras de escrita do PTS.")
    ap.add_argument("arquivos", nargs="*", help="arquivos para verificar (padrão: entrada padrão)")
    ap.add_argument("--modo", choices=["procedimento", "descritivo", "misto"],
                    default="misto", help="tipo de texto (padrão: misto)")
    ap.add_argument("--rigor", choices=["estrito", "pragmatico"],
                    default="pragmatico", help="nível de rigor: pragmatico (software/agentes, padrão) ou estrito (indústria/aeroespacial)")
    ap.add_argument("--formato", choices=["texto", "json", "agente"],
                    default="texto", help="formato de saída: texto (padrão), json ou agente")
    ap.add_argument("--vocabulario", default=None,
                    help="caminho para vocabulario.md (padrão: ../references/vocabulario.md)")
    ap.add_argument("--sem-vocabulario", action="store_true",
                    help="não compara as palavras com o vocabulário")
    args = ap.parse_args()

    rigor = args.rigor
    if args.sem_vocabulario:
        rigor = "pragmatico"

    approved = None
    if rigor == "estrito":
        wl = args.vocabulario
        if wl is None:
            default = Path(__file__).resolve().parent.parent / "references" / "vocabulario.md"
            wl = default if default.exists() else None
        if wl:
            approved = load_word_list(wl)

    report = Report()
    if args.arquivos:
        for f in args.arquivos:
            p = Path(f)
            if not p.exists():
                print(f"Erro: arquivo não encontrado: {f}", file=sys.stderr)
                return 1
            check_text(p.read_text(encoding="utf-8"), args.modo, report, f, approved, rigor=rigor)
    else:
        data = sys.stdin.buffer.read().decode("utf-8", errors="replace")
        check_text(data, args.modo, report, "entrada", approved, rigor=rigor)

    if args.formato == "json":
        report.print_json()
    elif args.formato == "agente":
        report.print_agent(rigor=rigor)
    else:
        report.print_text(rigor=rigor)

    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
