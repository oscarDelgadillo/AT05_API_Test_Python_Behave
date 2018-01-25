from behave import given, use_step_matcher

use_step_matcher("re")


@given(u'I have a valid zipcode as (?P<zipcode>[0-9]+)')
def step_impl(context, zipcode):
    # raise NotImplementedError(u'STEP: Given I have a valid zipcode 432')
    print(zipcode)
    assert 1 == 1


@given(u'I have a valid country name as (?P<country>[a-zA-Z_]+)')
def step_impl(context, country):
    # raise NotImplementedError(u'STEP: Given I have a valid country Bolivia')
    print(country)
    assert 1 == 1


@given(u'I have a (?P<habitants>[0-9]{1,3}(,[0-9]{3})*) as habitants')
def step_impl(context, habitants):
    print(habitants)
    assert 1 == 1
