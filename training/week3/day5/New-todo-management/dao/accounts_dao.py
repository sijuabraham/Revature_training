import psycopg
from model.account import Account


class AccountDao:

        def get_all_accounts_by_customer_id(self, customer_id):

            with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="postgres123") as conn:
                cur = conn.cursor()
                cur.execute("select * from accounts where cust_id = %s", (customer_id,))

                account_list = []

                # for row in cur:
                # account_list.append(Account(row[0], row[1], row[2], row[3]))
                #
                # return account_list

                my_list_of_accounts_objs = []

                for account in cur:
                    # a_id = account[0]
                    # bal = account[1]
                    # cust_id = account[2]
                    # act_type_id = account[3]
                    my_list_of_accounts_objs.append(Account(account[0], account[1], account[2], account[3]))

                return my_list_of_accounts_objs



