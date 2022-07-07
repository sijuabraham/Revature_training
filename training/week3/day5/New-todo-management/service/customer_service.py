from dao.customer_dao import CustomerDao
from exception.customer_already_exists import CustomerAlreadyExistsError
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError


class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):

         # return self.customer_dao.get_all_customers()
        list_of_customer_objects = self.customer_dao.get_all_customers()

        # Method #1. use a for loop and do it manually
        list_of_customer_dictionaries = []
        for customer_obj in list_of_customer_objects:
            list_of_customer_dictionaries.append(customer_obj.to_dict())

        return list_of_customer_dictionaries
        # # Method #2, use map
        # # return list(map(lambda x:x.to_dict(), list_of_user_objects)

    def get_customer_by_customer_id(self, customer_id):
        customer_obj = self.customer_dao.get_customer_by_customer_id(customer_id)
        if not customer_obj:
            raise CustomerNotFoundError(f"Customer with customer_id {customer_id} was not found")

        return customer_obj.to_dict()



    # 1. Check if username is atleast 6 characters
    # 2. check if username contains spaces ( not allowed)
    # Invoke add_user in DAO,passing in a user_object
    # Return the dictionary representation of the return value for that method

    def add_customer(self, customer_object):
        if " " in customer_object.customer_id:
            raise InvalidParameterError("Customer_id cannot contain spaces")

        if len(customer_object.customer_id) < 3:
            raise InvalidParameterError("Customer_id must be at least 3 characters")

        if self.customer_dao.get_customer_by_customer_id(customer_object.customer_id) is not None:
            raise CustomerAlreadyExistsError(f"Customer with customer_id {customer_object.customer_id} already exists in the database")

        added_customer_object = self.customer_dao.add_customer(customer_object)
        return added_customer_object.to_dict()

    def del_customer_by_customer_id(self, customer_id):

        if not self.customer_dao.del_customer_by_customer_id(customer_id):
            raise CustomerNotFoundError(f"Customer with customer_id {customer_id} not found")

    # Invoke edit_user_by_username in DAO, passing in a username and user_object
    # Return the dictionary representation of the return value for that method
    def update_customer_by_customer_id(self, customer_object):

        updated_customer_object = self.customer_dao.update_customer_by_customer_id(customer_object)
        if not updated_customer_object:
            raise CustomerNotFoundError()

        return updated_customer_object.to_dict()

