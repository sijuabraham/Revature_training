from flask import Flask
from controller.customer_controller import uc
from controller.account_controller import tc


if __name__ == '__main__':
    app = Flask(__name__)

    app.register_blueprint(uc)
    app.register_blueprint(tc)

    app.run(port=8080, debug=True)
