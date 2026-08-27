#python coding class 2
x = eval(input("Enter the Number: "))
print(x)
str1 = "Python" 
print(str1[3])
print(str1[-3])

for x in str1:
    print(x)
    for x in range(len(str1)-1,-1,-1):
        print(str1[x])
        for x in range(len(str1)):
            print(str1[x])
