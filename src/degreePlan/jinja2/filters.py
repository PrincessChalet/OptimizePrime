
# a jinja2 test used to determine if a variable is a list
def isList(l):
    if type(l) is list:
        return True
    else:
        return False

# a jinja2 filter used to extract a number from a string
def extractNumber(s):
    num = ''
    for c in s:
        if c.isdigit():
            num = num + c

    return int(num)
