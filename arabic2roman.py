# import floor() to discard remainders when doing division
from math import floor

"""
  Map significant digits to roman numeral letters
"""
numMap = {
  1000: 'M',
  500: 'D',
  100: 'C',
  50: 'L',
  10: 'X',
  5: 'V',
  1: 'I'
}

"""
  Process the 1000's, 100's, 10's, or 1's place of an
  arabic numeral and return the corresponding roman numerals
"""
def processPlace(num, place): # num == 1, place === 1000
  # declare an empty string to hold our output
  output = ''

  if num >= place:
    # get the number of [place]'s
    # this will ALWAYS give us a number between 0-9
    digit = floor(num / place)

    # check to see if place < 1000
    if place < 1000:
      # get the remainder when dividing by 5
      remainderWhenDividingBy5 = digit % 5
      # check to see if remainder is between 1 and 3
      if remainderWhenDividingBy5 >= 1 and remainderWhenDividingBy5 <= 3:
        # covers cases when the digit is in 1, 2, 3, 6, 7 8
        # we might have to add a D, L, or V first if the digit is 6, 7, or 8
        # if we subtract the remainder from digit
        # we'll ALWAYS get a multiple of 5
        if (digit - remainderWhenDividingBy5) % 10 == 5:
          # we have a digit between 6-8, so add a D, L, or V at the beginning
          output += numMap[5 * place]
        # loop remainderWhenDividingBy5 times
        for i in range(remainderWhenDividingBy5):
          output += numMap[place] # add the needed number of C's, X's, or I's
      elif remainderWhenDividingBy5 == 4:
        # covers cases when digit is in 4 or 9
        if (digit + 1) % 10 == 5: # the remainder when dividing (n + 1) by 10
          output += numMap[place] + numMap[5 * place] # e.g. remainderWhenDividingBy5 == 4, 14, 24, 34, 44, ...
        else:
          output += numMap[place] + numMap[10 * place] # e.g. remainderWhenDividingBy5 == 9, 19, 29, 39, 49, ...
      elif remainderWhenDividingBy5 == 0:
        # covers cases when digit is 5, requiring D, L, or V
        output += numMap[5 * place] # 500
    else:
      for i in range(digit):
        output += numMap[place]

    # get rid of the most significant digit
    num = num - (digit * place)

  # return the output
  return {
    "roman": output,
    "number": num
  }

"""
  A function that takes a positive integer arabic number and
  converts it into its roman numeral equivalent as a string
"""
def convert(num): # num == 1
  # create an empty string variable to hold our eventual output
  roman = ''
  result = processPlace(num, 1000) # process the 1000's place ==> { roman: 'MMMM', number: 321 }
  roman += result['roman']
  result = processPlace(result['number'], 100) # process the 100's place ==> { roman: 'CCC', number: 21 }
  roman += result['roman']
  result = processPlace(result['number'], 10) # process the 10's place ==> { roman: 'XX', number: 1 }
  roman += result['roman']
  result = processPlace(result['number'], 1) # process the 1's place ==> { roman: 'I', number: 0 }
  roman += result['roman']

  return roman
