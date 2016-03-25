#!/usr/bin/env python

# Create a new folder called problem2 and put all problem2 related files in that folder including this file.
# Create a python file, say math_library.py, and add the functions for addition, subtraction, multiplication and division.
# In this file, call the functions addition, subtraction, multiplication and division that you defined in the math_library.py.
# Make sure that the program starts at the main function. Like in dinkelbach.py. Good job on the last one.



from math_library import *

def main_function():
	print 'hello world'
	
	Addition = add(a,b)
	print "The Addition of a and b:", Addition
	
	Subtraction = sub(a,b)
	print "The Subtraction of a and b:", Subtraction
	
	Multiplication = mul(a,b)
	print "The Multiplication of a and b:", Multiplication
	
	Division = div(a,b)
	print "The Division of a and b:", Division
	
if __name__ == "__main__":
	main_function()