from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Lista de números aleatórios gerados
numeros_disponiveis = [f"+2449{random.randint(10000000, 99999999)}" for _ in range(10)]
mensagens_recebidas = {}

# Rota para gerar e retornar um número aleatório
@app.route("/get-number", methods=["GET"])
def get_number():
    numero = random.choice(numeros_disponiveis)
    mensagens_recebidas[numero] = []  # Cria uma caixa de entrada vazia para o número
    return jsonify({"numero": numero})

# Rota para enviar uma mensagem para um número
@app.route("/receive-sms", methods=["POST"])
def receive_sms():
    numero = request.json.get("numero")
    mensagem = request.json.get("mensagem")
    
    # Verifica se o número é válido
    if numero in mensagens_recebidas:
        mensagens_recebidas[numero].append(mensagem)
        return jsonify({"status": "Mensagem recebida!"})
    else:
        return jsonify({"status": "Número inválido!"}), 400

# Rota para obter todas as mensagens de um número específico
@app.route("/get-messages/<numero>", methods=["GET"])
def get_messages(numero):
    return jsonify({"mensagens": mensagens_recebidas.get(numero, [])})

if __name__ == "__main__":
    app.run(debug=True)