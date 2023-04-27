from flask import Flask, render_template, request
from markupsafe import escape
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/votacao/<int:id>", methods=["POST"])
def votacao(id):
        if id == 1:
             redis_client.incr('fulano')
             return f"Você votou em Fulano[{redis_client.get('fulano')}], obrigado"
        else:
             redis_client.incr('siclano')
             return f"Você votou em Siclano[{redis_client.get('siclano')}], obrigado"

@app.route('/resultado', methods=["POST"])
def resultado():
    if redis_client.get('fulano') > redis_client.get('siclano'):
         return f"Fulano foi o campeão com {redis_client.get('fulano')} votos"
    if redis_client.get('fulano') < redis_client.get('siclano'):
         return f"Siclano foi o campeão com {redis_client.get('siclano')} votos"
    if redis_client.get('fulano') == redis_client.get('siclano'):
         return f"A competição deu empate com {redis_client.get('siclano')} votos para ambos"

@app.route('/zera', methods=['POST'])
def zera():
    redis_client.set('fulano', 0)
    redis_client.set('siclano', 0)
    msg = "Competição zerada"
    return render_template("home.html", msg=(msg))

if __name__ == "__main__":
    app.run(host="0.0.0.0")