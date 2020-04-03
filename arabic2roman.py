def convert(num):
  # create an empty string variable to hold our roman numeral output
  roman = ''
  # divide by 5 and check the remainder
  mod5 = num % 5
  # is mod5 between 1 and 3?
  if mod5 >= 1 and mod5 <= 3:
    # yes, so add I to the end of our roman numeral
    for i in range(mod5):
      roman += 'I'
  elif mod5 == 4 and (num + 1) % 10 != 0:
    roman += 'IV'
  elif mod5 == 4 and (num + 1) % 10 == 0:
    roman += 'IX'
  # finally return our roman numeral
  return roman