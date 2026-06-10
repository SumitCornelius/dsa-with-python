def print_reverse_list(myList,i):
    try:
        myList[i]
    except IndexError:
        return
    print_reverse_list(myList,i+1)
    print(myList[i])

def is_palindrome(myString):
    if(myString=="" or myString==None or len(myString)==0 or len(myString)==1):
        return True
    if(myString[0]==myString[-1]):
        return is_palindrome(myString[1:-1])
    else:
        return False

def reverseString(myString):
    if(myString==None or len(myString)==0 or myString==""):
        return ""
    return reverseString(myString[1: len(myString)]) + myString[0]

def decimalToBinary(num):
    if num==0:
        return ""
    rem=num%2
    return decimalToBinary(num//2) + str(rem)


print(decimalToBinary(25))
