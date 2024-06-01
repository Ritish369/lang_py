# Can directly typecast the inputs to int by:
#x = int(input("What's x? "))
#y = int(input("What's y? "))

# Can directly typecast the inputs to float by:
x = float(input("What's x? "))
y = float(input("What's y? "))

# Won't work since the default input coming from keyboard is text i.e., a string
# Thus, concatenating the input numbers here
#z = round(x + y)
z = x / y
# Specify the number of digits to be rounded upto which is optional according to the documentation
#z = round(x / y, 2)

# This will work due to conversion from string to the integer version of thee input variables
# Because of typecasting
#z = int(x) + int(y)

# And printing the arithmetic directly without using any intermediate var
# Both are the same except the syntax kinda
print(round(x + y))
# Used for priniting in specfic formats, that's why, f is used (here the usual comma separation i nbig numbers)
# f is used when a string gneeds to be formatted
#print(f"{z:,}")
# number of decimsl digits wnt to print in a formatted way
print(f"{z:.2f}")
print(z)