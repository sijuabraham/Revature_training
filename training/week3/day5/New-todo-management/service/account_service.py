from dao.accounts_dao import AccountDao
from dao.customer_dao import CustomerDao
from service.customer_service import CustomerService
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError


class AccountService:

    def __init__(self):
        self.account_dao = AccountDao()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id):

        # return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_customer_id(customer_id)))
            if self.customer_dao.get_customer_by_customer_id(customer_id) is None:
                raise CustomerNotFoundError()

            list_of_account_objects = self.account_dao.get_all_accounts_by_customer_id(customer_id)
            list_of_account_dictionaries = []
            for account_obj in list_of_account_objects:
                list_of_account_dictionaries.append(account_obj.to_dict())

            return list_of_account_dictionaries
