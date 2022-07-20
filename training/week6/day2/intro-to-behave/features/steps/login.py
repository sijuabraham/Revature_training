@when(u'I click login')
def step_impl(context):
    print("FOUR")
    # Insert Selenium WebDriver code here that will click on the login button


@given(u'that I am at the login page')
def step_impl(context):
    print("ONE")
    # Insert Selenium WebDriver code here that will open the web browser and go to the login page


@when(u'I type in a valid username of john_doe')
def step_impl(context):
    pass
    #  Insert Selenium WebDriver code that will type in john_doe in the username input

@when(u'a valid password of password12345')
def step_impl(context):
    pass
    #  Insert Selenium WebDriver code that will type in password12345 in the username input


@then(u'I should be redirected to the student homepage')
def step_impl(context)
    pass
# Insert Selenium WebDriver code that will check if we are on the student homepage

@when(u'I type in a valid username of jane_doe')
def step_impl(context):
    pass
    #  Insert Selenium WebDriver code that will type in jane_doe in the username input


@when(u'a valid password of pass123')
def step_impl(context):
    pass
    # Insert Selenium WebDriver code that will type in pass123 in the username input

@when(u'I type in a valid username of bachy21')
def step_impl(context):
    pass
    # Insert Selenium WebDriver code that will type in bachy21 in the username input

@when(u'a valid password of password123')
def step_impl(context):
    pass
    # Insert Selenium WebDriver code that will type in password123 in the username input

@then(u'I should be redirected to the teacher homepage')
def step_impl(context):
    pass
    # Insert Selenium WebDriver code that will check if we are on the teacher homepage



