# Trilha Técnica – Cientista de Dados (Data Scientist / ML Engineer)

> Esta trilha foca exclusivamente em **habilidades técnicas (Habilidade Técnica)** para Cientistas de Dados e ML Engineers. Para competências comportamentais (Results, Direction, Talent, Culture), consulte os arquivos em [`/levels/`](../levels/).

---

## Visão Geral

**Cientistas de Dados** são responsáveis por construir modelos de Machine Aprendizado, sistemas de IA, experimentação e análises avançadas que geram valor de negócio. Consolidam expertise de **AI Engineering** (soluções de IA/LLM) e **MLOps/DRE** (operação e confiabilidade de ML).

### Tech Stack & Tools
- **Languages**: Python (expert), SQL (avançado), R (opcional)
- **ML Frameworks**: scikit-learn, XGBoost, LightGBM
- **Deep Aprendizado**: PyTorch, TensorFlow, Keras
- **GenAI/LLM**: OpenAI API, LangChain, LlamaIndex, Anthropic
- **Embeddings & Vector DBs**: OpenAI embeddings, Pinecone, Chroma, Weaviate
- **MLOps**: MLflow, Weights & Biases, Vertex AI
- **Experimentation**: A/B testing, Bayesian methods
- **Data Manipulation**: pandas, polars, NumPy
- **Visualization**: matplotlib, seaborn, plotly
- **Cloud**: GCP (Vertex AI, BigQuery ML), AWS SageMaker

---

## SE I – Junior Data Scientist

🔗 **Competências comportamentais**: [`SE_I_junior.md`](../levels/SE_I_junior.md)

### Entregas Principais
- Implementa componentes de projetos de ML/IA sob orientação
- Realiza análises exploratórias e estatísticas básicas
- Contribui em projetos de experimentação

### Python & Libraries
- Proficiente em Python (pandas, NumPy, matplotlib)
- Manipula dataframes (filter, groupby, merge, pivot)
- Cria visualizações básicas (scatter, line, bar plots)
- Usa Jupyter notebooks efetivamente
- Segue PEP 8 e boas práticas

### SQL & Data
- Proficiente em SQL (SELECT, JOIN, WHERE, GROUP BY)
- Extrai dados para análises
- Entende conceitos de sampling

### Estatística & Matemática
- Entende **estatística descritiva** (média, mediana, desvio padrão)
- Calcula **correlações** e interpreta
- Conhece **distribuições** básicas (normal, binomial)
- Aplica **testes de hipótese** simples (t-test, chi-square)

### Machine Aprendizado Básico
- Entende conceitos fundamentais: 
  - **Supervised** vs **Unsupervised** learning
  - **Regression** vs **Classification**
  - **Training** vs **Validation** vs **Test** sets
  - **Overfitting** vs **Underfitting**
- Treina modelos básicos com scikit-learn:
  - Linear Regression
  - Logistic Regression
  - Decision Trees
- Avalia modelos com métricas básicas (accuracy, MSE, R²)

### Boas Práticas
- Documenta análises em notebooks
- Versionamento de código (git)
- Comenta código e assumptions
- Reproduz análises (seeds, random_state)

---

## SE II – Pleno Data Scientist

🔗 **Competências comportamentais**: [`SE_II_pleno.md`](../levels/SE_II_pleno.md)

### Entregas Principais (SE I+)
- Desenvolve modelos de ML end-to-end independentemente
- Projeta e analisa experimentos (A/B tests)
- Constrói pipelines de ML básicos

### Python & Engineering (SE I+)
- **Fluente** em pandas, NumPy, scikit-learn
- Escreve código modular (functions, classes)
- Usa type hints e docstrings
- Implementa pipelines (sklearn Pipeline)
- Trabalha com APIs para deploy de modelos

### Machine Aprendizado (SE I+)
- Domina **feature engineering**:
  - Encoding categóricos (one-hot, target, embedding)
  - Scaling/normalization
  - Feature selection
  - Feature interactions
- Treina modelos avançados:
  - Random Forest, Gradient Boosting
  - **XGBoost, LightGBM, CatBoost**
  - Support Vector Machines
  - K-Means, DBSCAN (clustering)
- Faz **hyperparameter tuning** (GridSearch, RandomSearch)
- Usa **cross-validation** efetivamente
- Lida com **class imbalance** (SMOTE, class weights)

### Model Evaluation
- Escolhe métricas apropriadas:
  - **Classification**: precision, recall, F1, ROC-AUC, PR-AUC
  - **Regression**: MAE, RMSE, MAPE, R²
  - **Ranking**: NDCG, MAP
