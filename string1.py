meaning = 4
print('')

# if meaning > 10:
#     print('Right on!')
# else:
#     print('Not today')

# Ternary operator
print('Right on!') if meaning > 10 else print('Not today')

# Literal assignment
first = "Tariq"
last = "Ahsan"
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor function
pizza = "cheese"
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

# Casting a number to string
decade = str(1980)
print(type(decade))
print(decade)

# Multiple lines
multiline = '''
Hey! how are you?

I was just Checking in.    
            All good?
           
'''
print(multiline)

# Escaping special character
sentence = 'I\'m back at work\t Hey!\n\nWhere\'s this at\\located?'
print(sentence)

# String methods -- shft + alt + down arrow
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))

print(len(multiline))
multiline +="                               "
multiline = "        " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")
# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$3".rjust(4))

# string index values
print("")
print(first)
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some methods return boolean data
print("")
print(first.startswith("T"))
print(first.endswith("T"))
print(first.endswith("Q"))
print(first.endswith("q"))

# Boolean data type
print("")
myvalue = True # not 'true'
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))