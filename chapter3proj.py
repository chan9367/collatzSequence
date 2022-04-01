def collatz(number):
    if (number%2 == 0):
        print(number // 2)
    else:
        print(number * 3 + 1)
while True:
    try:
        print('Enter Number: ')
        number = int(input())
        collatz(number)
    except ValueError:
        print('That is not a number.')