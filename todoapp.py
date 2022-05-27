from flask import Flask, render_template, request, redirect, url_for  # librerias
from glob import escape
from os import abort

app = Flask(__name__)  # incializar variable


# funcion de bienvenida
@app.route('/')
def index():
    return render_template('index.html', NombreTarea = tareaNombre, CorreoTarea = correo, PrioridadTarea = prioridad)


tareaNombre = []
correo = []
prioridad = []

#add_tareas
@app.route('/', methods=['POST'])  # recive atravez del metodo POST
def add_tareas():
   if request.method == 'POST':
      # almacena el nombre de la tarea
      Nombre_Tarea = request.form['Nombre_Tarea']
      Correo_Tarea = request.form['Correo']
      prioridad_Tarea = request.form['prioridad']

      print(Nombre_Tarea)
      print(Correo_Tarea)
      print(prioridad_Tarea)

      tareaNombre.append(Nombre_Tarea)
      correo.append(Correo_Tarea)
      prioridad.append(prioridad_Tarea)

      #tareaNombre.clear()
      #correo.clear()
      #prioridad.clear()
      return redirect(url_for('index'))   
          
  
# main del programa
if __name__ == '__main__':
    app.run(debug=True)
