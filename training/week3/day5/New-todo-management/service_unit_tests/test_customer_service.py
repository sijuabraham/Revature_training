from model.customer import Customer
from service.customer_service import CustomerService


def test_get_all_customers(mocker):
    def mock_get_all_customers(self):
        return [Customer(1, "222", "abc1234", "111-222-3333", "aa@email.com"), Customer(2, "333", "ddd1234", "555-222-3333", "fg@email.com")]
    mocker.patch('dao.customer_dao.CustomerDao.get_all_customers', mock_get_all_customers)
    customer_service = CustomerService()
    actual = customer_service.get_all_customers()
    assert actual == [
        {
            "id": 1,
            "customer_id": "222",
            "customer_name": "abc1234",
            "mobile_num": "111-222-3333",
            "email": "aa@email.com"
        },
        {
            "id": 2,
            "customer_id": "333",
            "customer_name": "ddd1234",
            "mobile_num": "555-222-3333",
            "email": "fg@email.com"
        }
    ]

def test_get_customer_by_customer_id(mocker):

    def mock_get_customer_by_customer_id(self, customer_id):
        if customer_id == 333:
            return Customer(1, "333", "abc1234", "555-222-3333", "gg@email.com")
        else:
            return None
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_customer_id', mock_get_customer_by_customer_id)
    customer_service = CustomerService()
    actual = customer_service.get_customer_by_customer_id(333)
    assert actual == {
            "id": 1,
            "customer_id": "333",
            "customer_name": "abc1234",
            "mobile_num": "555-222-3333",
            "email": "gg@email.com"
        }
