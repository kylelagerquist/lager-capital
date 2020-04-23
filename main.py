from flask import Flask, render_template, redirect, request, url_for
#from models import *
import yahoo

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)
page = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quote", methods=['GET', 'POST'])
def quote():
    """If user puts quote in url, redirect back to home page"""
    if request.method == 'GET':
        return redirect("/")

    """Search bar sends form data here to be processed"""
    return redirect(url_for('stock_detail', ticker=request.form.get('ticker')))


@app.route("/quote/<string:ticker>", methods=["GET", "POST"])
def stock_detail(ticker):
    """User types ticker into url or submits search form"""
    if request.method == 'GET':
        stock_data = yahoo.get_stock_data(ticker)
        return render_template("stock.html", stock_data=stock_data)
    else:
        stock_data = yahoo.get_stock_data(request.form.ticker)
        return render_template("stock.html", stock_data=stock_data)


app.run(debug=True)