#!/usr/bin/python3
"""
Tte employee ID,will returns all information about the TODO list of this employee.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ Functions for gathering  data from an API """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    employee = json.loads(request_employee.text)
    employee_name = employee.get("name")
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    tasks = {}
    employee_todos = json.loads(request_todos.text)

    for dictionary in employee_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    EMPLOYEE_NAME = employee_name
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for k, v in tasks.items():
        if v is True:
            print("\t {}".format(k))
