import requests
from behave import *
from utilities.configurations import getConfig
from utilities.payLoad import addBookPayload
from utilities.resources import ApiResources


@given('the book details which need to add into library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload('m109', '227')


@when('execute AddBook post API method')
def step_impl(context):
    addBook_response = requests.post(context.url, json=context.payload, headers=context.headers, )
    print(addBook_response.json())
    context.response_json = addBook_response.json()
    print(context.response_json)

    context.bookId = context.response_json['ID']
    print(context.bookId)


@then('the book is successfully added')
def step_impl(context):
    if context.response_json['Msg'] != 'successfully added':
        assert 'Book Already Exists'


# implement parameterized to test scenario
@given('the book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload(isbn, aisle)
