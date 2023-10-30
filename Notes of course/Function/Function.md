we use it if I need to use a part of code more than once time
def name function (we can put argument or not):
the code 
we can call the function like this name function(if has arguments we have give the parameters )
return values can use it in the end of function
which default is considered? the default value of argument is empty but we can but the default value when we put the argument 
python style code recommends beginning the code block with a docstring *** fun desc ***
arbitrary argument lists I use it when I don't know how many parameters 
def name_fun(*args)
what the difference between if I definition the variables in side the function or out side?
if local or global 
global: in python can see it in all section of script scope
local: where definition is for example only in side the function
what happens to parameters defined in the fun after calling it?
if variable wasn't define within a function python will look for it in the global variables. however, unline other languages a function cannot modify a global variable
we can resolve this by using global in side the fun for example
be carful of the function 'shadow' of death
parameters passed by : value or reference
value : means I take a copy content from this variable and give it to parameters 
reference : that means I take the reference of variable name to function
Scope of Variables: Be mindful of variable scope. Variables inside a function do not affect variables with the same name outside the function.
Recursion: A function can call itself, which is called recursion. Be cautious when using recursion to avoid infinite loops.
Function Libraries: Python has a rich standard library with built-in functions for a wide range of tasks. You can also create your own libraries by organizing related functions into modules.
Best Practices: Write clear, concise, and well-documented functions. Functions should ideally have a single responsibility, making your code more modular and easier to maintain.
In Python, a lambda function is a small, anonymous function defined using the `lambda` keyword. Lambda functions are also known as anonymous functions or lambda expressions. They are typically used for short, simple operations that can be defined in a single line of code. Lambda functions are often used in situations where you need a small function for a short period and don't want to define a full function using the `def` keyword

