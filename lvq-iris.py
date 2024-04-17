# Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn_lvq import GlvqModel
from sklearn.metrics import accuracy_score, classification_report

# Carregando o dataset Iris
iris = load_iris()
X = iris.data  # features
y = iris.target  # target

# Dividindo o dataset em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizando os dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Inicializando e treinando o classificador LVQ
lvq = GlvqModel()
lvq.fit(X_train_scaled, y_train)

# Fazendo previsões com o conjunto de teste
y_pred = lvq.predict(X_test_scaled)

# Calculando a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia: {accuracy:.2f}')

# Exibindo o relatório de classificação
print('\nRelatório de Classificação:')
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Visualizando as regiões de decisão do LVQ
plt.figure(figsize=(8, 6))
plot_decision_regions(X_train_scaled[:, :2], y_train, lvq, title='LVQ - Regiões de Decisão (Treino)')
plt.show()
