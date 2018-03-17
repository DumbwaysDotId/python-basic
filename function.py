# python
def get_name():
    return "Gaphur"

def sum(first_number, second_number):
    return first_number + second_number

print(get_name())
print(sum(1, 2))

def get_full_name():
    return get_name() + " ...."

print(get_full_name())

def print_custom():
    print('debug something')

    return "this is from custom print"

print(print_custom())
