import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Passo 1: Abrir o conjunto de dados
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
columns = ['Class', 'Alcohol', 'Malic_acid', 'Ash', 'Alcalinity_of_ash', 'Magnesium', 
           'Total_phenols', 'Flavanoids', 'Nonflavanoid_phenols', 'Proanthocyanins', 
           'Color_intensity', 'Hue', 'OD280/OD315_of_diluted_wines', 'Proline']
data = pd.read_csv(url, names=columns)

# Passo 2: Normalização (z-score)
scaler = StandardScaler()
data_normalized = scaler.fit_transform(data.drop('Class', axis=1))

# Passo 3: Escolha dos representantes
num_cases_per_class = 10
class_0_indices = np.where(data['Class'] == 1)[0]
class_1_indices = np.where(data['Class'] == 2)[0]

representatives_indices = np.concatenate([np.random.choice(class_0_indices, num_cases_per_class, replace=False),
                                          np.random.choice(class_1_indices, num_cases_per_class, replace=False)])

representatives = data_normalized[representatives_indices]
representatives_labels = data['Class'].iloc[representatives_indices]

# Passo 4: Escolher o número K
K = 3

# Passo 5: Classificar todos os outros objetos
X_train, X_test, y_train, y_test = train_test_split(data_normalized, data['Class'], test_size=0.3, random_state=42)

knn_classifier = KNeighborsClassifier(n_neighbors=K)
knn_classifier.fit(X_train, y_train)
predictions = knn_classifier.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do classificador KNN com K={K}: {accuracy:.2f}')