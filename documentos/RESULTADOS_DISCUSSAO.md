# 3 Resultados e discussão

Foram analisados 707 artigos científicos, sendo 392 provenientes do periódico *Quantitative Science Studies* (QSS) (Volumes 1 a 6, cobrindo de 2020 a 2025) e 315 publicados nos anais do *Encontro Brasileiro de Bibliometria e Cientometria* (EBBC) (edições de 2020, 2022 e 2024). A classificação automatizada e a curadoria dos metadados permitiram quantificar e mapear a evolução histórica das ferramentas computacionais, as fontes de coleta de dados, a adoção de técnicas de Inteligência Artificial (IA) e as respectivas etapas metodológicas do fluxo de pesquisa.

A Tabela 1 consolida os indicadores globais extraídos ao longo do período analisado.

### Tabela 1: Indicadores gerais de adoção de tecnologia e Inteligência Artificial no QSS e EBBC (2020-2025)

![Tabela 1: Indicadores Gerais](tabela_resultados.png)

---

## 3.1 Evolução da utilização de ferramentas computacionais

A evolução da declaração explícita de ferramentas metodológicas revela dinâmicas distintas entre a comunidade científica internacional e a nacional (Tabela 1 e Figura 1). 

![Evolução Temporal](evolucao_ferramentas.png)

No âmbito do periódico internacional *QSS*, o índice de declaração de softwares permaneceu estável e em patamares moderados entre 2020 e 2023, oscilando em uma faixa estreita entre 32,2% e 36,5%. Contudo, observa-se um crescimento abrupto nos anos subsequentes: a taxa salta para **81,8% em 2024** (Volume 5) e consolida-se em **75,4% em 2025** (Volume 6). Este expressivo incremento de mais de 40 pontos percentuais reflete uma mudança metodológica significativa na cientometria global, impulsionada por maiores exigências editoriais de reprodutibilidade e transparência de código (compartilhamento de scripts em repositórios abertos).

No cenário nacional representado pelo *EBBC*, a evolução do uso declarado de ferramentas computacionais é caracterizada por uma trajetória de crescimento gradual e linear. Em 2020, apenas 8,9% das pesquisas declaravam abertamente o uso de algum software especializado. Esse índice subiu para 26,4% em 2022 e atingiu **39,1% em 2024**. Esse aumento consistente demonstra o avanço no letramento digital e na apropriação tecnológica por parte dos pesquisadores em estudos métricos no Brasil, embora ainda distante das taxas de declaração observadas na literatura global recente.

---

## 3.2 Adoção de Inteligência Artificial

A aplicação de técnicas de Inteligência Artificial (IA), Aprendizado de Máquina (ML) e Processamento de Linguagem Natural (NLP) constitui uma das maiores divergências estruturais entre as duas frentes analisadas.

No periódico *QSS*, a presença dessas abordagens é historicamente expressiva e estável, oscilando entre **41,0% e 49,2%** de todos os artigos publicados a cada ano. Os dados revelam que quase metade da produção científica internacional de fronteira utiliza algoritmos computacionais para lidar com a semântica de grandes volumes textuais. Os artigos mais antigos (2020-2022) concentram-se no uso de modelos locais de aprendizado supervisionado tradicional (como classificadores Random Forest, Naïve Bayes e algoritmos de agrupamento de rede como *Leiden* e *Louvain*), além de modelos de embeddings baseados em arquiteturas BERT. Nos volumes mais recentes (2024-2025), o perfil expandiu-se com a inserção de modelos de linguagem de grande porte (LLMs) proprietários e abertos (como GPT-3.5, GPT-4, Llama e Mistral) aplicados à rotulação semântica e extração automática de entidades bibliométricas.

