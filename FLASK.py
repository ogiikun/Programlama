from flask import Flask,render_template,redirect


app=Flask(__name__)

@app.route("/")   ##kök dizin index.html gibi
def anasayf():
    
    return render_template("index.html")



@app.route("/iletişim")
def iletişim():
    return render_template("iletişim.html")

@app.route("/hakkımızda")
def hakkımız():
    return render_template("hakkimiz.html")


@app.route("/filmler")
def filmler():

        return render_template ("film.html")

@app.route("/kayıt")
def kayıt():
    return render_template ("kayıt.html")

if __name__=="__main__":
    app.run()
