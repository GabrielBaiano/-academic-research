# Extrator de Metadados, Classificação Semântica e Curadoria por IA

[![DOI](https://zenodo.org/badge/1250735260.svg)](https://doi.org/10.5281/zenodo.20638523)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Language: EN](https://img.shields.io/badge/Language-EN-blue.svg)](README_EN.md)
[![Version: 1.1.0](https://img.shields.io/badge/Version-1.1.0-orange.svg)](https://github.com/gabrielbaiano/-academic-research/releases)

Este diretório contém o pipeline automatizado e inteligente para extração, análise de texto, curadoria semântica e consolidação em planilhas de **todas as publicações científicas** da prestigiada revista **Quantitative Science Studies (QSS)** (Volumes 1 a 6) e do **Encontro Brasileiro de Bibliometria e Cientometria (EBBC)** (anos 2020, 2022 e 2024).

O objetivo deste pipeline é classificar quais ferramentas de software/estatísticas foram aplicadas nos artigos, onde foram aplicadas (coleta, análise ou visualização) e de quais fontes os dados da pesquisa foram extraídos.

---

## 📊 Fluxo de Funcionamento do Pipeline

O diagrama abaixo ilustra o fluxo lógico de execução do projeto, desde a coleta inicial de metadados até a geração da planilha Excel consolidada:

```mermaid
graph TD
    A[OpenAlex API / OJS Journal Website] -->|1. Coleta e Raspagem| B(Arquivos JSON de metadados brutos)
    B -->|2. Identificação de Incompletos| C{Verifica Todos N/A & não processados}
    C -->|Sim: Precisa de Curação| D[Buscador de Resumos / Abstracts]
    C -->|Não: Já Curado/Completo| H[Consolidador de Excel]
    D -->|Busca Resumos pelo DOI ou Título| E[Abstracts Reconstituídos / Caching local]
    E -->|3. Curadoria com Contexto Completo| F[Gemini Flash Lite API]
    F -->|4. Grava Classificações nos JSONs| G[Arquivos JSON Refinados com tag _refined]
    G --> H
    H -->|5. Formatação Executiva e Cores Zebra| I[coleta de dados gabriel.xlsx]
```

---

## ⚡ Recursos de Robustez e Otimização

O pipeline foi projetado para ser resiliente a falhas e eficiente no consumo de recursos:
* **Persistência Intermediária (Gravação em Lote):** O progresso da classificação do Gemini é salvo nos arquivos JSON correspondentes após cada lote de 10 artigos processados com sucesso. Se a execução for interrompida (por exemplo, queda de energia, cancelamento ou falha de rede), o progresso é preservado e a execução continuará exatamente de onde parou na próxima rodada.
* **Paginação Automática no OpenAlex:** Toda a extração e mapeamento de metadados que consulta a API do OpenAlex (volumes do QSS) agora utiliza paginação dinâmica inteligente. Isso garante que nenhum artigo seja omitido do dataset consolidado, mesmo que o volume consultado ultrapasse o limite de registros por requisição.
* **Filtro Aprimorado para Linguagem R:** A expressão regular de primeira passagem que identifica o uso do "R" foi otimizada para capturar variações metodológicas comuns (ex: `uses R`, `using R`, `in R`, `R packages`, `R-based`, `R (version...)`), reduzindo os falsos negativos e diminuindo a quantidade de requisições de fallback enviadas à API do Gemini.

---

## 📈 Análise de Correspondência (Correspondence Analysis - CA)

Para compreender as associações metodológicas e mapear a estrutura intelectual da área, o pipeline inclui um script de **Análise de Correspondência (CA)**. Esse script correlaciona estatisticamente as **Ferramentas Utilizadas** com as **Fontes de Coleta de Dados** nos datasets do QSS e do EBBC.

### Como Executar a Análise
Para executar a análise de correspondência e regenerar os biplots, rode:
```bash
python scripts/correspondence_analysis.py
```

### Resultados Obtidos (Biplots)
A análise filtra automaticamente tautologias de nicho isolado (como Altmetric) e ruídos de baixa frequência ($N < 2$) para evitar distorções de escala, garantindo uma inércia explicada acumulada de **67,85%** no QSS:

1. **Mapa Combinado (QSS + EBBC)**: Revela três trajetórias metodológicas principais na cientometria:
   * **Ecossistema Python Nacional**: ScriptLattes fortemente associado à Plataforma Lattes.
   * **Ecossistema R Nacional**: IRaMuTeQ intimamente ligado a bases nacionais/locais (Brapci, CNPq).
   * **Núcleo Cientométrico Global**: Onde ferramentas visuais (VOSviewer, Bibliometrix) e ecossistemas de desenvolvimento (Python/ML, R/Stats) orbitam em torno das grandes bases de dados globais.

2. **Mapa Nacional (EBBC)**: Evidencia a forte preferência pela aplicação de softwares de prateleira (VOSviewer, Pajek, SciVal, Bibliometrix) aplicados a contextos de infraestrutura e dados brasileiros (Lattes, Brapci, Sucupira).

3. **Mapa Internacional (QSS)**: Mostra um ecossistema dominado por ecossistemas programáveis e algoritmos. O **Python/ML** atua como hub central conectando modelos de processamento de linguagem natural (Transformers/LLMs) a repositórios de preprints, enquanto o ecossistema do **Dimensions**, **OpenAlex** e **Crossref** se estruturam de forma vertical e integrada às suas respectivas APIs.

---

## 📂 Estrutura do Projeto

Os arquivos foram organizados de forma modular e limpa:

```text
├── coleta de dados gabriel.xlsx      # Planilha final consolidada com todas as abas estilizadas
├── executar_curadoria.py             # Script atalho de execução na raiz
├── README.md                         # Documentação do projeto
├── datasets/                         # Pasta contendo os conjuntos de dados em JSON
│   ├── cache/                        # Caches locais de resumos do EBBC (evita sobrecarga no OJS)
│   │   ├── ebbc_2020_abstracts_cache.json
│   │   ├── ebbc_2022_abstracts_cache.json
│   │   └── ebbc_2024_abstracts_cache.json
│   ├── ebbc_2020_data.json
│   ├── ebbc_2022_data.json
│   ├── ebbc_2024_data.json
│   ├── qss_volume_1_data.json
│   ├── qss_volume_2_data.json
│   ├── qss_volume_3_data.json
│   ├── qss_volume_4_data.json
│   ├── qss_volume_5_data.json
│   └── qss_volume_6_data.json
└── scripts/                          # Pasta contendo os códigos-fontes do pipeline
    ├── refine_with_abstracts.py      # Script principal do menu interativo e integração IA
    ├── generate_styled_xlsx_all.py   # Gerador da planilha final (todas as abas)
    ├── generate_styled_xlsx.py       # Gerador da planilha (Volumes 5 e 6 do QSS)
    ├── refine_dataset.py             # Curadoria manual específica do Volume 6
    └── ...                           # Outros scripts de extração e suporte
```

---

## 🛠️ Como Funciona e Como Executar (Tutorial)

### Pré-requisitos
- Python 3.10 ou superior.
- Instale as dependências executando:
  ```bash
  pip install -r requirements.txt
  ```

### Executando a Curadoria
Para rodar a curadoria inteligente dos dados e atualizar a planilha Excel, basta executar o atalho criado na raiz do projeto:

```bash
python executar_curadoria.py
```

Isso abrirá um menu de console interativo com estatísticas em tempo real:

```text
============================================================
      SISTEMA DE CURADORIA DE PESQUISAS ACADÊMICAS (IA)
============================================================
Opção  | Dataset              | Total  | Todos N/A (Incompletos)
------------------------------------------------------------
 1     | QSS Vol 1 (2020)     | 91     | 0                     
 2     | QSS Vol 2 (2021)     | 74     | 0                     
 3     | QSS Vol 3 (2022)     | 59     | 0                     
 4     | QSS Vol 4 (2023)     | 52     | 0                     
 5     | EBBC 2020            | 90     | 0                     
...
------------------------------------------------------------
 8    | REFINE TODOS os datasets acima consecutivamente
 9    | RECONSTRUIR Planilha Excel (coleta de dados gabriel.xlsx)
 10   | SAIR
============================================================
Selecione uma opção (1-10):
```

### Explicação das Opções:
- **Opções de 1 a 7**: Rodam a curadoria de IA em um volume/ano específico.
- **Opção 8**: Executa a curadoria em todos os conjuntos de dados que ainda possuem registros não refinados (`Incompletos`).
- **Opção 9**: Apenas lê os dados do diretório `datasets/` e reconstrói a planilha Excel consolidada `coleta de dados gabriel.xlsx` na raiz do projeto.
- **Opção 10**: Fecha o menu.

---

## 🔑 A Importância da Chave do Gemini (API Key)

Para realizar a classificação semântica avançada de texto dos resumos dos artigos, o pipeline utiliza o modelo de inteligência artificial de alta performance **Gemini Flash Lite (`gemini-flash-lite-latest`)** da Google. 

### Por que é necessária?
A IA é responsável por interpretar o resumo textual do artigo (que pode estar em inglês ou português), identificar se um software foi usado ativamente, classificar o local de uso e mapear de onde os dados empíricos foram extraídos. Isso substitui regras simples de busca por palavras-chave (regex), que falham frequentemente em encontrar termos não triviais.

### Como configurar a sua chave de API?
O pipeline possui uma chave pública padrão configurada para execuções iniciais livres. Caso você queira utilizar sua própria chave da Google AI Studio (recomendado para uso em larga escala ou chaves privadas dedicadas):

1. **Configuração Temporária (Terminal)**:
   - No Windows PowerShell:
     ```powershell
     $env:GEMINI_API_KEY="SUA_CHAVE_AQUI"
     python executar_curadoria.py
     ```
   - No CMD (Prompt de Comando):
     ```cmd
     set GEMINI_API_KEY=SUA_CHAVE_AQUI
     python executar_curadoria.py
     ```

2. **Edição do Código**:
   Você também pode editar diretamente o arquivo `scripts/refine_with_abstracts.py` e alterar o valor padrão da variável na linha 16.

---

## 📝 Como Citar

Se você utilizar este código ou os conjuntos de dados em sua pesquisa, por favor cite como:

**APA:**
Gama, G. N. (2026). Extrator de Metadados, Classificação Semântica e Curadoria por IA para Quantitative Science Studies (QSS) e EBBC (Versão 1.1.0). Zenodo. https://doi.org/10.5281/zenodo.20638523

**BibTeX:**
```bibtex
@software{gama_curadoria_2026,
  author       = {Gama, Gabriel Nascimento},
  title        = {Extrator de Metadados, Classificação Semântica e Curadoria por IA para Quantitative Science Studies (QSS) e EBBC},
  month        = jun,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {1.1.0},
  doi          = {10.5281/zenodo.20638523},
  url          = {https://doi.org/10.5281/zenodo.20638523}
}
```

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