Por outro lado, o *EBBC* apresenta uma taxa de adoção de IA/ML/NLP significativamente menor, embora estável, flutuando entre **12,6% e 15,2%** ao longo das edições. No contexto brasileiro, a utilização dessas tecnologias concentra-se quase exclusivamente no processamento de linguagem natural tradicional voltado a análises lexicais estruturadas (frequentemente implementadas via ferramentas prontas, como o IRaMuTeQ). A menção ao uso de algoritmos de aprendizado de máquina complexos ou de IA generativa (LLMs) para a curadoria de dados ainda é incipiente e restrita às publicações de 2024, evidenciando uma lacuna de aplicação de técnicas computacionais avançadas na pesquisa nacional de estudos métricos.

---

## 3.3 Perfil das ferramentas computacionais

A análise detalhada do perfil das ferramentas revela a contraposição entre metodologias de análise programática (código personalizado) e o uso de interfaces gráficas fechadas de prateleira (Figura 2).

![Top Ferramentas Mapeadas](top_ferramentas.png)

No *QSS*, o ecossistema metodológico é majoritariamente **programático**. A categoria dominante é **Python / Machine Learning & NLP** (26 artigos, 6,65%), seguida por análises estatísticas estruturadas por linguagem de programação na categoria **R/Stata/SPSS (Stats)** (16 artigos, 4,09%). Ferramentas baseadas em APIs de ciência aberta e grafos de conhecimento, além de algoritmos customizados de redes e clustering, também possuem representatividade expressiva. A preferência por programação indica um perfil de cientistas de dados voltados à flexibilidade, mineração complexa via APIs e modelagem probabilística adaptada.

Em contrapartida, no *EBBC*, há uma nítida hegemonia de **softwares visuais e interfaces gráficas predefinidas**. A ferramenta mais frequente é o **VOSviewer** (9 artigos, 2,86%), seguido pelo **Gephi** (4 artigos, 1,27%) e pelo **Excel** (4 artigos). Embora linguagens de programação gerais como Python e R estejam presentes, elas aparecem de forma periférica ou aplicadas a ferramentas de extração muito específicas de infraestrutura nacional, como o **ScriptLattes** (3 artigos), desenvolvido especificamente para a mineração de dados do CNPq, e o **IRaMuTeQ** (3 artigos) para processamento conceitual de corpora de textos em língua portuguesa.

---

## 3.4 Fontes de dados utilizadas

As fontes de dados utilizadas revelam como a literatura internacional e a nacional interagem com as bases de indexação de periódicos globais e regionais (Figura 3).

![Top Fontes de Dados](top_fontes.png)

As bases comerciais proprietárias consolidadas continuam exercendo papel fundamental em ambas as esferas de publicação. A base **Web of Science** lidera no *QSS* (56 artigos, 14,32%) e ocupa a segunda posição no *EBBC* (37 artigos, 11,75%). Já a base **Scopus** atua de forma inversa, liderando no *EBBC* (39 artigos, 12,38%) e ocupando a segunda colocação no *QSS* (47 artigos, 12,02%).

As diferenças metodológicas significativas emergem nas fontes alternativas:
* **No QSS (Internacional):** Observa-se uma rápida transição e fortalecimento das bases de dados abertas e integradas por APIs. Destacam-se o **Dimensions** (18 artigos, 4,60%), a infraestrutura legada do **Microsoft Academic** (16 artigos, 4,09%), a base do **Crossref** (12 artigos) e o indexador aberto **OpenAlex** (11 artigos), que tem demonstrado crescimento acelerado nos volumes de 2024 e 2025.
* **No EBBC (Nacional):** O perfil metodológico é fortemente ancorado na infraestrutura de fomento e informação científica brasileira. Destacam-se a **Plataforma Lattes** do CNPq (26 artigos, 8,25%) para mapeamento de currículos e colaboração científica, a base de dados nacional **Brapci** (21 artigos, 6,67%), o repositório latino-americano **SciELO** (12 artigos, 3,81%) e o portal de periódicos **CAPES**. Também se sobressai o uso de dados extraídos de **Mídias Sociais** (14 artigos, 4,44%) para fins de estudos altmétricos no Brasil.

