import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


def knn_analise(entrada: {}):
    # importando o arquivo
    data = pd.read_csv("./app/data/acoes_class.csv", sep=",")

    # Separe seus recursos (X) e rótulos (y)
    X = data.drop("Classificacao", axis=1)
    y = data["Classificacao"]

    # Parametro de normalização
    scaler = StandardScaler()

    # Ajuste e transforme seus dados usando o scaler
    X_normalized = scaler.fit_transform(X)

    # Dividir os dados em treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X_normalized, y, test_size=0.3, random_state=42
    )

    # Treinar o modelo knn
    k = 3
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # PL, PVP, DY, PAtivo, ROE, PCap PEBIT, PSR, ROIC
    dadosEntrada = [
        entrada["P/L"],
        entrada["P/VP"],
        entrada["DY"],
        entrada["P/Ativo"],
        entrada["ROE"],
        entrada["P/Cap.Giro"],
        entrada["P/EBIT"],
        entrada["PSR"],
        entrada["ROIC"],
    ]
    print(dadosEntrada)

    entradaProcessada = np.array(dadosEntrada)

    # Reshape do exemplo para formato 2D (uma única linha)
    X_new = entradaProcessada.reshape(1, -1)

    # Normalize X_new de acordo com o mesmo escalonamento usado nos dados de treinamento
    X_new_normalized = scaler.transform(X_new)

    # previsões
    return knn.predict(X_new_normalized)
