# Cian Hogan week 4 task
# take input and in its even divide by 2 if its odd muliply by 3 and add one
# https://en.wikipedia.org/wiki/Collatz_conjecture

# make sure the program doesnt crash if user enters an invalid response
try:
	num = int(input("Enter a positive whole number: "))

# make sure the user enters a positive number
	if num > 0:
		print(num, end=" ") # print the selected number without staring a new line after
		while num != 1: # run until num is 1

			if num % 2 == 0: # check for even number
				num = num/2
			# if the number is odd, do the following	
			else:
				num = (num * 3) + 1
			# print the updated number at the end of each iteration
			print(int(num), end=" ")
			
	else: # print out for input of negative number	
		print(num, "Doesn't look like a positive whole number. Try again")

except ValueError: # print out for user input error
	print("Are you sure you entered a whole number? Try again")