from practice_behave.customer_search.src.mod.clients import Clients
from practice_behave.customer_search.src.mod.prices import Prices
from behave import given, use_step_matcher, when, then
from compare import expect

use_step_matcher("re")


@given(u'I have two list of clients and prices')
def step_impl(context):
    context.list_clients = Clients()
    context.list_prices = Prices()


@when(u'I enter (?P<name>[a-zA-Z ]*) as name')
def step_impl(context, name):
    context.id_from_list = context.list_clients.get_id_by_name(name)
    context.name = name


@when(u'I enter (?P<id>[A-Z0-9]{5}) as ID')
def step_impl(context, id):
    context.price_from_list = context.list_prices.get_price_by_id(context.id_from_list)
    expect(context.id_from_list).to_equal(id)


@when(u'I enter (?P<price>[0-9]+\.[0-9]+) as a total price')
def step_impl(context, price):
    context.price = float(price)


@then(u'the total price should be in the total price list')
def step_impl(context):
    expect(context.price).to_equal(context.price_from_list)


@given(u'I have a list of clients')
def step_impl(context):
    context.list_clients = Clients()


@then(u'that name should be exist in the list of clients')
def step_impl(context):
    expect(context.list_clients.exist_client_in_list(context.name)).to_be_truthy()

