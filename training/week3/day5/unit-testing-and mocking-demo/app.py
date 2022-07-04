
import psycopg
def a():
    print("Function a() invoked!")
    return b() + 100


def b():
    print("Function b() invoked!")
    return -200

class CustomerDao:

    def get_all_customers(self):
            with psycopg.connect(host="127.0.0.1", port="5433", dbname="postgres", user="postgres", password="postgres123") as conn:
                cur = conn.cursor()

                cur.execute("select * from customers")

                customer_data = []
                for row in cur:
                    customer_data.append(row)
                return customer_data
def c():
    customer_dao = CustomerDao()
    return customer_dao.get_all_customers() # customer_dao.get_all_customers() is a dependency that we want to mock
# we don't want to unit test the c() function

# print(c())