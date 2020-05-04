#Get Input number
num=int(input("Enter a number:"))
i=0
while i>=0:
    if str(num+i) == str(num+i)[::-1]:
        print(num+i," is the nearest Palindrome")
        break
    elif str(num-i) == str(num-i)[::-1]:
        print(num-i," is the nearest Palindrome")
        break
    else:
        i+=1