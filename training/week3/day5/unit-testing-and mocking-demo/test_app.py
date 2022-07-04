from app import a, c
import psycopg

# A unit test case will fail if any exception occurs that is not handled
# Otherwise, it will pass
# Example of a unit test where we are mocking a function

def test_a(mocker):

    # What is the SUT (System under test)?
    # Answer: function a()

    # AAA
    # Arrange: set up whatever is necessary for the system under test
    # arrange is not necessary in this case

    # Here we are setting up a mock for function b() and telling it what to return instead of actually executing
    # the real function b
    mocker.patch('app.b', return_value=-1)

    # Act: invoke the SUT
    #actual = a()  # Here we invoke a(), which is what we are testing, which will then invoke b() (which is the
    # dependency that we mock)

    # Assert: failing the test if the assertion is not True
    # An assert, if False, produces an exception that will fail the test

    actual = a()
    assert (actual == 99)


def test_c(mocker):
    # Arrange
    def mock_get_all_customers(self):
        return [(4, '666', 'test123', '111-222-3333', 'aa@email.com'), (5, '777', 'ggg', '444-555-6666', 'gg@email.com')]
    mocker.patch('app.CustomerDao.get_all_customers', mock_get_all_customers)
    # Act


    # Assert
    actual = c()

    assert actual == [(4, '666', 'test123', '111-222-3333', 'aa@email.com'), (5, '777', 'ggg', '444-555-6666', 'gg@email.com')]



