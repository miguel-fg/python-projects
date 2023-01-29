from math import factorial as f
from decimal import Decimal, getcontext

def get_prec():
    """User enters the length of the series, affecting the precision of the calculation"""

    prec = input("Enter the algorithm precision setting: ")

    if(not prec.isdigit()):
        raise Exception("Precision parameter should be a positive integer")

    dec = input("Up to how many decimal places? ")

    if(not dec.isdigit()):
        raise Exception("Decimal places should be a positive integer")

    getcontext().prec = int(dec) + 1

    return int(prec)

def sum_q(q):
    """A single iteration of the summation part of Chudnovsky's algorithm to calculate PI"""

    num = pow(-1, q) * f(6*q) * (13591409 + 545140134*q)
    exp = 3 / 2 + 3*q
    den = f(3*q) * pow(f(q), 3) * pow(640320, Decimal(exp))

    return Decimal(num)/ Decimal(den)

def main():
    """Main function. Algorithm implementation"""

    print("CHUDNOVSKY ALGORITHM\n")
    print("--------------------")

    pi = 0
    precision = get_prec()

    for i in range(0, precision):
        pi += sum_q(i)

    pi *= 12
    pi = 1/pi

    print(pi)

if __name__ == "__main__":
    main()

