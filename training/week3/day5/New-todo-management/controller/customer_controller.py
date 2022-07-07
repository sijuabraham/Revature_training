from flask import Blueprint, request

from exception.customer_already_exists import CustomerAlreadyExistsError
from service.customer_service import CustomerService
from model.customer import Customer
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError

uc = Blueprint('customer_controller', __name__)
customer_service = CustomerService()


@uc.route('/customers')
def get_all_customers():

    # return customer_service.get_all_customers()
    return {
        "customers": customer_service.get_all_customers()  # a list of dictionaries
    }


@uc.route('/customers/<customer_id>', methods=['GET'])
def get_customer_by_customer_id(customer_id):
    try:
        return customer_service.get_customer_by_customer_id(customer_id)  # dictionary

    except CustomerNotFoundError as e:
        return{
            "message": f"Customer with customer_id {customer_id} was not found "
        }, 404


@uc.route('/customers/<customer_id>', methods=['DELETE'])
def del_customer_by_customer_id(customer_id):
    try:
        customer_service.del_customer_by_customer_id(customer_id)

        return {
                "message": f"Customer with customer_id {customer_id} deleted successfully"
            }
    except CustomerNotFoundError as e:
        return {
                "message": f"Customer with customer_id {customer_id} not found"
            }, 404


@uc.route('/customers', methods=['POST'])
def add_customer():
    customer_json_dictionary = request.get_json()
    customer_object = Customer(None, customer_json_dictionary['customer_id'], customer_json_dictionary['customer_name'], customer_json_dictionary['mobile_num'], customer_json_dictionary['email'])
    try:
        return customer_service.add_customer(customer_object), 201  # dictionary representation of the newly added user
        # 201 created
    except InvalidParameterError as e:

        return {
            "message": str(e)
        }, 400
    except CustomerAlreadyExistsError as e:
        return {
            "message": str(e)
        }, 400

@uc.route('/customers/<customer_id>', methods=['PUT'])
def update_customer_by_customer_id(customer_id):

    customer_json_dictionary = request.get_json()
    customer_object = Customer(customer_json_dictionary['id'], customer_id, customer_json_dictionary['customer_name'],
                              customer_json_dictionary['mobile_num'], customer_json_dictionary['email'])
    try:
        return customer_service.update_customer_by_customer_id(customer_object)

    except CustomerNotFoundError as e:
        return {
                    "message": f"Customer with customer_id {customer_id} not found !"
        }, 404

