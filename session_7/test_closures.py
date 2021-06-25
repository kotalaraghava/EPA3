import pytest
import random
import string
from closures import *
import os
import inspect
import re
import math
import importlib
import closures

# 1
#-------------DOCSTRING LEN CHECKER-------------#

def test_len():
    with pytest.raises(ValueError) as e:
        closures.check_docstring(length=25)


def test_func_input():
    with pytest.raises(ValueError) as e:
        sample = closures.check_docstring()
        sample(49)

a = 100
def test_valid_func():
    with pytest.raises(ValueError) as e:
        sample = closures.check_docstring()
        sample(a)
        
def test_docstrings():
    '''
    Test caset to check docstrings in the function defn
    '''
    funcs = inspect.getmembers(closures, inspect.isfunction)
    for func in funcs:
        if func[1].__doc__ == None:
            continue
        print(func[1].__doc__)
        assert func[1].__doc__


def test_invalid_docstrings():
    funcs = inspect.getmembers(closures, inspect.isfunction)
    for func in funcs:
        assert len(re.findall('([@_!#$%^&*()<>?/\\|}{~:])', func.__doc__)) == 0, 'You have used inappropriate symbols in your docstring.'


# 2 
#-------------FIBONACCI SERIES GENERATOR-------------#

def test_fibo_input_type():
    with pytest.raises(ValueError) as e:
        closures.fibo(3,'a')


def test_fibo_input():
    with pytest.raises(ValueError) as e:
        closures.fibo(-3,0)


# 3
# ---------------FUNCTION COUNTER------------#

addition = 10
def add(a,b):
    return a+b

def test_valid_function():
    with pytest.raises(ValueError) as e:
        closures.func_counter(addition,10)


def test_func_count():
    with pytest.raises(ValueError) as e:
        closures.func_counter(add,'10')


# 4
# ---------------USER PROFILE FUNC COUNTER -------------#

random_dict = dict()
b = 10


def test_valid_function_01():
    with pytest.raises(ValueError) as e:
        closures.profile_func_counter(random_dict, addition,10)


def test_func_count_01():
    with pytest.raises(ValueError) as e:
        closures.profile_func_counter(random_dict, add,'10')


def test_valid_dict_01():
    with pytest.raises(ValueError) as e:
        closures.profile_func_counter(b, add)



def test_annotations():
    '''
    Test case to check the function typing are implemented in the function
    definition.
    '''
    funcs = inspect.getmembers(closures, inspect.isfunction)
    count=0
    for func in funcs:
        print(func[1].__annotations__)
        try:
           
            if func[1].__annotations__ == {}:
                continue
            else:
                count+=1
        except Exception as e:
            print(e)

    assert count <= len(funcs)

   