---

## 3.5 Correlações entre ferramentas e fontes de dados (Discussão do Biplot)

A Análise de Correspondência (CA) revelou que a escolha da fonte de informação para a pesquisa correlaciona-se estatisticamente e atua como fator estruturador das ferramentas metodológicas empregadas pelos pesquisadores. Os biplots de correspondência combinados e específicos evidenciam agrupamentos nítidos de coocorrência (Figura 4).

As ferramentas clássicas de visualização de redes bibliométricas, **VOSviewer** e **Gephi**, exibem forte proximidade e associação estatística com as fontes proprietárias comerciais **Web of Science** e **Scopus**. Esse comportamento decorre da compatibilidade direta e da facilidade de integração dessas ferramentas gráficas com os formatos de exportação proprietários das bases comerciais (como arquivos `.csv` e `.txt` formatados de metadados de coautoria e citação).

Por outro lado, o uso das linguagens de programação **Python** e **R** (especialmente voltados a modelos avançados de NLP e curadoria de dados) encontra-se fortemente acoplado às bases abertas orientadas a APIs, como **OpenAlex** e **Crossref**. A fundamentação para essa correlação é tecnológica: bases abertas oferecem endpoints REST estruturados e gratuitos, o que incentiva a automação de consultas, raspagem de dados em larga escala e desenvolvimento de pipelines de dados personalizados via código, inexistentes ou altamente restritos nas APIs pagas das bases comerciais.

No âmbito nacional (*EBBC*), observa-se um padrão de associação muito forte das bases de dados brasileiras com ferramentas específicas. O software **IRaMuTeQ** apresenta proximidade espacial com a **Brapci** e a **Plataforma Lattes**, justificado pelo fato de estas bases fornecerem corpora em português (resumos de artigos de Ciência da Informação nacional e textos de currículos acadêmicos), exigindo processamento léxico e estatística textual adaptados à língua nativa, especialidade do IRaMuTeQ. De forma similar, a ferramenta **ScriptLattes** orbita estritamente ao redor da **Plataforma Lattes**, evidenciando um ecossistema nacional altamente especializado voltado para a análise do perfil e produtividade do pesquisador brasileiro.

---

## 3.6 Etapas metodológicas de utilização das ferramentas

Por fim, o mapeamento das etapas metodológicas indica os nichos de aplicação das tecnologias no ciclo de vida da pesquisa cientométrica:

* **Etapas de Coleta de Dados:** Esta fase é dominada por linguagens de programação gerais (Python e R) que atuam na orquestração de requisições de APIs abertas, bem como por scripts especializados em extração automatizada de perfis (ScriptLattes). As bases comerciais (WoS/Scopus), embora muito utilizadas, cumprem essa etapa majoritariamente por exportações manuais diretas de suas plataformas web.
* **Etapas de Análise de Dados:** Compreende a maior concentração de aplicação de ferramentas. Softwares estatísticos consolidados (SPSS, Stata) e ecossistemas estatísticos (R) são amplamente mobilizados para análises estatísticas multivariadas tradicionais e econometria. 
* **Etapas de Visualização de Dados:** Esta fase é caracterizada por ferramentas focadas em teoria dos grafos e mapeamento científico visual (VOSviewer, Gephi e Pajek). O VOSviewer é o principal responsável pela geração de redes de coautoria e acoplamento bibliográfico, enquanto o Gephi é mobilizado para cálculos estruturais de centralidade de rede de grande porte.
* **Tarefas Semânticas e IA:** Os modelos de linguagem de grande porte (LLMs) e modelos pré-treinados de linguagem (BERT) são aplicados quase em sua totalidade na etapa de análise, focando na classificação automatizada de temáticas de pesquisa, análise de sentimento de citações e rotulação conceitual dos resumos, substituindo análises qualitativas de conteúdo manuais e expandindo a escala de interpretação textual dos artigos cientométricos.
