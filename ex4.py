# the number of cars in inventory
cars = 100
# the number of spaces available for passengers in each car
space_in_a_car = 4.0
# the number of drives
drivers = 30
# the number of passengers
passengers = 90
# the number of cars less the number of drivers
cars_not_driven = cars - drivers
# the number of cars_drive is equal to the number of drivers available
cars_driven = drivers
# the number of cars times the number of spaces per car
carpool_capacity = cars_driven * space_in_a_car
# the average of passengers per cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."