
number = int(input("Input number: "))
for i in range(number):
    number -= 1
    print((" " * number) + ("*" * (i * 2 + 1)))