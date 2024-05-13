from flask import Blueprint, jsonify, request
from funcoes import maior_de_50
from random_data import *
from funcoes import *


bp = Blueprint("api", __name__)

@bp.route('/')
def index():
    return jsonify({"status": 200, "message": "API do Arthur Miele Malveste"})

@bp.route("/aleatorios")
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@bp.route('/A', methods=['GET'])
def contar_pessoas_maiores_de_50_route():
    contador = maior_de_50(pessoas)
    return jsonify({'quantidade': contador})

@bp.route('/B', methods=['GET'])
def contar_pessoas_mais_de_2000_route():
    count, porcentagem, total_registros = mais_2000(pessoas)
    return jsonify({'quantidade': count, 'porcentagem': porcentagem, 'total_registros': total_registros})

def salario_mais_baixo(lista):
    if len(lista) < 3:
        return None
    return min(pessoa['salario'] for pessoa in lista)

@bp.route('/C', methods=['GET'])
def obter_tres_maiores_salarios():
    tres_maiores_salarios = []
    for _ in range(3):
        pessoa = maior_salario(pessoas, maior=salario_mais_baixo(tres_maiores_salarios))
        tres_maiores_salarios.bpend(pessoa)
    return jsonify(tres_maiores_salarios)

@bp.route('/D', methods=['GET'])
def calcular_media_salarial_por_profissao():
    medias = media_profissoes(pessoas)
    return jsonify(medias)

@bp.route('/E', methods=['GET'])
def calcular_intervalo_idades_e_sexo():
    intervalo_idades, sexo = maior_2000_sexo(pessoas)
    return jsonify({'intervalo_idades': intervalo_idades, 'sexo': sexo})
