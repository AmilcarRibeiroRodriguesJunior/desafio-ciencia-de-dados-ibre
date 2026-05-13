import json
from sentence_transformers import SentenceTransformer

# Arquivos
ARQUIVO_ENTRADA = "dados/dados_limpos.json"
ARQUIVO_SAIDA = "dados/dados_com_embeddings.json"

modelo=SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as f:
    noticias=json.load(f)

for noticia in noticias:

    texto=noticia["texto_limpo"]

    embedding=modelo.encode(texto)

    noticia["embedding"]=embedding.tolist()

with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
    json.dump(noticias, f, ensure_ascii=False, indent=4)

print("Arquivo 'dados_com_embeddings.json' salvo com sucesso!")