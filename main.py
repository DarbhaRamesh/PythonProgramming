from Basics1 import basics1
from Basics2 import basics2

help(basics1)
basics1()
print('-'*25)
help(basics2)
basics2()


# After functions in Basics2 come here. 

# global_demo = 0
# def counter():
# 	global global_demo
# 	global_demo += 1
# 	return global_demo
	
# counter()
# counter()
# counter()
# counter()
# print(counter())

'''
Not a good practice to access different environments, it can become complex if we are building a large application.

Instead below can be done.
'''

# global_demo = 0

# def counter(global_demo):
# 	global_demo += 1
# 	return global_demo

# print(counter(counter(counter(counter(global_demo)))))

# print('-'*25)

# #non-local

# def outer():
# 	x= 'local'
# 	print("Before inner : ", x)
# 	def inner():
# 		nonlocal x #accesses immediate parent
# 		x='nonlocal'
# 		print("In inner : ", x)
# 	inner()
# 	print("After inner : " ,x)

# outer()
# print('-'*25)