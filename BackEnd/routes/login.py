from flask import Blueprint, request, jsonify
from routes.cadastro import usuarios

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = data.get('usuario')
    senha = data.get('senha')

    if not usuario or not senha:
        return jsonify({'sucesso': False, 'mensagem': 'Usuário e senha são obrigatórios.'}), 400

    if usuario in usuarios and usuarios[usuario] == senha:
        return jsonify({'sucesso': True, 'mensagem': 'Login realizado com sucesso!'}), 200
    else:
        return jsonify({'sucesso': False, 'mensagem': 'Login incorreto.'}), 401
