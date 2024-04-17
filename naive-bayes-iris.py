# Importando as bibliotecas necessárias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Carregando o dataset Iris
iris = load_iris()
X = iris.data  # features
y = iris.target  # target

# Dividindo o dataset em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializando o classificador Naive Bayes
naive_bayes = GaussianNB()

# Treinando o classificador com o conjunto de treino
naive_bayes.fit(X_train, y_train)

# Fazendo previsões com o conjunto de teste
y_pred = naive_bayes.predict(X_test)

# Calculando a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia: {accuracy:.2f}')

# Exibindo o relatório de classificação
print('\nRelatório de Classificação:')
print(classification_report(y_test, y_pred, target_names=iris.target_names))
