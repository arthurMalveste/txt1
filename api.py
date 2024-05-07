from flask import Blueprint, jsonify, request

bp = Blueprint("api", __name__)


@bp.route('/')
def index():
    return jsonify({"status": 200, "message": "API do Arthur Miele Malveste"})

@bp.route("/api/aleatorios")
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route("/api/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@bp.route('/api/A', methods=['GET'])
def contar_pessoas_maiores_de_50_route():
    contador = maior_de_50(pessoas)
    return jsonify({'quantidade': contador})

@bp.route('/api/B', methods=['GET'])
def contar_pessoas_mais_de_2000_route():
    count, porcentagem, total_registros = mais_2000(pessoas)
    return jsonify({'quantidade': count, 'porcentagem': porcentagem, 'total_registros': total_registros})

def salario_mais_baixo(lista):
    if len(lista) < 3:
        return None
    return min(pessoa['salario'] for pessoa in lista)

@bp.route('/api/C', methods=['GET'])
def obter_tres_maiores_salarios():
    tres_maiores_salarios = []
    for _ in range(3):
        pessoa = maior_salario(pessoas, maior=salario_mais_baixo(tres_maiores_salarios))
        tres_maiores_salarios.bpend(pessoa)
    return jsonify(tres_maiores_salarios)

@bp.route('/api/D', methods=['GET'])
def calcular_media_salarial_por_profissao():
    medias = media_profissoes(pessoas)
    return jsonify(medias)

@bp.route('/api/E', methods=['GET'])
def calcular_intervalo_idades_e_sexo():
    intervalo_idades, sexo = maior_2000_sexo(pessoas)
    return jsonify({'intervalo_idades': intervalo_idades, 'sexo': sexo})