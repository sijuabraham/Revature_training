from model.customer import Customer
import psycopg
import copy
# Right now, we don't have a database to connect to
# So we will store data inside of a collection


class CustomerDao:
    def get_all_customers(self):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="postgres123") as conn:

            # cur = conn.cursor()
            with conn.cursor() as cur:
                cur.execute("select * from customers")
                # cust_all = cur.fetchall()
                # print(cust_all)
                # return "success"

                my_list_of_customers_objs = []

                for customer in cur:
                    c_id = customer[0]
                    customer_id = customer[1]
                    customer_name = customer[2]
                    mobile_num = customer[3]
                    email = customer[4]

                    my_customer_obj = Customer(c_id, customer_id, customer_name, mobile_num, email)
                    my_list_of_customers_objs.append(my_customer_obj)

                return my_list_of_customers_objs



    def add_customer(self, customer_object):  # user will represent a user object
        customer_id_to_add = customer_object.customer_id
        customer_name_to_add = customer_object.customer_name
        customer_mobile_num_to_add = customer_object.mobile_num
        customer_email_to_add = customer_object.email

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="postgres123") as conn:
            with conn.cursor() as cur:
                cur.execute("insert into customers(customer_id, customer_name, mobile_num, email) values(%s, %s, %s, %s)returning *", (customer_id_to_add, customer_name_to_add, customer_mobile_num_to_add, customer_email_to_add))

                customer_row_that_was_just_inserted = cur.fetchone()
                conn.commit()

                return Customer(customer_row_that_was_just_inserted[0], customer_row_that_was_just_inserted[1],
                            customer_row_that_was_just_inserted[2], customer_row_that_was_just_inserted[3],customer_row_that_was_just_inserted[4])


    def del_customer_by_customer_id(self, customer_id):

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="postgres123") as conn:
            with conn.cursor() as cur:

                cur.execute("delete from customers where customer_id = %s", (customer_id,))
            # print(cur.fetchone())
                rows_deleted = cur.rowcount

                if rows_deleted != 1:
                    return False
                else:
                    conn.commit()
                    return True

    def get_customer_by_customer_id(self, customer_id):

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="postgres123") as conn:
            with conn.cursor() as cur:

                cur.execute("select * from customers where customer_id = %s", (customer_id,))

                customer_row = cur.fetchone()

                if not customer_row:
                    return None

                c_id = customer_row[0]
                customer_id = customer_row[1]
                customer_name = customer_row[2]
                customer_mobile_num = customer_row[3]
                customer_email = customer_row[4]

                return Customer(c_id, customer_id, customer_name, customer_mobile_num,  customer_email)

    def update_customer_by_customer_id(self, customer_object):

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="postgres123") as conn:

            with conn.cursor() as cur:

                cur.execute("update customers set id = %s, customer_id = %s, customer_name = %s, mobile_num = %s, email = %s  where  customer_id = %s returning *", (customer_object.id, customer_object.customer_id, customer_object.customer_name, customer_object.mobile_num, customer_object.email, customer_object.customer_id))
                customer_row = cur.rowcount
                if customer_row != 1:
                    return False

                conn.commit()
                updated_customer_row = cur.fetchone()
                c_id = updated_customer_row[0]
                cust_id = updated_customer_row[1]
                cust_name = updated_customer_row[2]
                cust_mobile = updated_customer_row[3]
                cust_email = updated_customer_row[4]

                return Customer(c_id, cust_id, cust_name, cust_mobile, cust_email)

