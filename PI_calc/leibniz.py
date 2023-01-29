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

def leibniz(p):
    """Algorithm implementation"""

    s = 3
    pi = 1
    sub = True

    for i in range(s, p, 2):
        if(sub):
            pi -= 1/i
        else:
            pi += 1/i

        sub = not sub

    return 4 * Decimal(pi)

def main():
    """Main function"""
    
    print("LEIBNIZ ALGORITHM\n")
    print("--------------------")

    precision = get_prec()
    
    pi = leibniz(precision)

    print(pi)

if __name__ == "__main__":
    main()