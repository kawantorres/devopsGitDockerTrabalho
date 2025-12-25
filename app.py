from flask import   Flask

import requests

app = Flask(__name__)

@app.route('/')

def index():
    try:

        response = requests.get('http://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl')
        dados = response.json()

        preco = dados['bitcoin']['brl']
        return f"<h1> Monitoramento de criptos</h1> <p> O preço atual  do Bitcoin esta sendo: R$ {preco}</p>"
    except:
        return "<h1>Erro ao buscar dados</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)