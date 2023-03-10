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

def sum_k(k):
    """Single iteration of the summation part of the algorithm"""
    
    series = 4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)

    return Decimal(1/pow(16, k)) * Decimal(series)

def algorithm(k):
    pi = 0

    for i in range(0, k):
        pi += sum_k(i)

    return pi

def main():
    """Main function. Algorithm implementation"""

    print("BBP ALGORITHM\n")
    print("--------------------")

    precision = get_prec()

    print(algorithm(precision))

if __name__ == "__main__":
    main()