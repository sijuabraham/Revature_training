from flask import Blueprint, request
from service.account_service import AccountService
from exception.customer_not_found import CustomerNotFoundError
from exception.account_not_found import AccountNotFoundError
from model.account import Account

tc = Blueprint("todo_controller", __name__)
account_service = AccountService()


# class AccountNotfoundError:
#     pass


class AccountNotfoundError:
    pass


@tc.route('/customers/<customer_id>/accounts')
def get_all_accounts_by_customer_id(customer_id):
    try:
        return {
            "Accounts": account_service.get_all_accounts_by_customer_id(customer_id)  # a list of dictionaries
        }
    except CustomerNotFoundError as e:
        return {
            "message": f"Customer with customer_id {customer_id} not found"
         }, 404

@tc.route('/customers/<customer_id>/accounts/<account_id>')
def get_accounts_by_customer_id_and_account_id(customer_id, account_id):
    try:
        return {
        "Accounts": account_service.get_accounts_by_customer_id_and_account_id(customer_id, account_id)
        }
    except CustomerNotFoundError as e:
        return {


            "message": f"Customer with customer_id {customer_id} not found"
         }, 404
    except AccountNotFoundError as e:
        return {
            "message": f"Customer with Account_id {account_id} not found"
         }, 404


@tc.route('/customers/<customer_id>/accounts', methods=['POST'])
def add_accounts_for_customer_by_customer_id(customer_id):
    account_json_dictionary = request.get_json()
    account_object = Account(None, account_json_dictionary['balance'], customer_id,
                               account_json_dictionary['account_type_id'])
    try:
        return account_service.add_accounts_for_customer_by_customer_id(account_object)  # dictionary representation of the newly added user

    except CustomerNotFoundError as e:

        return {
                   "message": f"Customer with Customer_id {customer_id} is not found"
               }, 400

@tc.route('/customers/<customer_id>/accounts/<id>', methods=['PUT'])
def update_accounts_for_customer_by_customer_id(customer_id, id):
    account_json_dictionary = request.get_json()
    account_object = Account(id, account_json_dictionary['balance'], account_json_dictionary['cust_id'], account_json_dictionary['account_type_id'])
    try:
        return account_service.update_accounts_for_customer_by_customer_id(account_object)

    except CustomerNotFoundError as e:
        return {
                   "message": f"Customer with customer_id {customer_id} not found !"
               }, 404

@tc.route('/customers/<customer_id>/accounts/<a_id>', methods=['DELETE'])
def del_accounts_for_customer_by_customer_id(customer_id, a_id):
    try:
        account_service.del_accounts_for_customer_by_customer_id(customer_id, a_id)

        return {
                "message": f"Customer customer_id{customer_id} and account_id {a_id} deleted successfully"
            }
    except CustomerNotFoundError as e:
        return {
                "message": f"Customer with customer_id{customer_id} not found"
            }, 404