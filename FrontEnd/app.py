from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ads")
def ADS():
    return render_template("ads.html")


@app.route("/bd")
def BD():
    return render_template("bd.html")


@app.route("/ads2020_2")
def ADS2020_2():
    return render_template("ads-2020-2.html")


@app.route("/bd2020_2")
def BD2020_2():
    return render_template("bd-2020-2.html")


@app.route("/logistica2020_2")
def Logistica2020_2():
    return render_template("Logistica2020.2.html")


@app.route("/manufaturaavançada2020_2")
def manufaturaavançada_2():
    return render_template("manufaturaavançada20202.html")


@app.route("/manutençaodeaeronaves2020_2")
def ManutençaodeAeronaves2020_2():
    return render_template("manutençaodeaeronaves20202.html")


@app.route("/ads2021_1")
def ADS2021_1():
    return render_template("ads2021-1.html")


@app.route("/bd2021_1")
def BD2021_1():
    return render_template("bd2021-1.html")


@app.route("/dsm2021")
def DSM2021_1():
    return render_template("dsm2021.html")


@app.route("/logistica20211")
def Logistica20211():
    return render_template("Logistica20211.html")


@app.route("/manufaturaavançada20211")
def manufaturaavançada20211():
    return render_template("manufaturaavançada20211.html")


@app.route("/manutençaodeaeronaves2021_1")
def ManutençaodeAeronaves2021_1():
    return render_template("manutençaodeaeronaves20211.html")
