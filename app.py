# Importa as bibliotecas Flask, request e jsonify
from flask import Flask, request, jsonify

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Define uma rota para o webhook do chatbot, que aceita apenas requisições POST
@app.route('/chatbot/webhook/', methods=['POST'])
def webhook():
    # Obtém os dados JSON da requisição POST
    data = request.json
    # Imprime os dados recebidos no console
    print(f'EVENTO RECEBIDO: {data}')
    # Retorna uma resposta JSON com status de sucesso
    return jsonify({'status': 'success'}), 200

# Executa a aplicação Flask se este arquivo for executado como o principal
if __name__ == '__main__':
    # Configura a aplicação para rodar no host 0.0.0.0 na porta 5000 com debug ativado
    app.run(host='0.0.0.0', port=5000, debug=True)