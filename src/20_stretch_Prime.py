# Algorithm to check if inputed value is prime or not.

def primeCheck(pNum):
    result = "Number is Prime"
    # 0, 1, 2 are all Prime Numbers
    if pNum > 3:
        for i in range(2, pNum):
            if (pNum % i) > 0:
                result = "Number is Prime"
            elif (pNum % i) == 0:
                result = "Number is not Prime"
                break
    return result


for i in range(5):
    num = input("Enter a number to determine if it is Prime: ")
    res = primeCheck(int(num))
    print('result: ', res)