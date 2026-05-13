import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

modelo=SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

with open('dados/dados_com_embeddings.json', 'r', encoding='utf-8') as f:
    noticias=json.load(f)

def buscar(query, top_k=3):
    query_embedding=modelo.encode(query)

    resultados=[]

    for noticia in noticias:

        embedding_noticia = np.array(noticia["embedding"])

        similaridade = cosine_similarity(
            [query_embedding],
            [embedding_noticia]
        )[0][0]

        resultados.append({
            "titulo": noticia["titulo"],
            "similaridade": float(similaridade),
            "texto": noticia["texto_limpo"]
        })

    resultados=sorted(
        resultados,
        key=lambda x: x["similaridade"],
        reverse=True
    )

    return resultados[:top_k]

queries=[
    "mudanças na taxa de juros",
    "mercado de trabalho e desemprego",
    "inflação e preços ao consumidor"
]

consultas_resultados={}

for query in queries:

    print("\n" + "=" * 80)
    print(f"CONSULTA: {query}")
    print("=" * 80)

    resultados=buscar(query)

    consultas_resultados[query]=resultados

    for i, resultado in enumerate(resultados, start=1):

        print(f"\nTOP {i}")
        print(f"Título: {resultado['titulo']}")
        print(f"Similaridade: {resultado['similaridade']:.4f}")
        print(f"Trecho: {resultado['texto'][:250]}...")

with open('dados/resultados_consultas.json', 'w', encoding='utf-8') as f:
    json.dump(consultas_resultados, f, ensure_ascii=False, indent=4)

print("\nArquivo 'resultados_consultas.json' salvo com sucesso!")