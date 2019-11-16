# Python Programming

How does machine understand Python code?

Its a high level language(which is understood by us, not by machine(it only understands O's and 1's)), therefore this needs to be converted to machine understandable language. We need a translator to translate this.

There are two types of Translators

Compiler (which reads whole code and translates) and Interpretor (which reads code line by line and translates)

Python uses Interpretor.

There are different python interpretors. When we refer to python,its mostly cpython i.e a program written in C to read python file and run it on a machine. Other are Jython(Translator written in Java),PyPy(written in python),IronPython(used for .Net framework) etc

Good source to dive in about different interprtors - https://docs.python-guide.org/starting/which-python/

when we download python from https://www.python.org/, its cpython.

Story of Python by creator - https://www.youtube.com/watch?v=J0Aq44Pze-w
## Python2 vs python3
some code which works in python2 doesn't work in python3
 
Example: In python2, print statement is print "Hello World"
 
In python3, its print("Hello world")

Checkout for more info. https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html 

# How does python works?
By interprtor, Python code is converted to bytecode and this bytecode is converted to 0's and 1's by python virtual machine. In this process, first interpretor checks for any syntactical errors,if yes, haults the process and throws error, if no, it translates to bytecode. and if any error occurs during tanslating byte code, haults the process and throws error,otherwise code will be translated and runs as per instructions.

# Essentials for learning any programming lanuage
Terms(different words,different definitions for these words),datatypes(what sort of data can hold),actions(store data, retrieve data and do some actions on it like printing, adding two numbers etc) and best practices.

# Data types
* int, float,complex, bool, str, list, tuple, set, dict

* Classes - custom types

* Specialized data types - Not built in to python but these are special packages, modules we can use from libraries.

* None (absence of value/nothing)

# Best practices for variable representation in python
* should be snake_case (Example: this_is_a_variable)

* start with lower case or underscore

* should consists of numbers,letters and underscore

* case sensitive

* Dont overwrite keywords

* should be descriptive

* if a variable is declared in capital letters it means it is constant. PI=3.14. can change it but it means its a constant.

* __something means its a dunder. its a special type of variable

# Best practices of Commenting your code 

  https://realpython.com/python-comments-guide/



