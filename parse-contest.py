import os
import sys

import requests
from bs4 import BeautifulSoup

ORANGE = '\033[93m'
END_COLOR = '\033[0m'


def parse_contest(contest_id):
    url = codeforces_url + contest_id
    create_folder(os.getcwd() + "/" + contest_id)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "problems"})

    rows = table.findAll("tr")

    os.chdir(contest_id)
    for row in rows[1:]:
        col = row.findAll("td")[0]
        link = col.find("a", href=True)
        prepare_problem_folder(link)


def prepare_problem_folder(link):
    problem_id = link.text.strip()
    print(f'{ORANGE} Preparing problem {problem_id} {END_COLOR}')

    create_folder(os.getcwd() + "/" + problem_id)
    create_solution_file(problem_id)
    parse_problem(problem_id)
    sys.stdout.flush()


def create_folder(path):
    access_rights = 0o755
    os.mkdir(path, access_rights)


def create_solution_file(problem_id):
    directory = os.getcwd() + "/" + problem_id
    filename = "Solution.java"
    with open("../solution.tmpl") as template:
        with open(f'{directory}/{filename}', "w+") as solution_file:
            for line in template:
                solution_file.write(line)


def parse_problem(problem_id):
    url = f'{codeforces_url}{contest}/problem/{problem_id}'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    examples = soup.find("div", {"class": "sample-test"})

    divs = examples.findAll("div")
    it = iter(divs)

    count = 1

    directory = os.getcwd() + "/" + problem_id

    for example in it:
        input_content = example.find("pre").contents
        input_file = open(f'{directory}/{count}.in', "w+")
        for content in input_content:
            value = content.string
            if value is not None:
                input_file.write(value.strip())
            else:
                input_file.write("\n")

        input_file.close()

        next(it)

        output = next(it)
        output_content = output.find("pre").contents
        output_file = open(f'{directory}/{count}.out', "w+")
        for content in output_content:
            value = content.string
            if value is not None:
                output_file.write(value.strip())
            else:
                output_file.write("\n")

        output_file.close()

        next(it)
        count = count + 1


codeforces_url = "https://codeforces.com/contest/"
contest = sys.argv[1]
parse_contest(contest)
