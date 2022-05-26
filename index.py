from flask import Flask, render_template, request, redirect, url_for         #librerias

app = Flask(__name__)  # incializar variable


#funcion de bienvenida
@app.route('/')
def index():
    return render_template('index.html')

#funcion para traer las tareas del index add_tareas 
@app.route('/add_tareas', methods=['POST'])             #  recive atravez del metodo POST    
def add_tareas():
   if request.method == 'POST':
      Nombre_Tarea = request.form['Nombre_Tarea']       #almacena el nombre de la tarea
      Correo = request.form['Correo']                  
      prioridad = request.form['prioridad']  
      return redirect(url_for('index'))               
    
     
  
# main del programa
if __name__ == '__main__':
    app.run(debug=True)
