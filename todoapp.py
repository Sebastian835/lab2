from flask import Flask, render_template, request, redirect, url_for         #librerias

app = Flask(__name__)  # incializar variable


#funcion de bienvenida
@app.route('/')
def index():
    return render_template('index.html')

  
# main del programa
if __name__ == '__main__':
    app.run(debug=True)
