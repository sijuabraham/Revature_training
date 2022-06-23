from flask import Flask

app = Flask(__name__)
users = {
    "siju": {
        "mobile": "101-111-3322",
         "todos": [
                  {
                    "description": "Do laundry", "completed": False
                  },
                  {
                    "description": "Go to the doctor's office", "completed": False
                  },
                  {
                    "description": "Call Fred", "completed": False
                  },
                  {
                    "description": "Take out trash", "completed": True
                  },
                  {
                    "description": "Wash dishes", "completed": True
                  }
                  ]
            },
    "binu": {
        "mobile": "101-111-3322",
         "todos": []
            }
        }


@app.route('/test')
def hello():
    return "Hello World"


@app.route('/users')
def get_all_users():
    my_users = []
    for key in users:
        user = {
            "username": key,
            "mobile": users[key]['mobile'],
            "todos": users[key]['todos']
        }
        my_users.append(user)

    return {
        "users": my_users
    }, 200


@app.route("/users/<username>")
def get_user_by_username(username):
    if username in users:
        return {
            "username": username,
            "mobile": users[username]['mobile'],
            "todos": users[username]['todos']
        }
    else:
        return {
            "message": f"user with username {username} does not exist"
        }, 404



app.run(port=8080)  # startup the webserver on 8080
