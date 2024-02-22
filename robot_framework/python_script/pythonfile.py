from robot.api.deco import keyword
@keyword("custom keyword")
def add(a, b):
    result = a + b
    return result
# add(10,20)
