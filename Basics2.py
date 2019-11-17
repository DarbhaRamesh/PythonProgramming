#conditional and loops

def basics2(execute = False):
	if execute:
		#if elif else
		print("if elif else demonstration")
		#age = int(input("Enter age"))
		age = 20
		if age >= 18 and age < 50:
			print("Eligible for license")
		elif age < 18:
			print("Too young to apply")
		else:
			print("Too old to apply")
		print('-'*25)

		#Truthy and falsey values

		'''
		Empty string, list, tuple, dictionary, set, None, 0 etc are considered as falsey values

		Except these all are truthy values
		'''
		print("Truthy and falsey values demonstration")

		valid = None

		if valid:
			print("Valid")
		else:
			valid = 'yes'
		
		if valid:
			print("Valid")
		
		print('-'*25)

		#Ternary Operator

		print("Ternary Operator")

		condition = True

		can_message = "message allowed" if condition else "message not allowed"

		print(can_message)

		print('-'*25)

		'''
		Short circuiting

		if condition1 and condition2:
			logic
		
		if condition1 is false, python interpretor doesn't check for condition2. Because the entire expresseion gives false even if condition2 is true or false.

		if condition1 or condition2:
			logic
		
		if condition1 is true, python interpretor doesn't check for condition2. Because the entire expresseion gives true even if condition2 is true or false.
		
		This concept is called short circuiting and it enhances the performance.

		'''

		#logical operators - >, <, ==, >=, <=, !==, and, or , not

		print("Logical operators")

		print(1 == 1)
		print(not (1 == 1))
		print(1 != 1)
		print('-'*25)
		
		#is vs ==
		print(True == 1)
		print('' == 1)
		print([] == 1)
		print(10 == 10.0)
		print([] == [])
		print([1,2,3] == [1,2,3])
		print('-'*25)
		print(True is 1)
		print('' is 1)
		print([] is 1)
		print(10 is 10.0)
		print([] is [])
		print([1,2,3] is [1,2,3])
		print('-'*25)
		
		'''
		Difference is == checks for values and tries to convert to bool.In first statement,1 will be converted to bool.whereas 'is' checks for the memory location and values in it.
		Therefore, there is difference in output of [] == [] and [] is []

		'''

		#loops
		'''
		for loop 

		for variable in iterable:
			logic

		iterable - list, string, tuple, dictionary, set

		'''
		print('for loop')

		for item in 'python':
			print(item)
		print('-'*5)
		print(item)
		print('-'*25)

		print('looping over dictionary')
		user = {
			'name' : 'john',
			'age' : 25,
			'can_swim' : True
		}
		print('with dictionary variable')
		for item in user:
			print(item)
		print('-'*5)

		print('with .items()')
		for item in user.items():
			print(item)
		print('-'*5)

		for key, value in user.items():
			print(key, value)
		print('-'*5)

		print('with .values()')
		for item in user.values():
			print(item)
		print('-'*5)

		print('with .keys()')
		for item in user.keys():
			print(item)
		
		print('-'*25)
		
		#range
		print(range(0,10,2))
		print(list(range(10,0,-2)))

		for _ in range(0,10,2):
			print(_)
		
		print('-'*25)
		
		#Best practice is that if a variable is _, indicates that we are not using that variable in the loop

		#enumerate
		for item in enumerate('Hello'):
			print(item)
		print('-'*25)

		#while - easy to fall in trap of infinite loop

		i = 0
		while i < 5:
			print(i)
			i+=1 #most important otherwise will fall into trap
		print("Done iterating")
		print('-'*5)

		while i < 5:
			print(i)
			i+=1
			break
		else:
			print("Done iterating")
		
		print('-'*25)

		# explore break, continue and pass