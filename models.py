import os, yahoo

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

page = {}


@app.route("/")
def home():
    if request.method == 'POST':
        data = yahoo.get_yahoo_data(request.form['ticker'])

        if data is None:
            flash('Invalid Stock Ticker')
            return redirect(url_for('/'))

        return render_template("stock.html", stock_data=data)
    elif request.method == 'GET':
        print('viewing page')
        return render_template("home.html",
                               page=page
                               )


@app.route('/stock')
def single_stock(ticker):
    if request.method == 'POST':
        data = yahoo.get_yahoo_data(ticker)

        if data is None:
            flash('Invalid Stock Ticker')
            return redirect(url_for('/'))

        return render_template("stock.html", stock_data=data)
    elif request.method == 'GET':
        return render_template('stock.html')
