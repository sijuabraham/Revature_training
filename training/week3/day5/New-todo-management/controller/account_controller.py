from flask import Blueprint, request
from service.account_service import AccountService
from exception.customer_not_found import CustomerNotFoundError

tc = Blueprint("todo_controller", __name__)
account_service = AccountService()


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


@tc.route('/customers/customer_id/accounts/<account_id>')
def get_accounts_by_customer_id_and_account_id(customer_id, account_id):
    pass

@tc.route('/customers/customer_id/accounts', methods=['POST'])
def add_accounts_for_customer_by_customer_id(customer_id):
    pass

@tc.route('/customers/customer_id/accounts/<account_id>', methods=['PUT'])
def edit_accounts_for_customer_by_customer_id(customer_id,accounts_id):
    pass