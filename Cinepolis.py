from flask import Flask, render_template, request
import boletos_cinepolis

app = Flask(__name__)

@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():

    if request.method == "POST":
        
        nombreCliente = request.form.get("txtNombre")
        compradores = request.form.get("txtCantCom")
        boletos = request.form.get("txtBoletos")
        op = request.form.get("rbtnTarjeta")

        if boletos is not None:
            b = int(boletos)
        else:
            b = 0
        
        if compradores is not None:
            com = int(compradores)
        else:
            com = 0

        
        res = boletos_cinepolis.ventaTicket(op, b, com)
            
        detalle = "{} \n Número de boletos: {}, personas: {}".format(nombreCliente, boletos, compradores)
        
        

        return render_template("Cinepolis.html", res = res, detalle = detalle)
    
    return render_template("Cinepolis.html")

    
    
    



if __name__=="__main__":
    app.run(debug=True,port=3000)


