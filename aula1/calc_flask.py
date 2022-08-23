from flask import Flask, render_template, request
import os 

'''
3 parametros
2 valores (int) e 1 resultado (str)
'''

app = Flask(__name__)

@app.route('/calc')

def calcula():
    valor1 = request.args.get('a')
    valor2 = request.args.get('b')
    op = request.args.get('op')

    a = int(valor1)
    b = int(valor2)

    if (op == 'soma'):
        resultado = a + b
    elif (op == 'subtrair'):
        resultado = a - b
    elif (op == 'dividir'):
        resultado = a // b
    elif (op == 'multiplicar'):
        resultado = a * b
    
    return str(resultado)
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host='127.0.0.1', port=port)

#http://127.0.0.1:5005/calc?a=10&b=5&op=soma
