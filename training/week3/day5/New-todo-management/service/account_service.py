from dao.customer_dao import CustomerDao
from dao.accounts_dao import AccountDao
from exception.account_not_found import AccountNotFoundError
from exception.customer_not_found import CustomerNotFoundError


class AccountService:

    def __init__(self):
        self.account_dao = AccountDao()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id, query_params1, query_params2):

        # return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_customer_id(customer_id)))
            if self.customer_dao.get_customer_by_customer_id(customer_id) is None:
                raise CustomerNotFoundError()

            list_of_account_objects = self.account_dao.get_all_accounts_by_customer_id(customer_id, query_params1, query_params2)
            list_of_account_dictionaries = []
            for account_obj in list_of_account_objects:
                list_of_account_dictionaries.append(account_obj.to_dict())

            return list_of_account_dictionaries

    def get_accounts_by_customer_id_and_account_id(self, customer_id, account_id):
        if self.customer_dao.get_customer_by_customer_id(customer_id) is None:
            raise CustomerNotFoundError()
        # if self.account_dao.get_accounts_by_customer_id_and_account_id(customer_id, account_id) is None:
        #     raise AccountNotFoundError()
        # else:

        list_of_account_objects = self.account_dao.get_accounts_by_customer_id_and_account_id(customer_id, account_id)
        if not list_of_account_objects:
            raise AccountNotFoundError()
        else:
            list_of_account_dictionaries = []
            for account_obj in list_of_account_objects:
                list_of_account_dictionaries.append(account_obj.to_dict())

            return list_of_account_dictionaries

    def add_accounts_for_customer_by_customer_id(self, account_object):
        if self.customer_dao.get_customer_by_customer_id(account_object.cust_id) is None:
            raise CustomerNotFoundError()

        added_account_object = self.account_dao.add_accounts_for_customer_by_customer_id(account_object)
        return added_account_object.to_dict()
    def update_accounts_for_customer_by_customer_id(self, account_object,cust_id):

        if self.customer_dao.get_customer_by_customer_id(cust_id) is None:
            raise CustomerNotFoundError()

        updated_account_object = self.account_dao.update_accounts_for_customer_by_customer_id(account_object)
        if not updated_account_object:
            raise AccountNotFoundError()

        return updated_account_object.to_dict()

    def del_accounts_for_customer_by_customer_id(self, customer_id, a_id):

        if self.customer_dao.get_customer_by_customer_id(customer_id) is None:
            raise CustomerNotFoundError()


        if not self.account_dao.del_accounts_for_customer_by_customer_id(customer_id, a_id):
            raise AccountNotFoundError()


