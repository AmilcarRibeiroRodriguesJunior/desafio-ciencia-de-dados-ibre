import json
import re
import html
from bs4 import BeautifulSoup

# Arquivos
ARQUIVO_ENTRADA = "dados/noticias_brutas.json"
ARQUIVO_SAIDA = "dados/dados_limpos.json"


def limpar_texto(texto):

    texto=html.unescape(texto)

    texto=BeautifulSoup(texto, "html.parser").get_text(separator=" ")

    padroes_metadados=[
        r"Publicado em:\s*\d{2}/\d{2}/\d{4}(?:\s*às\s*\d{2}h\d{2})?",
        r"\d{2}/\d{2}/\d{4}\s*[-—]\s*\d{2}h\d{2}",
        r"\d{2}/\d{2}/\d{4}",
        r"Nota à Imprensa",
        r"Mercados"
    ]

    for padrao in padroes_metadados:
        texto=re.sub(padrao, "", texto, flags=re.IGNORECASE)

    texto=re.sub(r"http\S+|www\.\S+", "", texto)

    texto=re.sub(r"\s+", " ", texto)

    texto=texto.strip()

    return texto


def texto_valido(texto, minimo_caracteres=30):
    return len(texto) >= minimo_caracteres

with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as f:
    noticias = json.load(f)

dados_limpos=[]

for noticia in noticias:

    texto_limpo=limpar_texto(noticia["texto"])

    noticia_tratada = {
        "id": noticia["id"],
        "titulo": noticia["titulo"],
        "texto_limpo": texto_limpo,
        "data": noticia["data"],
        "fonte": noticia["fonte"],
        "texto_valido": texto_valido(texto_limpo)
    }

    dados_limpos.append(noticia_tratada)

with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
    json.dump(dados_limpos, f, ensure_ascii=False, indent=4)

print("Arquivo 'dados_limpos.json' salvo com sucesso!")