#
print("Sameer Khan")

# This is a single-line comment

"""
This is a multi-line comment.
It can span multiple lines.
Used for documentation or explanation.
"""

print("Comments example")

# Data Types in Python
# Integer
num = 10

# Boolean
is_active = True

# Character (Python has no char, single character string is used)
ch = 'A'

# Float
price = 99.5

# Double (Python uses float for double precision)
value = 123.456789

print("Integer:", num)
print("Boolean:", is_active)
print("Character:", ch)
print("Float:", price)
print("Double:", value)

# defining global and local variables
x = 50   # Global variable

def demo():
    x = 20   # Local variable
    print("Local variable x =", x)

demo()
print("Global variable x =", x)
