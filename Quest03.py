# Exercise 0
import sys
# i = sys.argv[1:]
for i in sys.argv[1:]:
    print(i)

# ==========================================================
# Exercise 1
import sys
def my_is_negative(nbr):
  if nbr < 0:
    return 0
  else:
    return 1

sys.argv[-1]
sys.argv[1]
sys.argv[0]

# ==========================================================
# Exercise 2
import sys
def my_abs(param_1):
    return abs(param_1)
sys.argv[1]

# ==========================================================
# Exercise 3
import sys
def my_add(nbr1, nbr2):
    return nbr1+nbr2
sys.argv[1:]

# ==========================================================
# Exercise 4
import sys
def my_sub(param_1, param_2):
    return param_1 - param_2
sys.argv[1:]
# ==========================================================
# Exercise 5
import sys
def my_mult(nbr1, nbr2):
    return nbr1 * nbr2
sys.argv[1:]


# ==========================================================
# Exercise 6
# Hello, my name is john doe, I'm 37.
# "Hello, my name is FIRSTNAME LASTNAME, I'm AGE."
import sys
def my_string_formatting(param_1, param_2, param_3):
    print("Hello, my name is "+ param_1 + ' ' + param_2 + ', ' + "I'm " + str(param_3) +'.')
sys.argv[1:]

