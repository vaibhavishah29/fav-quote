from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:vaibhu123@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://krikdsngtlzdxk:e4aa9970e336b0d35c2f578d518aa8b53098b04ba932804178ea8bdebe25084c@ec2-54-197-100-79.compute-1.amazonaws.com:5432/d7s8lsihvnfat4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(1000))


@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']

    quotedata = Favquotes(author=author, quote=quote)

    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
