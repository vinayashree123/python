from behave import given,when,then

@given('Launch the app and click on login button')
def step_impl(context):
     print("L1 - Launching the App")

@when('enter userid')
def step_impl(context):
    print('L2 - When enter userid')

@when('password')
def step_impl(context):
    print('L3 - When password')


@when('click on login button')
def step_impl(context):
    print('L4 - When click on login button')


@when(u'opens home page')
def step_impl(context):
    print('L5 - When opens home page')


@then('verify home page')
def step_impl(context):
    print('L6 - Then verify home page')


@then('take screenshot')
def step_impl(context):
    print('L7 - Then take screenshot')

#feature 2

@given(u'Launch the App and Click on ContactForm')
def step_impl(context):
    print('Given Launch the App and Click on ContactForm')


@when(u'Enter Name')
def step_impl(context):
    print('When Enter Name')


@when(u'Enter Email')
def step_impl(context):
    print(' When Enter Email')


@when(u'Enter Mobile Number')
def step_impl(context):
    print(' When Enter Mobile Number')


@when(u'we need to click on submit button')
def step_impl(context):
    print(' When we need to click on submit button')


@then(u'Click on submit')
def step_impl(context):
    print(' Then Click on submit')


@then(u'Take Screenshot of contact Form')
def step_impl(context):
    print(' Then Take Screenshot of contact Form')


