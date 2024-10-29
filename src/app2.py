from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask import render_template

from config import config 

app=Flask(__name__)
con=MySQL(app)

@app.route("/")
def index():
	titulo='IEVN-1001'
	list=['Pedro','Juan','Fulanito','Sultanito']
	
	return render_template('uno.html',titulo = titulo, list = list)

@app.route("/user/<string:user>")#esto sirve para pasar parametros
def user(user):
	return "El usuario es: {}".format(user)

@app.route("/numero/<int:n1>")#esto sirve para pasar parametros
def numero(n1):
	return "El número es: {}".format(n1)
@app.route("/user/<string:nom>/<int:id>")#Se puede tener dos rutas con el mismo nombre, pero no el mismo método
def datos(nom,id):
	return "<h1>ID: {} Nombre: {}</h1>".format(id,nom)

@app.route("/suma/<float:n1>/<float:n2>")#esto sirve para pasar parametros
def suma(n1,n2):
	return "La suma es: {}".format(n2+n1)

@app.route("/default")
@app.route("/default/<string:nom>")

def nom2(nom = 'Kasss'):
	return"<h1> El nombre es: {} </h1>".format(nom)



if __name__ =="__main__":
	app.run(debug=True)