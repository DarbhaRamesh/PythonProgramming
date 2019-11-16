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

sample_list = ['toys',3,'Notebooks',5,'sunglasses',7]
print("lists" , sample_list)
print("list slicing", sample_list[0::2])
print("list slicing", sample_list[1::2])
sample_list[0] = "laptop"
print("lists mutable", sample_list)

#copying vs modifying list

print("-" * 25)
new_list = sample_list[:]
new_list[0] = 'grapes'
print("original list ", sample_list)
print("copied list ", new_list)

new_list = sample_list
new_list[0] = "Apples"
print("original list ", sample_list)
print("modified list ", new_list)
print("-" * 25)

#Matrices - used in datascience, image processing

# let say, Below matrix represents x

matrix = [
	[1, 0, 1],
	[0, 1, 0],
	[1, 0, 1]
]

print("matrix", matrix[0][0])
print("-" * 25)

#list Methods

#adding
basket = [1,2,3,4,5]
basket.append(100)
print("Append : ", basket)
basket.insert(2,101)
print("Inserting at index 2 : ", basket)
basket.extend([102, 103])
print("Extending a list : ", basket)
print("-" * 25)

#deleting
basket.pop()
print("pop : ", basket)
basket.pop(7)
print("pop at index 7 : ", basket)
basket.remove(100)
print("remove 100 : ", basket)
basket.clear()
print("clear : ", basket)
print("-" * 25)

#indexing
basket = ['a', 'b', 'c', 'd', 'e', 'd', 'c']
print(basket)
print("Indexes : ",basket.index('d'))
print("'d' between index 4 to 6 : ", basket.index('d',4,6))
#index returns error if element is not found 

print("In operator : ", 'c' in basket)
print("In operator : ", 'x' in basket)

print("counting an element", basket.count('d'))
print("-" * 25)

#sorting
basket = ['a', 'b', 'c', 'x','d', 'e', 'z', 'y']
print(basket)
basket.sort()
print("Inplace sort : ", basket)
basket = ['a', 'b', 'c', 'x','d', 'e', 'z', 'y']
print("sorting : ",sorted(basket))
print("No change in basket : ",basket)

#reverse
basket.reverse()
print("Inplace reversed list", basket)
print("-" * 25)
new_list = basket[::-1]
print("reversed list : ", new_list)
print("No change in basket : ",basket)
print("-" * 25)

#list to String 

sample_list = ['It\'s', 'a', 'Python', 'Module']
new_list = " ".join(sample_list)
print(new_list)
print("-" * 25)

#Removing spaces
new_list = "  " +new_list + "  " 
print("Original string with space : ", new_list)
print(len(new_list))
new_list = new_list.rstrip()
print("string without space at right : ",new_list)
print(len(new_list))
new_list = new_list.lstrip()
print("string without space at left : ",new_list)
print(len(new_list))
new_list = "  " +new_list + "  "
print("Original string with space : ",new_list)
print(len(new_list))
new_list = new_list.strip()
print("string without space : ",new_list)
print(len(new_list))
print("-" * 25)

#list unpacking

a,b,c,*others,d =[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(others)
print(d)
print("-" * 25)

#dictionary - its unordered key value pair

#dictionary keys must be immutabele and unique (otherwise wll overwrite the previous value)

dictionary = {
	'a' : 1,
	'b' : 2,
	'c' : 3
 }

 #accessing Keys

print(dictionary['a'])
#print(dictionary['d']) #- will get key error since it doesnt exist

print(dictionary.get('d'))

print("returns value of key specified : ",dictionary.get('d',4))

print("returns value of key from dictionary : ",dictionary.get('c',6))

user = dict(name = 'John' , age = 32)

print("creating a dictionary : ",user)

user.clear()

print(user)

print("-" * 25)

#dictionary methods

print("Keys : ",dictionary.keys())
print("Values :",dictionary.values())
print("Items",dictionary.items())

print('c' in dictionary.keys())
print(2 in dictionary.values())
print(('a' , 1) in dictionary.items())

print("-" * 25)

sample_dict  = dictionary.copy()
print(sample_dict)

print(sample_dict.pop('a'))
print(sample_dict)

print(sample_dict.popitem()) #Be careful with this as it randomly removes an item as it is unordered
print("-" * 25)
print(dictionary)
print("Updates the key value if present : ",
dictionary.update({'c' : 5}))
print(dictionary)
print("Adds the key value if not present :",
dictionary.update({'e' : 10}))
print(dictionary)
print("-" * 25)

#tuple - Immutable

my_tuple = (1,2,3,5,8,3,4,6,3)

print(my_tuple[0])
print(5 in my_tuple)

new_tuple = my_tuple[1:2]
print(new_tuple)

x,y,*other,z = (1,2,3,4,5,6,7,8,9)
print(other)

print("-" * 25)

print(my_tuple)
print("count of 3: ", my_tuple.count(3))
print("index of 2 : " , my_tuple.index(2))
print("length of tuple : ", len(my_tuple))

print("-" * 25)

#set - unordered collection of unique objects
my_set = {1,2,2,3,4,5,4,5}
print(my_set)
my_set.add(100)
my_set.add(2) #this doesnt get added as it is present already
print(my_set)
print(1 in my_set)
print("-" * 25)


my_list = [1,2,3,4,5,5,4,3,2]
print(list(set(my_list)))
print("-" * 25)


print(my_set)
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

print("-" * 25)

# set methods
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

print(set1.difference(set2))
print(set1)
print(set2.difference(set1))
print(set2)
print("-" * 25)

set1.discard(5)
print(set1)
print("-" * 25)
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

set1.difference_update(set2)
print(set1)

set2.difference_update(set1)
print(set2)
print("-" * 25)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

print(set1.intersection(set2))
print(set1 & set2)
print(set1.isdisjoint(set2))
print(set1.union(set2))
print(set1|set2)
print("-" * 25)

set1 = {4,5}
set2 = {4,5,6,7,8,9,10}
print(set1.issubset(set2))
print(set2.issuperset(set1))