# Print "Mary had a little lamb."

print("Mary had a little lamb.")

# Print "Its fleece was white as snow."
print("Its fleece was white as {}.".format('snow'))

# Print "And everywhere that Mary went."

print("And everywhere that Mary went.")

# Print ".........."

print("." * 10) # what'd that do?

# Declare end1 to end6 as "Cheese".

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"

# Declare end7 to end12 as "Burger".

end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# Removing the comma produces a syntax error.

# Print "Cheese ". (Note the space at the end.)

print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')

# Print "Burger".

print(end7 + end8 + end9 + end10 + end11 + end12)
