import fractions


def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    digits = []
    num = number

    if base not in range(2, 36):
        raise ValueError(f'Value of base :{base},  should be in the range of (2, 36)')
    if len(digit_map) < base:
        raise ValueError(f'Digit map {digit_map} cannot be encoded with the provided base')
    if not (len("".join(set(digit_map))) is len(digit_map)):
        raise ValueError(f"digit_map have repeating character")
    if not (len(set(digit_map)) is base):
        raise ValueError(f"digit_map must have sufficient length to represent the base {base}")

    if number == 0:
        digits = [0]

    while abs(num) > 0:
        remainder = abs(num) % base
        num = abs(num) // base
        digits.insert(0, remainder)

    encoding = ''.join([digit_map[digit] for digit in digits])
    encoding = '-'+encoding if number < 0 else encoding
    return encoding


def float_equality_testing(a, b):
    '''
    This function emulates the ISCLOSE method from the MATH module, but you can't use this function
    We are going to assume:
    - rel_tol = 1e-12
    - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    if(a == b):
        return 1
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point.
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    if not isinstance(f_num, (int, float)):
        raise ValueError(f'Input is not a valid number')
    integer_part = fractions.Fraction(f_num // 1).numerator
    return integer_part if integer_part >= 0 else integer_part + 1


def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    if not isinstance(f_num, (int, float)):
        raise ValueError(f'Input is not a valid number')
    integer_part = fractions.Fraction(f_num // 1).numerator
    fractional_part = f_num - integer_part
    return integer_part if fractional_part < 0.5 else integer_part + 1


def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't.
    Hint: use FRACTIONS and extract numerator.
    '''
    return fractions.Fraction(f_num).numerator
