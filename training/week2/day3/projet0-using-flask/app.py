from flask import Flask

app = Flask(__name__)
customers = {
    "111": {
                "accounts": [{
                                "checking": [{
                                            "id": 1, "amount": 1000
                                             },
                                            {
                                            'id': 2, "amount": 2000
                                            }],
                                "savings": [{
                                                    "id": 1, "amount": 1000
                                                     },
                                                    {
                                                        'id': 2, "amount": 2000
                                                    }],

                            }]
            },
    "222": {
                "accounts": [{
                                "checking": [{
                                            "id": 1, "amount": 100
                                             },
                                            {
                                            'id': 2, "amount": 200
                                            }],
                                "savings": [{
                                                    "id": 1, "amount": 1000
                                                     },
                                                    {
                                                        'id': 2, "amount": 2000
                                                    }],

                            }]
            },
"333": {
                "accounts": []
            }
}


# for key in customers:
#     print(key)
# print(customers)

@app.route('/test')
def hello():
    return "Hello World"


@app.route('/customers')
def get_all_customers():
    my_customers = []

    for key in customers:
        customer = {
                    "customer_id": key,
                    "customer_accounts": customers[key]['accounts']
                    }
        my_customers.append(customer)
    return {
            "customers": my_customers
        }, 200


@app.route('/customers/<customername>')
def get_user_by_username(customername):
    if customername in customers:
        return {
            "customer_id": customername,
            "customer_accounts": customers[customername]['accounts']
                }
    else:
        return{
            "message":f"User with username {customername} does not exist"
        }




app.run(port=8080)


