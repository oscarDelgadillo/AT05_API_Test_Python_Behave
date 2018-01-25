from behave import given


@given(u'I have ${amount:d} in my account')
def step_impl(context, amount):
    # raise NotImplementedError(u'STEP: Given I have $100 in my account')
    print("inside of the step", amount)
