import os
import subprocess
import sys
import time
from prettytable import PrettyTable

CLEAR_LINE = '\033[F'
RED = '\033[0;31m'
GREEN = '\033[0;32m'
END_COLOR = '\033[0m'

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def clear_previous_executions():
    directory = os.listdir(".")
    for file in directory:
        if file.endswith(".mine"):
            os.remove(file)


def compile_solution():
    subprocess.check_call(['javac', 'Main.java'])


def judge_solution():
    print("------------- TEST ------------")
    directory = os.listdir(".")
    inputs = []
    for file in directory:
        if file.endswith(".in"):
            inputs.append(file)
    inputs.sort(key=lambda f: int(os.path.splitext(os.path.basename(f))[0]))
    verdict = 1
    message = "Accepted"
    worst_time = 0
    for file in inputs:
        base = os.path.basename(file)
        number = os.path.splitext(base)[0]
        test_time = execute_test(number)
        verdict &= verify_test_result(number)
        if test_time > worst_time:
            worst_time = test_time
        if verdict == 0:
            message = f'Wrong answer on test #{number}'
            break

    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)
    print_verdict(verdict, message, worst_time)


def execute_test(number):
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)

    print(f'Running on test #{number}')

    sys.stdout.flush()
    input_stream = open(f'{number}.in', "r", encoding="utf-8")
    output_stream = open(f'{number}.mine', "w", encoding="utf-8")
    start_time = int(round(time.time() * 1000))
    process = subprocess.Popen(['java', 'Main'], stdin=input_stream, stdout=output_stream, stderr=output_stream)
    exit_code = process.wait()
    end_time = int(round(time.time() * 1000))
    output_stream.flush()
    output_stream.close()

    return end_time - start_time


def verify_test_result(number):
    files = [f'{number}.out', f'{number}.mine']

    result = []
    for file in files:
        with open(file, 'r') as output:
            temp = []
            for line in output:
                for word in line.split():
                    word = word.strip()
                    temp.append(word)
            if len(temp) > 0:
                result.append(temp)

    if len(result) != 2:
        return 0
    elif result[0] == result[1]:
        return 1
    else:
        return 0


def print_verdict(verdict, message, worst_time):
    table = PrettyTable(['Problem', 'Lang', 'Verdict', 'Time'])
    verdict_cell = ""
    if verdict == 1:
        verdict_cell = f'{GREEN} {message} {END_COLOR}'
    else:
        verdict_cell = f'{RED} {message} {END_COLOR}'
    table.add_row(['A', 'Java 8', verdict_cell, f'{worst_time} ms'])
    print(table)


def __main__():
    clear_previous_executions()
    compile_solution()
    judge_solution()


if __name__ == "__main__":
    __main__()
