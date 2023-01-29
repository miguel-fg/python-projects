from math import factorial as f
from decimal import Decimal, getcontext

def set_dec():
    """Sets the decimal places of the output"""

    dec = input("Up to how many decimal places? ")

    if(not dec.isdigit()):
        raise Exception("decimal places must be a positive integer")

    getcontext().prec = int(dec) + 1


def sum_q(q):
    """A single iteration of the sumation part of Chudnovsky's algorithm to calculate PI"""

    num = pow(-1, q) * f(6*q) * (13591409 + 545140134*q)
    exp = 3 / 2 + 3*q
    den = f(3*q) * pow(f(q), 3) * pow(640320, Decimal(exp))

    return Decimal(num)/ Decimal(den)

def main():
    """Prints PI value to console.
       Increase reps variable to modify the precision of the calculation, at cost of computing power.
    """
    set_dec()

    pi = 0
    reps = 100

    for i in range(0, reps):
        pi += sum_q(i)

    pi *= 12
    pi = 1/pi

    print(pi)

if __name__ == "__main__":
    main()

