# Ask user for their name
# input function takes a string as its input)
# This makes the code cleaner, shorter sand better
name = input("What's your name? ").strip().title()
# Split the user's name into first and last
first, last = name.split(" ")
print(f"Hello {first}")
# Removes the whitespace from the string (string in-built method) and capitalize it
#name = name.strip().title()
# Capitalize the user's name (the first letter)
#name = name.capitalize()
# Does the title based capitalization
#name = name.title()
# Kinda similar to one large argument
print("Hello " + name)
# Used with multiple args and a space is by default added
print("Hello", name)
# See documentation as print function has different parameters in it that can be overridden
print("Hello ", end = "")
print(name)
# or seeing the separator working as
print("Hello", name, sep = '??')
# Printing quotes within quotes(either use "" within '' or use \ escape char.)
print('Hello "friend"')
print("Hello \"friend\"")

# However, the elegant and most commonly used way of strings is by f/format strings
print(f"Hello {name}")
