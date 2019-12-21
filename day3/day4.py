#!/usr/bin/python

# Input given
bottom_of_range = 264360
top_of_range = 746325

def check_adjacent(input_num):
	num_list = []
	for number in str(input_num):
		num_list.append (int(number))
	for current_index, current_item in enumerate(num_list[:-1]):
		# Loop through each number and see if it has an adjacent number next to it
		if current_item == num_list[current_index+1]:
			return True
	return False

def check_decrease(input_num):
	num_list = []
	for number in str(input_num):
		num_list.append (int(number))
	for current_index, current_item in enumerate(num_list[:-1]):
		if current_item > num_list[current_index+1]:
			return False
	return True

def check_adjacent_part2(input_num):
	num_list = []
	for number in str(input_num):
		num_list.append (int(number))
	overall_match = False
	num_of_matches = 0

	# Cycle through each value in our number list. Enumerate returns the current index and the current value	
	for current_index, current_item in enumerate(num_list[:-1]):
		# Loop through each number and see if it has an adjacent number next to it
		if current_item == num_list[current_index + 1]:
			# This means our current value matches the next value. Increase our counter
			num_of_matches += 1
			if current_index == (len(num_list)-2):
				# We have hit the last number, so we need to do the same evaluation as below
				if num_of_matches == 1:
					overall_match = True
		else:
			# Our next value no longer matches our current. Let's see how many times we matched. If it's 2, that means our matches were limited to XX
			# Anything more disqualifies us according to the rules, so we disregard it and continue.
			if num_of_matches == 1:
				# Regardless of the rest of the number, we got what we wanted, so set this value
				overall_match = True
				break
			# Since there may be additional numbers left, reset the match count and keep going
			num_of_matches = 0
	return overall_match


password_count_part1 = 0
password_count_part2 = 0

for num in range(bottom_of_range, top_of_range+1):
	if check_adjacent(num) == True:
		if check_decrease(num) == True:
			password_count_part1 += 1
			# Part 2
			if check_adjacent_part2(num):
				password_count_part2 += 1
			
print("Total number of valid passwords for part 1 is: " + str(password_count_part1))
print("Total number of valid passwords for part 2 is: " + str(password_count_part2))
