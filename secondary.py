# -------------------- Section 2 -------------------- #

# ---------- Part 1 | Patterns ---------- #
print(
 #   '>> Section 2\n'
  #  '>> Part 1\n'
)

# 1 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   b. Prompt input from the user in the form of an integer. Save to a variable named size.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#   >> size... 4
#
#   $$$$
#    $$$
#     $$
#      $
#
# Write Code Below #
print('SECTION 2, PART 1')
s = input('enter a symbol: ')
size = input('enter a size: ')
for i in range(5, 0, -1):
    print(' ' * (5 - i) + '$' * i)
# 2 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#
#
# Write Code Below #
s2 = input('your symbol: ')
for i in range(6, 0, -1):
    print(' ' * (6 - i) + '%' * i)
for i in range(2, 7, 1):
    print(' ' * (7 - i - 1) + '%' * i)
# 3 - for Loop | Patterns
#   a. Prompt input from the user in the form of a symbol. Save to a variable named s.
#   a. Create the following pattern using a for loop, and the symbol and size provided by the user.
#
# Example Output
#
#   >> symbol... $
#
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#   $$$$
#   $$$
#   $$
#   $
#
#
# Write Code Below #
s3 = input('your symbol: ')
for i in range(1, 6, 1):
    print(' ' * (6 - i - 1) + '*' * i)
for i in range(4, 0, -1):
    print(' ' * (4 - i) + '*' * i)

# ---------- Part 2 | Mathematical Patterns ---------- #
print(
 #   '>> Section 2\n'
 #   '>> Part 2\n'
)

# 1 - for Loop | Sum n
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate the sum of all numbers between 0 and n, and print the value.
#
#   sum = n + n - 1 + n - 2 + n - 3
#
#   EXAMPLE: 5 --> 5 + 4 + 3 + 2 + 1
#
# Example Output
#
#   >> n = 10
#   >> 55
#
# Write Code Below #
n = input('enter your number: ')


# 1 - for Loop | n!
#   a. Prompt input from the user in the form of an integer. Save to a variable named n.
#   b. Calculate n! using loops.
#
#   n! or n factorial is equal to n * (n - 1) * (n - 2) * ... * 1
#
#   EXAMPLE: 5 --> 5 * 4 * 3 * 2 * 1
#
#
# Example Output
#
#   >> n = 10
#   >> 55
#
# Write Code Below #