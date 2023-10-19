from flask import Flask

from app.routes import routes_blueprint


app = Flask(__name__)
app.register_blueprint(routes_blueprint)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
