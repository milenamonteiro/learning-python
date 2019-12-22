"""Create a function that returns a reversed string without using .reverse() or reversed()
given: Hello, World!
return: !drloW ,olleH"""

# https://docs.python.org/2/whatsnew/2.3.html#extended-slices

def reverso(text):
    return text[::-1]

print(reverso("cash"))