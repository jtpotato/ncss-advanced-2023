SUPER_NUMS = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
SUB_NUMS = ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"]


def gcd(a, b):
    """
    Returns the Greatest Common Divisor between `a` and `b`.
    """
    while b:
        a, b = b, a % b
    return a


def simplify_fraction(numerator, denominator):
    """
    Simplifies a fraction given the numerator and denominator.
    """

    gcd_num = gcd(numerator, denominator)
    numerator = int(numerator / gcd_num)
    denominator = int(denominator / gcd_num)

    return (numerator, denominator)


def make_numeric(input_str):
    return "".join(c for c in input_str if c.isdigit())


class Rational:
    """
    Represents any rational number in fraction form.
    """

    def __init__(self, numerator, denominator=1):
        """
        Initialises a rational number with the given numerator and denominator.
        """
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        """
        Returns True if the two given Rational numbers are equal.
        """
        # simplify both fractions
        simple_self_numerator, simple_self_denominator = simplify_fraction(
            self.numerator, self.denominator
        )
        simple_other_numerator, simple_other_denominator = simplify_fraction(
            other.numerator, other.denominator
        )

        if (
            simple_self_numerator == simple_other_numerator
            and simple_self_denominator == simple_other_denominator
        ):
            return True

        return False

    def __str__(self):
        """
        Returns a string representing this Rational number.
        """

        numerator = self.numerator
        denominator = self.denominator

        # simplify fraction
        numerator, denominator = simplify_fraction(numerator, denominator)

        whole_number = ""
        negative_sign  = ""

        # negative number
        if numerator < 0:
            negative_sign = "-"

        # improper fraction
        if abs(numerator) >= denominator:
            whole_number = str(int(abs(int(numerator) / denominator)))

            numerator = abs(numerator) % denominator

            # simplify fraction
            numerator, denominator = simplify_fraction(numerator, denominator)

        # superscripts and subscripts
        numerator = make_numeric(str(numerator))
        denominator = make_numeric(str(denominator))

        numerator_str = "".join(SUPER_NUMS[int(i)] for i in numerator)
        denominator_str = "".join(SUB_NUMS[int(i)] for i in denominator)

        if numerator == "0":
            if whole_number == "":
                return "0"
            return f"{whole_number}"

        # return string
        return f"{negative_sign}{whole_number}{numerator_str}/{denominator_str}"

    def __add__(self, other):
        """
        Returns the addition (+) of two Rational numbers.
        """
        # equate denominators
        denominator = self.denominator * other.denominator
        self_numerator = self.numerator * other.denominator
        other_numerator = other.numerator * self.denominator

        # add numerators
        numerator = self_numerator + other_numerator

        # simplify fraction
        numerator, denominator = simplify_fraction(numerator, denominator)

        return Rational(numerator, denominator)

    def __mul__(self, other):
        """
        Returns the multiplication (*) of two Rational numbers.
        """
        # multiply numerators
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        # simplify fraction
        numerator, denominator = simplify_fraction(numerator, denominator)

        return Rational(numerator, denominator)

    def __sub__(self, other):
        """
        Returns self minus (-) other of two Rational numbers.
        """
        # equate denominators
        denominator = self.denominator * other.denominator
        self_numerator = self.numerator * other.denominator
        other_numerator = other.numerator * self.denominator

        # subtract numerators
        numerator = self_numerator - other_numerator

        # simplify fraction
        numerator, denominator = simplify_fraction(numerator, denominator)

        return Rational(numerator, denominator)

    def __truediv__(self, other):
        """
        Returns self divided by (/) other.
        """
        # multiply by reciprocal of other
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator

        # simplify fraction
        numerator, denominator = simplify_fraction(numerator, denominator)

        return Rational(numerator, denominator)


def test_rational():
    """
    Put your own tests here.
    This function will never be called during marking.
    """
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2))
    print(Rational(1, 2) + Rational(1, 2))
    print(Rational(1, 2) - Rational(1, 4))
    print(Rational(4, 2) * Rational(1, 2))
    print(Rational(-19, 2))
    print(Rational(-19, -2))
    print(Rational(19, -2))
    print(Rational(0))
    print(Rational(-13,4))


if __name__ == "__main__":
    test_rational()
