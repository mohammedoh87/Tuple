def palindrome(tuple1):
    length = len(tuple1)-1
    i = 0
    while(i < length):
        if(tuple1[i] != tuple1[length]):
            return False
        i += 1
        length -= 1
    return True

tuple1 = (1,2,3,4,2,1)
if(palindrome(tuple1)):
    print("It is a palindrome")
else:
    print("It is not a palindrome")


