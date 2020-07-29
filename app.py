from flask import Flask, jsonify
from Horoscope import Horoscope

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify("Use api")


@app.route("/<string:p>")
def sign_horoscope(p):
    horoscope = Horoscope(p)
    return jsonify({
        "horoscope": horoscope.horoscope(),
        "matches": horoscope.matches(),
        "star_rating": horoscope.star_ratings(),
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
