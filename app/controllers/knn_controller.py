from flask import request, jsonify


def analise():
    data = request.get_json()

    return jsonify(data)
