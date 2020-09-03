Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = int(input("Enter the length of the sequence: "))
#  Do not change this line
countnum =3
number1=1
number2=2
number3=3
print(number1)
print(number2)
print(number3)
while countnum <=n-1:
    sum = number1+number2+number3
    print(sum)
    countnum+=1
    number1=number2
    number2=number3
    number3=sum