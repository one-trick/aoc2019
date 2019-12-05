#!/usr/bin/python

# Sum of fuel required to transport all modules
fuel_sum = 0
# Sum of fuel required to transport all modules + fuel
total_fuel_sum = 0

with open("input", "r") as fh:
	for line in fh:
		mass = int(line.rstrip())
		# Get fuel required for module. Dont need to round down as int wont have decimal
		fuel = (mass / 3) - 2
		# Add the fuel to the total amount required to transport all modules 
		fuel_sum = fuel_sum + fuel
		# For the second challenge, we need the fuel required for modules, but also need additional fuel for fuel
		total_fuel_sum = total_fuel_sum + fuel
		# Now figure out additional fuel needed for the fuel we just added
		additional_fuel = (fuel / 3) - 2
		# Add the additional fuel to the total sum
		total_fuel_sum = total_fuel_sum + additional_fuel
		# At this point, we need to loop through the above until we hit zero or negative
		while additional_fuel > 0:
			additional_fuel = (additional_fuel / 3) - 2
			# Only add positive integers to the total
			if additional_fuel > 0:
				total_fuel_sum = total_fuel_sum + additional_fuel
	print("Fuel required for modules (Part 1): " + str(fuel_sum))
	print("Fuel required for modules + additional fuel (Part 2): " + str(total_fuel_sum))
		
		

