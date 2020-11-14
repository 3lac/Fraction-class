# Fraction.py  creates a class of fractions that can be used for operations

class Fraction:

    def __init__(self, num, den):
        if (not isinstance(num, int) or not isinstance(den,int)):
            raise Exception("Sorry, only intergers")
        if den == 0:
            raise Exception("Sorry, infinity is not valid")
        self.sign = 1
        if (num < 0 or den < 0):
            self.sign = -1
            if num < 0 and den < 0:
                self.sign = 1
        self.num = abs(num)
        self.den = abs(den)
        self.GCD()
        self.num = self.num * self.sign
        self.old_num = num
        self.old_den = den

    # Str and repr represenations

    def __repr__(self):

        return (f'{self.__class__.__name__}('
                f'{self.old_num!r}, {self.old_den!r})')

    def __str__(self):

        unreduced_frac_str = str(self.old_num) + "/" + str(self.old_den)
        reduced_frac_str = str(self.num) + "/" + str(self.den)
        if self.old_num == self.num:
            return unreduced_frac_str
        else:
            return unreduced_frac_str + " (**" + reduced_frac_str + "**)"

    # Fraction functions to covert to useful forms for operations

    def GCD(self):
        n = self.num
        m = self.den
        if n != 0:
            while m % n != 0:
                m, n = n, m % n
            common = n
            self.num = int(self.num / n)
            self.den = int(self.den / n)

    def common_frac(self, other_frac):
        first_new_num = self.num * other_frac.den
        second_new_num = other_frac.num * self.den
        common_den = self.den * other_frac.den
        return first_new_num, second_new_num, common_den

    # Returns the elements of Fraction class

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    # Operations for Fractions

    def __add__(self,other_frac):
        if isinstance(other_frac, int):
            temp_frac = Fraction(other_frac, 1)
        first_new_num, second_new_num, common_den = self.common_frac(other_frac)
        new_num = first_new_num + second_new_num
        return Fraction(new_num, common_den)

    def __iadd__(self, other):
        if isinstance(other,int):
            other = Fraction(other, 1)
        first_new_num, second_new_num, common_den = self.common_frac(other)
        new_num = first_new_num + second_new_num
        return Fraction(new_num, common_den)

    def __radd__(self, other):
        if isinstance(other, int):
            temp_frac = Fraction(other, 1)
            first_new_num, second_new_num, common_den = self.common_frac(temp_frac)
            return Fraction(first_new_num + second_new_num, common_den)

    def __sub__(self, other_frac):
        first_new_num, second_new_num, common_den = self.common_frac(other_frac)
        new_num = first_new_num - second_new_num
        return Fraction(new_num, common_den)

    def __mul__(self, other_frac):
        new_num = self.num * other_frac.num
        new_den = self.den * other_frac.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_frac):
        new_num = self.num * other_frac.den
        new_den = self.den * other_frac.num
        return Fraction(new_num, new_den)

    # Comparison for Fractions

    def __gt__(self, other_frac):
        first_new_num, second_new_num, common_den = self.common_frac(other_frac)
        if first_new_num > second_new_num:
            return True
        else:
            return False

    def __ge__(self, other_frac):
        first_new_num, second_new_num, common_den = self.common_frac(other_frac)
        if first_new_num >= second_new_num:
            return True
        else:
            return False

    def __lt__(self, other_frac):
        sfirst_new_num, second_new_num, common_den = self.common_frac(other_frac)
        if sfirst_new_num < second_new_num:
            return True
        else:
            return False

    def __le__(self, other_frac):
        first_new_num, second_new_num, common_den = self.common_frac(other_frac)
        if first_new_num <= second_new_num:
            return True
        else:
            return False

    def __ne__(self, other_frac):
        first_new_num, second_new_num, common_den = self.common_frac(other_frac)
        if first_new_num != second_new_num:
            return True
        else:
            return False

    def __eq__(self, other_frac):
        first_new_num, second_new_num, common_den = self.common_frac(other_frac)
        if first_new_num == second_new_num:
            return True
        else:
            return False

def main():
    a = Fraction(1, 232)
    b = Fraction(23, 4)
    c = a + b
    d = Fraction(5, 8)
    e = Fraction(6,10)
    f = d + e
    print(f'{a} + {b}  = {c}')
    print(f'{d} + {e}  = {f}')
    print( a == b)
    a += a
    print(repr(a))
    print(a)

main()