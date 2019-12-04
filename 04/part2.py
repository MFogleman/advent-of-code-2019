import sys
from functools import partial
from part1 import count_of_entries_that_satisfy, get_min_max, digits_never_decrease, is_six_digit

def has_pair_of_adjacent_digits(stringNum):
  streak = []
  for x in stringNum:
    # starting a new streak, or continuing
    if len(streak) == 0 or streak[-1] == x:
      streak.append(x)
    else: # we have a streak, but this is a new value
      if len(streak) == 2:
        return True
      else:
        streak = [x]

  return len(streak) == 2

predicates = [is_six_digit, has_pair_of_adjacent_digits, digits_never_decrease]

def main(filename):

  min, max = map(int, get_min_max(filename))

  list_of_numbers_in_range = list(range(min, max+1))

  print(count_of_entries_that_satisfy(predicates, list_of_numbers_in_range))

if __name__ == '__main__':
    main(sys.argv[1])

## 750