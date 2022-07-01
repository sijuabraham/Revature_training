class Customer:
    def __init__(self, id, customer_id, customer_name, mobile_num, email):
        self.id = id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.mobile_num = mobile_num
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "mobile_num": self.mobile_num,
            "email": self.email
        }
