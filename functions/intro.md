# Functions

```
def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
```

```python
def function(arg):
		"""
		A Nice documentation about what the function does

		:param arg: Purpose of this argument
		:return: What is returned by the function
		:raises Error: Use this to identify which exception might be raised
		"""
		# INSERT CODE

		return "VALUE"
```

Typing / Annotations

```python
def function(arg: str) -> list[int]:
		"""
		A Nice documentation about what the function does

		:param arg: Purpose of this argument
		:return: What is returned by the function
		:raises Error: Use this to identify which exception might be raised
		"""
		# INSERT CODE

		return [1, 2, 3]
```

# Global, Local and Nonlocal Variables

1. Local Variable
    
    Local variables can only be used where they are defined:
    
    ```python
    def foo():
        y = "local"
    
    foo()
    print(y)
    ```
    
    - Result
        
        ```python
        NameError: name 'y' is not defined
        ```
        
    - 
        
        ```python
        def foo():
            y = "local"
            print(y)
        
        foo()
        ```
        
        ```python
        local
        ```
        
2. Global Variable
    
    Can be used everywhere:
    
    ```python
    x = "global"
    
    def foo():
        print("x inside:", x)
    
    foo()
    print("x outside:", x)
    ```
    
    - Result
        
        ```python
        x inside: global
        x outside: global
        ```
        
    
    ```python
    x = "global"
    
    def foo():
        x = x * 2
        print(x)
    
    foo()
    ```
    
    - Result
        
        ```python
        UnboundLocalError: local variable 'x' referenced before assignment
        ```
        
    - 
        
        ```python
        x = "global "
        
        def foo():
            y = x * 2
            print(x)
        
        foo()
        ```
        
        ```python
        global global
        ```
        
    
    ```python
    x = 5
    
    def foo():
        x = 10
        print("local x:", x)
    
    foo()
    print("global x:", x)
    ```
    
    - Result
        
        ```python
        local x: 10
        global x: 5
        ```
        
    
    ```python
    x = "global "
    
    def foo():
        global x
        y = "local"
        x = x * 2
        print(x)
        print(y)
    
    foo()
    ```
    
    - Result
        
        ```python
        global global 
        local
        ```
        
3. Nonlocal Variable
    
    Nonlocal is used to work with variables inside nested functions, where the variable should not belong to the inner function.
    
    The variable can be neither in the local nor the global scope.
    
    ```python
    def outer():
        x = "local"
    
        def inner():
            nonlocal x
            x = "nonlocal"
            print("inner:", x)
    
        inner()
        print("outer:", x)
    
    outer()
    ```
    
    - Result
        
        ```python
        inner: nonlocal
        outer: nonlocal
        ```
        
    

# Arguments

1. Default Arguments
    
    ```python
    def power_of(number, power=2):
    	"""
    	Raises number to specific power
    	"""
    	return number ** power
    ```
    
    ```python
    		power_of(2, 2) == power_of(2)
    ```
    
2. Keyword Arguments
    
    ```python
    def greeting_name(greeting, name="World", exclamation=False):
    		print(f"{greeting}, {name}{'!' if exclamation else '.'}")
    ```
    
    ```python
    >> greeting_name("Hello")
    Hello, World.
    >> greeting_name("Hello", exclamation=True)
    Hello, World!
    >> greeting_name("Bye", name="Tom", exclamation=False)
    Bye, Tom.
    >> greeting_name("Bye", "Zach", True)
    Bye, Zach!
    ```
    
3. Additional Arguments
    
    ```python
    def greet(*names):
        for name in names:
            print("Hello", name)
    ```
    
    ```python
    >> greet("Zach", "Peter", "Marie")
    Hello Zach
    Hello Peter
    Hello Marie
    ```
    
4. Keyword additional Arguments
    
    ```python
    def intro(**data):
        for key, value in data.items():
            print("{} is {}".format(key,value))
    ```
    
    ```python
    >> intro(Firstname="Max", Lastname="Thunder", Age=22, Phone=1234567890)
    Firstname is Max
    Lastname is Thunder
    Age is 22
    Phone is 1234567890 
    ```
    
