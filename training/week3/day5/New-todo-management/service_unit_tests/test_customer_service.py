import pytest

from exception.customer_already_exists import CustomerAlreadyExistsError
from exception.customer_not_found import CustomerNotFoundError
from exception.invalid_parameter import InvalidParameterError
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

def test_get_customer_by_customer_id_positive(mocker):

    def mock_get_customer_by_customer_id(self, customer_id):
        if customer_id == "333":
            return Customer(1, "333", "abc1234", "555-222-3333", "gg@email.com")
        else:
            return None
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_customer_id', mock_get_customer_by_customer_id)
    customer_service = CustomerService()
    actual = customer_service.get_customer_by_customer_id("333")
    assert actual == {
            "id": 1,
            "customer_id": "333",
            "customer_name": "abc1234",
            "mobile_num": "555-222-3333",
            "email": "gg@email.com"
        }
def test_get_customer_by_customer_id_negative(mocker):

    def mock_get_customer_by_customer_id(self, customer_id):
        if customer_id == "555":
            return Customer(1, "555", "abc1234", "555-222-3333", "gg@email.com")
        else:
            return None
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_customer_id', mock_get_customer_by_customer_id)
    customer_service = CustomerService()

    with pytest.raises(CustomerNotFoundError) as excinfo:
            customer_service.get_customer_by_customer_id("1000")
    assert str(excinfo.value) == "Customer with customer_id 1000 was not found"

def test_del_customer_by_customer_id_positive(mocker):
    def mock_del_customer_by_customer_id(self, customer_id):
        if customer_id =='111':
            return True
        else:
            return False

    mocker.patch('dao.customer_dao.CustomerDao.del_customer_by_customer_id', mock_del_customer_by_customer_id)
    customer_service = CustomerService()
    actual = customer_service.del_customer_by_customer_id("111")
    assert actual is None

def test_del_customer_by_customer_id_negative(mocker):
    def mock_del_customer_by_customer_id(self, customer_id):
        if customer_id =='111':
            return True
        else:
            return False

    mocker.patch('dao.customer_dao.CustomerDao.del_customer_by_customer_id', mock_del_customer_by_customer_id)
    customer_service = CustomerService()
    with pytest.raises(CustomerNotFoundError) as excinfo:
         customer_service.del_customer_by_customer_id("333")
    assert str(excinfo.value) == "Customer with customer_id 333 not found"

def test_add_customer_positive(mocker):

    customer_object_to_add = Customer(None, "222", "ddd", "222-333-4444", "abc@email.com")
    def mock_get_customer_by_customer_id(self, customer_id):
        if customer_id == "222":
            return None
    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_customer_id", mock_get_customer_by_customer_id)

    def mock_add_customer(self, customer_object):

        if customer_object == customer_object_to_add:
            return Customer(1, "222", "ddd", "222-333-4444", "abc@email.com")
        else:
            return None

    mocker.patch("dao.customer_dao.CustomerDao.add_customer", mock_add_customer)

    customer_service = CustomerService()

    actual = customer_service.add_customer(customer_object_to_add)
    assert actual == {
        "id": 1,
        "customer_id": "222",
        "customer_name": "ddd",
        "mobile_num": "222-333-4444",
        "email": "abc@email.com"
    }
def test_add_customer_negative_spaces_in_customer_id(mocker):

    customer_object_to_add = Customer(None, " 222 ", "ddd", "222-333-4444", "abc@email.com")

    customer_service = CustomerService()
    # customer_service.add_customer(customer_object_to_add)

    with pytest.raises(InvalidParameterError):
        customer_service.add_customer(customer_object_to_add)


def test_add_customer_negative_length_is_less_than_3_for_customer_id(mocker):

    customer_object_to_add = Customer(None, "22", "ddd", "222-333-4444", "abc@email.com")



    customer_service = CustomerService()

    with pytest.raises(InvalidParameterError) as excinfo:
        actual = customer_service.add_customer(customer_object_to_add)
        assert str(excinfo.value) == "Customer_id must be at least 3 characters"

def test_add_customer_negative_customer_id_already_exists(mocker):
    customer_object_to_add = Customer(None, "222", "ccc", "234-333-4444", "aa@email.com")
    def mock_get_customer_by_customer_id(self, customer_id):
        if customer_id == "222":
            return Customer(1, "222", "ccc", "234-333-4444", "aa@email.com")

    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_customer_id", mock_get_customer_by_customer_id)

    customer_service = CustomerService()
    with pytest.raises(CustomerAlreadyExistsError):
        customer_service.add_customer(customer_object_to_add)

def test_update_customer_by_customer_id_positive(mocker):
    customer_object_to_update = Customer(1, "333", "ccc", "333-555-5555", "bb@email.com")

    def mock_update_customer_by_customer_id(self, customer_object):
        if customer_object.customer_id == "333":
            return Customer(1, "333", "ccc", "333-555-5555", "bb@email.com")
    mocker.patch("dao.customer_dao.CustomerDao.update_customer_by_customer_id", mock_update_customer_by_customer_id)

    customer_service = CustomerService()
    actual = customer_service.update_customer_by_customer_id(customer_object_to_update)
    assert actual == {
        "id": 1,
        "customer_id": "333",
        "customer_name": "ccc",
        "mobile_num": "333-555-5555",
        "email": "bb@email.com"
    }

def test_update_customer_by_customer_id_negative(mocker):
    customer_object_to_update = Customer(1, "444", "ccc", "333-555-5555", "bb@email.com")

    def mock_update_customer_by_customer_id(self, customer_object):
        if customer_object.customer_id == "333":
            return Customer(1, "333", "ccc", "333-555-5555", "bb@email.com")
        else:
            return None
    mocker.patch("dao.customer_dao.CustomerDao.update_customer_by_customer_id", mock_update_customer_by_customer_id)

    customer_service = CustomerService()
    with pytest.raises(CustomerNotFoundError):
        customer_service.update_customer_by_customer_id(customer_object_to_update)

