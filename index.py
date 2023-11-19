from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #Creacion de ruta home
def home():
    return render_template("home.html")

@app.route('/monitoreo') #Creacion de ruta monitoreo
def monitoreo():
    return render_template("home.html")

@app.route('/riskmap') #Creacion de ruta riskmap
def riskmap():
    return render_template("riskmap.html")

if __name__ == '__main__':
    app.run(debug=True)