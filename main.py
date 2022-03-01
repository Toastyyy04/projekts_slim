from flask import Flask, render_template, request

app = Flask('app')


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/autonomas_automasinas')
def autonomas_automasinas():
  return render_template("autonomas_automasinas.html")

@app.route('/ka_rezervet_automasinu')
def ka_rezervet_automasinu():
  return render_template("ka_rezervet_automasinu.html")

@app.route('/second_dot')
def second_dot():
  return render_template("second_dot.html")

@app.route('/third_dot')
def third_dot():
  return render_template("third_dot.html")

@app.route('/fourth_dot')
def fourth_dot():
  return render_template("fourth_dot.html")

@app.route('/fifth_dot')
def fifth_dot():
  return render_template("fifth_dot.html")

@app.route('/sixth_dot')
def sixth_dot():
  return render_template("sixth_dot.html")

@app.route('/autonomas_kontakti')
def autonomas_kontakti():
  return render_template("autonomas_kontakti.html")

@app.route('/log_in')
def log_in():
  return render_template("log_in.html")

@app.route('/reservacija')
def reservacija():
  return render_template("reservacija.html")



@app.route('/log_in', methods = ['POST']) 
def get_data(): 
    login = request.form['login']
    password = request.form['password']
    if request.method == 'POST': 
        with open('data.txt', 'a+') as f:
            f.write(str(login) + ' ' + str(password) + '\n')
    return render_template("log_in.html") 

@app.route('/autonomas_noteikumi')
def autonomas_noteikumi():
  return render_template("autonomas_noteikumi.html")



app.run(host='0.0.0.0', port=8080)
