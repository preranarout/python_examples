# Problem description:
# Take an input of two integers from the user and perform addition, subtraction, multiplication and division using different functions and print the output.
# Also, make sure that your program can do the same functions for floating point values.


a, b = input("Enter two Integers: ")

def add(a,b):
	return a + b
	
Addition = add(a,b)
print "The Addition of a and b:", Addition

def sub(a,b):
	return a - b
	
Subtraction = sub(a,b)
print "The Subtraction of a and b:", Subtraction

def mul(a,b):
	return a * b
	
Multiplication = mul(a,b)
print "The Multiplication of a and b:", Multiplication

def div(a,b):
	return a / b
	
Division = div(a,b)
print "The Division of a and b:", Division