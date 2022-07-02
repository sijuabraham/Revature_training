class Account:
    def __init__(self, a_id, balance, cust_id, account_type_id):
        self.id = a_id
        self.balance = balance
        self.cust_id = cust_id
        self.account_type_id = account_type_id

    def to_dict(self):
        return {
            "id": self.id,
            "balance": self.balance,
            "cust_id": self.cust_id,
            "account_type_id": self.account_type_id
        }
