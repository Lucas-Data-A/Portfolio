# 📊 Portfólio de Projetos — Lucas Barbosa dos Santos

### Cientista de Dados | Machine Learning, Analytics & Agentes de IA

Reúno aqui meus projetos de dados — de análise e modelagem preditiva a séries temporais, engenharia de dados na nuvem e deep learning. Cada projeto traz o problema, a abordagem, o resultado e as tecnologias usadas. Projetos de **Agentes de IA** a caminho.

👤 **Perfil:** [github.com/Lucas-Data-A](https://github.com/Lucas-Data-A) &nbsp;•&nbsp; 💼 **LinkedIn:** [Lucas Barbosa dos Santos](https://www.linkedin.com/in/lucas-barbosa-dos-santos-6328a2317)

---

## 🌟 Projetos em destaque

### 🔄 Previsão de churn de clientes (CRISP-DM completo)

Projeto de ponta a ponta seguindo as 6 fases do CRISP-DM, prevendo o cancelamento (churn) de clientes de telecom e transformando o modelo em um score acionável de retenção.

- **Problema:** antecipar quais clientes têm maior probabilidade de cancelar o serviço, para apoiar ações de retenção — em uma base com churn desbalanceado (~14,5%).
- **Abordagem:** entendimento de negócio, EDA com dicionário de dados, preparação (limpeza e seleção de variáveis) e comparação de dois pipelines (todas as variáveis vs. seleção por importância) entre Regressão Logística (baseline), Árvore de Decisão, Random Forest e Gradient Boosting — avaliados por ROC-AUC, F1, Recall e Precisão.
- **Resultado:** o Random Forest foi selecionado como modelo final, com ROC-AUC de ~0,87 e F1 de ~0,72 no conjunto de teste; a distribuição do score separou bem os clientes propensos ao churn, virando uma regra prática de priorização. A EDA também revelou os principais fatores de cancelamento (renovação de contrato, chamadas ao suporte e cobrança mensal).
- **Stack:** Python · Pandas · scikit-learn · Matplotlib · Seaborn
- 🔗 **Projeto:** https://github.com/Lucas-Data-A/Portfolio/tree/main/Portfolio-Ciencia-de-Dados/Vis%C3%A3o%20de%20Processo

> _Projeto individual — pós-graduação em Engenharia e Análise de Dados (CESAR School)._

---

### ☁️ Data Lake da Premier League na AWS

Pipeline de engenharia de dados que ingere, trata e consolida 10 temporadas da Premier League em um Data Lake na AWS, seguindo a arquitetura de três zonas (Raw → Cleaned → Curated).

- **Problema:** transformar arquivos brutos de várias temporadas em uma base analítica confiável e consultável, resolvendo inconsistências de dados entre temporadas.
- **Abordagem:** construção de um Data Lake em três camadas no Amazon S3; ETL visual no AWS Glue com particionamento e conversão para Parquet; catalogação no Glue Data Catalog e consultas no Amazon Athena. Na zona Curated, cálculo de gols marcados/sofridos e médias por temporada, mando e visitante.
- **Resultado:** base analítica particionada e otimizada (Parquet), consultável via Athena para perguntas como maior ataque, pior defesa e médias por time/temporada. Inclui o tratamento de um problema real: a temporada "0910" perdia o zero à esquerda na leitura do Pandas e tinha formato de data divergente, o que quebrava o particionamento no catálogo.
- **Stack:** AWS S3 · AWS Glue · AWS Athena · Parquet · Python (Pandas)
- 🔗 **Projeto:** https://github.com/Lucas-Data-A/Portfolio/blob/main/Portfolio-Ciencia-de-Dados/Nuvem-AWS/Premier%20League%20-%20Data%20Lake.ipynb

> _Projeto individual — pós-graduação em Engenharia e Análise de Dados (CESAR School)._

---

### 📉 Previsão de séries temporais — comparação de modelos

Estudo de previsão de uma série temporal financeira (preço de ação da Netflix) comparando abordagens clássicas, modernas e de deep learning.

- **Problema:** prever os próximos valores de uma série temporal e identificar qual família de modelos performa melhor sobre o mesmo conjunto.
- **Abordagem:** análise da série (decomposição sazonal e testes de estacionariedade — KPSS) e comparação de quatro abordagens — SARIMA/AutoARIMA, MLP, MiniRocket + XGBoost e Prophet — todas avaliadas por MAE, RMSE e MAPE.
- **Resultado:** a rede neural (MLP) obteve o melhor desempenho, com MAPE de ~3,6% e RMSE de ~24,7, superando SARIMA (~9,2%), MiniRocket+XGBoost (~8,3%) e Prophet (~13,5%).
- **Stack:** Python · statsmodels · pmdarima · Prophet · sktime (MiniRocket) · XGBoost · scikit-learn
- 🔗 **Projeto:** https://github.com/Lucas-Data-A/Portfolio/blob/main/Portfolio-Ciencia-de-Dados/S%C3%A9ries%20Temporais/Projeto%20final%20-%20S%C3%A9ries%20Temporais.ipynb

> _Projeto individual — pós-graduação em Engenharia e Análise de Dados (CESAR School)._

---

### 📈 Predição de expectativa de vida (regressão)

Modelo de regressão que prevê a expectativa de vida de países a partir de indicadores socioeconômicos e de saúde (base da OMS).

- **Problema:** prever a expectativa de vida a partir de dezenas de indicadores de saúde, economia e imunização, lidando com variáveis correlacionadas e valores ausentes.
- **Abordagem:** EDA, seleção de variáveis e pré-processamento (encoding e padronização), seguidos da comparação entre Regressão Linear e XGBoost — ambos avaliados com validação cruzada (10-fold), múltiplas métricas (R², MAPE, RMSE) e análise de resíduos.
- **Resultado:** o XGBoost superou a regressão linear com folga — R² de 0,96 (vs 0,82) e MAPE de 1,9% (vs 4,7%), explicando 96% da variabilidade da expectativa de vida.
- **Stack:** Python · Pandas · scikit-learn · XGBoost · Matplotlib · Seaborn
- 🔗 **Projeto:** https://github.com/Lucas-Data-A/Portfolio/blob/main/Portfolio-Ciencia-de-Dados/Modelos%20Preditivos%20Cl%C3%A1ssicos/Projeto_final_Regressao.ipynb

> _Projeto individual — pós-graduação em Engenharia e Análise de Dados (CESAR School)._

---

### 🧩 Segmentação de clientes bancários com clusterização

Análise não supervisionada que agrupa clientes de um banco por comportamento transacional e perfil financeiro.

- **Problema:** identificar perfis distintos de clientes a partir de transações, saldo, idade e duração das operações — sem rótulos prévios.
- **Abordagem:** EDA completa e padronização (StandardScaler), seguida da comparação entre dois algoritmos de clusterização — K-Means (com método do cotovelo e análise de silhueta para definir o número de grupos) e DBSCAN (com ajuste do eps pela curva de k-distância).
- **Resultado:** identificação de 3 segmentos de clientes (baixo, médio e alto saldo) como melhor configuração do K-Means; no DBSCAN, o ajuste de parâmetros (eps = 0.8) reduziu os outliers de 830 para 179 transações, capturando melhor os padrões de densidade.
- **Stack:** Python · Pandas · NumPy · scikit-learn · Matplotlib · Seaborn
- 🔗 **Projeto:** https://github.com/Lucas-Data-A/Portfolio/blob/main/Portfolio-Ciencia-de-Dados/Modelos%20Descritivos/%5BProjeto_Final%5D.ipynb

> _Projeto em equipe — pós-graduação em Engenharia e Análise de Dados (CESAR School)._

---

### 🖼️ Classificação de imagens com rede neural (PyTorch)

Rede neural construída do zero em PyTorch para classificar imagens entre dois personagens (Homer e Bart), cobrindo o fluxo completo de deep learning.

- **Problema:** classificar imagens em duas classes a partir dos pixels, construindo e treinando uma rede neural do zero.
- **Abordagem:** classe de Dataset personalizada (carregamento, redimensionamento para 64×64 e normalização), rede feedforward com ReLU e regularização por weight decay (AdamW), treino por 30 épocas e avaliação com acurácia e matriz de confusão.
- **Resultado:** ~73% de acurácia em validação; a diferença para a acurácia de treino (~95%) evidenciou overfitting, diagnosticado pela matriz de confusão e pelas curvas de treino — apontando os próximos passos (data augmentation e arquitetura convolucional).
- **Stack:** Python · PyTorch · scikit-learn · NumPy · Matplotlib · Pillow
- 🔗 **Projeto:** https://github.com/Lucas-Data-A/Portfolio/blob/main/Portfolio-Ciencia-de-Dados/Redes%20Neurais%20e%20Deep%20Learning/Projeto%20final.ipynb

> _Projeto em equipe — pós-graduação em Engenharia e Análise de Dados (CESAR School)._

---


## 🗂️ Como o repositório está organizado

- **`ciencia-de-dados/`** — projetos de análise, estatística, modelagem preditiva, séries temporais, deep learning e engenharia de dados.
- **`engenharia-de-agentes-de-ia/`** — projetos de LLMs, RAG e orquestração de agentes _(em construção)_.
- **`certificados/`** — certificações e formações concluídas.

---

## 🛠️ Principais tecnologias

`Python` · `SQL (PostgreSQL)` · `Pandas` · `NumPy` · `scikit-learn` · `PyTorch` · `XGBoost` · `Power BI` · `AWS (S3, Glue, Athena)` · `LLMs / RAG / CrewAI`

---

## 📫 Contato

- 💼 [LinkedIn](https://www.linkedin.com/in/lucas-barbosa-dos-santos-6328a2317)
- 📧 lbs.70x@gmail.com
