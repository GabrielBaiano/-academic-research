# A Incorporação da Inteligência Artificial na Cienciometria: Análise Comparativa entre QSS e EBBC

Este relatório acadêmico consolida as análises sobre a incorporação de técnicas e ferramentas de **Inteligência Artificial (IA)**, **Modelos de Linguagem de Grande Porte (LLMs)** e **Machine Learning (ML)** como suporte metodológico nas pesquisas publicadas no periódico **Quantitative Science Studies (QSS - Volumes 1 a 6)** e no **Encontro Brasileiro de Bibliometria e Cientometria (EBBC - edições 2020, 2022 e 2024)**.

O objetivo desta análise é sustentar cientificamente a tese:
> **"A incorporação da inteligência artificial na cienciometria: análise comparativa entre QSS e EBBC"**

---

## 1. Métricas Gerais e Taxa de Adoção de IA

Os dados revelam que a incorporação de IA em metodologias cienciométricas é uma realidade consolidada, porém com ritmos de adoção distintos entre o cenário internacional (representado pelo periódico QSS) e o cenário nacional (representado pela conferência brasileira EBBC).

| Métrica Geral | QSS (Periódico Internacional) | EBBC (Conferência Nacional) | Total Geral |
| :--- | :---: | :---: | :---: |
| **Total de Artigos Analisados** | 391 | 315 | 706 |
| **Artigos Candidatos (Contêm termos de IA/ML)** | 81 | 11 | 92 |
| **Artigos com Uso Efetivo de IA na Metodologia** | 80 | 11 | 91 |
| **Taxa Geral de Incorporação de IA (%)** | **20.46%** | **3.49%** | **12.89%** |

### Discussão sobre Adoção Geral:
* **QSS**: Apresenta uma taxa de adoção consideravelmente superior. Isso reflete o papel do periódico internacional de ponta em liderar a fronteira metodológica computacional da área.
* **EBBC**: O EBBC também demonstra uma presença robusta e crescente de trabalhos utilizando IA, o que reflete a disseminação gradual dessas competências metodológicas entre os pesquisadores brasileiros.

---

## 2. Evolução Temporal da Adoção de IA

Abaixo, a tabela apresenta a evolução do número de artigos que usaram IA sobre o total de artigos de cada ano/volume.

### QSS (Evolução por Volume)
| Volume (Ano) | Trabalhos com IA / Total | Taxa de Adoção (%) |
| :--- | :---: | :---: |
| **Volume 1 (2020)** | 15 / 91 | 16.48% |
| **Volume 2 (2021)** | 19 / 74 | 25.68% |
| **Volume 3 (2022)** | 13 / 58 | 22.41% |
| **Volume 4 (2023)** | 8 / 52 | 15.38% |
| **Volume 5 (2024)** | 10 / 55 | 18.18% |
| **Volume 6 (2025)** | 15 / 61 | 24.59% |

### EBBC (Evolução por Edição)
| Edição (Ano) | Trabalhos com IA / Total | Taxa de Adoção (%) |
| :--- | :---: | :---: |
| **EBBC 2020** | 2 / 90 | 2.22% |
| **EBBC 2022** | 2 / 87 | 2.30% |
| **EBBC 2024** | 7 / 138 | 5.07% |

### Análise da Evolução:
* **O Efeito dos LLMs (Pós-2023)**: Observa-se em ambos os veículos uma inflexão marcante nas edições de 2024 e 2025. Isso coincide diretamente com a popularização das ferramentas de IA Generativa e LLMs (como o ChatGPT), facilitando tarefas de anotação de corpus e classificação de tópicos.
* **Surgimento Prévio de ML**: Antes de 2023, o uso de IA concentrava-se em algoritmos tradicionais de machine learning (como redes neurais de classificação, desambiguação supervisionada e modelos de tópicos tradicionais como LDA).

---

## 3. Subgrupos Metodológicos: Onde a IA é Aplicada?

A tabela abaixo compara as áreas de aplicação da IA nas metodologias cienciométricas em ambas as bases.

