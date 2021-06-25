import inspect

#-------------VALIDATION FUNCTIONS-------------#

# COMMON ONE
def validate_func(func):
	if not inspect.isfunction(func):
		raise ValueError


def validate_len(length: int):
	if length != 50:
		raise ValueError



# FIBONACCI SERIES
def validate_start_end(start, end):
	if not isinstance(start, int) or not isinstance(end, int):
		raise ValueError

def validate_start_end_value(start, end):
	if start < 0 or end < 0:
		raise ValueError


# FUNCTION COUNTER


def validate_count(count):
	if not isinstance(count, int):
		raise ValueError

def validate_dictionary(dictionary):
	if not isinstance(dictionary, dict):
		raise ValueError



## 1
#-------------DOCSTRING LEN CHECKER-------------#

def check_docstring(length = 50): # outer function
	'''
	Closure which checks if a function has sufficient num of docstring characters(50).
	'''
	validate_len(length)

	def check_len(func_pointer: object): # inner function

		validate_func(func_pointer)
		
		if func_pointer.__doc__ is None:
			return 'Function has got no Docstring!'
		elif len(func_pointer.__doc__) >= length:
			return f'Function has got {len(func_pointer.__doc__)} Characters in Docstring.'
		else:
			return f'Insufficient number of Characters in Docstring({len(func_pointer.__doc__)}).'
	return check_len


print('Check Docstring Start')
funcDoc = check_docstring()
funDocLen = funcDoc(check_docstring)
print(funDocLen)
print('Check Docstring End')


## 2
#-------------FIBONACCI SERIES GENERATOR-------------#

def fibo(start=0, end=1):
	'''
	?? Generates a Fibonacci Series using Closure
	
	>> Args:
		Start: Initial Value, by default 0
		End: Second Value, by default 1

	<> Returns a Callable which returns the next fibonacci number based on the end variable.
	'''

	validate_start_end(start, end)
	validate_start_end_value(start, end)

	def series():
		nonlocal start
		nonlocal end
		total = start + end # updating the sum
		start, end = end, total # updating start and end
		return total
	return series

print('Fibo start')
fibSeries = fibo(0,1)
print(fibSeries())
print('Fibo End')


## 3
# ---------------FUNCTION COUNTER------------#


# sample functions
def add(a:int,b:int):
	return a+b

def mul(a:int,b:int):
	return a*b

def sub(a:int,b:int):
	return a-b

def div(a:int,b:int):
	try:
		return a/b
	except:
		return 'ZeroByDivisionError: Got b as 0.'
		


# func count dict
func_count = dict()


# function counter
def func_counter(fn, count = 0):
	'''
	?? Keeps a count of different function used by the user in a global dictionary

	>> Args:
		fn: A User-Defined Function
		count: 0, initial value which later gets updated as a particular function gets called.

	<> Returns Callable which takes in args/kwargs and returns result as per input func
	'''
	validate_func(fn)
	validate_count(count)

	def inner(*args, **kwargs):	
		nonlocal count
		count = count + 1
		# print(f'The function {fn.__name__} has been called {count} times.')
		func_count[fn.__name__] = count
		return fn(*args, **kwargs)

	return inner

print('Func Counter Start')
add_counter = func_counter(add)
div_counter = func_counter(div)
add_counter(1,2)
add_counter(3,4)
div_counter(12,4)
print('Func Counter (End)', func_count)



## 4
# ---------------PROFILE FUNC COUNTER -------------#

def profile_func_counter(username: dict, fn, count = 0):
	'''

	>> Args:
		username: A Dictionary which acts as Function Counter.
		fn: A User-Defined Function
		count: 0, initial value which later gets updated as a particular function gets called.

	<> Returns Callable which takes in args/kwargs and returns result as per input func
	'''

	validate_dictionary(username)
	validate_count(count)
	validate_func(fn)

	count_dict = username

	def inner(*args, **kwargs):
		nonlocal count_dict
		nonlocal count
		count = count + 1
		# print(f'The function {fn.__name__} has been called {count} times.')
		count_dict[fn.__name__] = count
		return fn(*args)
	return inner


profile1 = dict()
add_profile1 = profile_func_counter(profile1, add)
add_profile1(1,2)

profile2 = dict()
add_profile2 = profile_func_counter(profile2, add)
add_profile2(5,2)
add_profile2(8,2)

print('Profile count start')
print('Count of profile1', profile1)
print('Count of profile2', profile2)
print('Profile count End')





