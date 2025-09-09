# Dog Breed Classifier

Projeto acadêmico para identificar raças de cachorro a partir de imagens, utilizando Python e técnicas de aprendizado de máquina.

**Autor:** Fabio Ramos  
**Curso:** Engenharia de Software - UFMS  
**Disciplina:** Inteligência Artificial

---

## 📁 Estrutura do Projeto

- `data/` — Dataset de imagens (treino/teste)
- `notebooks/` — Notebooks Jupyter para experimentação
- `src/` — Código-fonte organizado
	- `dataset.py` — Carregamento e preprocessamento dos dados
	- `model.py` — Definição do modelo (CNN ou transfer learning)
	- `train.py` — Script de treinamento
	- `predict.py` — Script de predição
- `requirements.txt` — Dependências do projeto

## 📦 Dataset
Base: [Dog Breed Identification - Kaggle](https://www.kaggle.com/competitions/dog-breed-identification/overview)

## 🚀 Como começar
1. Instale as dependências:
	 ```bash
	 pip install -r requirements.txt
	 ```
2. Baixe o dataset do Kaggle e coloque o conteúdo em `data/`.
3. Utilize os notebooks para explorar, treinar e avaliar modelos.
4. Execute a interface gráfica em `src/app.py` para testar a classificação de raças em imagens novas.

---

Projeto simples, objetivo e didático para fins acadêmicos.