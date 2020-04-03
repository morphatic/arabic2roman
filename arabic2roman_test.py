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