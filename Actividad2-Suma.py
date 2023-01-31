from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/operasbas", methods = ["GET"])
def operasbas():
    return render_template("operasbas.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    n1=request.form.get("txtNum1")
    n2=request.form.get("txtNum2")
    suma = 0
    i = 0
    
    while i < int(n2):
        suma = int(n1) + suma
        i+=1
        

    res = suma
    
    return render_template("resultado.html", res=res)


if __name__=="__main__":
    app.run(debug=True,port=3000)