"""
Python 101 - CI Academy 2022
Function exercises
"""
import math


# 1. Write a Python function to find the Max of three numbers
#
#    Example: (1, 2, 3) -> 3
from cmath import sqrt


def get_max_of_three(x, y, z):
    """
    Return the Max out of three given numbers
    :param x:
    :param y:
    :param z:
    :return:
    """
    return max([x,y,z])
    # pytest test_exercises.py::test_get_max_of_three


# 2. Write a Python function to sum all the numbers in a list
#
#    Example: [8, 2, 3, 0, 7] -> 20
def get_sum_of_list(num_list):
    """
    Return the sum of all numbers in num_list
    :param num_list: List of numbers
    :return:
    """
    return sum(num_list)
    # pytest test_exercises.py::test_get_sum_of_list


# 3. Write a Python function to multiply all the numbers in a list
#
#    The function should have an argument `absolute`, whose default value is False.
#    If `absolute` is True, the product should be done from the absolute values of given numbers.
#
#    Example:
#    [8, 2, 3, -1, 7], False -> -336
#    [8, 2, 3, 1, 7], True -> 336
def get_prod_of_list(num_list, absolute=False):
    """
    Return the product of all numbers in num_list
    :param num_list: List of numbers
    :param absolute: Use absulute values
    :return:
    """
    product =  1
    if absolute :
        for num in num_list:
            product *= abs(num)
    else:
        for num in num_list:
            product *= num
    return product
    # pytest test_exercises.py::test_get_prod_of_list


# 4. Write a Python program to reverse a string.
#
#    Example: "1234abcd" -> "dcba4321"
def get_reversed_string(string):
    """
    Return given string reversed
    :param string: String to be reversed
    :return:
    """
    return string[::-1]

    # pytest test_exercises.py::test_get_reversed_string


# 5. Write a Python function to calculate the factorial of a number (a non-negative integer).
#    The function accepts the number as an argument.
#
#    Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
def get_factorial(number):
    """
    Return given factorial of given number
    :param string: String to be reversed
    :return:
    :raises NotImplementedError: If number is negative
    """
    factorial = 1
    if number < 0:
        raise NotImplementedError("Negative number!")
    
    if number == 0:
        return factorial

    for n in range(number,1,-1):
        factorial *= n
    
    return factorial
    # pytest test_exercises.py::test_get_factorial


# 6. Write a Python function to check whether a number falls within a given range
#
#    Example: is 5 within 4 and 10? -> True
def check_num_in_range(number, range_min, range_max):
    """
    Check if number falls between a range of two numbers
    :param number:
    :param range_min:
    :param range_max:
    :return:
    """
    
    return True if range_min <= number and range_max >= number else False
    # pytest test_exercises.py::test_check_num_in_range


# 7. Write a Python function that accepts a string and calculate
#    the number of upper case letters and lower case letters.
#
#   Example: "Hello World!" -> (2, 8)
def get_num_cases(string):
    """
    Get number of upper and lower cases in a string
    :param string:
    :return:
    """
    upper = 0
    lower = 0

    for char in string:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1

    return (upper,lower)
    # pytest test_exercises.py::test_get_num_cases


# 8. Write a Python function that takes a list and returns a new
#    list with unique elements of the first list.
#
#    Example: [1,2,3,3,3,3,4,5] -> [1, 2, 3, 4, 5]
def get_unique_item_list(original_list):
    """
    Return given big_list without duplicated elements
    :param original_list:
    :return:
    """
    return list(set(original_list))
    # pytest test_exercises.py::test_get_unique_item_list


# 9. Write a Python function that takes a number as a parameter
#    and check the number is prime or not.
#
#    Note : A prime number (or a prime) is a natural number greater
#    than 1 and that has no positive divisors other than 1 and itself.
#
#    Example:
#       7 -> True
#       8 -> False
def check_prime(number):
    """
    Check if given number is a prime number
    :param number:
    :return:
    """
    if number <= 1:
        return False

    for n in range(2,int(math.ceil(number**0.5))):
        if number%n == 0 and number != n:
            return False

    return True
    # pytest test_exercises.py::test_check_prime


# 10. Return a list of even numbers from all given args (*args)
#
#     Example: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> [2, 4, 6, 8]
def get_even(*args):
    """
    Get list of even numbers from a given list
    :param num_list:
    :return:
    """
    list = []
    for arg in args:
        if arg%2==0:
            list.append(arg)

    return list
    # pytest test_exercises.py::test_get_even


# 11. Write a Python function to check whether a number is perfect or not.
#
#     According to Wikipedia : In number theory, a perfect number is a positive
#     integer that is equal to the sum of its proper positive divisors, that is,
#     the sum of its positive divisors excluding the number itself (also known
#     as its aliquot sum). Equivalently, a perfect number is a number that is
#     half the sum of all of its positive divisors (including itself).
#
#     Example: 6 -> True
#
#     The first perfect number is 6, because 1, 2, and 3 are its proper positive
#     divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the
#     sum of all its positive divisors: (1 + 2 + 3 + 6 ) / 2 = 6. The next perfect
#     number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers
#     496 and 8128.
def check_perfect(number):
    """
    Check if given number is a perfect number
    :param number:
    :return:
    """
    
    divs = [n for n in range(1,number-1) if number%n == 0]

    return True if sum(divs) == number and (sum(divs) + number)/2 == number else False
    # pytest test_exercises.py::test_check_perfect