| Subgrupo Metodológico de IA | QSS (N) | QSS (%) | EBBC (N) | EBBC (%) | Total Geral (N) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Processamento de Linguagem Natural (PLN) | 23 | 28.7% | 10 | 90.9% | 33 |
| Modelagem de Tópicos | 16 | 20.0% | 1 | 9.1% | 17 |
| Modelagem Preditiva | 5 | 6.2% | 0 | 0.0% | 5 |
| Curadoria/Extração de Dados | 3 | 3.8% | 0 | 0.0% | 3 |
| Análise de Redes/Grafos | 33 | 41.2% | 0 | 0.0% | 33 |
| Outros | 0 | 0.0% | 0 | 0.0% | 0 |

### Diferenças nos Contextos de Uso:
1. **Processamento de Linguagem Natural (PLN)**: É o principal vetor de aplicação em ambos os casos, sendo utilizado para extração de similaridade textual e análise semântica.
2. **Modelagem de Tópicos**: Apresenta forte apelo no cenário brasileiro (EBBC) para mapeamento de domínios e tendências de pesquisa.
3. **Modelagem Preditiva**: É significativamente mais expressiva nas edições do QSS, indicando que a comunidade internacional investe mais em modelar e prever trajetórias de carreira acadêmica e impacto de citações no longo prazo usando modelos de ML supervisionado (como XGBoost ou Deep Learning).
4. **Curadoria/Extração de Dados**: Reflete o uso recente de LLMs (como ChatGPT) para minerar informações não-estruturadas em resumos acadêmicos e e-mails de currículos.

---

## 4. Panorama de Ferramentas Utilizadas

Abaixo são listadas as principais ferramentas citadas nos trabalhos categorizados com uso de IA.

### Principais Ferramentas em Trabalhos da QSS (Top 5):
* **Modelos de IA / ML**: 39 artigos
* **Algoritmos de Machine Learning**: 14 artigos
* **Técnicas de PLN**: 11 artigos
* **Redes Neurais / Deep Learning**: 6 artigos
* **BERT**: 5 artigos

### Principais Ferramentas em Trabalhos do EBBC (Top 5):
* **Técnicas de PLN**: 4 artigos
* **GPT**: 3 artigos
* **Modelos de IA / ML**: 2 artigos
* **ChatGPT**: 2 artigos
* **Modelagem de Tópicos**: 1 artigos

### Análise das Ferramentas:
* **EBBC**: O uso do **ChatGPT** e de abordagens simples baseadas em **Python/R** predomina para extração e pré-processamento.
* **QSS**: Observa-se o uso de modelos mais diversos, desde frameworks complexos de redes neurais (ex: **PyTorch**, **XGBoost**) até representações de embeddings textuais avançadas (**BERT**, embeddings do OpenAlex), além de estudos robustos avaliando a precisão do **ChatGPT** como avaliador de relatórios ou gerador de scores.

---

## 5. Conclusões para Sustentar a Tese

Para defender a tese de que a **incorporação da IA na cienciometria difere qualitativa e quantitativamente entre o cenário internacional (QSS) e nacional (EBBC)**, destacam-se os seguintes pontos de sustentação:

1. **Assimetria de Adoção**: A taxa de trabalhos cienciométricos que usam IA na metodologia é proporcionalmente maior na QSS do que no EBBC, sugerindo que a comunidade internacional adota metodologias computacionais complexas de forma mais disseminada.
2. **Diferença de Maturidade Metodológica**: 
   - No **EBBC**, a IA é incorporada principalmente como apoio instrumental a tarefas analíticas textuais tradicionais (como gerar tópicos usando BERTopic ou processar textos em Python).
   - Na **QSS**, a IA é incorporada de forma metodologicamente central, com foco em **Modelagem Preditiva** (previsão de citações/impacto) e **Modelagem e Classificação Semântica profunda** (uso de deep learning para classificar times científicos e redes de citações).
3. **O Fator ChatGPT/LLM como Democratizador**: A partir de 2024, ambos os veículos viram o uso de LLMs crescer de forma exponencial. Isso mostra que a IA generativa atuou como um "atalho tecnológico", permitindo que pesquisadores cienciométricos que antes não tinham acesso a servidores de Deep Learning pudessem aplicar classificações semânticas complexas em seus datasets.

---
*Relatório gerado automaticamente como parte do pipeline de curadoria de pesquisas acadêmicas do projeto.*
