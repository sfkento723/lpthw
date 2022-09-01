# Declare that there are 2 types of people in binary.

types_of_people = 10

# Declare the setup to the joke.

x = f"There are {types_of_people} types of people."

# Declare variable binary as the string "binary"

binary = "binary"

# Declare variable do_not as its contraction "don't" as a string

do_not = "don't"

# Declare the punchline.
# Two strings (binary and do_not) are inserted into string y.

y = f"Those who know {binary} and those who {do_not}."

# Print the setup.

print(x)

# Print the punchline.

print(y)

# Insert string x inside of another string, and output it.

print(f"I said: {x}")

# Insert string y inside of another string, and output it.

print(f"I also said: '{y}'")

# That joke sucked.

hilarious = False

# Declare a string asking if the joke was funny.

joke_evaluation = "Isn't that joke so funny?! {}"

# Print that the joke sucked.

print(joke_evaluation.format(hilarious))

# Declare the left side of the string.

w = "This is the left side of..."

# Declare the right side of the string.

e = "a string with a right side."

# Print both sides of the string.

print(w + e)
