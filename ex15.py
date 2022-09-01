# Import command line arguments from system


# Open the given filename

filename = input("Enter file name: ")
txt = open(filename)

# Display file contents

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()
