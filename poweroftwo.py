import math

NUMBER = int(input("Enter a number: "))

LOG = math.log(NUMBER, 2)
if (LOG).is_integer():
    print("The number given is a power of two! 2^{0} = {1}".format(int(LOG), NUMBER))
else:
    print("Your number isn't a power of two!")
