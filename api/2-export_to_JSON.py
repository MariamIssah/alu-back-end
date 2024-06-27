#!/usr/bin/python3
"""
Python script that fetches and analyzes TODO list progress from an API.
"""
import json
import requests
from sys import argv
if __name__ == "__main__":
    # Step 1: Fetch employee information from the API.
    user_id = argv[1]
    request_employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}'
    )
    employee = json.loads(request_employee.text)
    employee_name = employee.get("name")
    USERNAME = employee.get("username")
    # Step 2: Fetch the employee's TODO list from the API.
    request_todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    )
    tasks = {}
    employee_todos = json.loads(request_todos.text)
    # Step 3: Analyze and process the TODO list data.
    for dictionary in employee_todos:
        TASK_TITLE = dictionary.get("title")
        TASK_COMPLETED_STATUS = dictionary.get("completed")
        tasks.update({TASK_TITLE: TASK_COMPLETED_STATUS})
    task_list = []
    for k, v in tasks.items():
        task_list.append({
            "task": k,
            "completed": v,
            "username": USERNAME
        })
    json_to_dump = {user_id: task_list}
    # Step 4: Export the analyzed data to a JSON file.
    with open(f'{user_id}.json', mode='w') as file:
        json.dump(json_to_dump, file)
