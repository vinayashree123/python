from behave import given,when,then

@given('Launch the app and click on login button')
def step_impl(context):
     print("L1 - Launching the App")

@when('enter {userid} userid')
def step_impl(context,userid):
    context.userid = userid
    print('L2 - When enter userid {}'.format(context.userid))

@when('password {password}')
def step_impl(context,password):
    context.pwd = password
    print('L3 - When password {}'.format(context.pwd))


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





