import os


def create_test():
    number = count_existing_tests()
    print(f'Found {number} tests for this problem')
    fetch_input(number + 1)
    fetch_output(number + 1)


def count_existing_tests():
    directory = os.listdir(".")
    result = 0
    for file in directory:
        if file.endswith(".in"):
            result = result + 1
    return result


def fetch_input(number):
    print("Enter your input:")
    file = open(f'{number}.in', 'w+')
    while True:
        line = input('> ')
        if line == '...':
            break
        file.write(line)
        file.write("\n")
    file.close()


def fetch_output(number):
    print("Enter the correct output (if you know it):")
    file = open(f'{number}.out', 'w+')
    while True:
        line = input('> ')
        if line == '...':
            break
        file.write(line)
        file.write("\n")
    file.close()


create_test()
