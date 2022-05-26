from flask import Flask, render_template, request

app = Flask(__name__)  # incializar variable


#funcion de bienvenida
@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/add_tareas', methods=['POST'])
def add_tareas():
   if request.method == 'POST':
      Nombre_Tarea = request.form['Nombre_Tarea']
      Correo = request.form['Correo']
      #prioridad = request.form['prioridad']
      print(Nombre_Tarea)
      print(Correo)
      #print(prioridad)
      return 'OK'
     
  
# main del programa
if __name__ == '__main__':
    app.run(debug=True)
