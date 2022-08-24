from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("calc.html")

@app.route("/calculadora", methods=["POST", "GET"])
def calcula():
    val1 = request.form.get("v1")  #o que esta entre ('') faz referencia ao html
    val2 = request.form.get("v2")
    op = request.form.get("op")
    print(op)

    v1 = int(val1)
    v2 = int(val2)

    if (op == 'soma'):
        resultado = v1 + v2
    elif (op == 'subtrair'):
        resultado = v1 - v2
    elif (op == 'dividir'):
        resultado = v1 // v2
    elif (op == 'multiplicar'):
        resultado = v1 * v2
    
    return str(resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host='127.0.0.1', port=port)   
    


