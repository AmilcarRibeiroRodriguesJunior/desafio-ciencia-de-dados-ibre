# Motor de Busca Semântico para Notícias Econômicas

## Descrição do Projeto

Este projeto implementa um pipeline completo de processamento textual utilizando técnicas de NLP (Natural Language Processing) aplicadas a notícias fictícias sobre a economia brasileira.

O sistema foi dividido em três etapas principais:

1. Limpeza e tratamento dos textos;
2. Geração de embeddings semânticos;
3. Implementação de um motor de busca semântico.

O objetivo é permitir que consultas em linguagem natural recuperem automaticamente as notícias mais relevantes do corpus com base em similaridade semântica.

---

# Estrutura do Projeto

```plaintext
desafio-ciencia-de-dados-ibre/
│
├── dados/
│   ├── noticias_brutas.json
│   ├── dados_limpos.json
│   ├── dados_com_embeddings.json
│   └── resultados_consultas.json
│
├── src/
│   ├── etapa1_limpeza.py
│   ├── etapa2_embeddings.py
│   └── etapa3_busca.py
│
├── requirements.txt
│
└── README.md
```

---

# Tecnologias Utilizadas

- Python
- BeautifulSoup
- Sentence Transformers
- Scikit-Learn
- NumPy

---

# Etapa 1 — Limpeza e Tratamento de Texto

Nesta etapa foi realizado o pré-processamento dos textos presentes no arquivo 'noticias_brutas.json'.

O tratamento incluiu:

- remoção de tags HTML;
- remoção de entidades HTML;
- remoção de URLs;
- remoção de timestamps e metadados;
- remoção de múltiplos espaços e quebras de linha;
- padronização textual.

Além disso, foi criada uma validação simples para identificar conteúdos muito curtos.

O resultado do processamento foi salvo em:

```plaintext
dados/dados_limpos.json
```

---

# Etapa 2 — Geração de Embeddings

Após a limpeza dos textos, foi utilizada a biblioteca Sentence Transformers para gerar embeddings semânticos.

## Modelo Escolhido

```plaintext
paraphrase-multilingual-MiniLM-L12-v2
```

## Justificativa da Escolha

O modelo foi escolhido porque:

- possui suporte multilíngue, incluindo português;
- apresenta ótimo desempenho em tarefas de similaridade semântica;
- é leve e eficiente computacionalmente;
- gera embeddings densos de 384 dimensões;
- é amplamente utilizado em aplicações de NLP.

Cada notícia foi convertida em um vetor numérico e armazenada no arquivo:

```plaintext
dados/dados_com_embeddings.json
```

---

# Etapa 3 — Motor de Busca Semântico

Foi implementado um motor de busca baseado em similaridade semântica utilizando embeddings vetoriais.

A busca funciona da seguinte forma:

1. A consulta do usuário é transformada em embedding;
2. O embedding da consulta é comparado com os embeddings das notícias;
3. A similaridade é calculada utilizando Cosine Similarity;
4. O sistema retorna os artigos mais semanticamente relevantes.

As seguintes consultas foram utilizadas para validação:

```plaintext
"mudanças na taxa de juros"
"mercado de trabalho e desemprego"
"inflação e preços ao consumidor"
```

Os resultados foram armazenados em:

```plaintext
dados/resultados_consultas.json
```

---

# Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

---

## 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 3. Executar a Etapa 1 — Limpeza

```bash
python src/etapa1_limpeza.py
```

Esse script irá gerar:

```plaintext
dados/dados_limpos.json
```

---

## 4. Executar a Etapa 2 — Embeddings

```bash
python src/etapa2_embeddings.py
```

Esse script irá gerar:

```plaintext
dados/dados_com_embeddings.json
```

---

## 5. Executar a Etapa 3 — Busca Semântica

```bash
python src/etapa3_busca.py
```

Esse script irá:

- executar as consultas de teste;
- exibir os resultados no terminal;
- gerar:

```plaintext
dados/resultados_consultas.json
```

---

# Avaliação Qualitativa dos Resultados

Os resultados obtidos foram satisfatórios para o objetivo proposto.

O sistema conseguiu recuperar notícias semanticamente relacionadas às consultas realizadas, mesmo quando os termos pesquisados não apareciam exatamente nos textos.

Exemplos observados:

- consultas relacionadas a "taxa de juros" retornaram notícias sobre Selic e decisões do Copom;
- buscas envolvendo "mercado de trabalho" recuperaram notícias sobre desemprego, renda e emprego formal;
- pesquisas sobre "inflação" retornaram notícias relacionadas ao IPCA e preços ao consumidor.

Isso demonstra que os embeddings foram capazes de capturar relações semânticas relevantes entre os documentos do corpus.

---

# Reprodutibilidade

O projeto foi estruturado de forma que qualquer pessoa consiga executar o pipeline completo do zero.

Basta:

1. clonar o repositório;
2. instalar as dependências;
3. executar os scripts na ordem correta.

Todos os arquivos intermediários e finais são gerados automaticamente pelos scripts Python.
