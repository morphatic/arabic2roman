# pylint: disable=unused-variable
"""Unit tests for Arabic2Roman."""

from arabic2roman import convert

def describe_an_arabic2roman_program_that():
  """A program to convert Arabic numerals to Roman numerals."""

  def has_a_smoke_test():
    """Make sure our testing infrastructure is working."""
    assert True == True

  def can_convert_1_to_I():
    assert convert(1) == "I"

  def can_convert_2_to_II():
    assert convert(2) == "II"

  def returns_I_II_or_III_if_remainder_of_division_by_5_is_1_to_3():
    """
      Test that our program ends in I, II, or III if the remainder
      when dividing by 5 is 1, 2, or 3, respectively.
    """
    assert convert(1)[-1:] == "I"
    assert convert(2)[-2:] == "II"
    assert convert(3)[-3:] == "III"
    assert convert(6)[-1:] == "I"
    assert convert(7)[-2:] == "II"
    assert convert(8)[-3:] == "III"
    assert convert(11)[-1:] == "I"
    assert convert(12)[-2:] == "II"
    assert convert(13)[-3:] == "III"

  def returns_IV_if_num_mod_5_is_4_and_num_plus_1_not_divisible_by_10():
    assert convert(4)[-2:] == "IV"
    assert convert(9)[-2:] != "IV"
    assert convert(14)[-2:] == "IV"
    assert convert(19)[-2:] != "IV"
    assert convert(124)[-2:] == "IV"
    assert convert(129)[-2:] != "IV"

  def returns_IX_if_num_mod_5_is_4_and_num_plus_1_divisible_by_10():
    assert convert(4)[-2:] != "IX"
    assert convert(9)[-2:] == "IX"
    assert convert(14)[-2:] != "IX"
    assert convert(19)[-2:] == "IX"
    assert convert(124)[-2:] != "IX"
    assert convert(129)[-2:] == "IX"

  def return_V_or_X_if_num_mod_5_is_0():
    assert convert( 5)[-1] == "V"
    assert convert(10)[-1] == "X"
    assert convert(15)[-1] == "V"
    assert convert(20)[-1] == "X"
    assert convert(25)[-1] == "V"
    assert convert(30)[-1] == "X"

  def can_correctly_convert_numbers_1_to_10():
    assert convert(1) == 'I'
    assert convert(2) == 'II'
    assert convert(3) == 'III'
    assert convert(4) == 'IV'
    assert convert(5) == 'V'
    assert convert(6) == 'VI'
    assert convert(7) == 'VII'
    assert convert(8) == 'VIII'
    assert convert(9) == 'IX'
    assert convert(10) == 'X'

  def can_correctly_convert_numbers_11_to_20():
    assert convert(11) == 'XI'
    assert convert(12) == 'XII'
    assert convert(13) == 'XIII'
    assert convert(14) == 'XIV'
    assert convert(15) == 'XV'
    assert convert(16) == 'XVI'
    assert convert(17) == 'XVII'
    assert convert(18) == 'XVIII'
    assert convert(19) == 'XIX'
    assert convert(20) == 'XX'

  def can_correctly_convert_numbers_21_to_30():
    assert convert(21) == 'XXI'
    assert convert(22) == 'XXII'
    assert convert(23) == 'XXIII'
    assert convert(24) == 'XXIV'
    assert convert(25) == 'XXV'
    assert convert(26) == 'XXVI'
    assert convert(27) == 'XXVII'
    assert convert(28) == 'XXVIII'
    assert convert(29) == 'XXIX'
    assert convert(30) == 'XXX'

  def can_correctly_convert_numbers_31_to_40():
    assert convert(31) == 'XXXI'
    assert convert(32) == 'XXXII'
    assert convert(33) == 'XXXIII'
    assert convert(34) == 'XXXIV'
    assert convert(35) == 'XXXV'
    assert convert(36) == 'XXXVI'
    assert convert(37) == 'XXXVII'
    assert convert(38) == 'XXXVIII'
    assert convert(39) == 'XXXIX'
    assert convert(40) == 'XL'

  def can_correctly_convert_all_the_numbers():
    assert convert(50)  == 'L'  
    assert convert(90)  == 'XC'  
    assert convert(100) == 'C'  
    assert convert(110) == 'CX'  
    assert convert(140) == 'CXL'
    assert convert(150) == 'CL'
    assert convert(190) == 'CXC'
    assert convert(400) == 'CD'
    assert convert(500) == 'D'
    assert convert(900) == 'CM'
    assert convert(1000) == 'M'
    assert convert(2949) == 'MMCMXLIX'
    assert convert(4321) == 'MMMMCCCXXI'