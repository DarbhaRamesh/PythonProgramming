## Data types
## int float bool str list tuple set dict.
print("Int and float")
print(type(2))
print(2 + 4)
print(type(2 + 4))
print(2 - 4)
print(type(2 - 4))
print(2 * 4)
print(type(2 * 4))
print(2 / 4)
print(type(2 / 4))
print("-" * 25 )
print(4E2) # 4*(10^2)
print(4e2)
print("-" * 25 )
#float takes lot more memory than int.

print("2 to the power 3" , 2 ** 3)
print( "4 // 3", 4 // 3)
 #returns an integer which is rounded down
print("4 % 3", 4 % 3)

#math functions
print("Rounding 5.526535 to 2 decimal places ",round(5.526535,2))
print("absolute value of -52",abs(-52))

#complex (a+ib)
print("complex number",complex(2+3j))
print("real part of 2+3j", (2+3j).real)
print("imaginary part of 2+3j", (2+3j).imag)

print("-" * 25 )

print("Binary number",bin(5)) # 0,1
print(int('0b101', 2))

print("Octadecimal Number",oct(8)) #0,1,2,...7
print(int('0o10', 8))

print("Hexadecimal number",hex(15)) # 0,1...9,a,b,c,d,e,f
print(int('0xf', 16))

print("Hexadecimal number",hex(20))
print(int('0x14', 16))

print("-" * 25 )

#operator precedence
# ()
# **
# * /
# + -

'''
best practices for variable representation
should be snake_case
start with lower case or underscore
should consists of numbers,letters and underscore
case sensitive
Dont overwrite keywords
if a variable is declared in capital letters it means it is constant. PI=3.14. can change it but it means its a constant.
__something means its a dunder. its a special type of variable

'''

a,b,c =1,2,3
print(a,b,c)

# expression (which gives output) vs statement
iq=100
user_age= iq/2
#expression is iq/2 ans statement is iq=100 or user_age=iq/2

#augmented assignment operator
some_value= 5
some_value += 2 #can be used with +, -, *, /, //
print("augmented assignment", some_value)
print("-" * 25 )

#strings
print("Strings")

long_string = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''
print(long_string)
print("-" * 25 )

#Type conversion
#str(),int()
print("Type conversion",float('5'))
print("-" * 25 )

#Escape sequence
weather = '\t It\'s sunny \n Hope you have a good day'
print("Escape sequence")
print(weather)
print("-" * 25 )

#Formatted strings
print("Formatted strings")
name = "John"
age = 32

print(f'Hi {name}! You are {age} years old') #newer version

#In older versions
print('Hi {0}! You are {1} years old'.format(name,age))

print('You are {1} years old. Hi {0}!'.format(name,age))

print('Hi {new_name}! You are {new_age} years old'.format(new_name=name,new_age=age))

print("-" * 25 )

print("string Indexes")

number_string = "0123456789"

# [start:stop:stepover]
print(number_string[0::2])
print(number_string[-1:-5:-1])
print(number_string[::-1])

'''
strings are immutable
gives error number_string[0] = '5'
if you want to change u need to completely change
'''
number_string = '5678901234'
print("Strings Immutable" , number_string)
print("-" * 25 )

quote = "to be or not to be"
print("Length" , len(quote))
print("upper",quote.upper())
print("capitalize",quote.capitalize())
print("lower",quote.lower())
print("find",quote.find("be"))
print("rfind",quote.rfind("be"))
print("replace",quote.replace("be","me"))

print("-" * 25 )

#boolean
print(bool(5))
print(bool(None))
print("-" * 25)

#list
