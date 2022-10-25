from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("INDEX.html")

@app.route("/HOME")
def home():
   return render_template("INDEX.html")

@app.route("/GAS")
def Gas():
   return render_template("GAS.html")

@app.route("/LIQUID")
def Liquid():
   return render_template("LIQUID.html")

@app.route("/SOLID")
def Solid():
   return render_template("SOLID.html")

   
@app.route("/PLASMA")
def Plasma():
   return render_template("PLASMA.html")

@app.route("/success/<name>")
def success(name):
    return "Welcome %s" % name

@app.route('/LOGIN',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == "__MAIN__":
   app.run()