- Analisa **confusion matrix**
- Interpreta **feature importance**
- Cria **calibration plots**

### Experimentação
- Projeta **A/B tests** básicos
- Calcula **sample size** necessário
- Analisa resultados com testes estatísticos
- Entende **statistical significance** e **power**

### GenAI & LLMs (Básico)
- Usa **OpenAI API** para tasks simples
- Faz **prompt engineering** básico
- Entende conceitos de **embeddings**
- Implementa **semantic search** simples

---

## SE III – Senior Data Scientist

🔗 **Competências comportamentais**: [`SE_III_senior.md`](../levels/SE_III_senior.md)

### Entregas Principais (SE II+)
- Lidera tecnicamente projetos de ML/IA complexos
- Define estratégia de experimentação
- Implementa MLOps end-to-end

### Machine Aprendizado Avançado (SE II+)
- Expert em algoritmos e quando usar cada um
- Domina **ensemble methods** (stacking, blending)
- Implementa **custom loss functions**
- Usa **Bayesian optimization** para tuning
- Trabalha com **time series** (ARIMA, Prophet, LSTM)
- Implementa **recommendation systems**
- Conhece **anomaly detection** methods

### Deep Aprendizado
- Treina redes neurais com **PyTorch** ou **TensorFlow**
- Implementa **architectures**:
  - MLP (Multilayer Perceptron)
  - CNN (Convolutional Neural Networks)
  - RNN, LSTM, GRU (Recurrent)
  - Transformers (básico)
- Usa **transfer learning**
- Faz **fine-tuning** de modelos pré-treinados
- Entende **regularization** (dropout, batch norm)
- Usa **learning rate scheduling**

### GenAI & LLMs (Avançado)
- Implementa **RAG** (Retrieval Augmented Generation):
  - Chunking strategies
  - Embedding generation
  - Vector databases (Pinecone, Chroma)
  - Retrieval + generation
- Usa **LangChain** ou **LlamaIndex** efetivamente
- Faz **prompt engineering** avançado:
  - Few-shot prompting
  - Chain-of-thought
  - ReAct patterns
- **Fine-tunes** LLMs (LoRA, QLoRA)
- Implementa **LLM agents**
- Avalia LLMs (ROUGE, BLEU, human eval)

### MLOps & Productionization
- Implementa **ML pipelines** completos:
  - Data ingestion
  - Feature engineering
  - Training
  - Evaluation
  - Deployment
- Usa **MLflow** ou **Weights & Biases**:
  - Experiment tracking
  - Model registry
  - Model versioning
- Implementa **monitoring** de modelos:
  - **Data drift** detection
  - **Concept drift** detection
  - **Model performance** tracking
- Containeriza modelos (**Docker**)
- Implementa **CI/CD** para ML

### Experimentação Avançada
- Projeta **experiments complexos** (multi-armed bandits, sequential testing)
- Aplica **Bayesian A/B testing**
- Usa **causal inference** methods (quando apropriado)
- Implementa **bandit algorithms**
- Analisa **network effects** e **interference**

### Feature Engineering Avançado
- Cria **embedding representations**
- Implementa **feature stores**
- Usa **automated feature engineering** (Featuretools)
- Aplica **dimensionality reduction** (PCA, t-SNE, UMAP)

### Model Interpretability
- Usa **SHAP** values
- Implementa **LIME**
- Analisa **partial dependence plots**
- Cria **model cards** e documentação

---

## Lead Engineer

🔗 **Competências comportamentais**: [`Lead_engineer.md`](../levels/Lead_engineer.md)

### Entregas Principais (SE III+)
- Define arquitetura de ML/IA de longo prazo
- Cria frameworks e plataformas de ML reutilizáveis
- Resolve os problemas de ML/IA mais complexos

### ML Platform & Infrastructure
- Desenha **ML platform** escalável:
  - **Feature store** (Feast, Tecton)
  - **Model registry**
  - **Experiment tracking**
  - **Model serving** (Vertex AI, SageMaker)
  - **Monitoring & Observability**
- Implementa **AutoML** pipelines
- Cria **reusable ML components**

### Advanced ML Systems
- Implementa **online learning** systems
- Usa **reinforcement learning** quando apropriado
- Implementa **multi-modal models** (text + image + tabular)
- Cria **ensemble systems** complexos

### GenAI Systems
- Arquiteta **LLM applications** robustas
- Implementa **prompt optimization** systems
- Cria **evaluation frameworks** para LLMs
- Otimiza **cost** e **latency** de LLM calls
- Implementa **fallback strategies**

### Performance & Scale
- Otimiza **inference latency** (<100ms)
- Implementa **model compression** (quantization, pruning)
- Usa **batch prediction** eficientemente
- Otimiza custos de compute

