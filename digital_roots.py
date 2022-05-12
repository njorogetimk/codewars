#! /usr/bin/env python3
def digital_root(n):
    # ...
    # Test if n is non-negative
    if type(n) == int:
        if n > 0:
            #---
            #Cont
            str_n = str(n)
            sum_n = 0
            for digit in str_n:
                sum_n += int(digit)
            
            if len(str(sum_n)) > 1:
                sum_n = digital_root(sum_n)
            
            return sum_n
        else:
            return 'n must be non-negative'
        
    else:
        return 'n must be an integer'


def main():
    val = digital_root(493193)
    print(val)


if __name__ == '__main__':
    main()