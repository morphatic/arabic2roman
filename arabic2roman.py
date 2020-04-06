def convert(num):
  # create an empty string variable to hold our roman numeral output
  roman = ''
  # divide by 5 and check the remainder
  mod5 = num % 5
  # is mod5 between 1 and 3?
  if mod5 >= 1 and mod5 <= 3:
    # check to see if this is a 6, 7, 8 scenario
    if (num - mod5) % 10 != 0:
      # yes, so we need to add a V to our roman numeral
      roman += 'V'
    # yes, so add I to the end of our roman numeral
    for i in range(mod5):
      roman += 'I'
  # else, is mod5 equal to 4
  elif mod5 == 4:
    roman += 'IV' if (num + 1) % 10 != 0 else 'IX'
  # else, is mod5 equal to 0
  elif mod5 == 0:
    roman += 'V' if num % 10 != 0 else 'X'
  # finally return our roman numeral
  return roman