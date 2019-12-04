import sys
from functools import partial

def allPass(list_of_callbacks, x):
  return [f(x) for f in list_of_callbacks].count(False) == 0

def get_min_max(filename):
  return open(filename, 'r').read().split('-')

def is_six_digit(stringNum):
  return len(stringNum) == 6

def has_two_adjacent_digits(stringNum):
  for i in range(1, len(stringNum)):
    [left, right] = stringNum[i-1:i+1]
    if (left == right):
      return True

  return False

def digits_never_decrease(stringNum):
  biggest = 0
  for i in stringNum:
    if (i < biggest):
      return False
    biggest = i

  return True

def count_matching_combos(predicates, total_count, number):
  if (allPass(predicates, str(number))):
    total_count += 1
  return total_count


def count_of_entries_that_satisfy(predicates, input):
  return reduce(partial(count_matching_combos, predicates), input, 0)

def main(filename):
    """
    Determine how many valid 6 digit combinations exist in range of input

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same
    (like 111123 or 135679).

    Parameters:
    filename (string): name of local

    Returns:
    int: number of combinations from input that satisfied all rules

    """
    min, max = map(int, get_min_max(filename))

    list_of_numbers_in_range = list(range(min, max+1))

    predicates = [is_six_digit, has_two_adjacent_digits, digits_never_decrease]

    print(count_of_entries_that_satisfy(predicates, list_of_numbers_in_range))

if __name__ == '__main__':
    main(sys.argv[1])

## answer is 1154