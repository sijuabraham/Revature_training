import psycopg
from model.account import Account


class AccountDao:

        def get_all_accounts_by_customer_id(self, customer_id, query_params1, query_params2):

            with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="postgres123") as conn:

                with conn.cursor() as cur:

                    if query_params1 is not None and query_params2 is not None:

                        cur.execute("select * from accounts where cust_id = %s and balance > %s and balance < %s", (customer_id, query_params1, query_params2))

                    elif query_params1 is not None:

                        cur.execute("select * from accounts where cust_id = %s and balance > %s", (customer_id, query_params1))

                    elif query_params2 is not None:

                        cur.execute("select * from accounts where cust_id = %s and balance < %s", (customer_id, query_params2))

                    else:

                        cur.execute("select * from accounts where cust_id = %s", (customer_id,))




                    my_list_of_accounts_objs = []

                    for account in cur:

                        my_list_of_accounts_objs.append(Account(account[0], account[1], account[2], account[3]))

                    return my_list_of_accounts_objs

        def get_accounts_by_customer_id_and_account_id(self, customer_id, account_id):

            with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="postgres123") as conn:
                with conn.cursor() as cur:
                    cur.execute("select * from accounts where cust_id = %s and id = %s", (customer_id, account_id))

                # account_row = cur.fetchone()
                # if not account_row:
                #     return None
                    my_list_of_accounts_objs = []
                    for account in cur:
                        my_list_of_accounts_objs.append(Account(account[0], account[1], account[2], account[3]))

                    return my_list_of_accounts_objs

        def add_accounts_for_customer_by_customer_id(self, account_object):  # user will represent a user object
            account_balance_to_add = account_object.balance
            cust_id_to_add = account_object.cust_id
            account_type_id_to_add = account_object.account_type_id


            with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                                 password="postgres123") as conn:
                with conn.cursor() as cur:
                    cur.execute("insert into accounts(balance, cust_id, account_type_id) values(%s, %s, %s)returning *", (account_balance_to_add, cust_id_to_add, account_type_id_to_add))

                    account_row_that_was_just_inserted = cur.fetchone()
                    conn.commit()

                    return Account(account_row_that_was_just_inserted[0], account_row_that_was_just_inserted[1],
                                account_row_that_was_just_inserted[2], account_row_that_was_just_inserted[3])

        def update_accounts_for_customer_by_customer_id(self, account_object):

            with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                                 password="postgres123") as conn:
                with conn.cursor() as cur:

                    cur.execute("update accounts set id = %s, balance = %s, cust_id = %s, account_type_id = %s where  cust_id = %s and id = %s returning *",
                    (account_object.id, account_object.balance, account_object.cust_id, account_object.account_type_id, account_object.cust_id, account_object.id))
                    customer_row = cur.rowcount
                    if customer_row != 1:
                        return False

                    conn.commit()
                    updated_account_row = cur.fetchone()
                    a_id = updated_account_row[0]
                    a_balance = updated_account_row[1]
                    a_cust_id = updated_account_row[2]
                    a_type_id = updated_account_row[3]


                    return Account(a_id, a_balance, a_cust_id, a_type_id)


        def del_accounts_for_customer_by_customer_id(self, customer_id,a_id):

            with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="postgres123") as conn:
                with conn.cursor() as cur:

                    cur.execute("delete from accounts where cust_id = %s and id = %s", (customer_id, a_id))
            # print(cur.fetchone())
                    rows_deleted = cur.rowcount

                    if rows_deleted != 1:
                        return False
                    else:
                        conn.commit()
                        return True