# 12. Write a Python function that checks whether a passed string is palindrome or not.
#
#     Note: A palindrome is a word, phrase, or sequence that reads
#     the same backward as forward
#     Example:
#     "madam" -> True
#     "nurses run" -> True
#     "False" -> False
def check_palindrome(string):
    """
    Check if a given string is a palindrome
    :param string:
    :return:
    """
    str = [ n for n in string if not n.isspace() ]

    return str == str[::-1]
    # pytest test_exercises.py::test_check_palindrome


# 13. Write a Python function that returns the first n rows of Pascal's triangle.
#
#     Note : Pascal's triangle is an arithmetic and geometric figure first imagined
#     by Blaise Pascal. Each number is the two numbers above it added together.
#
#              | 1 |
#            | 1 | 1 |
#          | 1 | 2 | 1 |
#        | 1 | 3 | 3 | 1 |
#      | 1 | 4 | 6 | 4 | 1 |
#
#     Example:
#     5 -> [[1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
def get_pascal_rows(number):
    """
    Get the first `number` of rows of pascal triangle
    :param number:
    :return:
    """
    list = []  
    for n in range(0, number):
        list2=[]
        for k in range(0, n + 1):
            list2.append(formula(n, k))
        list.append(list2)
    return list

def formula(n,k):
    return int(get_factorial(n)/(get_factorial(n-k)*get_factorial(k)))

    # pytest test_exercises.py::test_get_pascal_rows


# 14. Write a Python function to check whether a string is a pangram or not.
#
#     Note : Pangrams are words or sentences containing
#     every letter of the alphabet at least once.
#
#     Additionally, the function should be able to receive any `keyword=value` pair
#     where the keyword is expected to be a lowercase letter and the value a boolean (True or False).
#
#     If a given letter, e.g. `a`, is set to False the absence of this letter shouldn't matter for
#     the pangram analysis.
#     If a given letter if set to True, the `keyword=value` pair has no effect in the end result.
#
#     Example:  "The quick brown fox jumps over the lazy dog" -> True
def check_pangram(input_str, **kwargs):
    """
    Check if a given string is a pangram
    :param input_str:
    :return:
    """

    list = []
    for key, value in kwargs.items():
        if not value:
            list.append(key)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in input_str.lower() and char not in list:
            return False
  
    return True
    # pytest test_exercises.py::test_check_pangram


# 15. Write a Python program that accepts a hyphen-separated sequence
#     of words as input and prints the words in a hyphen-separated
#     sequence after sorting them alphabetically.
#
#     Example: "green-red-yellow-black-white" -> "black-green-red-white-yellow"
def reorder_hyphen_sequence(string):
    """
    Return a string of words separated by hyphen with the same words reordered
    :param string:
    :return:    
    """
    list = string.split('-')
    list.sort()
    mystr = '-'.join(list)

    return mystr
    # pytest test_exercises.py::test_reorder_hyphen_sequence


# 16. Write a Python function to create and return a list where the
#     values are square of numbers between 1 and 30 (both included)
#
#     Additionally, the function has an `without_ods` argument, whose
#     default value is False. When set to True, all the odd numbers are
#     filtered out of the returned list.
#     Suggestion: Use your knowledge on lambdas
def squared_nums(without_odds=False):
    """
    Return list of squared numbers between 0 and 31
    :param without_odds: If True Odd numbers are not returned
    :return:
    """
    list_nums = [] 
    for i in range(1,31): 
            list_nums.append(i*i) 
    if without_odds:
        return list(filter(lambda x: x%2 == 0, list_nums))

    return list_nums
    # pytest test_exercises.py::test_squared_nums


# 17. Write a chain of function decorators that will add HTML tags
#     (like "<b>Word</b>") into a simple strings (like "Word")
#
#     Decorators to be created:
#       1. bold -> <b>Word</b>
#       2. italic -> <i>Word</i>
#       3. underline -> <u>Word</u>
#
# 17.1. bold -> <b>...</b>
def make_bold(fn):
    """
    Make function returned value bold
    :param fn: Function to be wrapped
    :return:
    """
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


# 17.2. italic -> <i>...</i>
def make_italic(fn):
    """
    Make function returned value italic
    :param fn: Function to be wrapped
    :return:
    """
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped



# 17.3. underline -> <u>...</u>
def make_underline(fn):
    """
    Make function returned value underlined
    :param fn: Function to be wrapped
    :return:
    """
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped


# 17.4. Define a function that will use the decorators created previously
# INSERT YOUR CODE HERE
@make_bold
@make_italic
@make_underline
def word():
    return "Word"


# pytest test_exercises.py::test_decorators
