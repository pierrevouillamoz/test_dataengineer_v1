from flask import Flask, render_template, request, url_for, flash, redirect
app = Flask(__name__)

import recuperation as recup
import exploitation as explo

data=list()

@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/recuperation_nettoyage', methods=('POST',))
def recuperation_nettoyage():
    
    #La récupération des données se fait en une ligne
    recup.fonction_recuperation()
    return redirect(url_for('index'))

@app.route('/graph',methods=('GET','POST'))
def graph():
    
    if request.method == "POST":
        date = request.form["date"]
        #l'exploitation des données se fait en une ligne
        explo.fonction_exploitation(date=date)
        return render_template("graph.html", date=date)
    
    return render_template('graph.html', date=None) 
 
if __name__ == "__main__":
    app.run("0.0.0.0", 5000)

app.run(debug=True)