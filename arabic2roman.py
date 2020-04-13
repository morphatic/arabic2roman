"""
  A function that takes a positive integer arabic number and
  converts it into its roman numeral equivalent as a string
"""
def convert(num): # num == 1
  # create an empty string variable to hold our eventual output
  roman = ''

  # we need to be able to add X to the beginning of numbers > 10
  if num > 10:
    # add an X onto the beginning
    roman += 'X'
  if num > 20:
    roman += 'X'
  if num > 30:
    roman += 'X'  

  # we know that there are patterns that repeat every 5 numbers
  # so, let's figure out where we are in that cycle
  remainderWhenDividingBy5 = num % 5 # modulus operator (%) give us the remainder
  if remainderWhenDividingBy5 >= 1 and remainderWhenDividingBy5 <= 3:
    # covers cases when number ends in 1, 2, 3, 6, 7 8
    # we might have to add a V first if the number ends in 6, 7, or 8
    # if we subtract the remainder from the original number
    # we'll ALWAYS get a multiple of 5
    if (num - remainderWhenDividingBy5) % 10 == 5:
      roman += 'V'
    # loop remainderWhenDividingBy5 times
    for x in range(remainderWhenDividingBy5):
      roman += 'I'
  elif remainderWhenDividingBy5 == 4:
    # covers cases when number ends in 4, 9
    # sometimes this will be IV and sometimes IX
    # need to determine which one
    if (num + 1) % 10 == 5: # the remainder when dividing (n + 1) by 10
      roman += 'IV' # e.g. remainderWhenDividingBy5 == 4, 14, 24, 34, 44, ...
    else:
      roman += 'IX' # e.g. remainderWhenDividingBy5 == 9, 19, 29, 39, 49, ...
  elif remainderWhenDividingBy5 == 0:
    # covers cases when number ends in 5, 0
    # sometimes this will be V and otherwise X
    # determine which one
    if num % 10 == 5:
      roman += 'V' # 5, 15, 25, 35, ...
    else:
      roman += 'X' # 10, 20, 30, 40, ...

  # return the result
  return roman