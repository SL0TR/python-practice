def greeting(name):
    print("hello there " + name)

greeting("Mohaimin")

def cube(num):
    return num * num * num


result = cube(5)
print(result)

is_male = False
is_small = False

if is_male and is_small:
    print("male and small")
elif is_male and not(is_small):
    print("You neither male or tall")
else:
    print("You neither male or tall PERIOD")