### Expertise Profunda
- Expert em domínio específico (NLP, Computer Vision, Recommender Systems, etc.)
- Contribui para código aberto (libraries, papers)
- Referência técnica em ML/IA

---

## Staff Engineer

🔗 **Competências comportamentais**: [`Staff_engineer.md`](../levels/Staff_engineer.md)

### Entregas Principais (Lead+)
- Define estratégia de ML/IA multi-ano
- Influencia práticas de ML de múltiplos times
- Cria capacidades que transformam o negócio

### ML Strategy
- Define **ML/IA roadmap** de 2-3 anos
- Identifica **high-impact ML opportunities**
- Avalia **build vs buy vs API** para ML capabilities
- Alinha ML strategy com objetivos de negócio

### Organizational ML Capabilities
- Estabelece **MLOps practices** organizacionais
- Define **ML governance** e **responsible AI**
- Cria **training programs** para ML practitioners
- Implementa **ML engineering standards**

### Advanced GenAI
- Define **GenAI strategy** para empresa
- Avalia **LLM providers** (OpenAI, Anthropic, Cohere)
- Implementa **LLM governance** (cost, safety, privacy)
- Cria **GenAI use case framework**

---

## Staff II & Principal Engineer

🔗 **Competências comportamentais**: 
- [`Staff_II_senior_staff.md`](../levels/Staff_II_senior_staff.md)
- [`Principal_engineer.md`](../levels/Principal_engineer.md)

### Entregas Principais
- Define direção de ML/IA para empresa inteira
- Cria vantagem competitiva através de ML/IA
- Influencia indústria através de pesquisa e liderança

### Company-Wide ML/AI Strategy
- Define como ML/IA cria diferenciação competitiva
- Influencia decisões de investimento em ML/IA
- Alinha ML/AI strategy com visão de longo prazo do negócio
- Avalia implicações de M&A do ponto de vista de ML/IA

### Research & Innovation
- Publica **research papers** em conferências (NeurIPS, ICML, ICLR, etc.)
- Cria **novel algorithms** ou **architectures**
- Contribui significativamente para **código aberto** (frameworks influentes)
- **Patents** em ML/IA

### Liderança da Indústria
- Keynotes em conferências principais
- Advisory para startups ou investidores
- Representa empresa como líder em ML/IA

---

## 📚 Recursos de Aprendizado

### Fundamentos
- **[Coursera: Machine Aprendizado (Andrew Ng)](https://www.coursera.org/learn/machine-learning)** - Clássico
- **[Fast.ai](https://www.fast.ai/)** - Practical Deep Aprendizado
- **[Kaggle Learn](https://www.kaggle.com/learn)** - Prático courses

### Intermediário/Avançado
- **[Made With ML](https://madewithml.com/)** - MLOps e Engineering
- **[Hugging Face Course](https://huggingface.co/learn)** - NLP e Transformers
- **[DeepLearning.AI](https://www.deeplearning.ai/)** - Especializations em DL, MLOps, GenAI

### GenAI/LLM
- **[LangChain Documentation](https://python.langchain.com/)** - RAG e LLM apps
- **[OpenAI Cookbook](https://github.com/openai/openai-cookbook)** - Recipes
- **[Prompt Engineering Guide](https://www.promptingguide.ai/)** - Comprehensive

### Livros
- **Hands-On Machine Aprendizado (Aurélien Géron)** - Prático
- **Deep Aprendizado (Goodfellow, Bengio, Courville)** - Teórico
- **Designing Machine Aprendizado Systems (Chip Huyen)** - MLOps

### Certificações
- **Google Cloud Professional ML Engineer**
- **AWS Certified Machine Aprendizado – Specialty**
- **TensorFlow Developer Certificate**

---

## 🔄 Como Usar Esta Trilha

1. **Identifique seu nível atual** nos arquivos de `/levels/`
2. **Compare** suas habilidades de ML, DL, GenAI com as expectativas
3. **Identifique gaps**:
   - Preciso aprender Deep Aprendizado?
   - Preciso dominar RAG e LLMs?
   - Preciso entender MLOps melhor?
4. **Crie plano de desenvolvimento**:
   - Faça cursos (Fast.ai, DeepLearning.AI)
   - Pratique em Kaggle
   - Implemente em projetos reais do time
   - Leia papers recentes
5. **Busque mentoria** de scientists/engineers mais seniores

**Lembre-se**: Expertise técnica em ML/IA é crítica, mas não suficiente. Você também precisa demonstrar impacto de negócio e crescimento nas 4 dimensões: Results, Direction, Talent e Culture.
