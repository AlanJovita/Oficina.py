from flask import Flask,render_template
from Data.base import connectionString, db

from Routes.carro import carro
from Routes.cliente import cliente
from Routes.produto import produto
from Routes.usuario import usuario

app = Flask(__name__,template_folder="View")
app.config['SQLALCHEMY_DATABASE_URI'] = connectionString()

db.init_app(app)

app.register_blueprint(carro)
app.register_blueprint(cliente)
app.register_blueprint(produto)
app.register_blueprint(usuario)

@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True)
