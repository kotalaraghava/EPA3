# Scopes & Closures:

A variable is only available from inside the region it is created. This region is called **Scope**. Four Types of Scope: Local, Enclosing, Global & Built-in. 

**Closure** is a function(inner) that's defined withing the scope of other function(outer). Return value of outer function is the inner function itself.
Two important things to understand here, **Enclosing Scope** and **Free Variable(Non-Local)**.

Example:

        def greeting(word):
            def greet(name):
                return f'{word}, {name}'
            return greet

        hi = greeting('Hi')
        hi('Test')
        >> 'Hi, Test'

Now let's breakdown those two. First **Enclosing Scope**, hard to explain in writing, but check this **greeting()** has its own local scope and same goes for greet(). Now notice that greet() uses **word**, which is a free variable(non-local one), while **name** is in local variable. **greet()** binds with non local variable, **word** and returns the string output. **Free Variable** is the one which is not in the inner func's scope but in the Enclosing scope. Now for greet(), the enclosing scope is greeting()'s local scope. The Python Interpreter looksup for the variable in LEGB order i.e, Local, Enclosing,Global and Built-in scopes.

## Docstring Length Checker :

Used Closure which takes a function as input and then checks whether the function has a docstring with more than 50 Characters. Here the length acts as free variable. And the inner main function checks the docstring character length. 


    def check_docstring(length = 50): # outer function
            '''
            Closure which checks if a function has sufficient num of docstring char(50).
            '''
            validate_len(length)

            def check_len(func_name: object): # inner function
            
                validate_func(func_name)
            
                if func_name.__doc__ is None:
                    return 'Function has got no Docstring!'
                elif len(func_name.__doc__) >= length:
                    return f'Func has got {len(func_name.__doc__)} Chars in Docstring.'
                else:
                    return f'Insufficient no of Chars in Docstring({len(func_name.__doc__)}).'
            return check_len

## Fibonacci Series Generator :
Wrote a simple closure which generates next Fibonacci Number. Now this uses start and end as free variable, which is assigned to 0 & 1 initially. The next value of series is obtained by summing by start and end, which are then swapped to end and new value respectively.


	def series():
		nonlocal start
		nonlocal end
		total = start + end # updating the sum
		start, end = end, total # updating start and end
		return total

## Function Counter:

This seems interesting, like a closure that can keep track of number of times the function has been called. So here we need two things i.e a simple function and a count variable. While the inner function is allowed to take function args/kwargs. The tracking part is assigned to the global dictionary which has function name as key,and number of times it being called as it's value. 

Here's the inner function's snippet


	def inner(*args, **kwargs):	
		nonlocal count
		count = count + 1
		print(f'The function {fn.__name__} has been called {count} times.')
		func_count[fn.__name__] = count
		return fn(*args, **kwargs)



## Modified Function Counter :

This is the extension of previous task and goal here is to modify it such that now we can pass in different dictionary variables to update different dictionaries. More like user profiling, and different users passing different input dictionaries. I made on simple change, i.e added user dictionary as one more input and now we have around 3 free variables viz., userdict, function and count(default=0).

    def inner(*args, **kwargs):
            nonlocal count_dict
            nonlocal count
            count = count + 1
            print(f'The function {fn.__name__} has been called {count} times.')
            count_dict[fn.__name__] = count
            return fn(*args)
	    

## Closures Code : 
[https://github.com/ganeshkcs/EPAI/blob/master/S7_CLOSURES/closures.py]


## FUNCTION TEST CASES :

* test_len(): Checks if the Docstring length is valid or not.

* test_func_input(): Checks if the function input is valid or not.

* test_valid_func(): Checks if the function passed is valid or not.

* test_fibo_input_type(): Checks if the input type passed is valid or not.

* test_fibo_input(): Checks if the input passed is valid or not.

* test_valid_function(): Checks if the function passed as input is valid or not. 

* test_func_count(): Checks if the input passed is of valid type or not. 

* test_valid_function_01(): Checks if the function passed as input is valid or not.

* test_func_count_01(): Checks if the input passed is of valid type or not. 

* test_valid_dict_01(): Checks if the user dict passed is valid or invalid.

* test_annotations(): Checks if the functions have annotations or not. 

* test_docstrings(): Checks if the functions have docstring or not. '

* test_invalid_docstrings(): Checks if the docstrings contain any irrelevant symbols. 

## Unit Test Cases : 
[https://github.com/ganeshkcs/EPAI/blob/master/S7_CLOSURES/test_closures.py]

