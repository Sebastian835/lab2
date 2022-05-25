from flask import Flask, render_template

app = Flask (__name__)      #incializar variable


#funcion de bienvenida
@app.route('/')

def principal():
    return render_template('index.html')


@app.route('/')
def contacto():
    return render_template(' ')


@app.route('/ ')
def lenguajesdeprogramacion():
    return render_template(' ')


#main del programa
if __name__ == '__main__':
    app.run(debug=True)
