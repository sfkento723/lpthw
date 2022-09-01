# Number of cars = 100

cars = 100

# Amount of space in a car = 4

space_in_a_car = 4

# Number of drivers = 30

drivers = 30

# Number of passengers = 90

passengers = 90

# Deficit between cars and drivers if there are more cars than drivers = 70

cars_not_driven = cars - drivers

# Number of cars driven = 30

cars_driven = drivers

# Total amount of carpool space = 120

carpool_capacity = cars_driven * space_in_a_car

# Average number of passengers in a car = 3

average_passengers_per_car = passengers / cars_driven

# There are 100 cars available.

print("There are", cars, "cars available.")

# There are only 30 drivers available.

print("There are only", drivers, "drivers available.")

# There will be 70 empty cars today.

print("There will be", cars_not_driven, "empty cars today.")

# We can transport 120 people today.

print("We can transport", carpool_capacity, "people today.")

# We have 90 to carpool today.

print("We have", passengers, "to carpool today.")

# We need to put about 3 in each car.

print("We need to put about", average_passengers_per_car, "in each car.")
