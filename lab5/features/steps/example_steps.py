from behave import given, when, then
from lab_python_fp.sort import sort_abs, sort_abs1

@given("List is [{array}]")
def step_given(context, array):
    context.array = [int(i) for i in array.split(', ')]

@when("Sorted this list with Sort_abs")
def step_when(context):
    context.sorted_array = sort_abs(context.array)

@then("List is [{array}]")
def step_then(context, array):
    result = [int(i) for i in array.split(', ')]
    assert context.sorted_array == result   
