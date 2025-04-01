from flask import Flask, jsonify
import random

app = Flask(__name__)

# Função para gerar um número aleatório de telefone em Angola com o prefixo +244
def generate_angola_number():
    # O número começa com +244 e depois tem 9 dígitos aleatórios
    number = "+244" + "".join([str(random.randint(0, 9)) for _ in range(9)])
    return number

@app.route('/get-number', methods=['GET'])
def get_number():
    # Gera 10 números aleatórios no formato de Angola com o prefixo +244
    numbers = [generate_angola_number() for _ in range(10)]
    return jsonify({"numbers": numbers})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
