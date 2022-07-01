from flask import Flask
from controller.customer_controller import uc


if __name__ == '__main__':
    app = Flask(__name__)

    app.register_blueprint(uc)

    app.run(port=8080, debug=True)
