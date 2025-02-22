from flask import jsonify, Blueprint

from .services import calcular_intervalos

app = Blueprint('api', __name__, url_prefix='/api')


@app.route('/produtoras/intervalo_premiacoes', methods=['GET'])
def get_award_intervals():
    result = calcular_intervalos()
    return jsonify(result), 200
