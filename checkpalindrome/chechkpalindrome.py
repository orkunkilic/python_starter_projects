global a
a=0
input1=str(input("Enter a word:"))

arr=list(input1)

if len(arr)%2 == 0:

    for i in range((len(arr)//2)):
        if arr[i] != arr[len(arr)-1-i]:
            a=1
            break
        else:
            pass
else:
    for i in range((len(arr)-1)//2):
        if arr[i] != arr[len(arr)-1-i]:
            a=1
            break
        else:
            pass

if a==1:
    print("NO! It's not a palindrome")
else:
    print("YES! It's a palindrome")