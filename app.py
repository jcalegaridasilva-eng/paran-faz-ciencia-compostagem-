from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'chave_super_secreta_uem' # Troque para produção

# Configuração do Banco de Dados (SQLite preparado para migração PostgreSQL)
# Para PostgreSQL, mude para: 'postgresql://user:password@localhost/dbname'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ==========================================
# MODELOS DE BANCO DE DADOS
# ==========================================
class Compostagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    tipo_residuo = db.Column(db.String(100), nullable=False)
    peso_kg = db.Column(db.Float, nullable=False)
    observacoes = db.Column(db.Text)
    responsavel = db.Column(db.String(100))

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    temperatura = db.Column(db.Float)
    umidade_solo = db.Column(db.Float)
    umidade_ar = db.Column(db.Float)
    nivel_agua = db.Column(db.Float)
    irrigacao_ativa = db.Column(db.Boolean, default=False)

# Cria as tabelas no primeiro start
with app.app_context():
    db.create_all()

# ==========================================
# ROTAS FRONTEND
# ==========================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        senha = request.form['password']
        # Simulação de login - Conectar com tabela de Usuários depois
        if user == 'admin' and senha == 'uem2026':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    registros = Compostagem.query.order_by(Compostagem.data.desc()).limit(10).all()
    sensores = SensorData.query.order_by(SensorData.timestamp.desc()).first()
    return render_template('dashboard.html', registros=registros, sensores=sensores)

# ==========================================
# API REST PARA O ESP32 (IoT)
# ==========================================
@app.route('/api/esp32/update', methods=['POST'])
def update_sensors():
    """ Rota para receber o JSON do ESP32 """
    data = request.get_json()
    if not data:
        return jsonify({"erro": "Nenhum dado recebido"}), 400
    
    novo_dado = SensorData(
        temperatura=data.get('temp'),
        umidade_solo=data.get('umid_solo'),
        umidade_ar=data.get('umid_ar'),
        nivel_agua=data.get('nivel_agua'),
        irrigacao_ativa=data.get('irrigacao')
    )
    db.session.add(novo_dado)
    db.session.commit()
    return jsonify({"status": "sucesso", "mensagem": "Dados registrados"}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)