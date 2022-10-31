"""
Python 101 - CI Academy 2022

Test Function exercises
"""
import pytest

import exercises


@pytest.mark.parametrize("numbers,result", [([1, 2, 3], 3), ([5, 2, 3], 5)])
def test_get_max_of_three(numbers, result):
    assert exercises.get_max_of_three(numbers[0], numbers[1], numbers[2]) == result


@pytest.mark.parametrize(
    "numbers,result", [([1, 2, 3], 6), ([5, 2, 3], 10), ([8, 2, 3, 0, 7], 20)]
)
def test_get_sum_of_list(numbers, result):
    assert exercises.get_sum_of_list(numbers) == result


@pytest.mark.parametrize(
    "numbers,result",
    [([1, 2, 3], 6), ([5, 2, 3], 30), ([8, 2, 3, 0, 7], 0), ([8, 2, 3, -1, 7], -336)],
)
def test_get_prod_of_list(numbers, result):
    assert exercises.get_prod_of_list(numbers) == result
    assert exercises.get_prod_of_list(numbers, True) == abs(result)


@pytest.mark.parametrize(
    "string,result",
    [("ABBA", "ABBA"), ("1234abcd", "dcba4321"), ("Hello World!", "!dlroW olleH")],
)
def test_get_reversed_string(string, result):
    assert exercises.get_reversed_string(string) == result


@pytest.mark.parametrize("numbers,result", [(5, 120), (10, 3628800), (-3, None)])
def test_get_factorial(numbers, result):
    if result:
        assert exercises.get_factorial(numbers) == result
    else:
        with pytest.raises(NotImplementedError):
            exercises.get_factorial(numbers)


@pytest.mark.parametrize("numbers,result", [([5, 4, 10], True), ([-10, -3, 10], False)])
def test_check_num_in_range(numbers, result):
    assert exercises.check_num_in_range(numbers[0], numbers[1], numbers[2]) == result


@pytest.mark.parametrize(
    "string,result",
    [("ABBA", (4, 0)), ("The quick Brow Fox", (3, 12)), ("Hello World!", (2, 8))],
)
def test_get_num_cases(string, result):
    assert exercises.get_num_cases(string) == result


@pytest.mark.parametrize(
    "original_list,result",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8]),
        (["Hi", "Hi, Bye", "Bye"], ["Hi", "Bye"]),
    ],
)
def test_get_unique_item_list(original_list, result):
    assert exercises.get_unique_item_list(original_list).sort() == result.sort()


@pytest.mark.parametrize(
    "number,result", [(7, True), (36, False), (11, True), (8, False)]
)
def test_check_prime(number, result):
    assert exercises.check_prime(number) == result


@pytest.mark.parametrize(
    "numbers,result", [([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8])]
)
def test_get_even(numbers, result):
    assert exercises.get_even(*numbers) == result


@pytest.mark.parametrize(
    "number,result", [(6, True), (7, False), (496, True), (8, False)]
)
def test_check_prime(number, result):
    assert exercises.check_perfect(number) == result


@pytest.mark.parametrize(
    "string,result", [("madam", True), ("nurses run", True), ("False", False)]
)
def test_check_palindrome(string, result):
    assert exercises.check_palindrome(string) == result


def test_get_pascal_rows():
    assert exercises.get_pascal_rows(10) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
    ]


@pytest.mark.parametrize(
    "sentence,result",
    [("The quick brown fox jumps over the lazy dog", True), ("not all", False)],
)
def test_check_palindrome(sentence, result):
    assert exercises.check_pangram(sentence) == result
    assert (
        exercises.check_pangram(
            sentence.replace("a", "").replace("z", ""), a=False, z=False
        )
        == result
    )


@pytest.mark.parametrize(
    "sentence,result",
    [
        ("green-red-yellow-black-white", "black-green-red-white-yellow"),
        ("zebra-monkey-buffalo-horse", "buffalo-horse-monkey-zebra"),
    ],
)
def test_reorder_hyphen_sequence(sentence, result):
    assert exercises.reorder_hyphen_sequence(sentence) == result


def test_squared_nums():
    assert exercises.squared_nums() == [
        1,
        4,
        9,
        16,
        25,
        36,
        49,
        64,
        81,
        100,
        121,
        144,
        169,
        196,
        225,
        256,
        289,
        324,
        361,
        400,
        441,
        484,
        529,
        576,
        625,
        676,
        729,
        784,
        841,
        900,
    ]

    assert exercises.squared_nums(without_odds=True) == [
        4,
        16,
        36,
        64,
        100,
        144,
        196,
        256,
        324,
        400,
        484,
        576,
        676,
        784,
        900,
    ]


def test_decorators():
    @exercises.make_bold
    @exercises.make_italic
    @exercises.make_underline
    def get_hello_world():
        """
        Get "Hello World!" string

        :return:
        """
        return "Hello World!"

    assert get_hello_world() == "<b><i><u>Hello World!</u></i></b>"
