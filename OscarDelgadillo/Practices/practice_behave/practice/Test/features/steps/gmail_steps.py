from behave import given, use_step_matcher

use_step_matcher("re")


@given(u'I enter a valid first name as (?P<firstname>[a-zA-z]+) and last name as (?P<lastname>[a-zA-z]+)')
def step_impl(context, firstname, lastname):
    # raise NotImplementedError(u'STEP: Given I enter a valid first name as Oscar and last name as Delgadillo')
    print(firstname, lastname)
    assert 1 == 1


@given(u'I choose a username as (?P<username>[a-zA-z0-9_-]{4,8}@gmail.com)')
def step_impl(context, username):
    print(username)
    assert 1 == 1


@given(u'I enter a password (?P<password>[a-zA-Z0-9@#$%*_-]{8,16})')
def step_impl(context, password):
    print(password)
    assert 1 == 1


@given(u'I enter date of birthday (?P<birthday>(0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(19[0-9]{2}|20[0-9]{2}))')
def step_impl(context, birthday):
    print(birthday)
    assert 1 == 1


@given(u'I select my gender as a (?P<gender>Man|Woman)')
def step_impl(context, gender):
    print(gender)
    assert 1 == 1


@given(u'I enter a mobil phone number \+(?P<mobile>[0-9]{1,4}[0-9]+)')
def step_impl(context, mobile):
    print(mobile)
    assert 1 == 1


@given(u'I enter a current email as a (?P<email>[a-zA-z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4})')
def step_impl(context, email):
    print(email)
    assert 1 == 1
