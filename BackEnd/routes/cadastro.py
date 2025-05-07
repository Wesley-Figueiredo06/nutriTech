from flask import Blueprint, request, jsonify

cadastro_bp = Blueprint('cadastro', __name__)

usuarios = {}

@cadastro_bp.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.json
    usuario = data.get('usuario')
    senha = data.get('senha')

    if not usuario or not senha:
        return jsonify({'mensagem': 'Usuário e senha são obrigatórios.'}), 400

    if usuario in usuarios:
        return jsonify({'mensagem': 'Usuário já cadastrado.'}), 409

    usuarios[usuario] = senha
    return jsonify({'mensagem': 'Cadastro concluído.'}), 201



