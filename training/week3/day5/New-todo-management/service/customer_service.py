from dao.customer_dao import CustomerDao
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError


class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):
        list_of_customer_objects = self.customer_dao.get_all_customers()

        # Method #1. use a for loop and do it manually
        list_of_customer_dictionaries = []
        for customer_obj in list_of_customer_objects:
            list_of_customer_dictionaries.append(customer_obj.to_dict())

        return list_of_customer_dictionaries
        # Method #2, use map
        # return list(map(lambda x:x.to_dict(), list_of_user_objects)

    def get_customer_by_customer_id(self, customer_id):
        customer_obj = self.customer_dao.get_customer_by_customer_id(customer_id)

        if not customer_obj:
            raise CustomerNotFoundError()

        return customer_obj.to_dict()



    # 1. Check if username is atleast 6 characters
    # 2. check if username contains spaces ( not allowed)
    # Invoke add_user in DAO,passing in a user_object
    # Return the dictionary representation of the return value for that method

    def add_customer(self, customer_object):
        if " " in customer_object.customer_id:
            raise InvalidParameterError("Customerid cannot contain spaces")

        if len(customer_object.customer_id) < 3:
            raise InvalidParameterError("Customerid must be at least 6 characters")

        added_customer_object = self.customer_dao.add_customer(customer_object)
        return added_customer_object.to_dict()

    def del_customer_by_customer_id(self, customer_id):

        if not CustomerDao.del_customer_by_customer_id(customer_id,):
            raise CustomerNotFoundError()

    # Invoke edit_user_by_username in DAO, passing in a username and user_object
    # Return the dictionary representation of the return value for that method
    def edit_customer_by_customer_id(self, customer_object):
        updated_customer_object = self.customer_dao.edit_customer_by_customer_id(customer_object)
        return updated_customer_object.to_dict()