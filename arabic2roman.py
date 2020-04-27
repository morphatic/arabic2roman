from math import floor

"""
  A function that takes a positive integer arabic number and
  converts it into its roman numeral equivalent as a string
"""
def convert(num):
  # create an empty string variable to hold our eventual output
  roman = ''

  ###############
  # Is the number high enough that we need to use M (1000)?
  ###############
  if num >= 1000:
    # get the number of M's we need
    m = floor(num/1000)
    # loop m times and add that number of M's to roman
    for i in range(m):
      roman += 'M'
    # now subtract the part accounted for from our number
    # this ALWAYS gives us a number between 0-999
    num = num - (m * 1000)

  # To prepare for the next step, divide by 100 and discard
  # the decimal part of the number
  if num >= 100:
    # get the number of 100's
    # this will ALWAYS give us a number between 0-9
    c = floor(num / 100)
    # get the remainder when dividing by 5
    remainderWhenDividingBy5 = c % 5
    # check to see if remainder is between 1 and 3
    if remainderWhenDividingBy5 >= 1 and remainderWhenDividingBy5 <= 3:
      # covers cases when number of 100s in 1, 2, 3, 6, 7 8
      # we might have to add a D first if the number is in the 600, 700, or 800 range
      # if we subtract the remainder from c
      # we'll ALWAYS get a multiple of 5
      if (c - remainderWhenDividingBy5) % 10 == 5:
        # we have a number between 600-800, so add a "D" at the beginning
        roman += 'D'
      # loop remainderWhenDividingBy5 times
      for x in range(remainderWhenDividingBy5):
        roman += 'C'
    elif remainderWhenDividingBy5 == 4:
      # covers cases when C is in 400, 900 range
      # sometimes this will be CD and sometimes CM
      # need to determine which one
      if (c + 1) % 10 == 5: # the remainder when dividing (n + 1) by 10
        roman += 'CD' # e.g. remainderWhenDividingBy5 == 4, 14, 24, 34, 44, ...
      else:
        roman += 'CM' # e.g. remainderWhenDividingBy5 == 9, 19, 29, 39, 49, ...
    elif remainderWhenDividingBy5 == 0:
      # covers cases when number is in the 500 range
      # sometimes this will be V and otherwise X
      roman += 'D' # 500
  
    # get rid of all digits over 100, i.e. get this to a number between 0 - 99
    num = num - (c * 100)

  # To prepare for the next step, divide by 10 and discard
  # the decimal part of the number
  if num >= 10:
    # get the number of 10's
    # this will ALWAYS give us a number between 0-9
    x = floor(num / 10)
    # get the remainder when dividing by 5
    remainderWhenDividingBy5 = x % 5
    # check to see if remainder is between 1 and 3
    if remainderWhenDividingBy5 >= 1 and remainderWhenDividingBy5 <= 3:
      # covers cases when number of 10s in 1, 2, 3, 6, 7 8
      # we might have to add a L first if the number is in the 60, 70, or 80 range
      # if we subtract the remainder from x
      # we'll ALWAYS get a multiple of 5
      if (x - remainderWhenDividingBy5) % 10 == 5:
        # we have a number between 60-80, so add a "L" at the beginning
        roman += 'L'
      # loop remainderWhenDividingBy5 times
      for i in range(remainderWhenDividingBy5):
        roman += 'X'
    elif remainderWhenDividingBy5 == 4:
      # covers cases when X is in 40, 90 range
      # sometimes this will be CD and sometimes CM
      # need to determine which one
      if (x + 1) % 10 == 5: # the remainder when dividing (n + 1) by 10
        roman += 'XL' # e.g. remainderWhenDividingBy5 == 4, 14, 24, 34, 44, ...
      else:
        roman += 'XC' # e.g. remainderWhenDividingBy5 == 9, 19, 29, 39, 49, ...
    elif remainderWhenDividingBy5 == 0:
      # covers cases when number is in the 500 range
      # sometimes this will be V and otherwise X
      if x % 10 == 5:
        roman += 'L' # 50
      else:
        roman += 'X'

    # get rid of all digits over 100, i.e. get this to a number between 0 - 99
    num = num - (x * 10)

  ###############
  # Handle the V and I part
  ###############
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

  # return the result
  return roman