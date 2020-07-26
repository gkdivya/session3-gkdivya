# Numeric Types

int, float, complex
There are three distinct numeric types: integers, floating point numbers, and complex numbers. In addition, Booleans are a subtype of integers. Integers have unlimited precision. Floating point numbers are usually implemented using double in C; information about the precision and internal representation of floating point numbers for the machine on which your program is running is available in sys.float_info. Complex numbers have a real and imaginary part, which are each a floating point number. To extract these parts from a complex number z, use z.real and z.imag. (The standard library includes the additional numeric types fractions.Fraction, for rationals, and decimal.Decimal, for floating-point numbers with user-definable precision.)

      The byte order used to represent the integer.  If byteorder is # big
      the most significant byte is at the beginning of the byte array.  If
      byteorder is # little the most significant byte is at the end of the
      byte array.  To request the native byte order of the host system, use
      `sys.byteorder#  as the byte order value.
    signed
      Indicates whether two# s complement is used to represent the integer.

----------------------------------------------------------------------
Static methods defined here:

__new__(*args, **kwargs) from builtins.type
    Create and return a new object.  See help(type) for accurate signature.

----------------------------------------------------------------------
Data descriptors defined here:

denominator
    the denominator of a rational number in lowest terms

imag
    the imaginary part of a complex number

numerator
    the numerator of a rational number in lowest terms

real
    the real part of a complex number

 # math
 This module provides access to the mathematical functions defined by the C standard.

These functions cannot be used with complex numbers; use the functions of the same name from the cmath module if you require support for complex numbers. The distinction between functions which support complex numbers and those which don’t is made since most users do not want to learn quite as much mathematics as required to understand complex numbers. Receiving an exception instead of a complex result allows earlier detection of the unexpected complex number used as a parameter, so that the programmer can determine how and why it was generated in the first place.

Mainly in this assignment, we have tried to create alternative functions instead of using math module built in functions to understand what happens in details 

 # encoded_from_base10(number, base, digit_map):
This function simulates int(x, base=10) method constructor. It returns encoded value as a string based on the base input. This function will throw ValueError with appropriate error message for the end user. digit_map is the used to encode the digit to the base value.

a binary number is a number expressed in the base-2 numeral system or binary numeral system, which uses only two symbols: typically "0" (zero) and "1" (one). The base-2 numeral system is a positional notation with a radix of 2. Each digit is referred to as a bit.

>>> bin(10)
'0b1010'

The octal numeral system, or oct for short, is the base-8 number system, and uses the digits 0 to 7. Octal numerals can be made from binary numerals by grouping consecutive binary digits into groups of three (starting from the right). For example, the binary representation for decimal 74 is 1001010.

>>> oct(8)
'0o10'

hexadecimal (also base 16, or hex) is a positional system that represents numbers using a base of 16. ... Hexadecimal is used in the transfer encoding Base16, in which each byte of the plaintext is broken into two 4-bit values and represented by two hexadecimal digits.

>>> hex(10)
'0xa'

 # float_equality_testing(a, b):
This function emulates the ISCLOSE method from the MATH module

isclose(a, b, rel_tol=1e-9, abs_tol=0.0)
a and b: are the two values to be tested to relative closeness

rel_tol: is the relative tolerance -- it is the amount of error allowed, relative to the larger absolute value of a or b. For example, to set a tolerance of 5%, pass tol=0.05. The default tolerance is 1e-9, which assures that the two values are the same within about 9 decimal digits. rel_tol must be greater than 0.0

abs_tol: is a minimum absolute tolerance level -- useful for comparisons near zero.

Modulo error checking, etc, the function will return the result of:

abs(a-b) <= max( rel_tol * max(abs(a), abs(b)), abs_tol )
The name, isclose, is selected for consistency with the existing isnan and isinf.


 # manual_truncation_function(f_num):
This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
It must check whether f_num is of correct type before proceed. 

 # manual_rounding_function(f_num):
This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
expected to write your one manually.

# rounding_away_from_zero(f_num):
This function implements rounding away from zero using FRACTIONS and extract numerator. 
