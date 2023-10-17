from flask import request, jsonify

from app.service import knn_service


def analise():
    data = request.get_json()

    entrada = list(data.values())

    classificacao = knn_service.knn_analise(entrada)

    return jsonify({"recomendação": classificacao[0]})