5. Deeper:
    
    ```python
    a = [*"CI Academy"]
    print(a)
    ```
    
    - What is Printed?
        
        ```python
        ['C', 'I', ' ', 'A', 'c', 'a', 'd', 'e', 'm', 'y']
        ```
        
    
    ```python
    my_first_dict = {"A": 1, "B": 2}
    my_second_dict = {"C": 3, "D": 4}
    print({**my_first_dict, **my_second_dict})
    ```
    
    - What is Printed?
        
        ```python
        {"A": 1, "B": 2, "C": 3, "D": 4}
        ```
        

# Lambda Expressions

A lambda function is a small anonymous function.

I see them as either one-liner function or a function generator.

IIFE - immediately invoked function execution, not actually used in practise…

```python
print((lambda x: x + 1)(2))
```

- Result
    
    ```python
    (lambda x: x + 1)(2) = lambda 2: 2 + 1
                         = 2 + 1
                         = 3
    ```
    
    ```python
    3
    ```
    

```python
add_ten = lambda a : a + 10
print(add_ten(5))
```

- Result
    
    ```python
    15
    ```
    

```python
multiply = lambda a, b : a * b
print(multiply(5, 6))
```

- Result
    
    ```python
    30
    ```
    

Are they useful for what?

Be aware of which variables are lambda bound variables!

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
```

- Result
    
    ```python
    22
    33
    ```
    

Functions within Functions!

```python
high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))
print(high_ord_func(2, lambda x: x + 3))
```

- Result
    
    ```python
    6
    7
    ```
    

All types of arguments

```python
>>> (lambda x, y, z: x + y + z)(1, 2, 3)
6
>>> (lambda x, y, z=3: x + y + z)(1, 2)
6
>>> (lambda x, y, z=3: x + y + z)(1, y=2)
6
>>> (lambda *args: sum(args))(1,2,3)
6
>>> (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
6
>>> (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
6
```

Don’t over do it!

- It might not be “Pythonic”
- It’s cumbersome and difficult to read.
- It’s unnecessarily clever at the cost of difficult readability.

Use it for simple operations!

```python
>>> list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
```

Note: The built-in function `map()` takes a function as a first argument and applies it to each of the elements of its second argument, an iterable. Examples of iterables are strings, lists, and tuples.

- Result
    
    ```python
    ['CAT', 'DOG', 'COW']
    ```
    

```python
>>> list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))
```

Note: The built-in function `filter()`, another classic functional construct, can be converted into a list comprehension.. It builds an iterator containing all the elements of the initial collection that satisfies the predicate function.

- Result
    
    ```python
    ['dog', 'cow']
    ```
    

# Decorators

Functions can be passed on to be used later.

```python
def power_of_2(number):
    return number ** 2

def double(number):
    return number * 2

def exec_in_10(func):
    return func(10)

print(exec_in_10(power_of_2))
print(exec_in_10(double))
```

- Result
    
    ```python
    100
    20
    ```
    

Inner Functions

```python
def parent_func():
		
		def child_func():
				return "Child return!"
		
		print(child_func)
		print(child_func())

parent_func()
```

- Result
    
    ```python
    <function parent_func.<locals>.child_func at 0x000001F8FD007560>
    Child return!
    ```
    

They are locally scoped to `parent()`: they only exist inside the `parent()` function as local variables.

Decorators

```python
def my_decorator(func):
    def wrapper():
        print("Decorator: Something is about to Happen!")
        func()
        print("Decorator: God Dammit, He said it!")
    return wrapper

def say_whee():
    print("Wrapped Func: Whee!")

say_whee = my_decorator(say_whee)
say_whee()
```

- Result
    
    ```python
    Decorator: Something is about to Happen!
    Wrapped Func: Whee!
    Decorator: God Dammit, He said it!
    ```
    

Improved Syntax

```python
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

@not_during_the_night
def say_whee():
    print("Whee!")
```

Passing arguments

```python
global_num = 0

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def add_to_global(number):
    global global_num
		global_num += number

add_to_global(2)
```

- Result
    
    ```python
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: do_twice.<locals>.wrapper_do_twice() takes 0 positional arguments but 1 was given
    ```
    

```python
GLOBAL_VALUE = 0

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def add_to_global(number):
    global GLOBAL_VALUE 
		GLOBAL_VALUE += number

add_to_global(2)
print(GLOBAL_VALUE)
```

- Result
    
    ```python
    4
    ```
    

Return values through decorator

```python
GLOBAL_VALUE = 0

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def add_to_global(number):
    global GLOBAL_VALUE 
		GLOBAL_VALUE += number
		return GLOBAL_VALUE 

print(add_to_global(2))
```